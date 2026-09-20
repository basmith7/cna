"""Axis Replacement Pool (SPI 20.66): truck production (a), German and Italian production charts —
per type the lifetime total, cap per period, planning dates and convoy tonnage."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t():
    return json.loads((ROOT / "data" / "tables" / "axis-replacement-pool.json").read_text())


def test_trucks():
    t = _t()
    by = {r["item"]: r for r in t["trucks"]["rows"]}
    assert t["trucks"]["arrive_turns_later"] == 2
    assert by["light"]["total"] == 835 and by["light"]["tonnage"] == 45
    assert by["light"]["periods"] == [{"max": 4, "max_per": "turn", "from_turn": 4, "to_turn": 12}, {"max": 15, "max_per": "turn", "from_turn": 13}]
    assert by["medium"]["total"] == 2890 and by["medium"]["periods"][1] == {"max": 50, "max_per": "turn", "from_turn": 13}
    assert by["heavy"]["total"] == 525 and by["heavy"]["tonnage"] == 150 and by["heavy"]["periods"][0] == {"max": 3, "max_per": "turn", "from_turn": 5, "to_turn": 12}


def test_german():
    t = _t()
    by = {r["item"]: r for r in t["german"]["rows"]}
    assert len(by) == len(t["german"]["rows"]) == 23
    assert by["infantry"] == {"item": "infantry", "total": 400, "tonnage": 30, "periods": [{"max": 12, "max_per": "turn", "from_turn": 38}], "sources": ["CNA1979:20.66", "scan:p175"]}
    assert by["armed-recce"]["periods"] == [{"max": 2, "max_per": "fortnight", "from_turn": 47}]
    assert by["heavy-aa"]["periods"] == [{"max": 1, "max_per": "month", "from_turn": 59}] and by["heavy-aa"]["tonnage"] == 65
    assert by["17cm-k18"]["tonnage"] == 206 and by["21cm-mrs18"]["tonnage"] == 197
    assert by["sp-10-5cm"]["periods"] == [{"max": 3, "max_per": "month", "from_turn": 63}]
    assert by["2-8cm-spzb41"]["total"] == 15 and by["7-62cm-pak-r"]["total"] == 22
    assert by["pziii-e"]["total"] == 38 and by["pziii-h"]["periods"][0]["from_turn"] == 53 and by["pziv-f2-special"]["tonnage"] == 235


def test_italian():
    t = _t()
    by = {r["item"]: r for r in t["italian"]["rows"]}
    assert len(by) == len(t["italian"]["rows"]) == 20
    inf = by["infantry"]
    assert inf["tonnage"] == 30 and inf["periods"] == [{"total": 100, "max": 5, "max_per": "turn", "from_turn": 5, "to_turn": 8},
                                                       {"max": 10, "max_per": "turn", "from_turn": 9, "to_turn": 24},
                                                       {"total": 1100, "max": 25, "max_per": "turn", "from_turn": 25}]
    assert by["armoured-recce"]["autoblinda_41"] is True and by["armoured-recce"]["periods"] == [{"total": 25, "max": 1, "max_per": "turn", "from_turn": 31}]
    assert by["light-aa"]["group"] == "anti-air" and by["light-aa"]["periods"][1] == {"total": 45, "max": 1, "max_per": "turn", "from_turn": 25}
    assert by["105-28-gun"]["periods"][0] == {"total": 3, "max": 1, "max_per": "month", "from_turn": 9, "to_turn": 24}
    assert by["149mm-fr"]["tunis_box"] is True and by["149mm-fr"]["periods"] == [{"total": 10, "max": 2, "max_per": "turn", "from_turn": 39}]
    assert by["ca-l6-40"]["periods"] == [{"total": 5, "max": 1, "max_per": "month", "from_turn": 33, "to_turn": 68}, {"total": 21, "max": 2, "max_per": "turn", "from_turn": 69}]
    assert by["ca-m-14-41"]["tonnage"] == 73
    assert t["italian"]["call_up_max_per_type_per_turn"] == 2 and t["italian"]["no_replacements_for"] == ["m-13-39"]


def test_errata_e014_overlay():
    e = json.loads((ROOT / "data" / "errata" / "E-014.json").read_text())
    assert e["table"] == "axis-replacement-pool" and e["affects"] == ["20.66"]
    assert e["patches"] == [{"op": "replace", "path": "/italian/no_replacements_for", "value": ["m-11-39"]}]
