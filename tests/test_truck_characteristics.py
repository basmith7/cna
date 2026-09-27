"""Truck Characteristics Chart (SPI 54.2): what one truck point of each class carries, its CPAs, fuel and breakdown."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _by():
    t = json.loads((ROOT / "data" / "tables" / "truck-characteristics.json").read_text())
    return t, {r["truck"]: r for r in t["rows"]}


def test_shape():
    t, by = _by()
    assert set(by) == {"light", "medium", "heavy"} and len(t["rows"]) == 3


def test_cells_read_from_scan():
    _, by = _by()
    assert by["light"]["cpa"] == {"infantry": 25, "guns": None, "supplies": 40}
    assert by["medium"]["cpa"] == {"infantry": 20, "guns": 15, "supplies": 30}
    assert by["light"]["toe"] == {"infantry": 0.5, "artillery": None, "anti_aircraft": 1}
    assert by["heavy"]["toe"] == {"infantry": 2, "artillery": 1, "anti_aircraft": 4}
    assert by["heavy"]["supply_points"] == {"ammo": 8, "fuel": 250, "stores": 30, "water": 200}
    assert by["medium"]["supply_points"] == {"ammo": 4, "fuel": 120, "stores": 15, "water": 100}
    assert by["light"]["supply_points"] == {"ammo": 2, "fuel": 50, "stores": 6, "water": 40}
    assert [by[k]["fuel_capacity"] for k in ("light", "medium", "heavy")] == [8, 6, 6]
    assert all(r["fuel_consumption"] == 1 and r["bar"] == "2L" for r in by.values())
    assert by["light"]["off_road_extra_breakdown"] is True
    assert "off_road_extra_breakdown" not in by["heavy"]


def test_heavy_carries_at_least_medium():
    _, by = _by()
    for k, v in by["medium"]["supply_points"].items():
        assert by["heavy"]["supply_points"][k] >= v >= by["light"]["supply_points"][k]
