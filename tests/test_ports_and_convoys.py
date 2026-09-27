"""Port Capacity and Efficiency Level Chart (SPI 55.3), Axis Naval Convoy Level Chart (56.4) and
Axis Naval Convoy Capacity Table (56.5). Cells read by hand from scan jp2 109 and 178."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t(name):
    return json.loads((ROOT / "data" / "tables" / f"{name}.json").read_text())


def test_port_capacity():
    t = _t("port-capacity")
    by = {r["port"]: r for r in t["rows"]}
    assert list(by) == ["tripoli", "bizerta", "alexandria", "tobruk", "benghazi", "mersa-matruh",
                        "bardia", "sollum", "derna", "all-others"]
    tob = by["tobruk"]
    assert (tob["efficiency_level"], tob["sp_in"], tob["sp_out"], tob["max_tons"]) == (5, 1, 3, 1700)
    assert (by["benghazi"]["efficiency_level"], by["benghazi"]["max_tons"]) == (3, 2500)  # also the 55.14 example
    assert by["bizerta"]["max_tons"] == 3333 and by["alexandria"]["sp_in"] == 5
    assert by["bardia"]["sp_in"] == 0 and by["bardia"]["sp_in_zero_sp_unit"] is True
    assert by["derna"]["sp_in"] is None and by["all-others"]["sp_out"] is None
    assert sum(r["max_tons"] for r in t["rows"]) == 38833  # checksum of the column as read


def test_convoy_level():
    lv = _t("axis-convoy-level")["levels"]
    assert lv["1940"][:8] == [None] * 8 and lv["1940"][8:] == ["B"] * 4
    assert lv["1941"] == list("BEFEDGCECDEA")
    assert lv["1942"] == list("CBBGFAFBDAGC")


def test_convoy_capacity_and_56_21_example():
    t = _t("axis-convoy-capacity")
    by = {r["level"]: r for r in t["rows"]}
    assert [by[k]["fixed_tons"] for k in "ABCDEFG"] == [6000, 7000, 10000, 11000, 11000, 15000, 32000]
    assert [by[k]["tons_per_pip"] for k in "ABCDEFG"] == [1000, 1500, 1500, 2000, 2500, 2000, 3000]
    assert t["round_up_to"] == 1000
    # 56.21: November 1941 is level E; a roll of 4 gives 21,000 tons
    level = _t("axis-convoy-level")["levels"]["1941"][10]
    assert level == "E" and by[level]["fixed_tons"] + 4 * by[level]["tons_per_pip"] == 21000
