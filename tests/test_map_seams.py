import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SEAMS = json.loads((ROOT / "data" / "map" / "seams.json").read_text())


def test_seams_file_is_fresh():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "map_seams.py"), "--check"])
    assert r.returncode == 0, "run tools/map_seams.py"


def test_pair_counts_match_the_vassal_geometry():
    # derived independently from the VASSAL board's zone origins (EXTRACTION.md)
    assert {f"{s['west']}|{s['east']}": len(s["pairs"]) for s in SEAMS["seams"]} == \
        {"A|B": 112, "B|C": 99, "C|D": 83, "D|E": 65}


def test_every_sheet_edge_slope_and_escarpment_meets_its_twin():
    hexes = json.loads((ROOT / "data" / "map" / "hexes.json").read_text())["hexes"]
    assert hexes
    for s in SEAMS["seams"]:
        for p in s["pairs"]:
            assert not {"slope", "escarpment"} & set(p.get("one_side_only", []))


def test_hexes_exist():
    ids = {h["id"] for h in json.loads((ROOT / "data" / "map" / "hexes.json").read_text())["hexes"]}
    assert all(p["west"] in ids and p["east"] in ids for s in SEAMS["seams"] for p in s["pairs"])
