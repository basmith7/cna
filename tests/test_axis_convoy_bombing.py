"""Simple Axis Naval Convoy Bombing Chart (SPI 32.66): per convoy route, the westernmost hex column
a qualifying Commonwealth division must have reached for each bomb-point band."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_bands_and_thresholds():
    t = json.loads((ROOT / "data" / "tables" / "axis-convoy-bombing.json").read_text())
    rows = t["rows"]
    assert len(rows) == 10 and t["routes"] == [1, 2, 3, 4, 5, 6]
    assert rows[0]["bomb_points"] == {"from": 21, "to": 40} and rows[9]["bomb_points"] == {"from": 471, "to": None}
    assert [r["bomb_points"]["from"] for r in rows] == [21, 41, 81, 121, 161, 201, 261, 321, 391, 471]
    assert rows[0]["thresholds"] == [{"map": "C", "column": 1}, {"map": "D", "column": 1}, {"map": "D", "column": 1}, {"map": "E", "column": 1}, {"map": "E", "column": 11}, {"map": "D", "column": 11}]
    assert rows[3]["thresholds"][0] == {"map": "A", "column": 18} and rows[4]["thresholds"][0] is None
    assert rows[9]["thresholds"] == [None, None, None, {"map": "B", "column": 10}, {"map": "B", "column": 20}, {"map": "A", "column": 18}]
    # bands are contiguous and each route's thresholds only ever move west (map letter down, or column down within a map)
    assert all(rows[i]["bomb_points"]["to"] + 1 == rows[i + 1]["bomb_points"]["from"] for i in range(9))
