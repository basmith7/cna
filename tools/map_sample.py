#!/usr/bin/env python3
"""Seeded review sample for one map sheet: crops from the redraw and the scan plus a checklist.

  python3 tools/map_sample.py C              # 50 hexes -> build/map/sample-C/<id>-vassal.png, <id>-scan.png, checklist.md
  python3 tools/map_sample.py C --hex C4023  # crops for one hex (any id), no checklist

Everything is written under build/ (git-ignored).  The filled checklist's
misread count goes to EXTRACTION.md; the crops never leave the machine.
Needs build/map/debug-<S>.csv from map_extract.py for the redraw centres, and
tools/sources.json -> archive_org.map_pages[S].scan_grid for the scan crops
(skipped with a note when the grid for that sheet has not been measured).
"""
import csv
import json
import pathlib
import random
import sys

from PIL import Image

import map_geom

Image.MAX_IMAGE_PIXELS = None
ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / "build" / "map"
N = 50


def sample(sheet, n=N, seed=None):
    """n distinct hex ids of the sheet, stable: seeded by the sheet letter's ordinal."""
    hexes = json.loads((ROOT / "data" / "map" / "hexes.json").read_text())["hexes"]
    ids = sorted(h["id"] for h in hexes if h["sheet"] == sheet)
    return random.Random(ord(sheet) if seed is None else seed).sample(ids, min(n, len(ids)))


def _redraw_centres(sheet):
    p = BUILD / f"debug-{sheet}.csv"
    if not p.exists():
        raise SystemExit(f"{p} missing: run map_extract.py --zone for the sheet first")
    return {r["hex"]: (int(r["x"]), int(r["y"])) for r in csv.DictReader(p.open())}


def scan_centre(hid, grid, sheets):
    """Pixel centre on the scan page from the measured grid of the reference hex."""
    s, r, c = map_geom.parse_hex_id(hid)
    _, r0, c0 = map_geom.parse_hex_id(grid["ref_hex"])
    x = grid["x"] + (c - c0) * grid["col_w"]
    if map_geom.row_shifted_east(r, sheets[s]) != map_geom.row_shifted_east(r0, sheets[s]):
        x += grid["col_w"] / 2 * (1 if map_geom.row_shifted_east(r, sheets[s]) else -1)
    return int(x), int(grid["y"] - (r - r0) * grid["row_h"])


def crops(sheet, ids, out):
    import fetch
    import map_extract
    sheets = json.loads((ROOT / "data" / "map" / "sheets.json").read_text())["sheets"]
    pages = json.loads((ROOT / "tools" / "sources.json").read_text())["archive_org"].get("map_pages", {}).get(sheet, {})
    centres = _redraw_centres(sheet)
    redraw = Image.open(map_extract.CACHE / map_extract.MAP_IMAGE).convert("RGB")
    inr = map_extract.load_zones()[1][0]["grid"]["dy"] / 2
    scan = Image.open(fetch.scan_page(pages["page"])).convert("RGB") if pages.get("scan_grid") and pages.get("page") else None
    out.mkdir(parents=True, exist_ok=True)
    for hid in ids:
        cx, cy = centres[hid]
        r = int(inr * 3)
        redraw.crop((cx - r, cy - r, cx + r, cy + r)).save(out / f"{hid}-vassal.png")
        if scan is not None:
            sx, sy = scan_centre(hid, pages["scan_grid"], sheets)
            rs = int(pages["scan_grid"]["col_w"] * 1.6)
            scan.crop((sx - rs, sy - rs, sx + rs, sy + rs)).save(out / f"{hid}-scan.png")
    return scan is not None


def checklist(sheet, ids, out, have_scan):
    hexes = {h["id"]: h for h in json.loads((ROOT / "data" / "map" / "hexes.json").read_text())["hexes"]}
    sides = json.loads((ROOT / "data" / "map" / "hexsides.json").read_text())["hexsides"]
    by_hex = {}
    for s in sides:
        for h in (s["a"], s["b"]):
            if h:
                by_hex.setdefault(h, []).append(f"{(s['b'] if h == s['a'] else s['a']) or s['side']}:{'+'.join(s['features'])}")
    lines = [f"# Map {sheet}: {len(ids)}-hex sample (seed {ord(sheet)})", "",
             "Fill *agrees?* (y/n) and *note* from `<id>-vassal.png`" + (" and `<id>-scan.png`" if have_scan else " (no scan grid measured for this sheet)") + ".", "",
             "| id | terrain | settlement | coastal | hexsides | agrees? | note |", "|---|---|---|---|---|---|---|"]
    for hid in ids:
        h = hexes[hid]
        lines.append(f"| {hid} | {h['terrain']} | {h['settlement'] or '-'} | {'y' if h['coastal'] else '-'} | {' '.join(sorted(by_hex.get(hid, []))) or '-'} |  |  |")
    (out / "checklist.md").write_text("\n".join(lines) + "\n")


def main(argv):
    sheet = next((a for a in argv if not a.startswith("--")), None)
    if not sheet:
        raise SystemExit(__doc__)
    out = BUILD / f"sample-{sheet}"
    if "--hex" in argv:
        ids = [argv[argv.index("--hex") + 1]]
        crops(sheet, ids, out)
        print(f"wrote crops for {ids[0]} under {out.relative_to(ROOT)}")
        return
    ids = sample(sheet)
    have_scan = crops(sheet, ids, out)
    checklist(sheet, ids, out, have_scan)
    print(f"wrote {len(ids)} hex crops and checklist.md under {out.relative_to(ROOT)}" + ("" if have_scan else " (no scan crops: grid not measured)"))


if __name__ == "__main__":
    main(sys.argv[1:])
