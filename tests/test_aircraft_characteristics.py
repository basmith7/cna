import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "aircraft-characteristics.json").read_text())


def test_row_counts_as_printed():
    assert Counter(r["nation"] for r in TABLE["rows"]) == {"cw": 68, "it": 20, "de": 14}


def test_ids_unique_and_alternatives_point_at_a_row():
    ids = [r["id"] for r in TABLE["rows"]]
    assert len(ids) == len(set(ids))
    assert all(r["alternative_of"] in ids for r in TABLE["rows"] if "alternative_of" in r)


def test_fighters_and_bombers_use_their_own_mission_columns():
    for r in TABLE["rows"]:
        want = {"F", "S", "R", "D"} if r["table"] == "fighter" else {"D", "R", "B", "Transport"}
        assert set(r["missions"]) == want, r["id"]
