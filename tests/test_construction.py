"""Construction Chart (SPI 24.17) and Demolition Chart (SPI 24.18): what each item needs to build,
rebuild, block, clear or destroy — builders, supplies, stages and where it may happen."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _rows(name):
    t = json.loads((ROOT / "data" / "tables" / f"{name}.json").read_text())
    return t, {(r["item"], r["situation"]): r for r in t["rows"]}


def test_construction_rows_and_key_values():
    t, by = _rows("construction")
    assert len(by) == len(t["rows"]) == 18  # the chart prints 16 rows; two are 'X rebuild or Y build' pairs
    fort = by[("fortification", "build-or-rebuild")]
    assert fort["supplies"] == {"stores": 30} and fort["stages"] == 3 and fort["one_at_a_time"] is True
    assert fort["builders"] == [{"units": ["any-engineer", "infantry-battalion-3toe"]}]
    assert fort["terrain_not"] == ["salt-marsh", "delta", "major-city"]
    assert by[("real-minefield", "build")]["supplies"] == {"ammo": 15, "stores": 15}
    assert by[("fake-minefield", "build")]["supplies"] == {"stores": 3}
    assert by[("railroad", "build")]["builders"] == [{"units": ["nzrrc"]}]
    assert by[("railroad", "rebuild")]["hexes_per_stage"] == 3
    road = by[("road", "build-or-rebuild")]
    assert road["supplies"] == {"stores": 2} and road["supplies_per_hex"] is True
    assert {o["hexes_per_stage"] for o in road["builders"]} == {1, 3}
    assert by[("temporary-repair-facility", "build")]["supplies"] == {"fuel": 50, "stores": 250}
    assert by[("repair-facility", "rebuild-level")]["enemy_zoc_allowed"] is True
    assert by[("airfield", "build")]["stages"] == 3 and by[("airfield", "build")]["supplies"] == {"fuel": 50, "stores": 100}
    assert by[("air-landing-strip", "build")]["supplies"] == by[("airfield", "rebuild-level")]["supplies"] == {"fuel": 10, "stores": 20}
    assert by[("flying-boat-basin", "build")]["coastal_only"] is True
    port = by[("port", "block-level")]
    assert port["supplies_by_port"] == {"tobruk": {"ammo": 50, "stores": 25}, "other": {"ammo": 25, "stores": 10}}
    assert port["ports_not"] == ["tripoli", "bizerta", "alexandria", "aboukir", "rosetta"]
    assert by[("real-supply-dump", "build")]["cp"] == 3 and by[("real-supply-dump", "build")]["supplies"] == {"stores": 10}
    assert by[("fake-supply-dump", "build")]["cp"] == 2 and "supplies" not in by[("fake-supply-dump", "build")]
    assert t["hot_weather_extra_water"] == 10


def test_demolition_rows_and_key_values():
    t, by = _rows("demolition")
    assert len(by) == len(t["rows"]) == 13
    assert by[("fortification", "reduce-level")]["by_units"] is False
    assert by[("fortification", "reduce-level")]["also_by"] == ["air-bombardment", "barrage"]
    assert by[("fake-minefield", "clear")]["timing"] == "end-of-movement-segment-entered"
    assert by[("real-minefield", "clear")]["builders"] == [{"units": ["any-engineer"]}, {"units": ["tank-battalion-6toe-scorpions"]}]
    assert by[("road", "destroy")]["by_units"] is False and by[("road", "destroy")]["only_by"] == ["air-bombardment", "barrage"]
    assert by[("repair-facility", "dismantle")]["recovers"] == {"fuel": 25, "stores": 120}
    assert by[("water-pipeline", "destroy")]["also_by"] == ["barrage", "strafing", "desert-raider-raid"]
    assert by[("port-tobruk", "unblock-level")]["supplies"] == {"ammo": 25, "stores": 10}
    assert by[("port-benghazi", "unblock-level")]["supplies"] == {"ammo": 100, "stores": 50}
    assert by[("port-benghazi", "unblock-level")]["builders"] == [{"units": ["engineer-battalion", "cw-engineer-hq"], "count": 2}]
    assert by[("port-other", "unblock-level")]["supplies"] == {"ammo": 50, "stores": 25}
    assert by[("fake-supply-dump", "destroy")]["timing"] == "on-entry"
    assert by[("real-supply-dump", "blow")]["timing"] == "cp-percentage"
