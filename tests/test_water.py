"""Water Availability Table (SPI 52.7) and Poisoning and Sweetening Wells Table (SPI 52.8)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t(name):
    return json.loads((ROOT / "data" / "tables" / f"{name}.json").read_text())


def test_water_availability_shape_and_cells():
    t = _t("water-availability")
    by = {r["source"]: r["results"] for r in t["rows"]}
    assert set(by) == {"town", "bir"}
    for res in by.values():
        assert [c["die"] for c in res] == [1, 2, 3, 4, 5, 6]
        pts = [c["points"] for c in res]
        assert pts == sorted(pts)  # yield never falls as the die rises
    # read by hand from jp2 108
    assert [c["points"] for c in by["town"]] == [100, 150, 200, 300, 350, 500]
    assert [c["points"] for c in by["bir"]] == [50, 100, 150, 200, 300, 400]
    assert [c["depletion_check"] for c in by["town"]] == [False] * 4 + [True] * 2
    assert [c["depletion_check"] for c in by["bir"]] == [False] * 3 + [True] * 3
    assert t["depletion_roll"] == {"dice": 1, "depleted_on": [1], "secret": True}
    assert set(t["unlimited_sources"]) == {"major-city", "oasis"}


def test_poisoning_and_sweetening():
    t = _t("well-poisoning")
    by = {r["attempt"]: r for r in t["rows"]}
    assert set(by) == {"poison", "sweeten"}
    assert by["poison"]["success_on"] == [1] and by["poison"]["cp"] == 1
    assert by["sweeten"]["success_on"] == [1, 2, 3] and by["sweeten"]["cp"] == 5
    assert by["poison"]["retry_same_stage"] is False
    assert by["sweeten"]["retry_same_stage"] is True
