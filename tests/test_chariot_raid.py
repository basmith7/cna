"""Chariot Raid Table (SPI 30.46): one die decides how many dice of damage the raid does."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_rows():
    t = json.loads((ROOT / "data" / "tables" / "chariot-raid.json").read_text())
    rows = t["rows"]
    assert sorted(n for r in rows for n in range(r["die"]["from"], r["die"]["to"] + 1)) == [1, 2, 3, 4, 5, 6]
    by = {r["die"]["from"]: r["damage_dice"] for r in rows}
    assert by == {1: 3, 2: 2, 4: 1, 6: 0}
