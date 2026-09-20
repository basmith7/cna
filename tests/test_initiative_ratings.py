"""Initiative Ratings Chart (SPI 7.2): Commonwealth rating by game-turn band (covering turns 1–111
once), Axis rating by the presence of Rommel / German land combat units on the map."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_commonwealth_bands_cover_turns_1_to_111_once_and_rise():
    t = json.loads((ROOT / "data" / "tables" / "initiative-ratings.json").read_text())
    cw = t["commonwealth"]
    turns = sorted(n for b in cw for n in range(b["turns"]["from"], b["turns"]["to"] + 1))
    assert turns == list(range(1, 112))
    assert [b["rating"] for b in cw] == sorted(b["rating"] for b in cw)


def test_axis_rows_are_the_three_situations():
    t = json.loads((ROOT / "data" / "tables" / "initiative-ratings.json").read_text())
    assert {r["situation"]: r["rating"] for r in t["axis"]} == {"rommel-on-map": 6, "german-land-combat-units-no-rommel": 3, "no-german-combat-units": 1}
