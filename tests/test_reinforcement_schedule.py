import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "reinforcement-schedule.json").read_text())
OA = {u["id"]: u for p in (ROOT / "data" / "oa").glob("*.json")
      for f in json.loads(p.read_text())["formations"] for u in f["units"]}


# Units whose OA sheet prints a different arrival from the schedule (both charts read twice).
PRINTED_DISAGREEMENTS = {"unit:cw:22-gds", "unit:de:5-pz-regt-hq", "unit:de:i-5-pz-bn", "unit:de:ii-5-pz-bn", "unit:de:2-mg-bn",
                         "unit:cw:102nd-anti-tank-regt", "unit:cw:22-armd-bde-hq", "unit:cw:78-fld"}


def test_schedule_agrees_with_oa_arrivals():
    mismatches = set()
    for row in TABLE["rows"]:
        if any("returns" in n for n in row.get("notes", [])) or row["kind"] != "arrives":
            continue
        for uid in row["units"]:
            if OA[uid]["arrives"] != {"game_turn": row["game_turn"], "opstage": row["opstage"]}:
                mismatches.add(uid)
    assert mismatches == PRINTED_DISAGREEMENTS


def test_rows_stop_at_the_transcribed_turn():
    assert all(r["game_turn"] <= TABLE["through"] for r in TABLE["rows"])
