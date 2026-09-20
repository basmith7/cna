"""Raid on Rommel Table (SPI 27.92; the chart prints the heading 27.54): two dice, one result."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_rows_cover_two_dice_and_key_results():
    t = json.loads((ROOT / "data" / "tables" / "raid-on-rommel.json").read_text())
    rows = t["rows"]
    covered = sorted(n for r in rows for n in range(r["dice"]["from"], r["dice"]["to"] + 1))
    assert covered == list(range(2, 13))
    by = {r["dice"]["from"]: r for r in rows}
    assert by[2]["result"] == "axis-initiative-3-temporary" and by[2]["turns"] == 2
    assert by[3]["result"] == "lrdg-eliminated" and by[9]["result"] == "lrdg-eliminated" and by[11]["result"] == "lrdg-eliminated"
    assert by[4]["dice"] == {"from": 4, "to": 8} and by[4]["result"] == "none" and by[10]["result"] == "none"
    assert by[12]["result"] == "rommel-removed"
    assert t["lrdg_eliminated_unless_hex_empty"] is True
