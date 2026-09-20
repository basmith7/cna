"""Commonwealth Production System (SPI 20.78): truck production by die and period (A), infantry
production by two dice and game-turn band (B), and the production chart of everything else (C)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t():
    return json.loads((ROOT / "data" / "tables" / "cw-production.json").read_text())


def test_truck_table():
    t = _t()
    rows = t["trucks"]["rows"]
    assert [r["die"] for r in rows] == [1, 2, 3, 4, 5, 6]
    assert rows[0]["turns_1_30"] == {"light": 0, "medium": 10, "heavy": 0}
    assert rows[5]["turns_1_30"] == {"light": 5, "medium": 20, "heavy": 4}
    assert rows[0]["turns_31_107"] == {"light": 3, "medium": 30, "heavy": 3}
    assert rows[5]["turns_31_107"] == {"light": 14, "medium": 60, "heavy": 13}
    assert t["trucks"]["alexandria_max_share"] == 0.25 and t["trucks"]["arrive_turns_later"] == 4


def test_infantry_table():
    t = _t()
    rows = {r["dice"]: r for r in t["infantry"]["rows"]}
    assert sorted(rows) == list(range(2, 13))
    assert t["infantry"]["bands"] == [[3, 30], [31, 46], [47, 102], [103, 107]]
    assert rows[2]["points"] == [0, 0, 5, 0]
    assert rows[4]["points"] == [15, 10, 25, 3]
    assert rows[9]["points"] == [5, 18, 30, 1]
    assert rows[12]["points"] == [20, 0, 8, 0]


def test_production_chart():
    t = _t()
    by = {r["item"]: r for r in t["chart"]["rows"]}
    assert len(by) == len(t["chart"]["rows"]) == 24
    assert by["25-pounder"] == {"item": "25-pounder", "total": 250, "max": 4, "max_per": "turn", "from_turn": 11, "sources": ["CNA1979:20.78", "scan:p140"]}
    assert by["heavy-aa"]["max"] == 1 and by["heavy-aa"]["max_per"] == "month"
    assert by["155mm-howitzer"]["from_turn"] == 51 and by["155mm-howitzer"]["to_turn"] == 59
    assert by["crusader-3"]["max_per"] == "fortnight" and by["crusader-3"]["max"] == 6 and by["crusader-3"]["from_turn"] == 88
    assert by["stuart"] == {"item": "stuart", "total": 44, "max": 10, "max_per": "month", "from_turn": 35, "to_turn": 54, "sources": ["CNA1979:20.78", "scan:p140"]}
    assert by["churchill"]["total"] == 1 and "max" not in by["churchill"] and by["churchill"]["from_turn"] == 90
    assert t["chart"]["tiger_convoy_turn"] == 32
