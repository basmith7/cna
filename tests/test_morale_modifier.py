"""Morale Modifier Table (SPI 17.4): cohesion-level rows × modifier columns of sequential dice
ranges; every row tiles 11–66 exactly once, and the modifier never rises as cohesion falls."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DICE = [10 * a + b for a in range(1, 7) for b in range(1, 7)]
COLS = ["+4", "+3", "+2", "+1", "0", "-1", "-2", "-3", "-4", "surrender"]


def _table():
    return json.loads((ROOT / "data" / "tables" / "morale-modifier.json").read_text())


def test_rows_cover_levels_plus8_to_minus17_and_tile_the_dice():
    t = _table()
    assert [r["level"] for r in t["rows"]] == list(range(8, -18, -1))
    gaps = {g["level"]: set(g["readings"]) for g in t.get("known_gaps", [])}
    for r in t["rows"]:
        assert list(r["modifier"]) == COLS
        covered = sorted(d for c in COLS for cell in [r["modifier"][c]] if cell for d in DICE if cell["from"] <= d <= cell["to"])
        assert covered == sorted(set(DICE) - gaps.get(r["level"], set())), r["level"]
    assert t["known_gaps"] == [{"level": -4, "readings": [56]}]   # the one printed gap, confirmed in both scans


def test_best_reachable_modifier_never_improves_as_cohesion_falls():
    def best(r):
        return next(i for i, c in enumerate(COLS) if r["modifier"][c])
    bests = [best(r) for r in _table()["rows"]]
    assert bests == sorted(bests)
