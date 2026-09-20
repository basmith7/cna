"""Stacking Point Values chart (SPI 9.4): SP per unit equivalent, full or shell, plus the two
per-5-points rates for truck convoys and replacement points."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_values_descend_by_size_and_shells_map_down_one_level():
    t = json.loads((ROOT / "data" / "tables" / "stacking-point-values.json").read_text())
    by = {r["equivalent"]: r for r in t["rows"]}
    assert [by[k]["sp"] for k in ("division", "super-brigade", "brigade", "battalion", "company")] == [5, 3, 2, 1, 0]
    assert by["super-brigade"]["shell_of"] == ["division"]
    assert by["battalion"]["shell_of"] == ["brigade", "battle-group"]
    assert by["company"]["shell_of"] == ["battalion", "hq-with-attachments"]
    assert t["per_five_points"] == {"truck-convoy": 0.5, "replacement-points": 1}
