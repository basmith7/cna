#!/usr/bin/env python3
"""Data gate: schemas valid, every table/errata file validates, every case reference exists.

  python3 tools/check_data.py [data_dir]     # exit 1 and print errors on failure
"""
import json
import pathlib
import re
import sys

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parents[1]
CASE_REF = re.compile(r"^CNA1979:(\d{1,2}\.\d{1,2})$")


def _registry(schema_dir: pathlib.Path) -> Registry:
    reg = Registry()
    for p in schema_dir.glob("*.schema.json"):
        reg = reg.with_resource(p.name, Resource.from_contents(json.loads(p.read_text())))
    return reg


def _validate(instance, schema_path: pathlib.Path, reg: Registry, label: str) -> list[str]:
    v = Draft202012Validator(json.loads(schema_path.read_text()), registry=reg)
    return [f"{label}: /{'/'.join(str(x) for x in e.absolute_path)}: {e.message}"
            for e in sorted(v.iter_errors(instance), key=lambda e: str(list(e.absolute_path)))]


def _case_refs(obj) -> set[str]:
    if isinstance(obj, str):
        m = CASE_REF.match(obj)
        return {obj} if m else set()
    if isinstance(obj, dict):
        return set().union(*(_case_refs(v) for v in obj.values())) if obj else set()
    if isinstance(obj, list):
        return set().union(*(_case_refs(v) for v in obj)) if obj else set()
    return set()


def _load_json(path: pathlib.Path, label: str, errors: list[str]):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f"{label}: invalid JSON: {e}")
        return None


def validate_all(data_dir: pathlib.Path) -> list[str]:
    errors: list[str] = []
    schema_dir = data_dir / "schema"
    for p in sorted(schema_dir.glob("*.schema.json")):
        try:
            Draft202012Validator.check_schema(json.loads(p.read_text()))
        except Exception as e:  # noqa: BLE001 — report any schema problem
            errors.append(f"{p.name}: invalid schema: {e}")
    if errors:
        return errors
    reg = _registry(schema_dir)

    cases_path = data_dir / "spi-cases.json"
    cases = _load_json(cases_path, "spi-cases.json", errors)
    if cases is None:
        return errors
    errors += _validate(cases, schema_dir / "spi-cases.schema.json", reg, "spi-cases.json")
    if not isinstance(cases, dict) or not isinstance(cases.get("cases"), list):
        errors.append("spi-cases.json: expected an object with a list 'cases'")
        return errors
    case_list = cases["cases"]
    for i, c in enumerate(case_list):
        if not isinstance(c, dict) or "id" not in c:
            errors.append(f"spi-cases.json: cases[{i}]: missing 'id'")
            return errors
    known = {c["id"] for c in case_list}

    tables = {}
    for p in sorted((data_dir / "tables").glob("*.json")) if (data_dir / "tables").is_dir() else []:
        schema = schema_dir / f"{p.stem}.schema.json"
        if not schema.exists():
            errors.append(f"tables/{p.name}: no schema (expected schema/{schema.name})")
            continue
        tables[p.stem] = _load_json(p, f"tables/{p.name}", errors)
        if tables[p.stem] is None:
            continue
        errors += _validate(tables[p.stem], schema, reg, f"tables/{p.name}")
        for ref in sorted(_case_refs(tables[p.stem]) - {f"CNA1979:{k}" for k in known}):
            errors.append(f"tables/{p.name}: unknown case reference {ref}")

    for p in sorted((data_dir / "errata").glob("*.json")) if (data_dir / "errata").is_dir() else []:
        patch = _load_json(p, f"errata/{p.name}", errors)
        if patch is None:
            continue
        errors += _validate(patch, schema_dir / "errata-patch.schema.json", reg, f"errata/{p.name}")
        if patch.get("id") and patch["id"] != p.stem:
            errors.append(f"errata/{p.name}: id {patch['id']} does not match filename")
        if patch.get("table") and patch["table"] not in tables:
            errors.append(f"errata/{p.name}: table '{patch['table']}' does not exist")
        for ref in sorted(_case_refs(patch) - {f"CNA1979:{k}" for k in known}):
            errors.append(f"errata/{p.name}: unknown case reference {ref}")
        affects = patch.get("affects")
        if isinstance(affects, list):  # otherwise the schema error above already covers it
            for c in sorted(set(map(str, affects)) - known):
                errors.append(f"errata/{p.name}: affects unknown case {c}")
    errors += validate_map(data_dir, reg, known)
    errors += validate_units(data_dir, reg, known, tables)
    return errors


