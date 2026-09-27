"""Supply Dump Capacity Chart (SPI 54.13; headed 54.12 on the chart sheet)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_capacity_cells():
    t = json.loads((ROOT / "data" / "tables" / "supply-dump-capacity.json").read_text())
    by = {r["location"]: r for r in t["rows"]}
    assert list(by) == ["tunis-tripoli-box", "major-city", "village", "other-terrain", "non-dump"]
    assert by["major-city"]["ammo"] == "unlimited" and by["tunis-tripoli-box"]["water"] == "unlimited"
    cells = lambda r: (by[r]["ammo"], by[r]["fuel"], by[r]["stores"], by[r]["water"])  # noqa: E731
    assert cells("village") == (2500, 8000, 3000, 1000)
    assert cells("other-terrain") == (1500, 5000, 1000, 1000)
    assert cells("non-dump") == (50, 0, 50, 0)
