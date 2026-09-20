"""The anti-armour CRT (SPI 14.6) as data: 18 dice-pair rows × 17 point columns of damage points.
Damage never falls as points rise or as the dice rise; the 0* column is only reachable from raw 1–4."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAIRS = [f"{a}{b}" for a in range(1, 7) for b in (1, 3, 5)]   # 11, 13, 15, 21, … 65: first reading of each pair


def _table():
    return json.loads((ROOT / "data" / "tables" / "anti-armour-results.json").read_text())


def test_grid_is_complete():
    t = _table()
    cols = [c["id"] for c in t["columns"]]
    assert cols[0] == "0" and cols[-1] == "16+" and len(cols) == 17
    assert [r["dice"] for r in t["rows"]] == PAIRS
    for r in t["rows"]:
        assert list(r["damage"]) == cols


def test_damage_is_monotonic_across_points_and_dice():
    t = _table()
    cols = [c["id"] for c in t["columns"]]
    grid = [[r["damage"][c] for c in cols] for r in t["rows"]]
    for row in grid:
        vals = [v for v in row if v is not None]
        assert vals == sorted(vals)
        assert all(v is None for v in row[:len(row) - len(vals)])   # blanks only at the low end
    for j in range(len(cols)):
        col = [row[j] for row in grid if row[j] is not None]
        assert col == sorted(col)
