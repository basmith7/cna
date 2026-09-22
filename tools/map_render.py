#!/usr/bin/env python3
"""Render data/map/ as one schematic SVG per sheet (ours: own palette, own symbols).

  python3 tools/map_render.py             # write site/public/map/<sheet>.svg for every sheet with data, and site/map.md
  python3 tools/map_render.py --check     # exit 1 if any committed SVG or site/map.md is stale
  python3 tools/map_render.py --golden    # refresh tests/golden/M.svg

Output is deterministic: coordinates as f"{v:.2f}", hexes in id order, hexsides in
key order, places in id order.  No SPI or Guthrie artwork or text is embedded.
"""
import json
import math
import pathlib
import sys
from dataclasses import dataclass

import map_geom as g

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "site" / "public" / "map"
SIZE = 20.0

PALETTE = {"clear": "#f3ecd8", "gravel": "#e2d9bf", "salt-marsh": "#d8d2b0", "heavy-vegetation": "#b9c98a",
           "rough": "#d9c9a0", "mountain": "#b8a377", "delta": "#cfe0c8", "desert": "#efd98a",
           "major-city": "#c9c9c9", "swamp": "#a9cdb0", "sea": "#cfe1ec"}
STROKES = {"escarpment": ("#333333", 2.5, ""), "ridge": ("#7a6a3a", 2, ""), "slope": ("#7a6a3a", 1.5, "4 2"),
           "wadi": ("#5f8a7f", 1.5, "2 2"), "major-river": ("#3b78a8", 3, ""), "minor-river": ("#3b78a8", 1.5, ""),
           "road": ("#5a3d1e", 2, ""), "unfinished-road": ("#5a3d1e", 2, "3 3"), "railroad": ("#222222", 1.5, "6 2"),
           "unfinished-railroad": ("#222222", 1.5, "2 4"), "track": ("#7a7a7a", 1, "3 3"),
           "coast": ("#3b78a8", 1, ""), "lake": ("#3b78a8", 1, "1 2")}


@dataclass
class MapData:
    sheets: dict
    hexes: dict
    hexsides: list
    places: list

    @classmethod
    def load(cls, data_dir):
        m = pathlib.Path(data_dir) / "map"
        rd = lambda n, k: json.loads((m / n).read_text())[k] if (m / n).exists() else ([] if k != "sheets" else {})
        return cls(rd("sheets.json", "sheets"), {h["id"]: h for h in rd("hexes.json", "hexes")},
                   rd("hexsides.json", "hexsides"), rd("places.json", "places"))


def _f(v):
    return f"{v:.2f}"


def _style():
    fills = "".join(f".terrain-{k}{{fill:{v}}}" for k, v in PALETTE.items())
    strokes = "".join(f".hexside.{k}{{stroke:{c};stroke-width:{w}" + (f";stroke-dasharray:{d}" if d else "") + "}"
                      for k, (c, w, d) in STROKES.items())
    return ("<style>.hex{stroke:#8a8a8a;stroke-width:0.4}.hexside{fill:none;stroke-linecap:round}"
            ".hexnum{font:5px sans-serif;fill:#666;text-anchor:middle}.place{font:7px sans-serif;fill:#222;text-anchor:middle}"
            ".settlement.village,.settlement.bir,.settlement.oasis{fill:#222}.settlement.major-city{fill:#444}"
            ".legend text{font:7px sans-serif;fill:#222}" + fills + strokes + "</style>")


def _edge(a, b, sheets, size):
    """The two shared corners of adjacent hexes a and b, plus the midpoint and the unit normal towards b."""
    ca, cb = g.centre(a, sheets, size), g.centre(b, sheets, size)
    pa, pb = g.corners(*ca, size), g.corners(*cb, size)
    shared = [p for p in pa if any(math.dist(p, q) < 0.01 for q in pb)]
    mx, my = (ca[0] + cb[0]) / 2, (ca[1] + cb[1]) / 2
    d = math.dist(ca, cb)
    return shared, (mx, my), ((cb[0] - ca[0]) / d, (cb[1] - ca[1]) / d)


