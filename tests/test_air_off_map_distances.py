"""Air Distance Chart (SPI 37.4) and Allied Off-Map Air Facilities Chart (36.53), ranged onto the
map as R-168 decides: shortest path through charted points, P closing the country nearer the
barred place."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import map_geom as g  # noqa: E402

T = json.loads((ROOT / "data" / "tables" / "air-off-map-distances.json").read_text())
SHEETS = json.loads((ROOT / "data" / "map" / "sheets.json").read_text())["sheets"]
HEXES = {p["id"]: p["hexes"] for p in T["places"] if p["kind"] == "place"}
FIG = {(r["a"], r["b"]): r["hexes"] for r in T["rows"]}


def fig(a, b):
    return FIG.get((a, b), FIG.get((b, a), "unlisted"))


def map_d(a, b):
    return min(g.distance(x, y, SHEETS) for x in a for y in b)


def air(src, hex_):
    """R-168: one chart figure from off-map `src` to a charted place (or a base to its entry hex),
    then the map; the shortest such path, or None if P closes the hex."""
    near = {p: map_d(h, [hex_]) for p, h in HEXES.items()}
    bases = {b["id"]: b for b in T["commonwealth_bases"]}
    if src in bases:
        return bases[src]["hexes"] + map_d([bases[src]["entry_hex"]], [hex_])
    open_ = [p for p in HEXES if isinstance(fig(src, p), int)]
    barred = [p for p in HEXES if fig(src, p) is None]
    if not open_ or any(near[b] < min(near[o] for o in open_) for b in barred):
        return None
    return min(fig(src, p) + near[p] for p in open_)


def test_every_cell_as_printed():
    assert len(T["rows"]) == len(FIG) == 49  # 18 in part A, 31 in part B (Malta's own cell is a dash)
    assert all(a < b for a, b in FIG)
    assert sum(r["part"] == "A" for r in T["rows"]) == 18
    assert fig("tripoli", "tripolitania") == 32 and fig("benghazi", "tunis") == 136
    assert fig("gabes", "malta") == 58 and fig("gabes", "nofilia") == 104
    assert [fig(p, "crete") for p in ("malta", "nofilia", "benghazi", "derna", "tobruk", "bardia", "mersa-matruh", "alexandria")] == [105, None, 62, 27, 48, 50, 66, 84]
    assert [fig(p, "malta") for p in ("nofilia", "benghazi", "derna", "tobruk", "bardia", "mersa-matruh", "alexandria")] == [80, 84, 108, 126, 144, None, None]
    assert [fig(p, "sicily") for p in ("malta", "nofilia", "benghazi", "derna", "tobruk")] == [24, None, 96, 105, None]
    assert [fig(p, "italy") for p in ("malta", "benghazi", "derna", "alexandria")] == [72, 138, 147, None]
    assert {b["id"]: (b["entry_hex"], b["hexes"], b["max_squadrons"]) for b in T["commonwealth_bases"]} == {
        "port-said": ("E4033", 12, 3), "abu-seier": ("E3433", 7, 9), "ismailia": ("E3433", 9, 9),
        "fayid": ("E1833", 11, 9), "deversoir": ("E1833", 12, 9), "kabrit": ("E1833", 13, 9),
        "ethiopia": ("E0127", 60, None)}


def test_place_hexes_match_places_json():
    pj = {p["id"]: p["hex"] for p in json.loads((ROOT / "data" / "map" / "places.json").read_text())["places"]}
    for pid, hexes in HEXES.items():
        want = [pj["alexandria-west"], pj["alexandria-east"]] if pid == "alexandria" else [pj[pid]]
        assert hexes == want


def test_worked_example_agedabia_to_ismailia_is_149():
    # 37.4 example 2: 140 hexes on the map to the entry hex, 9 beyond it
    assert air("ismailia", "A2629") == 149


def test_shortest_path_through_charted_points():
    # Malta-Bardia: the printed 144, or Malta-Tobruk 126 plus 16 on the map
    assert air("malta", "C4321") == 142
    assert air("crete", "C4807") == 48  # Crete-Derna 27 + Derna-Tobruk 21 equals the printed 48
    assert air("tripoli", "A4827") == 88  # not 32 to the Tripolitania box + 44 on: no chaining through boxes
    assert air("sicily", "B5925") == 105


def test_p_closes_the_country_nearer_the_barred_place():
    assert air("sicily", "C4807") is None  # Tobruk
    assert air("sicily", "A2703") is None  # Nofilia
    assert air("malta", "E3613") is None  # Alexandria
    assert air("crete", "A2703") is None
    assert air("crete", "E3613") == 84
    # B2719 is 32 hexes from both Derna (open to Sicily) and Tobruk (P): a tie stays open
    assert air("sicily", "B2719") is not None
    assert air("tripoli", "C4807") is not None  # part A areas have no P
