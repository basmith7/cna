"""Logistics Game sequence of play (SPI 48.0): every stage, phase and segment in order, each
tagged with the Land Game point (SPI 5.2) it attaches to and whether it is new to the Logistics Game."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t():
    return json.loads((ROOT / "data" / "tables" / "logistics-sequence.json").read_text())


def _by():
    return {(r["stage"], r.get("phase"), r.get("segment")): r for r in _t()["rows"]}


def test_order_is_contiguous_and_keys_unique():
    rows = _t()["rows"]
    assert [r["order"] for r in rows] == list(range(1, len(rows) + 1))
    keys = [(r["stage"], r.get("phase"), r.get("segment")) for r in rows]
    assert len(set(keys)) == len(keys)
    assert [r["stage"] for r in rows if r.get("phase") is None] == ["I", "II", "III", "IV", "V", "VIII", "IX"]


def test_stages_and_frequency():
    rows = _t()["rows"]
    by = _by()
    assert by[("IV", None, None)]["name"] == "stores-expenditure" and by[("IV", None, None)]["new_in_logistics"]
    assert by[("IV", None, None)]["frequency"] == "turn"
    assert by[("V", None, None)]["repeat_as"] == ["VI", "VII"]
    assert all(r["frequency"] == "stage" for r in rows if r["stage"] == "V")
    assert {r["stage"] for r in rows if r["air_game_only"]} == {"II", "III", "V", "VIII"}
    assert by[("II", None, None)]["air_game_only"] and by[("VIII", None, None)]["air_game_only"]
    assert by[("III", "B", 1)]["air_game_only"] and by[("III", "B", 2)]["air_game_only"]
    assert not by[("III", "B", 3)]["air_game_only"]


def test_operations_stage_letters_and_attachment():
    rows = [r for r in _t()["rows"] if r["stage"] == "V" and r.get("segment") is None and r.get("phase")]
    assert [r["phase"] for r in rows] == list("ABCDEFGHIJKL")
    att = {r["phase"]: r["attaches_to"] for r in rows}
    assert att["G"] == "reserve-designation" and att["I"] == "truck-convoy" and att["J"] == "rail"
    assert att["C"] == "organisation" and att["D"] == "arrival" and att["H"] == "movement-combat"
    by = _by()
    assert by[("V", "C", 1)]["new_in_logistics"] and by[("V", "C", 3)]["new_in_logistics"]
    assert by[("V", "C", 6)]["new_in_logistics"] and not by[("V", "C", 7)]["new_in_logistics"]
    seg = [r["name"] for r in _t()["rows"] if r["stage"] == "V" and r.get("phase") == "C" and r.get("segment")]
    assert seg == ["water-distribution", "reorganisation", "attrition", "construction", "training",
                   "supply-distribution", "tactical-shipping"]