def _edge_on_side(a, side, sheets, size):
    ca = g.centre(a, sheets, size)
    deg = {"E": 0, "SE": 60, "SW": 120, "W": 180, "NW": 240, "NE": 300}[side]
    nx, ny = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    apo = size * math.sqrt(3) / 2
    mx, my = ca[0] + apo * nx, ca[1] + apo * ny
    half = size / 2
    tx, ty = -ny, nx
    return [(mx - half * tx, my - half * ty), (mx + half * tx, my + half * ty)], (mx, my), (nx, ny)


def _hexside_svg(s, sheets, size):
    if s["b"] is None:
        pts, mid, normal = _edge_on_side(s["a"], s["side"], sheets, size)
    else:
        pts, mid, normal = _edge(s["a"], s["b"], sheets, size)
    if len(pts) != 2:
        return ""
    d = f"M {_f(pts[0][0])} {_f(pts[0][1])} L {_f(pts[1][0])} {_f(pts[1][1])}"
    out = []
    for feat in s["features"]:
        tick = ""
        if feat in ("slope", "escarpment") and s["up"]:
            sign = -1 if s["up"] == s["b"] else 1      # tick points to the DOWN hex
            tick = f" M {_f(mid[0])} {_f(mid[1])} l {_f(sign * normal[0] * size * 0.3)} {_f(sign * normal[1] * size * 0.3)}"
        out.append(f'<path class="hexside {feat}" data-a="{s["a"]}" data-b="{s["b"] or ""}" data-up="{s["up"] or ""}" d="{d}{tick}"/>')
    return "".join(out)


def _hex_svg(h, sheets, size):
    cx, cy = g.centre(h["id"], sheets, size)
    pts = " ".join(f"{_f(x)},{_f(y)}" for x, y in g.corners(cx, cy, size))
    cls = f"hex terrain-{h['terrain']}" + (" coastal" if h["coastal"] else "")
    return f'<polygon id="{h["id"]}" class="{cls}" points="{pts}"/>'


def _settlement_svg(h, sheets, size):
    if not h["settlement"]:
        return ""
    cx, cy = g.centre(h["id"], sheets, size)
    if h["settlement"] == "major-city":
        return f'<rect class="settlement major-city" x="{_f(cx - size * 0.25)}" y="{_f(cy - size * 0.25)}" width="{_f(size * 0.5)}" height="{_f(size * 0.5)}"/>'
    return f'<circle class="settlement {h["settlement"]}" cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(size * 0.15)}"/>'


def _labels_svg(h, places_by_hex, sheets, size):
    cx, cy = g.centre(h["id"], sheets, size)
    out = [f'<text class="hexnum" x="{_f(cx)}" y="{_f(cy + size * 0.75)}">{h["id"][1:]}</text>']
    for p in places_by_hex.get(h["id"], []):
        out.append(f'<text class="place" x="{_f(cx)}" y="{_f(cy - size * 0.35)}">{p["name"]}</text>')
    return "".join(out)


def _legend_svg(terrains, feats, x, y):
    rows = [(f"terrain-{t}", t, "swatch") for t in sorted(terrains)] + [(f"hexside {f}", f, "line") for f in sorted(feats)]
    out = [f'<g class="legend" transform="translate({_f(x)} {_f(y)})">']
    for i, (cls, label, kind) in enumerate(rows):
        yy = i * 11
        if kind == "swatch":
            out.append(f'<rect class="{cls}" x="0" y="{yy}" width="14" height="8" stroke="#888" stroke-width="0.4"/>')
        else:
            out.append(f'<path class="{cls}" d="M 0 {yy + 4} L 14 {yy + 4}"/>')
        out.append(f'<text x="18" y="{yy + 7}">{label}</text>')
    out.append("</g>")
    return "".join(out)


