"""Axis Airplane Reinforcement Chart (34.87, printed as 34.85), read from scan jp2 176."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLES = ROOT / "data" / "tables"


def _rows():
    return json.loads((TABLES / "axis-air-reinforcement-schedule.json").read_text())["rows"]


def test_entries_as_read():
    rows = _rows()
    assert len(rows) == 28 and sum(len(r["arrivals"]) for r in rows) == 286
    assert sum(a["count"] for r in rows for a in r["arrivals"] if a["count"] is not None) == 5061  # checksum as read
    first = rows[0]
    assert first["game_turns"] == {"from": 2, "to": 2}
    assert first["arrivals"] == [{"nation": "italian", "count": 12, "aircraft": "Ba65"}]
    # the Germans' first month
    feb41 = next(r for r in rows if r["game_turns"]["from"] == 19)
    assert [(a["count"], a["aircraft"]) for a in feb41["arrivals"] if a["nation"] == "german"] == [
        (30, "Bf110"), (15, "FW200C"), (30, "Ju87B"), (36, "Ju88D")]
    assert all(a["nation"] == "italian" for r in rows if r["game_turns"]["from"] < 19 for a in r["arrivals"])


def test_the_one_unreadable_count():
    unread = [(r["game_turns"]["from"], a) for r in _rows() for a in r["arrivals"] if a["count"] is None]
    assert unread == [(63, {"nation": "italian", "count": None, "count_as_printed": "B", "aircraft": "BR20"})]


def test_months_follow_the_calendar_without_gaps():
    cal = {r["game_turn"]: r for r in json.loads((TABLES / "calendar.json").read_text())["rows"]}
    rows = _rows()
    for a, b in zip(rows, rows[1:]):
        assert b["game_turns"]["from"] == a["game_turns"]["to"] + 1
    for r in rows[1:]:
        f, t = r["game_turns"]["from"], r["game_turns"]["to"]
        assert t - f == 3 and cal[f]["week"] == 1 and cal[f]["month"] == cal[t]["month"], r["period"]
    assert rows[-1]["game_turns"]["to"] == 110


def test_marks_are_torpedo_bomber_notes():
    marked = [(r["game_turns"]["from"], a["mark"], a["count"], a["aircraft"]) for r in _rows() for a in r["arrivals"] if "mark" in a]
    assert marked == [(35, "*", 24, "SM79"), (43, "*", 18, "SM79"), (55, "†", 36, "SM79"), (71, "*", 6, "SM79"),
                      (75, "†", 12, "SM84"), (79, "*", 6, "SM84"), (95, "†", 12, "SM79")]
