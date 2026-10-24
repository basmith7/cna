import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "unit-characteristics.json").read_text())


def test_row_counts_per_nation_as_printed():
    assert Counter(r["nation"] for r in TABLE["rows"]) == {"cw": 43, "it": 50, "de": 31}


def test_one_row_per_nation_and_id_code():
    keys = [(r["nation"], r["id_code"]) for r in TABLE["rows"]]
    assert len(keys) == len(set(keys))


def test_every_oa_id_code_has_a_row():
    known = {(r["nation"], r["id_code"]) for r in TABLE["rows"]}
    missing = []
    for p in sorted((ROOT / "data" / "oa").glob("*.json")):
        oa = json.loads(p.read_text())
        for f in oa["formations"]:
            for u in f["units"]:
                if u["id_code"] and (oa["nation"], u["id_code"]) not in known:
                    missing.append((u["id"], u["id_code"]))
    assert missing == []


def test_only_the_two_mixed_rows_defer_their_equivalent_to_the_unit():
    by_unit = sorted((r["nation"], r["id_code"]) for r in TABLE["rows"] if r["equivalent"] == "by-unit")
    assert by_unit == [("cw", "uu"), ("de", "gg")]


def test_every_by_unit_oa_unit_names_its_equivalent():
    by_unit = {(r["nation"], r["id_code"]) for r in TABLE["rows"] if r["equivalent"] == "by-unit"}
    wrong = []
    for p in sorted((ROOT / "data" / "oa").glob("*.json")):
        oa = json.loads(p.read_text())
        for f in oa["formations"]:
            for u in f["units"]:
                if ((oa["nation"], u["id_code"]) in by_unit) != ("equivalent" in u):
                    wrong.append(u["id"])
    assert wrong == []


def test_every_oa_headquarters_and_only_headquarters_has_an_echelon():
    hq = {(r["nation"], r["id_code"]) for r in TABLE["rows"] if r["unit_type"] == "Headquarters"}
    wrong, levels = [], Counter()
    for p in sorted((ROOT / "data" / "oa").glob("*.json")):
        oa = json.loads(p.read_text())
        for f in oa["formations"]:
            for u in f["units"]:
                if ((oa["nation"], u["id_code"]) in hq) != ("echelon" in u):
                    wrong.append(u["id"])
                if "echelon" in u:
                    levels[u["echelon"]] += 1
                    # a division HQ is always independent (19.1x), so it never has a parent
                    if u["echelon"] == "division" and u["parent"]:
                        wrong.append(u["id"])
    assert wrong == []
    assert levels == {"division": 45, "brigade": 140, "battle-group": 6, "corps": 1}


def test_every_reconnaissance_unit_and_only_those_has_a_vehicle_class():
    recon = {(r["nation"], r["id_code"]) for r in TABLE["rows"] if "Rec" in r["unit_type"]}
    bar = {r["vehicle"] for r in json.loads((ROOT / "data" / "tables" / "breakdown-adjustments.json").read_text())["rows"]}
    wrong, by_row = [], {}
    for p in sorted((ROOT / "data" / "oa").glob("*.json")):
        oa = json.loads(p.read_text())
        for f in oa["formations"]:
            for u in f["units"]:
                key = (oa["nation"], u["id_code"])
                if (key in recon) != ("vehicle" in u) or u.get("vehicle", "none") not in bar | {"none"}:
                    wrong.append(u["id"])
                if "vehicle" in u:
                    by_row.setdefault(key, set()).add(u["vehicle"])
    assert wrong == []
    # the Axis chart notes give ee, ff, vv and ww a BAR of 1 left: armoured cars
    for key in [("de", "ee"), ("de", "ff"), ("it", "vv"), ("it", "ww")]:
        assert by_row[key] == {"armoured-car"}
    # only the Commonwealth chart leaves the split to the unit (R-125)
    assert {k for k, v in by_row.items() if len(v) > 1} == {("cw", "ll")}
