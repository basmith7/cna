import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLES = ROOT / "data" / "tables"
ROWS = json.loads((TABLES / "calendar.json").read_text())["rows"]
BY_TURN = {r["game_turn"]: r for r in ROWS}
MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7,
          "Aug": 8, "Sep": 9, "Sept": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def test_every_turn_once_and_weeks_advance_one_at_a_time():
    assert [r["game_turn"] for r in ROWS] == list(range(1, 112))
    for a, b in zip(ROWS, ROWS[1:]):
        same_month = (a["year"], a["month"]) == (b["year"], b["month"])
        if same_month:
            assert b["week"] == a["week"] + 1
        else:
            assert (a["week"], b["week"]) == (4, 1)
            assert (b["year"], b["month"]) == ((a["year"], a["month"] + 1) if a["month"] < 12 else (a["year"] + 1, 1))


def test_agrees_with_the_air_reinforcement_chart():
    """34.84 prints every period beside its Game-Turns; each must land in that month."""
    chart = json.loads((TABLES / "air-reinforcement-schedule.json").read_text())["rows"]
    for row in chart:
        name = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Sep|Oct|Nov|Dec)", row["period"]).group(1)
        week = re.search(r"\b(I|II|III|IV)\s*\(", row["period"])
        for gt in range(row["game_turns"]["from"], row["game_turns"]["to"] + 1):
            assert BY_TURN[gt]["month"] == MONTHS[name], row["period"]
            if week:
                assert BY_TURN[gt]["week"] == ["I", "II", "III", "IV"].index(week.group(1)) + 1, row["period"]


def test_agrees_with_the_seasons_and_weather_bands():
    seasons = json.loads((TABLES / "seasons.json").read_text())["rows"]
    weather = json.loads((TABLES / "weather.json").read_text())["rows"]

    def season_of(r):
        key = (r["month"], r["week"])
        for s in seasons:
            lo, hi = (s["from"]["month"], s["from"]["week"]), (s["to"]["month"], s["to"]["week"])
            if (lo <= key <= hi) if lo <= hi else (key >= lo or key <= hi):
                return s["season"]

    # weather.json holds the bands as printed; E-025 swaps each band with the opposite season's
    opposite = {"spring": "autumn", "autumn": "spring", "summer": "winter", "winter": "summer"}
    for row in weather:
        for band in row["turns"]:
            for gt in range(band["from"], band["to"] + 1):
                assert season_of(BY_TURN[gt]) == opposite[row["season"]], gt


def test_printed_anchors():
    assert (BY_TURN[1]["year"], BY_TURN[1]["month"], BY_TURN[1]["week"]) == (1940, 9, 3)
    assert (BY_TURN[35]["year"], BY_TURN[35]["month"], BY_TURN[35]["week"]) == (1941, 6, 1)
    assert (BY_TURN[110]["year"], BY_TURN[110]["month"], BY_TURN[110]["week"]) == (1942, 12, 4)
