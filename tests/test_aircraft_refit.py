import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "aircraft-refit.json").read_text())


def test_by_squadron_covers_every_modified_roll_once():
    faces = [f for r in TABLE["by_squadron"] for f in range(r["die"]["from"], r["die"]["to"] + 1)]
    assert faces == list(range(1, 10))


def test_worse_rolls_never_refit_more():
    pct = [r["percent_refitted"] for r in TABLE["by_squadron"]]
    assert pct == sorted(pct, reverse=True) and pct[0] == 100 and pct[-1] == 33
