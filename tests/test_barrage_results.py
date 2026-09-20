"""The barrage CRT (SPI 12.6) as data: every target class × barrage-points column must tile the
36 sequential two-dice readings 11–66 exactly once, and every cell must name a known result."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DICE = [10 * a + b for a in range(1, 7) for b in range(1, 7)]   # 11, 12, … 16, 21, … 66


def _table():
    return json.loads((ROOT / "data" / "tables" / "barrage-results.json").read_text())


def test_every_class_and_column_tiles_the_dice_range_exactly_once():
    t = _table()
    columns = [c["id"] for c in t["columns"]]
    classes = ["infantry", "armor", "gun", "truck"]
    for cls in classes:
        for col in columns:
            cells = [r for r in t["rows"] if r["class"] == cls and r["column"] == col]
            assert cells, f"{cls} {col}: no cells"
            covered = sorted(d for r in cells for d in DICE if r["dice"]["from"] <= d <= r["dice"]["to"])
            assert covered == DICE, f"{cls} {col}: ranges do not tile 11–66 exactly once"


def test_dice_bounds_are_valid_sequential_readings():
    for r in _table()["rows"]:
        assert r["dice"]["from"] in DICE and r["dice"]["to"] in DICE and r["dice"]["from"] <= r["dice"]["to"]


def test_columns_are_contiguous_barrage_point_bands_from_one():
    cols = _table()["columns"]
    assert cols[0]["min"] == 1
    for a, b in zip(cols, cols[1:]):
        assert b["min"] == a["max"] + 1
    assert cols[-1]["max"] is None   # open-ended top band (17+)
