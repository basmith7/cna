"""Patrol Survival Table (SPI 16.6): one die (minus one for an all-recce patrol, so 0 is possible)
-> killed / captured TOE points of the patrolling force. Faces 0-6 covered once."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_faces_zero_to_six_covered_once_and_losses_rise():
    t = json.loads((ROOT / "data" / "tables" / "patrol-survival.json").read_text())
    faces = sorted(f for r in t["rows"] for f in range(r["die"]["from"], r["die"]["to"] + 1))
    assert faces == [0, 1, 2, 3, 4, 5, 6]
    totals = [r["killed"] + r["captured"] for r in t["rows"]]
    assert totals == sorted(totals) and totals[-1] == 2
    assert t["recce_only_modifier"] == -1
