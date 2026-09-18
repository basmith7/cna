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
    cases = json.loads(cases_path.read_text())
    errors += _validate(cases, schema_dir / "spi-cases.schema.json", reg, "spi-cases.json")
    known = {c["id"] for c in cases.get("cases", [])}

    tables = {}
    for p in sorted((data_dir / "tables").glob("*.json")) if (data_dir / "tables").is_dir() else []:
        schema = schema_dir / f"{p.stem}.schema.json"
        if not schema.exists():
            errors.append(f"tables/{p.name}: no schema (expected schema/{schema.name})")
            continue
        tables[p.stem] = json.loads(p.read_text())
        errors += _validate(tables[p.stem], schema, reg, f"tables/{p.name}")
        for ref in sorted(_case_refs(tables[p.stem]) - {f"CNA1979:{k}" for k in known}):
            errors.append(f"tables/{p.name}: unknown case reference {ref}")

    for p in sorted((data_dir / "errata").glob("*.json")) if (data_dir / "errata").is_dir() else []:
        patch = json.loads(p.read_text())
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
