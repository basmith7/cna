"""Fuel evaporation and spillage rates (SPI 49.3), printed in the rules text on jp2 66."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _table():
    t = json.loads((ROOT / "data" / "tables" / "fuel-evaporation.json").read_text())
    return t, {r["id"]: r for r in t["rows"]}


def test_fuel_evaporation_shape_and_rates():
    t, by = _table()
    assert len(by) == len(t["rows"]) == 3
    assert by["standard"]["percent"] == 6 and by["standard"]["when"] == "stores-expenditure-stage"
    assert by["hot-weather"]["percent"] == 5 and by["hot-weather"]["when"] == "hot-weather-determined"
    cw = by["commonwealth-1940-41"]
    assert cw["percent"] == 9 and cw["replaces"] == "standard"
    assert all(r["rounding"] == "down" for r in t["rows"])
    assert "scan:p66" in t["sources"]
