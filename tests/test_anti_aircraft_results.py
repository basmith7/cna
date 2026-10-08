import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "anti-aircraft-results.json").read_text())
ROLLS = [r for r in range(11, 67) if 1 <= r % 10 <= 6]


def _faces(span):
    return [r for r in ROLLS if span["from"] <= r <= span["to"]]


def test_every_column_of_every_block_covers_each_roll_once():
    blocks = [TABLE["fighter_missions"], TABLE["other_missions"]["destroyed"], TABLE["other_missions"]["aborted"]]
    for block in blocks:
        for i in range(len(TABLE["columns"])):
            got = [f for row in block if row["dice"][i] for f in _faces(row["dice"][i])]
            assert sorted(got) == ROLLS


def test_shape_as_printed():
    assert len(TABLE["columns"]) == 10
    assert [len(TABLE["fighter_missions"]), len(TABLE["other_missions"]["destroyed"]), len(TABLE["other_missions"]["aborted"])] == [4, 6, 8]