def _render(hex_ids, data, size, overlay_svg="", legend=True):
    sheets = data.sheets
    hexes = [data.hexes[i] for i in sorted(hex_ids)]
    if not hexes:
        raise ValueError("no hexes to render")
    idset = set(hex_ids)
    sides = [s for s in sorted(data.hexsides, key=lambda s: s["key"]) if s["a"] in idset and (s["b"] is None or s["b"] in idset)]
    places_by_hex = {}
    for p in sorted(data.places, key=lambda p: p["id"]):
        places_by_hex.setdefault(p["hex"], []).append(p)
    xs, ys = zip(*[c for h in hexes for c in g.corners(*g.centre(h["id"], sheets, size), size)])
    x0, y0, x1, y1 = min(xs) - size, min(ys) - size, max(xs) + size, max(ys) + size
    legend_w = 90 if legend else 0
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{_f(x0)} {_f(y0)} {_f(x1 - x0 + legend_w)} {_f(y1 - y0)}" class="cna-map" data-sheet="{hexes[0]["sheet"]}">',
             _style(),
             '<g class="hexes">' + "".join(_hex_svg(h, sheets, size) for h in hexes) + "</g>",
             '<g class="hexsides">' + "".join(_hexside_svg(s, sheets, size) for s in sides) + "</g>",
             '<g class="settlements">' + "".join(_settlement_svg(h, sheets, size) for h in hexes) + "</g>",
             '<g class="labels">' + "".join(_labels_svg(h, places_by_hex, sheets, size) for h in hexes) + "</g>"]
    if legend:
        parts.append(_legend_svg({h["terrain"] for h in hexes}, {f for s in sides for f in s["features"]}, x1 + 4, y0 + size))
    if overlay_svg:
        parts.append(f'<g class="overlay">{overlay_svg}</g>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def render_sheet(sheet, data, size=SIZE):
    return _render([i for i, h in data.hexes.items() if h["sheet"] == sheet], data, size)


def render_region(hex_ids, data, size=SIZE, overlay_svg=""):
    return _render(list(hex_ids), data, size, overlay_svg, legend=False)


SHEET_TITLES = {"A": "Map A — Tripolitania and the Gulf of Sirte", "B": "Map B — Cyrenaica", "C": "Map C — the frontier",
                "D": "Map D — Matruh and the Western Desert", "E": "Map E — the Delta", "M": "Malta"}


def render_page(data):
    have = sorted({h["sheet"] for h in data.hexes.values()})
    out = ["---", "title: Map", "---", "", "# The map", "",
           "Our own schematic redraw of the theatre, generated by `tools/map_render.py` from `data/map/` (CC0): hex terrain, ",
           "hexside features, and the named places. It is not a copy of SPI's map art or of any other redraw; the terrain data ",
           "was read from Mitch Guthrie's 2021 VASSAL redraw and checked against the SPI scan, with every hand correction logged ",
           "in `data/map/corrections/`. See `data/README.md` for the hex convention and the legal posture.", ""]
    for s in have:
        out += [f"## {SHEET_TITLES[s]}", "", f"![{SHEET_TITLES[s]}](/map/{s}.svg)", ""]   # markdown image: VitePress base-prefixes it; a raw <img> would not be
    missing = [SHEET_TITLES[s] for s in "ABCDEM" if s not in have]
    if missing:
        out += ["## Not yet captured", "", ", ".join(missing) + ".", ""]
    return "\n".join(out)


def targets(data):
    t = {OUT / f"{s}.svg": render_sheet(s, data) for s in sorted({h["sheet"] for h in data.hexes.values()})}
    t[ROOT / "site" / "map.md"] = render_page(data)
    return t


def main(argv):
    data = MapData.load(ROOT / "data")
    if "--golden" in argv:
        (ROOT / "tests" / "golden").mkdir(exist_ok=True)
        (ROOT / "tests" / "golden" / "M.svg").write_text(render_sheet("M", data))
        return
    stale = [p for p, text in targets(data).items() if not p.exists() or p.read_text() != text]
    if "--check" in argv:
        for p in stale:
            print(f"{p.relative_to(ROOT)} is stale: run tools/map_render.py")
        print(f"map_render --check: {'FAIL' if stale else 'OK'}")
        sys.exit(1 if stale else 0)
    OUT.mkdir(parents=True, exist_ok=True)
    for p, text in targets(data).items():
        p.write_text(text)
    print(f"wrote {len(targets(data))} files")


if __name__ == "__main__":
    main(sys.argv[1:])
