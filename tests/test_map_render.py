import math
import pathlib
import re
import xml.etree.ElementTree as ET

import map_geom as g
import map_render as mr

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHEETS = {"M": {"zone": "Malta", "odd_rows_shift": "west", "rows": [1, 4], "cols": [1, 4]}}


def data():
    hexes = {f"M{r:02d}{c:02d}": {"id": f"M{r:02d}{c:02d}", "sheet": "M", "terrain": "clear", "settlement": None, "coastal": False}
             for r in range(1, 5) for c in range(1, 5)}
    hexes["M0202"]["settlement"] = "village"
    sides = [{"key": "M0202|M0203", "a": "M0202", "b": "M0203", "side": None, "features": ["slope"], "up": "M0203"},
             {"key": "M0101|W", "a": "M0101", "b": None, "side": "W", "features": ["coast"], "up": None}]
    places = [{"id": "x", "hex": "M0202", "name": "X", "kind": "village", "port": True}]
    return mr.MapData(SHEETS, hexes, sides, places)


def test_every_hex_is_one_polygon_with_its_id_and_nothing_else_has_an_id():
    svg = mr.render_sheet("M", data())
    root = ET.fromstring(svg)                      # well-formed XML
    ids = [e.get("id") for e in root.iter() if e.get("id")]
    assert sorted(ids) == sorted(data().hexes) and len(ids) == 16
    assert all(e.tag.endswith("polygon") for e in root.iter() if e.get("id"))


def test_neighbour_polygons_share_an_edge():
    svg = mr.render_sheet("M", data())
    pts = {m.group(1): [tuple(map(float, p.split(","))) for p in m.group(2).split()]
           for m in re.finditer(r'<polygon id="(M\d{4})"[^>]*points="([^"]+)"', svg)}
    for a, pa in pts.items():
        for b in g.neighbours(a, SHEETS):
            if b in pts:
                shared = [p for p in pa if any(math.dist(p, q) < 0.01 for q in pts[b])]
                assert len(shared) == 2, (a, b)


def test_hexside_paths_carry_endpoints_and_up():
    svg = mr.render_sheet("M", data())
    assert 'class="hexside slope" data-a="M0202" data-b="M0203" data-up="M0203"' in svg
    assert 'class="hexside coast" data-a="M0101" data-b="" data-up=""' in svg


def test_settlement_symbol_and_label_and_legend():
    svg = mr.render_sheet("M", data())
    assert 'class="settlement village"' in svg and ">X<" in svg
    assert 'class="legend"' in svg and "slope" in svg.split('class="legend"')[1]


def test_region_renders_only_the_listed_hexes_plus_overlay():
    svg = mr.render_region(["M0101", "M0102"], data(), overlay_svg='<circle class="unit" r="3"/>')
    assert svg.count("<polygon") == 2 and 'class="unit"' in svg and 'class="legend"' not in svg


def test_render_is_deterministic():
    assert mr.render_sheet("M", data()) == mr.render_sheet("M", data())


def test_committed_svgs_and_golden_are_current():
    d = mr.MapData.load(ROOT / "data")
    for sheet in sorted(d.sheets):
        p = ROOT / "site" / "public" / "map" / f"{sheet}.svg"
        if any(h["sheet"] == sheet for h in d.hexes.values()):
            assert p.read_text() == mr.render_sheet(sheet, d), f"{p} is stale: run tools/map_render.py"
    assert (ROOT / "tests" / "golden" / "M.svg").read_text() == mr.render_sheet("M", d), "golden stale: run tools/map_render.py --golden"
