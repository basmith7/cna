"""One-die lookup tables from the chart sheet: prisoners captured (15.89), patrol reconnaissance
(16.7), objective loss (16.8) and the SAS raid (27.93). Each covers die faces 1–6 exactly once."""
import json
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t(name):
    return json.loads((ROOT / "data" / "tables" / f"{name}.json").read_text())


@pytest.mark.parametrize("name", ["prisoners-captured", "sas-raid", "objective-loss"])
def test_die_faces_covered_once(name):
    faces = sorted(f for r in _t(name)["rows"] for f in range(r["die"]["from"], r["die"]["to"] + 1))
    assert faces == [1, 2, 3, 4, 5, 6]


def test_prisoner_and_raid_percentages_never_fall():
    for name, key in (("prisoners-captured", "percent"), ("sas-raid", "percent")):
        vals = [r[key] for r in _t(name)["rows"]]
        assert vals == sorted(vals)


def test_patrol_reconnaissance_grid():
    t = _t("patrol-reconnaissance")
    assert [r["die"] for r in t["rows"]] == [1, 2, 3, 4, 5, 6]
    for r in t["rows"]:
        assert list(r["units_revealed"]) == ["1", "2", "3"]
        vals = [r["units_revealed"][k] for k in ("1", "2", "3")]
        nums = [v for v in vals if v != "all"]
        assert nums == sorted(nums)
    assert t["rows"][-1]["units_revealed"]["3"] == "all"
