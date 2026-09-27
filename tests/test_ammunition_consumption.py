"""Ammunition Consumption Rates Chart (SPI 50.2): Ammunition Points spent per action,
for the Logistics Game played (per TOE Strength Point) and abstracted (per unit)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _table():
    t = json.loads((ROOT / "data" / "tables" / "ammunition-consumption.json").read_text())
    return t, {(r["mode"], r["action"]): r for r in t["rows"]}


def test_shape():
    t, by = _table()
    assert len(by) == len(t["rows"]) == 14
    assert sum(1 for m, _ in by if m == "played") == 7
    assert sum(1 for m, _ in by if m == "abstracted") == 7


def test_cells_read_from_scan():
    _, by = _table()
    assert by[("played", "barrage")]["ammo"] == 4  # 50.14's example uses this rate
    assert by[("played", "anti-armour")]["ammo"] == 3
    assert by[("played", "close-assault")]["ammo"] == 2
    assert by[("played", "close-assault")]["applies_to"] == [
        "armor-class", "gun-class", "mg-infantry", "heavy-weapons-infantry"]
    assert by[("played", "anti-air")]["ammo"] == 2
    assert by[("played", "air-combat-or-strafe")]["ammo"] == "tacair-bombload"
    assert by[("abstracted", "barrage-phasing")]["ammo"] == 4
    assert by[("abstracted", "barrage-non-phasing")]["ammo"] == 2
    assert by[("abstracted", "assault-phasing")]["ammo"] == 1
    assert by[("abstracted", "non-fighter-flight")]["ammo"] == "bombload"


def test_sources():
    t, _ = _table()
    for r in t["rows"]:
        assert "CNA1979:50.2" in r["sources"] and "scan:p107" in r["sources"]
