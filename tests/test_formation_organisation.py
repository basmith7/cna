"""Formation Organisation Charts (SPI 19.3x): what each parent formation is made of, by organisation
type and game-turn period."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _strip(c):
    return {k: v for k, v in c.items() if k != "counts_for_shell"}


def _t():
    t = json.loads((ROOT / "data" / "tables" / "formation-organisation.json").read_text())
    for r in t["rows"]:
        r["shell_base"] = sum(c["count"] for c in r["components"] if c["counts_for_shell"])
        r["components"] = [_strip(c) for c in r["components"]]
    return t, {(r["nation"], r["parent"], r.get("type"), (r.get("turns") or {}).get("from")): r for r in t["rows"]}


def _row(by, nation, parent, type_=None):
    (row,) = [r for k, r in by.items() if k[:3] == (nation, parent, type_)]
    return row


def test_every_component_unit_is_keyed():
    t, by = _t()
    for r in t["rows"]:
        for c in r["components"]:
            for u in ([c["unit"]] if "unit" in c else c["any_of"]):
                assert u in t["units"], u


def test_cw_rows():
    t, by = _t()
    assert sum(r["nation"] == "cw" for r in t["rows"]) == 15  # 14 printed rows, type II armoured brigade in two periods
    ad1 = _row(by, "cw", "armoured-division", "I")
    assert ad1["sp"] == 5 and ad1["turns"] == {"from": 1, "to": 18}
    assert ad1["components"] == [{"count": 2, "unit": "armoured-brigade", "sp": 2, "type": "I"}, {"count": 1, "unit": "support-group", "sp": 2, "type": "I"}]
    assert _row(by, "cw", "armoured-division", "II")["components"][-1] == {"count": 1, "any_of": ["armoured-car-unit", "armoured-recce-unit"], "sp": 1}
    ad4 = _row(by, "cw", "armoured-division", "IV")
    assert ad4["turns"] == {"from": 92, "to": None}
    assert {c["unit"]: c["count"] for c in ad4["components"] if "unit" in c} == {"armoured-brigade": 1, "infantry-brigade": 1, "artillery-unit": 3, "anti-tank-regiment": 1, "light-aa-unit": 1, "machinegun-battalion": 1, "engineer-battalion": 1}
    inf = _row(by, "cw", "infantry-division", None)
    assert inf["components"][0] == {"count": 3, "unit": "infantry-brigade", "sp": 2}
    assert any(c.get("unit") == "anti-tank-unit" and c["sp"] is None for c in inf["components"])
    assert _row(by, "cw", "armoured-brigade", "I")["components"] == [{"count": 3, "unit": "tank-battalion", "sp": 1}]
    ab2 = [r for r in t["rows"] if (r["nation"], r["parent"], r.get("type")) == ("cw", "armoured-brigade", "II")]
    assert [r["turns"] for r in ab2] == [{"from": 19, "to": 70}, {"from": 92, "to": None}]
    assert ab2[0]["components"] == ab2[1]["components"]
    assert _row(by, "cw", "support-group", "III")["components"] == [{"count": 3, "unit": "infantry-battalion", "sp": 1}, {"count": 1, "unit": "artillery-unit", "sp": 1}]
    assert _row(by, "cw", "allied-infantry-brigade", None)["components"][1] == {"count": 1, "any_of": ["artillery-unit", "anti-tank-unit"], "sp": 1}


def test_it_rows():
    t, by = _t()
    assert sum(r["nation"] == "it" for r in t["rows"]) == 12
    assert _row(by, "it", "tank-group", None)["turns"] == {"from": 1, "to": 26} and _row(by, "it", "tank-group", None)["components"] == [{"count": 2, "unit": "tank-regiment", "sp": 3}]
    assert _row(by, "it", "tank-regiment-3sp", None)["components"] == [{"count": 5, "unit": "tank-battalion", "sp": 1}]
    assert _row(by, "it", "libyan-or-parachute-infantry-division", None)["components"][1] == {"count": 1, "unit": "anti-tank-company", "sp": 0}
    assert _row(by, "it", "recam", None)["components"][0] == {"count": 1, "unit": "armoured-car-battalion", "sp": 1}


def test_de_rows():
    t, by = _t()
    assert sum(r["nation"] == "de" for r in t["rows"]) == 11
    assert _row(by, "de", "15-panzer-division", None)["components"][1] == {"count": 1, "unit": "15-infantry-brigade", "sp": 3}
    assert _row(by, "de", "armoured-regiment", None)["components"] == [{"count": 2, "unit": "tank-battalion", "sp": 1}]
    assert _row(by, "de", "288-sonderverband", None)["components"][-1] == {"count": 1, "unit": "engineer-company", "sp": 0}
    assert _row(by, "de", "ramcke-brigade", None)["sp"] == 3


def test_every_row_has_one_set_of_turns():
    t, _ = _t()
    for r in t["rows"]:
        assert "turns_list" not in r


def test_shell_base_r141():
    """9.26 counts brigade-equivalents in a division and battalions in a brigade or regiment (R-141)."""
    t, by = _t()
    # a CW infantry division counts its three brigades, not its battalions
    assert _row(by, "cw", "infantry-division")["shell_base"] == 3
    # a CW 3 SP brigade counts its 1 SP components only: not the unfigured anti-tank, recce or 'unit' slots
    assert _row(by, "cw", "infantry-brigade-3sp")["shell_base"] == 5
    # 0 SP companies never count
    assert _row(by, "de", "288-sonderverband")["shell_base"] == 4
    assert _row(by, "it", "libyan-or-parachute-infantry-division")["shell_base"] == 2
    # the 5th Light's only brigade-equivalent is its armoured regiment
    assert _row(by, "de", "5-leichte-panzer-division")["shell_base"] == 1
    # the 15th Infantry Brigade is built of regiments, and counts them
    assert _row(by, "de", "15-infantry-brigade")["shell_base"] == 3
