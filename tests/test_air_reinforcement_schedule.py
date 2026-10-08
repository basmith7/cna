import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "air-reinforcement-schedule.json").read_text())


def test_entries_run_in_turn_order_without_overlap():
    spans = [(r["game_turns"]["from"], r["game_turns"]["to"]) for r in TABLE["rows"]]
    assert len(spans) == 28 and spans[0] == (2, 2) and spans[-1] == (107, 110)
    assert all(a[1] < b[0] for a, b in zip(spans, spans[1:]))


def test_month_entries_are_four_turns():
    for r in TABLE["rows"][4:]:
        assert r["game_turns"]["to"] - r["game_turns"]["from"] == 3, r["period"]
