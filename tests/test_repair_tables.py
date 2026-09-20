"""Broken Down Vehicle Repair Table (SPI 22.8) and Destroyed Tanks Repair Table (SPI 22.44)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t(name):
    return json.loads((ROOT / "data" / "tables" / f"{name}.json").read_text())


def test_vehicle_repair_covers_die_0_to_8_and_never_improves_with_the_roll():
    t = _t("vehicle-repair")
    faces = sorted(f for r in t["rows"] for f in range(r["die"]["from"], r["die"]["to"] + 1))
    assert faces == list(range(0, 9))
    for col in ("field_truck", "field_armoured_car", "field_tank_percent", "temporary_facility_percent", "major_facility_percent"):
        vals = [r[col] for r in t["rows"] if r[col] is not None]
        assert vals == sorted(vals, reverse=True), col
    assert all(r["field_truck"] is None for r in t["rows"] if r["die"]["from"] >= 7)   # field repair is a d6


def test_destroyed_tank_repair_covers_die_1_to_7_with_known_results():
    t = _t("destroyed-tank-repair")
    faces = sorted(f for r in t["rows"] for f in range(r["die"]["from"], r["die"]["to"] + 1))
    assert faces == list(range(1, 8))
    cols = ["field", "axis_facility_german", "axis_facility_italian", "axis_facility_commonwealth", "cw_facility"]
    for r in t["rows"]:
        for c in cols:
            assert r[c] in ("repaired", "junked", None)
    assert all(r["field"] is None for r in t["rows"] if r["die"]["from"] > 1)