UNIT_REF = re.compile(r"^unit:(cw|it|de):")


def _walk(obj):
    """Yield (key, value) for every dict entry and ('', item) for list items, recursively."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k, v
            yield from _walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield "", v
            yield from _walk(v)


def validate_units(data_dir: pathlib.Path, reg: Registry, known: set[str], tables: dict) -> list[str]:
    """data/oa/ and data/scenarios/: schemas, unique unit ids and their parents, then
    every unit, hex, place and extends a scenario (or the reinforcement schedule) names."""
    errors: list[str] = []
    schema_dir = data_dir / "schema"
    case_refs = {f"CNA1979:{k}" for k in known}
    units: dict[str, str] = {}
    parents: list[tuple[str, str, str]] = []
    formations: set[str] = set()
    for p in sorted((data_dir / "oa").glob("*.json")) if (data_dir / "oa").is_dir() else []:
        label = f"oa/{p.name}"
        doc = _load_json(p, label, errors)
        if doc is None:
            continue
        errs = _validate(doc, schema_dir / "oa.schema.json", reg, label)
        errors += errs
        if errs:
            continue
        if doc["nation"] != p.stem:
            errors.append(f"{label}: nation {doc['nation']} does not match filename")
        for ref in sorted(_case_refs(doc) - case_refs):
            errors.append(f"{label}: unknown case reference {ref}")
        for f in doc["formations"]:
            formations.add(f"{doc['nation']}:{f['id']}")
            for u in f["units"]:
                if not u["id"].startswith(f"unit:{doc['nation']}:"):
                    errors.append(f"{label}: {u['id']} is not {doc['nation']}")
                if u["id"] in units:
                    errors.append(f"{label}: duplicate unit {u['id']}")
                units[u["id"]] = label
                if u["parent"]:
                    parents.append((label, u["id"], u["parent"]))
    for label, uid, parent in parents:
        if parent not in units:
            errors.append(f"{label}: {uid}: unknown parent {parent}")

    hexes: set[str] = set()
    places: set[str] = set()
    m = data_dir / "map"
    if (m / "hexes.json").exists():
        hexes = {h["id"] for h in (_load_json(m / "hexes.json", "map/hexes.json", []) or {"hexes": []})["hexes"]}
    if (m / "places.json").exists():
        places = {pl["id"] for pl in (_load_json(m / "places.json", "map/places.json", []) or {"places": []})["places"]}

    def refs(label: str, doc) -> None:
        for k, v in _walk(doc):
            if isinstance(v, str) and UNIT_REF.match(v) and v not in units:
                errors.append(f"{label}: unknown unit {v}")
            if k in ("hexes", "minefields") and isinstance(v, list):
                errors.extend(f"{label}: unknown hex {h}" for h in v if isinstance(h, str) and hexes and h not in hexes)
            if k in ("of", "railroad_ends") and isinstance(v, str) and hexes and re.match(r"^[A-EM][0-9]{4}$", v) and v not in hexes:
                errors.append(f"{label}: unknown hex {v}")
            if k == "formation" and isinstance(v, str) and v not in formations:
                errors.append(f"{label}: unknown formation {v}")
            if k == "place" and isinstance(v, str) and places and v not in places:
                errors.append(f"{label}: unknown place {v}")

    scenarios: dict[str, tuple[str, dict]] = {}
    for p in sorted((data_dir / "scenarios").glob("*.json")) if (data_dir / "scenarios").is_dir() else []:
        label = f"scenarios/{p.name}"
        doc = _load_json(p, label, errors)
        if doc is None:
            continue
        errs = _validate(doc, schema_dir / "scenario.schema.json", reg, label)
        errors += errs
        if errs:
            continue
        if doc["id"] != f"scenario:{p.stem}":
            errors.append(f"{label}: id {doc['id']} does not match filename")
        for ref in sorted(_case_refs(doc) - case_refs):
            errors.append(f"{label}: unknown case reference {ref}")
        scenarios[doc["id"]] = (label, doc)
        refs(label, doc)
    for sid, (label, doc) in scenarios.items():
        if "extends" in doc and doc["extends"] not in {f"scenario:{p.stem}" for p in (data_dir / "scenarios").glob("*.json")}:
            errors.append(f"{label}: extends unknown {doc['extends']}")
    if tables.get("reinforcement-schedule"):
        refs("tables/reinforcement-schedule.json", tables["reinforcement-schedule"])
    return errors


def validate_map(data_dir: pathlib.Path, reg: Registry, known: set[str]) -> list[str]:
    """data/map/: schemas, then the referential rules data/README.md lists (hexside
    endpoints exist and are adjacent, keys match, up is an endpoint, coast joins two
    coastal land hexes, places match settlements one-to-one)."""
    import map_geom
    m = data_dir / "map"
    if not m.is_dir():
        return []
    errors: list[str] = []
    schema_dir = data_dir / "schema"
    docs = {}
    for name, schema in (("sheets", "map-sheets"), ("hexes", "map-hexes"), ("hexsides", "map-hexsides"), ("places", "map-places")):
        p = m / f"{name}.json"
        if not p.exists():
            continue
        docs[name] = _load_json(p, f"map/{p.name}", errors)
        if docs[name] is not None:
            errors += _validate(docs[name], schema_dir / f"{schema}.schema.json", reg, f"map/{p.name}")
    for p in sorted((m / "raw").glob("*.json")) if (m / "raw").is_dir() else []:
        doc = _load_json(p, f"map/raw/{p.name}", errors)
        if doc is not None:
            # a raw file holds both record kinds; each half validates against its own schema
            errors += _validate({k: doc[k] for k in ("sources", "sheet", "hexes") if k in doc},
                                schema_dir / "map-hexes.schema.json", reg, f"map/raw/{p.name}")
            errors += _validate({k: doc[k] for k in ("sources", "sheet", "hexsides") if k in doc},
                                schema_dir / "map-hexsides.schema.json", reg, f"map/raw/{p.name}")
    for p in sorted((m / "corrections").glob("M-*.json")) if (m / "corrections").is_dir() else []:
        doc = _load_json(p, f"map/corrections/{p.name}", errors)
        if doc is not None:
            errors += _validate(doc, schema_dir / "map-correction.schema.json", reg, f"map/corrections/{p.name}")
            if doc.get("id") != p.stem:
                errors.append(f"map/corrections/{p.name}: id {doc.get('id')} does not match filename")
    if errors or not all(k in docs and docs[k] for k in ("sheets", "hexes", "hexsides")):
        return errors
    sheets = docs["sheets"]["sheets"]
    hexes = {h["id"]: h for h in docs["hexes"]["hexes"]}
    for s in docs["hexsides"]["hexsides"]:
        a, b = s["a"], s["b"]
        for hid in (a, b):
            if hid is not None and hid not in hexes:
                errors.append(f"map/hexsides.json: {s['key']}: unknown hex {hid}")
        if b is not None and a in hexes and b in hexes and not map_geom.is_adjacent(a, b, sheets):
            errors.append(f"map/hexsides.json: {s['key']}: {a} and {b} are not adjacent")
        if s["key"] != map_geom.hexside_key(a, b, s["side"]):
            errors.append(f"map/hexsides.json: {s['key']}: key does not match a/b/side")
        if s["up"] is not None and s["up"] not in (a, b):
            errors.append(f"map/hexsides.json: {s['key']}: up {s['up']} is not an endpoint")
        if "coast" in s["features"] and b is not None and not all(
                hexes.get(h, {}).get("coastal") and hexes.get(h, {}).get("terrain") != "sea" for h in (a, b)):
            errors.append(f"map/hexsides.json: {s['key']}: coast between non-coastal or sea hexes")
    seen_hex: dict[str, str] = {}
    for pl in (docs.get("places") or {"places": []})["places"]:
        h = hexes.get(pl["hex"])
        if h is None:
            errors.append(f"map/places.json: {pl['id']}: unknown hex {pl['hex']}")
            continue
        if pl["kind"] != "feature":
            if h["settlement"] != pl["kind"]:
                errors.append(f"map/places.json: {pl['id']}: hex {pl['hex']} settlement is {h['settlement']!r}, place kind is {pl['kind']!r}")
            if pl["hex"] in seen_hex:
                errors.append(f"map/places.json: {pl['id']}: hex {pl['hex']} already has place {seen_hex[pl['hex']]}")
            seen_hex[pl["hex"]] = pl["id"]
    return errors


def main(argv: list[str]) -> None:
    data_dir = pathlib.Path(argv[0]) if argv else ROOT / "data"
    errors = validate_all(data_dir)
    for e in errors:
        print(e)
    print(f"check_data: {'FAIL' if errors else 'OK'} ({len(errors)} errors)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
