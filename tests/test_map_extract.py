import pathlib
import numpy as np
import pytest

import map_extract as mx

ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = pathlib.Path.home() / ".cache" / "cna-vassal"

ZONE_C = {"name": "Map C", "fmt": "$name$$gridLocation$",
          "poly": [(0, 0), (1000, 0), (1000, 1000), (0, 1000)],
          "grid": {"dx": 72.95, "dy": 85.25, "x0": 0, "y0": 0, "sideways": True},
          "num": {"hOff": 0, "vOff": 0, "hLeading": 1, "vLeading": 1, "stagger": False,
                  "vDescend": True, "hDescend": False, "first": "H", "sep": ""}}


def test_hex_id_is_structured_and_matches_hex_name():
    for nx, ny in ((0, 0), (3, 5), (12, 1)):
        s, r, c = mx.hex_id(ZONE_C, nx, ny)
        assert s == "C"
        assert mx.hex_name(ZONE_C, nx, ny) == f"Map C{r:02d}{c:02d}"


def test_sheet_letter_for_malta():
    z = {**ZONE_C, "name": "Malta"}
    assert mx.hex_id(z, 0, 0)[0] == "M"


def test_observed_shift_is_west_or_east():
    assert mx.observed_shift(ZONE_C) in ("west", "east")


def test_observed_shift_is_in_numbering_space():
    """Map A's module staggers the numbering: odd rows sit half a hex east on screen but carry column
    numbers one higher, so in the printed numbering (what map_geom and check_data use) they sit west."""
    plain = mx.observed_shift(ZONE_C)
    staggered = mx.observed_shift({**ZONE_C, "num": {**ZONE_C["num"], "stagger": True}})
    assert {plain, staggered} == {"west", "east"}


def test_clip_drops_out_of_range_ids():
    bounds = {"rows": [1, 13], "cols": [1, 13]}
    inside = [("M", 1, 1), ("M", 13, 13)]
    outside = [("M", 0, 5), ("M", 14, 2), ("M", 5, 0), ("M", 5, 14)]
    assert all(mx.in_bounds(t, bounds) for t in inside)
    assert not any(mx.in_bounds(t, bounds) for t in outside)


def test_raw_records_have_only_game_fact_fields():
    hexes = [{"hex": "M0304", "sheet": "M", "x": 10, "y": 20, "terrain": "clear", "village": 1, "cov_sea": 0.1, "cov_clear": 0.9}]
    sides = [{"hex_a": "M0304", "side": "E", "hex_b": "M0305", "feature": "slope", "band_hex": "M0304"}]
    doc = mx.raw_records("M", hexes, sides)
    assert set(doc) == {"sources", "sheet", "hexes", "hexsides"}
    assert doc["hexes"] == [{"id": "M0304", "sheet": "M", "terrain": "clear", "settlement": "village", "coastal": False}]
    assert doc["hexsides"] == [{"key": "M0304|M0305", "a": "M0304", "b": "M0305", "side": None, "features": ["slope"], "up": "M0305"}]


def test_raw_records_map_classes_to_the_data_enum_and_merge_features():
    hexes = [{"hex": "A0101", "sheet": "A", "x": 0, "y": 0, "terrain": "salt_marsh", "village": 0, "cov_sea": 0.4},
             {"hex": "A0102", "sheet": "A", "x": 0, "y": 0, "terrain": "major_city", "village": 0, "cov_sea": 0.0}]
    sides = [{"hex_a": "A0101", "side": "E", "hex_b": "A0102", "feature": "road", "band_hex": ""},
             {"hex_a": "A0101", "side": "E", "hex_b": "A0102", "feature": "wadi", "band_hex": ""},
             {"hex_a": "A0102", "side": "W", "hex_b": "", "feature": "minor_river", "band_hex": ""}]
    doc = mx.raw_records("A", hexes, sides)
    assert doc["hexes"][0]["terrain"] == "salt-marsh" and doc["hexes"][0]["coastal"] is True
    assert doc["hexes"][1]["terrain"] == "major-city" and doc["hexes"][1]["settlement"] == "major-city"
    assert doc["hexsides"] == [
        {"key": "A0101|A0102", "a": "A0101", "b": "A0102", "side": None, "features": ["wadi", "road"], "up": None},
        {"key": "A0102|W", "a": "A0102", "b": None, "side": "W", "features": ["minor-river"], "up": None}]


@pytest.mark.skipif(not (CACHE / "buildFile.xml").exists() and not (CACHE / "CNAv2.1.0.vmod").exists(), reason="VASSAL cache absent")
def test_load_zones_from_cache_names_six_zones():
    img, zones = mx.load_zones(CACHE)
    assert img.exists() and (CACHE / "buildFile.xml").exists()
    assert {z["name"] for z in zones} >= {"Map A", "Map B", "Map C", "Map D", "Map E", "Malta"}


def _cm(w=200, h=200, fill="clear"):
    return np.full((h, w), mx.CLASS[fill], dtype=np.uint8)


def test_coast_detected_when_midpoint_is_sea_between_land_hexes():
    cm = _cm()
    cm[:, 95:105] = mx.CLASS["sea"]          # a 10 px water channel down the middle
    inr = 42.6
    # hex at (60,100), neighbour to the east at (145,100): the E hexside midpoint is x≈102
    feats = mx.classify_side(cm, 60, 100, inr, 0, "clear", "clear", coastal=True)
    assert ("coast", "") in feats
    assert not any(f[0].endswith("river") for f in feats)


def test_no_coast_on_a_plain_land_hexside():
    feats = mx.classify_side(_cm(), 60, 100, 42.6, 0, "clear", "clear", coastal=False)
    assert ("coast", "") not in feats
