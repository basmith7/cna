"""Commonwealth Fleet Reinforcement Schedule (SPI 30.6): which warships arrive when, and where."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_ships_and_arrivals():
    t = json.loads((ROOT / "data" / "tables" / "cw-fleet-schedule.json").read_text())
    by = {r["ship"]: r for r in t["rows"]}
    assert len(by) == len(t["rows"]) == 19
    assert by["valiant"] == {"ship": "valiant", "type": "BB", "arrival": {"turn": 1, "stage": 1}, "gun_rating": 6, "aa_rating": 12,
                             "sources": ["CNA1979:30.59", "scan:p141", "vassal:CNAv2.1.0"]}
    assert by["arethusa"]["type"] == "CL" and by["arethusa"]["malta_option"] == "one-of-cruisers"
    assert by["dido"]["type"] == "CLAA" and by["euryalus"]["malta_option"] == "one-of-cruisers"
    assert [s for s, r in by.items() if r.get("malta_option") == "two-of-destroyers"] == ["airedale", "bedouin", "jervis", "lance", "ledbury", "mohawk", "nubian"]
    assert by["barham"]["arrival"] == {"turn": 8, "stage": 3} and by["york"]["type"] == "CA" and by["ajax"]["type"] == "CL"
    assert by["marne"]["arrival"] == by["partridge"]["arrival"] == {"turn": 8, "stage": 3}
    assert by["queen-elizabeth"]["arrival"] == {"turn": 33, "stage": 1} and by["fiji"]["type"] == "CA" and by["naiad"]["type"] == "CLAA"
    assert t["malta_options"] == {"one-of-cruisers": 1, "two-of-destroyers": 2}


def test_ratings_follow_type():
    """30.11's battleship is 6 guns and 12 AA; ships of a type share a gun rating, and AA is never below guns."""
    t = json.loads((ROOT / "data" / "tables" / "cw-fleet-schedule.json").read_text())
    guns = {}
    for r in t["rows"]:
        guns.setdefault(r["type"], set()).add(r["gun_rating"])
        assert r["aa_rating"] >= r["gun_rating"]
    assert guns == {"BB": {6}, "CA": {4}, "CL": {3}, "CLAA": {2}, "DD": {1}}
    by = {r["ship"]: (r["gun_rating"], r["aa_rating"]) for r in t["rows"]}
    assert by["airedale"] == (1, 1) and by["bedouin"] == by["marne"] == (1, 3) and by["naiad"] == (2, 6)
