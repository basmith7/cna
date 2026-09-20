"""Desert Raider Raids Table (SPI 27.91): per target, the die results and the raid's conditions."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_targets_and_key_values():
    t = json.loads((ROOT / "data" / "tables" / "desert-raider-raids.json").read_text())
    by = {r["target"]: r for r in t["rows"]}
    assert len(by) == len(t["rows"]) == 7
    assert t["cp_cost"] == 5 and t["combined_airfield_and_planes_cp"] == 10
    assert by["water-pipeline"]["die"] == [{"from": 1, "to": 4, "result": "destroyed"}, {"from": 5, "to": 6, "result": "none"}]
    assert by["water-pipeline"]["limit"] == "once-per-raider-per-stage"
    assert by["airfield"]["die"][0] == {"from": 1, "to": 2, "result": "reduce-level"}
    assert by["airfield"]["not_if_combat_units"] is True and by["airfield"]["limit"] == "once-per-target-per-turn"
    planes = by["planes-on-ground"]["die"]
    assert planes[0] == {"from": 1, "to": 2, "result": "destroy-percent", "percent": 10}
    assert planes[2] == {"from": 6, "to": 6, "result": "none", "raider_eliminated": True}
    assert by["rommel"]["see"] == "table:raid-on-rommel" and by["rommel"]["lrdg_only"] is True
    g = by["supply-dump-guarded"]
    assert g["guard_check"] == {"dice": 2, "survive_if_sum_at_least": "raw-close-assault-defence", "else": "raider-eliminated"} and g["then"] == "supply-dump"
    d = by["supply-dump"]["die"]
    assert d[0] == {"from": 1, "to": 2, "result": "destroy-percent", "percent": 10}
    assert d[2] == {"from": 6, "to": 6, "result": "none", "raider_eliminated_if_combat_units": True}
    tr = by["truck-convoy"]["die"]
    assert tr[0] == {"from": 1, "to": 2, "result": "truck-points-lost", "points": 1}
    assert tr[2]["reroll_if_infantry_replacements"] == {"from": 5, "to": 6, "result": "raider-eliminated"}
    assert by["truck-convoy"]["all_infantry_replacements"] == "raider-eliminated"
