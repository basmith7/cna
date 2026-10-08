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
