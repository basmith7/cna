import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "reinforcement-schedule.json").read_text())
OA = {u["id"]: u for p in (ROOT / "data" / "oa").glob("*.json")
      for f in json.loads(p.read_text())["formations"] for u in f["units"]}


def test_schedule_agrees_with_oa_arrivals():
    for row in TABLE["rows"]:
        for uid in row["units"]:
            assert OA[uid]["arrives"] == {"game_turn": row["game_turn"], "opstage": row["opstage"]}, uid


def test_rows_stop_at_the_transcribed_turn():
    assert all(r["game_turn"] <= TABLE["through"] for r in TABLE["rows"])
