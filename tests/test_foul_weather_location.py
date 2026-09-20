"""Foul Weather Location Table (SPI 29.7): one die -> the map sections a storm covers."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_one_row_per_die_face_with_valid_sections():
    t = json.loads((ROOT / "data" / "tables" / "foul-weather-location.json").read_text())
    assert [r["die"] for r in t["rows"]] == [1, 2, 3, 4, 5, 6]
    for r in t["rows"]:
        assert r["sections"] == sorted(set(r["sections"]))
        assert set(r["sections"]) <= set("ABCDE")
    assert next(r for r in t["rows"] if r["die"] == 3)["delta_sandstorm_is_normal"] is True
