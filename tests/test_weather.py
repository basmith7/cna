"""The Weather Table (SPI 29.61) as data: per season, the sequential dice readings tile 11–66 across
the four weather results; game-turn bands per season cover turns 1–110 exactly once after E-025."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DICE = [10 * a + b for a in range(1, 7) for b in range(1, 7)]
WEATHER = ["normal", "hot", "sandstorm", "rainstorm"]


def _table():
    return json.loads((ROOT / "data" / "tables" / "weather.json").read_text())


def _patched():
    t = _table()
    patch = json.loads((ROOT / "data" / "errata" / "E-025.json").read_text())
    for op in patch["patches"]:
        assert op["op"] == "replace"
        parts = op["path"].strip("/").split("/")
        node = t
        for k in parts[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        node[int(parts[-1]) if isinstance(node, list) else parts[-1]] = op["value"]
    return t


def test_each_season_tiles_the_dice_across_the_four_weathers():
    for row in _table()["rows"]:
        covered = sorted(d for w in WEATHER for r in [row["weather"][w]] if r for d in DICE if r["from"] <= d <= r["to"])
        assert covered == DICE, row["season"]


def test_turn_bands_cover_1_to_110_once_after_errata():
    t = _patched()
    turns = sorted(n for row in t["rows"] for b in row["turns"] for n in range(b["from"], b["to"] + 1))
    assert turns == list(range(1, 111))
    by_season = {row["season"]: row["turns"] for row in t["rows"]}
    assert by_season["autumn"][0] == {"from": 1, "to": 12}     # the campaign opens in September 1940
    printed = {row["season"]: row["turns"] for row in _table()["rows"]}
    assert printed["spring"][0] == {"from": 1, "to": 12}       # as printed (E-025: backwards)
