"""Axis shipping lanes and the Axis Naval Convoy Air Distance Chart (SPI 56.1), read from scan jp2 71."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t(name):
    return json.loads((ROOT / "data" / "tables" / f"{name}.json").read_text())


def test_lanes_as_read():
    t = _t("convoy-lanes")
    by = {r["lane"]: r for r in t["lanes"]}
    assert sorted(by) == [1, 2, 3, 4, 5, 6]
    assert [r["id"] for r in t["rally_points"]] == ["sicily", "italy", "crete", "malta", "benghazi", "derna", "tobruk"]
    assert by[1]["distances"]["crete"] is None  # the chart's only dash
    assert list(by[2]["distances"].values()) == [45, 82, 134, 35, 100, 135, 160]
    assert by[5]["distances"]["derna"] == 18 and by[1]["distances"]["tobruk"] == 165
    assert sum(v for r in t["lanes"] for v in r["distances"].values() if v is not None) == 2993  # checksum as read


def test_destinations_are_ports_and_places():
    t = _t("convoy-lanes")
    ports = {r["port"] for r in _t("port-capacity")["rows"]}
    places = {p["id"]: p for p in json.loads((ROOT / "data" / "map" / "places.json").read_text())["places"]}
    for lane in t["lanes"]:
        dest = lane["destination"]
        assert dest["port"] in ports
        if "hex" in dest:
            assert places[dest["port"]]["hex"] == dest["hex"]
    for rp in t["rally_points"]:
        if rp["kind"] == "place":
            assert places[rp["id"]]["hex"] == rp["hex"]


def test_opening_turns_follow_the_calendar():
    t = _t("convoy-lanes")
    cal = {r["game_turn"]: (r["year"], r["month"], r["week"]) for r in _t("calendar")["rows"]}
    by = {r["lane"]: r for r in t["lanes"]}
    assert cal[by[4]["first_game_turn"]] == cal[by[5]["first_game_turn"]] == (1941, 5, 2)  # 56.14
    assert cal[by[1]["first_game_turn"]] == (1941, 6, 1) and by[1]["activation_roll"]  # 55.17
    # Graziani's Offensive (September 1940) may use lanes 2, 3 and 6 only (60.37): exactly the open ones
    assert sorted(n for n, r in by.items() if r["first_game_turn"] is None) == [2, 3, 6]


def test_lane_numbers_are_the_bombing_chart_routes():
    assert _t("axis-convoy-bombing")["routes"] == [r["lane"] for r in _t("convoy-lanes")["lanes"]]
