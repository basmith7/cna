"""Formation Organisation Charts (SPI 19.3x): what each parent formation is made of, by organisation
type and game-turn period."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t():
    t = json.loads((ROOT / "data" / "tables" / "formation-organisation.json").read_text())
    return t, {(r["nation"], r["parent"], r.get("type")): r for r in t["rows"]}


def test_every_component_unit_is_keyed():
    t, by = _t()
    for r in t["rows"]:
        for c in r["components"]:
            for u in ([c["unit"]] if "unit" in c else c["any_of"]):
                assert u in t["units"], u


def test_cw_rows():
    t, by = _t()
    assert sum(r["nation"] == "cw" for r in t["rows"]) == 14
    ad1 = by[("cw", "armoured-division", "I")]
    assert ad1["sp"] == 5 and ad1["turns"] == {"from": 1, "to": 18}
    assert ad1["components"] == [{"count": 2, "unit": "armoured-brigade", "sp": 2, "type": "I"}, {"count": 1, "unit": "support-group", "sp": 2, "type": "I"}]
    assert by[("cw", "armoured-division", "II")]["components"][-1] == {"count": 1, "any_of": ["armoured-car-unit", "armoured-recce-unit"], "sp": 1}
    ad4 = by[("cw", "armoured-division", "IV")]
    assert ad4["turns"] == {"from": 92, "to": None}
    assert {c["unit"]: c["count"] for c in ad4["components"] if "unit" in c} == {"armoured-brigade": 1, "infantry-brigade": 1, "artillery-unit": 3, "anti-tank-regiment": 1, "light-aa-unit": 1, "machinegun-battalion": 1, "engineer-battalion": 1}
    inf = by[("cw", "infantry-division", None)]
    assert inf["components"][0] == {"count": 3, "unit": "infantry-brigade", "sp": 2}
    assert any(c.get("unit") == "anti-tank-unit" and c["sp"] is None for c in inf["components"])
    assert by[("cw", "armoured-brigade", "I")]["components"] == [{"count": 3, "unit": "tank-battalion", "sp": 1}]
    assert by[("cw", "armoured-brigade", "II")]["turns_list"] == [{"from": 19, "to": 70}, {"from": 92, "to": None}]
    assert by[("cw", "support-group", "III")]["components"] == [{"count": 3, "unit": "infantry-battalion", "sp": 1}, {"count": 1, "unit": "artillery-unit", "sp": 1}]
    assert by[("cw", "allied-infantry-brigade", None)]["components"][1] == {"count": 1, "any_of": ["artillery-unit", "anti-tank-unit"], "sp": 1}


def test_it_rows():
    t, by = _t()
    assert sum(r["nation"] == "it" for r in t["rows"]) == 12
    assert by[("it", "tank-group", None)]["turns"] == {"from": 1, "to": 26} and by[("it", "tank-group", None)]["components"] == [{"count": 2, "unit": "tank-regiment", "sp": 3}]
    assert by[("it", "tank-regiment-3sp", None)]["components"] == [{"count": 5, "unit": "tank-battalion", "sp": 1}]
    assert by[("it", "libyan-or-parachute-infantry-division", None)]["components"][1] == {"count": 1, "unit": "anti-tank-company", "sp": 0}
    assert by[("it", "recam", None)]["components"][0] == {"count": 1, "unit": "armoured-car-battalion", "sp": 1}


def test_de_rows():
    t, by = _t()
    assert sum(r["nation"] == "de" for r in t["rows"]) == 11
    assert by[("de", "15-panzer-division", None)]["components"][1] == {"count": 1, "unit": "15-infantry-brigade", "sp": 3}
    assert by[("de", "armoured-regiment", None)]["components"] == [{"count": 2, "unit": "tank-battalion", "sp": 1}]
    assert by[("de", "288-sonderverband", None)]["components"][-1] == {"count": 1, "unit": "engineer-company", "sp": 0}
    assert by[("de", "ramcke-brigade", None)]["sp"] == 3
