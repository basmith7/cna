"""Desert raider counters (SPI 27.11, 27.13, 27.2; R-147): pieces of their own, formable in play."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _units(nation):
    oa = json.loads((ROOT / "data" / "oa" / f"{nation}.json").read_text())
    return [u for f in oa["formations"] for u in f["units"]]


def test_two_lrdg_and_one_dsa_with_27_14_values():
    raiders = {u["id"]: u for n in ("cw", "de", "it") for u in _units(n) if "raider" in u}
    assert sorted(raiders) == ["unit:cw:lrdg-1", "unit:cw:lrdg-2", "unit:de:dsa"]
    for u in raiders.values():
        r = u["raider"]
        assert u["id_code"] is None and u["toe"] == [] and u["fills"] == []
        assert (r["cpa"], r["stacking_points"], r["combat_ratings"], r["breaks_down"]) == (50, 0, False, False)
    assert raiders["unit:cw:lrdg-1"]["raider"]["max_in_play"] == 2
    assert raiders["unit:de:dsa"]["raider"] == raiders["unit:de:dsa"]["raider"] | {"kind": "dsa", "max_in_play": 1}


def test_each_raider_can_be_formed_from_a_unit_of_its_own_nation():
    # 27.13: only recce/armoured-car TOE points; 27.2b: the DSA from German units only.
    for nation, rid in (("cw", "unit:cw:lrdg-1"), ("de", "unit:de:dsa")):
        units = _units(nation)
        r = next(u for u in units if u["id"] == rid)["raider"]
        donors = [u for u in units if u.get("vehicle") in r["formed_from_vehicle"]]
        assert donors, f"no {nation} unit can form {rid}"


def test_rommels_arrival_places_one_lrdg_at_jalo():
    s = json.loads((ROOT / "data" / "scenarios" / "rommels-arrival.json").read_text())
    text = json.dumps(s)
    assert text.count("unit:cw:lrdg-") == 1 and '"unit": "unit:cw:lrdg-1"' in text
