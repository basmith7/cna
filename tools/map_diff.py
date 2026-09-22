#!/usr/bin/env python3
"""Diff our map data against Norman Harman's private hex database (diff-only source).

  python3 tools/map_diff.py C            # -> build/map/diff-C.md, one row per disagreement

His files live under ~/.cache/cna-njharman/ and are never committed, quoted or
copied: this tool only points at hexes worth a second look at the scan.  Only
counts leave build/ (EXTRACTION.md).  Exits 0 with a note when the cache is
absent so CI never needs it.
"""
import ast
import json
import os
import pathlib
import sys

import map_geom

ROOT = pathlib.Path(__file__).resolve().parents[1]
NJ_DATA = pathlib.Path(os.path.expanduser("~/.cache/cna-njharman/cna_src/src/core/cna/data"))
OUT = ROOT / "build" / "map"

# his terrain code -> our mapTerrain (codes 11-14 are off-map boxes, not hexes)
CODE_MAP = {0: "clear", 1: "sea", 2: "salt-marsh", 3: "heavy-vegetation", 4: "rough", 5: "mountain",
            6: "delta", 7: "desert", 8: "swamp", 9: "gravel", 10: "major-city"}
# his per-feature dict name -> our hexsideFeature; each dict is hex -> [neighbour hexes]
FEATURE_MAP = {"slopes": "slope", "escarpments": "escarpment", "wadis": "wadi", "minor_rivers": "minor-river",
               "major_rivers": "major-river", "roads": "road", "tracks": "track", "rails": "railroad",
               "future_roads": "unfinished-road", "future_rails": "unfinished-railroad"}
DIRECTED = {"slopes", "escarpments"}      # hex -> [hexes upslope of it]
COMPARED_FEATURES = set(FEATURE_MAP.values()) | {"ridge"}


def normalise_id(hid):
    """His ids are ours (sheet letter + RRCC); tolerate 'Map C 4023' / 'C 4023' / lowercase."""
    s = str(hid).replace("Map ", "").replace(" ", "").upper()
    map_geom.parse_hex_id(s)
    return s


def _literal_assignments(path, names):
    """Top-level `name = <literal>` (or set([...])) assignments from a module, without importing it."""
    tree = ast.parse(pathlib.Path(path).read_text())
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and node.targets[0].id in names:
            value = node.value
            if isinstance(value, ast.Call) and getattr(value.func, "id", "") == "set" and value.args:
                value = value.args[0]
            try:
                out[node.targets[0].id] = ast.literal_eval(value)
            except ValueError:
                continue
    return out


def load_njharman(root=NJ_DATA):
    """(hex id -> terrain, hexside key -> {feature: up-or-None}) in our vocabulary."""
    data = _literal_assignments(pathlib.Path(root) / "mapterrain.py", set(FEATURE_MAP) | {"terrain"})
    terrain = {}
    for hid, code in data.get("terrain", {}).items():
        if code in CODE_MAP:
            try:
                terrain[normalise_id(hid)] = CODE_MAP[code]
            except ValueError:
                continue
    sides = {}
    for name, feat in FEATURE_MAP.items():
        for hid, nbs in data.get(name, {}).items():
            for nb in nbs:
                try:
                    a, b = normalise_id(hid), normalise_id(nb)
                except ValueError:
                    continue
                key = map_geom.hexside_key(a, b)
                rec = sides.setdefault(key, {})
                if name in DIRECTED:
                    # listed both ways = ridge (his note: ridges are slopes in each direction)
                    if rec.get(feat) not in (None, b):
                        rec.pop(feat, None); rec["ridge"] = None
                    elif "ridge" not in rec:
                        rec[feat] = b
                else:
                    rec[feat] = None
    return terrain, sides


def diff_sheet(sheet, ours, theirs):
    """[{kind, key, ours, theirs}] for every disagreement on the sheet, sorted by key."""
    his_terrain, his_sides = theirs
    diffs = []
    for hid, h in ours.hexes.items():
        if h["sheet"] != sheet or hid not in his_terrain:
            continue
        if h["terrain"] != his_terrain[hid]:
            diffs.append({"kind": "hex", "key": hid, "ours": h["terrain"], "theirs": his_terrain[hid]})
    our_sides = {s["key"]: s for s in ours.hexsides if s["a"][0] == sheet and s["b"] is not None}
    keys = set(our_sides) | {k for k in his_sides if k[0] == sheet}
    for key in sorted(keys):
        mine = our_sides.get(key)
        ours_f = {f for f in mine["features"] if f in COMPARED_FEATURES} if mine else set()
        his = his_sides.get(key, {})
        theirs_f = set(his)
        if ours_f != theirs_f:
            diffs.append({"kind": "hexside", "key": key, "ours": ",".join(sorted(ours_f)) or "-",
                          "theirs": ",".join(sorted(theirs_f)) or "-"})
            continue
        for feat in ("slope", "escarpment"):
            if feat in ours_f and his.get(feat) and mine["up"] != his[feat]:
                diffs.append({"kind": "up", "key": key, "ours": mine["up"] or "null", "theirs": his[feat]})
    return sorted(diffs, key=lambda d: (d["key"], d["kind"]))


def write_report(sheet, diffs, out_dir=OUT):
    out_dir = pathlib.Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / f"diff-{sheet}.md"
    lines = [f"# Map {sheet}: {len(diffs)} differences (ours vs the second database)", "",
             "| kind | key | ours | theirs |", "|---|---|---|---|"]
    lines += [f"| {d['kind']} | {d['key']} | {d['ours']} | {d['theirs']} |" for d in diffs]
    p.write_text("\n".join(lines) + "\n")
    return p


def main(argv):
    if not (NJ_DATA / "mapterrain.py").exists():
        print("njharman cache absent — diff skipped")
        return 0
    import map_render
    sheet = next((a for a in argv if not a.startswith("--")), "C")
    ours = map_render.MapData.load(ROOT / "data")
    diffs = diff_sheet(sheet, ours, load_njharman())
    p = write_report(sheet, diffs)
    from collections import Counter
    print(f"Map {sheet}: {len(diffs)} differences ({dict(Counter(d['kind'] for d in diffs))}); report {p.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
