"""Breakdown Table (SPI 21.38): accumulated-breakdown-point bands × percentage rows of sequential
dice ranges; every band tiles 11–66 exactly once."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DICE = [10 * a + b for a in range(1, 7) for b in range(1, 7)]


def _table():
    return json.loads((ROOT / "data" / "tables" / "breakdown.json").read_text())


def test_bands_are_contiguous_from_zero_and_open_ended():
    cols = _table()["columns"]
    assert cols[0]["min"] == 0 and cols[-1]["max"] is None
    for a, b in zip(cols, cols[1:]):
        assert b["min"] == a["max"] + 1


def test_every_band_tiles_the_dice_across_the_percent_rows():
    t = _table()
    for col in [c["id"] for c in t["columns"]]:
        cells = [r for r in t["rows"] if r["column"] == col]
        covered = sorted(d for r in cells for d in DICE if r["dice"]["from"] <= d <= r["dice"]["to"])
        assert covered == DICE, col
        assert [r["percent"] for r in cells] == sorted(r["percent"] for r in cells)
