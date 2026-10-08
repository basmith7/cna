import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "axis-coastal-ships.json").read_text())


def test_four_ships_as_in_the_vassal_counters():
    assert {r["counter"]: r["capacity_tons"] for r in TABLE["rows"]} == {"A": 1000, "B": 1000, "C": 1000, "D": 2000}
