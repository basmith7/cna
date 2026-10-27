"""Which Formation Organisation Chart slot each OA counter fills (19.3, R-142)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

# Counters the O/A sheets assign beyond their parent's chart row (19.2): they stay assigned but fill no slot.
BEYOND_CHART = {
    "cw": {"14th-bde-anti-tank-coy", "16th-bde-anti-tank-coy", "23rd-bde-anti-tank-coy", "14-nz-lt", "30-laa",
           "61-laa", "40-laa", "2-3-laa", "2-infld", "97-fld", "157-fld", "164-fld", "1-sa-laa", "2-sa-laa"},
    "it": {"iii-monferrato-squadrone", "sahariano-camel-regt-hq", "101st-heavy-wpns-bn", "8th-armored-bersaglieri-bn",
           "iv-66-support-coy", "40th-heavy-wpns-bn", "60th-anti-tank-coy", "17th-anti-tank-coy", "25th-anti-tank-coy",
           "55th-anti-tank-coy", "27th-anti-tank-coy", "64th-anti-tank-coy", "61-anti-tank-coy", "62-anti-tank-coy",
           "63-anti-tank-coy"},
    "de": {"200-schutzen-regt-hq", "613-flak-bn"},
}


def _j(rel):
    return json.loads((ROOT / rel).read_text())


ORG = _j("data/tables/formation-organisation.json")


def _units(nat):
    return {u["id"]: u for f in _j(f"data/oa/{nat}.json")["formations"] for u in f["units"]}


def _slots(row):
    """One entry per counted or uncounted slot: (set of slugs, counts_for_shell)."""
    out = []
    for c in row["components"]:
        slugs = {c["unit"]} if "unit" in c else set(c["any_of"])
        out += [(slugs, c["counts_for_shell"])] * c["count"]
    return out


def _counted_filled(row, counters):
    """Counted slots the counters fill, each counter in one slot: whole counters by augmenting-path matching,
    then part slots from the counters left over (enough for the rows these tests use)."""
    slots = [sl for sl, counted in _slots(row) if counted]
    match = {}

    def place(k, seen):
        for i, sl in enumerate(slots):
            if i not in seen and sl & set(counters[k]["fills"]):
                seen.add(i)
                if i not in match or place(match[i], seen):
                    match[i] = k
                    return True
        return False

    for k in range(len(counters)):
        place(k, set())
    left = [u for k, u in enumerate(counters) if k not in match.values()]
    filled = len(match)
    for i, sl in enumerate(slots):
        for slug in sl & set(ORG["part_slots"]):
            if i in match:
                break
            parts = [u for u in left if slug in u.get("fills_part", [])][:ORG["part_slots"][slug]["min"]]
            if len(parts) == ORG["part_slots"][slug]["min"]:
                left = [u for u in left if u not in parts]
                match[i] = None
                filled += 1
    return filled


def _row(nat, parent):
    (r,) = [r for r in ORG["rows"] if r["nation"] == nat and r["parent"] == parent and "type" not in r]
    return r


def test_every_fill_names_a_slug_of_the_chart():
    for nat in ("cw", "it", "de"):
        for u in _units(nat).values():
            for s in u["fills"] + u.get("fills_part", []):
                assert s in ORG["units"], (u["id"], s)
            for s in u.get("fills_part", []):
                assert s in ORG["part_slots"], (u["id"], s)
    for p in ORG["part_slots"].values():
        assert 1 <= p["min"] <= p["parts"]


def test_every_hq_fills_its_own_organisation():
    for nat in ("cw", "it", "de"):
        for u in _units(nat).values():
            if u.get("organisation"):
                assert u["organisation"] in u["fills"], u["id"]


def test_assigned_counters_fit_their_parent_or_are_beyond_the_chart():
    slugs = {}
    for r in ORG["rows"]:
        for sl, _ in _slots(r):
            slugs.setdefault((r["nation"], r["parent"]), set()).update(sl)
    for nat in ("cw", "it", "de"):
        by = _units(nat)
        misfits = set()
        for u in by.values():
            org = by[u["parent"]].get("organisation") if u["parent"] else None
            if org and not (set(u["fills"]) | set(u.get("fills_part", []))) & slugs[(nat, org)]:
                misfits.add(u["id"].split(":")[2])
        assert misfits == BEYOND_CHART[nat], nat


def test_a_company_never_fills_a_battalion_slot():
    by = _units("cw")
    assert by["unit:cw:kopanski-mg"]["fills"] == ["unit"]
    polish = [u for u in by.values() if u["parent"] == "unit:cw:polish-hq"]
    assert _counted_filled(_row("cw", "infantry-brigade-3sp"), polish) == 4  # of 5: no light AA or MG battalion


def test_surplus_battalions_fill_no_extra_slot():
    by = _units("cw")
    ff = [u for u in by.values() if u["parent"] == "unit:cw:1-freefr-hq"]
    row = _row("cw", "infantry-brigade-3sp")
    assert _counted_filled(row, ff) == 5
    infantry = [u for u in ff if u["id_code"] == "r"]
    assert len(infantry) == 5 and _counted_filled(row, infantry) == 3


def test_artillery_group_takes_three_artillery_counters():
    by = _units("de")
    arty = [u for u in by.values() if u["parent"] == "unit:de:15-pz-div-hq" and "artillery-group" in u.get("fills_part", [])]
    assert sorted(u["id"] for u in arty) == ["unit:de:140-arty-regt", "unit:de:33-arty-regt", "unit:de:i-115-arty-bn"]
    row = _row("de", "15-panzer-division")
    assert _counted_filled(row, arty) == 1
    assert _counted_filled(row, arty[:2]) == 0
    assert by["unit:de:220-arty-regt-hq"]["fills"] == ["artillery-group"]
    assert by["unit:de:arko-104-hq"]["fills"] == []


def test_italian_part_slots_fill_from_one_counter():
    by = _units("it")
    coy = by["unit:it:60th-anti-tank-coy"]
    assert coy["fills_part"] == ["anti-tank-battalion"]
    assert _counted_filled({"components": [{"count": 1, "unit": "anti-tank-battalion", "sp": 1, "counts_for_shell": True}]}, [coy]) == 1
