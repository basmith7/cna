#!/usr/bin/env python3
"""Build data/map/hexes.json and hexsides.json from raw/<sheet>.json + corrections/M-nnn.json.

  python3 tools/map_build.py [data_dir]           # write the final files
  python3 tools/map_build.py --check [data_dir]   # exit 1 if the committed files are stale

A correction targets one record by key.  Its `before` must equal the raw record
(or be null when raw has none) or the build fails; patches are RFC 6902
add/remove/replace against that record, with path "" creating or deleting the
whole record.  `superseded: true` corrections are skipped unchecked.
"""
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


class CorrectionError(Exception):
    pass


def _dump(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=False) + "\n"


def load_sheets(data_dir):
    return json.loads((pathlib.Path(data_dir) / "map" / "sheets.json").read_text())["sheets"]


def load_raw(data_dir):
    hexes, sides, sources = [], [], []
    for p in sorted((pathlib.Path(data_dir) / "map" / "raw").glob("*.json")):
        doc = json.loads(p.read_text())
        hexes += doc["hexes"]; sides += doc["hexsides"]
        sources += [s for s in doc["sources"] if s not in sources]
    return sorted(hexes, key=lambda h: h["id"]), sorted(sides, key=lambda s: s["key"]), sources


def load_corrections(data_dir):
    return [json.loads(p.read_text()) for p in sorted((pathlib.Path(data_dir) / "map" / "corrections").glob("M-*.json"))]


def _apply_patches(rec, patches, cid):
    for op in patches:
        path = op["path"]
        if path == "":
            if op["op"] == "add":
                rec = copy.deepcopy(op["value"])
            elif op["op"] == "remove":
                rec = None
            else:
                raise CorrectionError(f"{cid}: replace with empty path; use add")
            continue
        if rec is None:
            raise CorrectionError(f"{cid}: patch {path} on an absent record")
        parts = path.lstrip("/").split("/")
        target = rec
        for part in parts[:-1]:
            target = target[int(part) if isinstance(target, list) else part]
        last = parts[-1]
        key = int(last) if isinstance(target, list) and last != "-" else last
        if op["op"] == "remove":
            del target[key]
        elif op["op"] == "replace":
            if isinstance(target, dict) and key not in target:
                raise CorrectionError(f"{cid}: replace of missing {path}")
            target[key] = copy.deepcopy(op["value"])
        elif op["op"] == "add":
            if isinstance(target, list):
                target.insert(len(target) if last == "-" else key, copy.deepcopy(op["value"]))
            else:
                target[key] = copy.deepcopy(op["value"])
    return rec


def apply_corrections(hexes, sides, corrections):
    by_hex = {h["id"]: copy.deepcopy(h) for h in hexes}
    by_side = {s["key"]: copy.deepcopy(s) for s in sides}
    raw_hex = {h["id"]: h for h in hexes}
    raw_side = {s["key"]: s for s in sides}
    for c in corrections:
        if c.get("superseded"):
            continue
        table, raw = (by_hex, raw_hex) if c["target"] == "hex" else (by_side, raw_side)
        if raw.get(c["key"]) != c["before"]:
            raise CorrectionError(f"{c['id']}: 'before' does not match raw for {c['key']}: raw={raw.get(c['key'])!r}")
        new = _apply_patches(table.get(c["key"]), c["patches"], c["id"])
        if new is None:
            table.pop(c["key"], None)
        else:
            table[c["key"]] = new
    return (sorted(by_hex.values(), key=lambda h: h["id"]), sorted(by_side.values(), key=lambda s: s["key"]))


def build(data_dir):
    hexes, sides, sources = load_raw(data_dir)
    hexes, sides = apply_corrections(hexes, sides, load_corrections(data_dir))
    return {"sources": sources, "hexes": hexes}, {"sources": sources, "hexsides": sides}


def _paths(data_dir):
    d = pathlib.Path(data_dir) / "map"
    return d / "hexes.json", d / "hexsides.json"


def write(data_dir):
    hexes, sides = build(data_dir)
    ph, ps = _paths(data_dir)
    ph.write_text(_dump(hexes)); ps.write_text(_dump(sides))


def check(data_dir):
    hexes, sides = build(data_dir)
    errors = []
    for path, want in zip(_paths(data_dir), (hexes, sides)):
        have = path.read_text() if path.exists() else ""
        if have != _dump(want):
            errors.append(f"{path.name} is stale: run tools/map_build.py")
    return errors


def main(argv):
    data_dir = pathlib.Path(next((a for a in argv if not a.startswith("--")), ROOT / "data"))
    if "--check" in argv:
        errs = check(data_dir)
        for e in errs:
            print(e)
        print(f"map_build --check: {'FAIL' if errs else 'OK'}")
        sys.exit(1 if errs else 0)
    write(data_dir)
    print("wrote map/hexes.json, map/hexsides.json")


if __name__ == "__main__":
    main(sys.argv[1:])
