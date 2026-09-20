"""Replacement Point Conversion Chart (SPI 20.3): what one TOE point of each unit type costs in
replacement points. E-012 removes the SGSU row (SGSUs need no replacement points)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _t():
    return json.loads((ROOT / "data" / "tables" / "replacement-conversion.json").read_text())


def test_every_row_has_a_cost_or_is_free_and_ids_are_unique():
    t = _t()
    ids = [r["unit"] for r in t["rows"]]
    assert len(ids) == len(set(ids)) == 20
    for r in t["rows"]:
        assert r["cost"] == [] or all(alt and all(c["points"] >= 1 for c in alt) for alt in r["cost"])
    assert next(r for r in t["rows"] if r["unit"] == "road-or-rail-construction")["cost"] == []
    assert next(r for r in t["rows"] if r["unit"] == "heavy-weapons")["cost"] == [[{"class": "infantry", "points": 1}, {"class": "gun", "points": 1}]]
    assert next(r for r in t["rows"] if r["unit"] == "armoured-car")["cost"] == [[{"class": "armoured-recce", "points": 2}], [{"class": "light-tank", "points": 1}]]


def test_e012_removes_the_sgsu_row():
    t = _t()
    patch = json.loads((ROOT / "data" / "errata" / "E-012.json").read_text())
    assert patch["table"] == "replacement-conversion"
    idx = next(i for i, r in enumerate(t["rows"]) if r["unit"] == "squadron-ground-support")
    assert patch["patches"] == [{"op": "remove", "path": f"/rows/{idx}"}]
