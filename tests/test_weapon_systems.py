import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "weapon-systems.json").read_text())


def test_row_counts_per_nation_as_printed():
    assert Counter(r["nation"] for r in TABLE["rows"]) == {"cw": 32, "it": 21, "de": 28}


def test_ids_unique():
    ids = [r["id"] for r in TABLE["rows"]]
    assert len(ids) == len(set(ids))


def test_every_oa_weapon_name_has_a_row():
    ids = {r["id"] for r in TABLE["rows"]}
    assert all(v in ids for names in TABLE["oa_names"].values() for v in names.values())
    missing = set()
    for p in sorted((ROOT / "data" / "oa").glob("*.json")):
        oa = json.loads(p.read_text())
        for f in oa["formations"]:
            for u in f["units"]:
                for t in u["toe"]:
                    if t["weapon"] not in TABLE["oa_names"][oa["nation"]]:
                        missing.add((oa["nation"], t["weapon"]))
    # 'vv' on the RECAM HQ is an ID code where a weapon name belongs; no row
    assert missing == {("it", "vv")}


def test_realigned_rows_keep_what_was_printed():
    printed = {r["weapon"] for r in TABLE["rows"] if "printed" in r}
    assert printed == {"Pz III E", "7.62cm Pak(R)", "Marder III (SP)", "5cm Pak 38"}
