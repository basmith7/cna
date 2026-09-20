"""Terrain Effects Chart (SPI 8.37): CP cost, breakdown value, combat column shifts and stacking
limit per hex terrain, hexside feature, fortification level and minefield."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _table():
    t = json.loads((ROOT / "data" / "tables" / "terrain-effects.json").read_text())
    return t, {r["terrain"]: r for r in t["rows"]}


def test_rows_and_key_values():
    t, by = _table()
    assert len(by) == len(t["rows"]) == 27
    assert by["clear"] == {"kind": "hex", "terrain": "clear", "cp": {"non_mot": 2, "mot": 2}, "breakdown": 4,
                           "shifts": {"barrage": 0, "anti_armour": 0, "close_assault": 0}, "stacking": 6,
                           "sources": ["CNA1979:8.37", "scan:p69"]}
    assert by["salt-marsh"]["shifts"] == {"barrage": 0, "anti_armour": 0, "close_assault": 1} and by["salt-marsh"]["footnotes"] == [2]
    assert by["mountain"]["cp"] == {"non_mot": 4, "mot": 6} and by["mountain"]["breakdown"] == 12 and by["mountain"]["stacking"] == 3
    assert by["mountain"]["shifts"] == {"barrage": -2, "anti_armour": -2, "close_assault": -3}
    assert by["desert"]["breakdown"] == 24 and by["desert"]["footnotes"] == [3]
    assert by["major-city"]["cp"] == {"non_mot": 1, "mot": 0.5} and by["major-city"]["breakdown"] == 0.5
    assert by["major-city"]["shifts"] == "see-fortifications" and by["major-city"]["stacking"] == 8
    assert by["swamp"]["cp"] == "road-or-railroad-only" and by["swamp"]["footnotes"] == [4]
    assert by["village-bir-oasis"]["cp"] == "as-hex-terrain" and by["railroad"]["cp"] == "as-hex-terrain"
    assert by["road"]["cp"] == {"non_mot": 1, "mot": 0.5} and by["road"]["breakdown"] == 0.5 and by["road"]["stacking"] == 5
    assert by["track"]["cp"] == {"non_mot": 1, "mot": 1} and by["track"]["breakdown"] == "halves" and by["track"]["footnotes"] == [7, 8]
    assert by["ridge"]["kind"] == "hexside" and by["ridge"]["cp"] == {"non_mot": 2, "mot": 4}
    assert by["up-escarpment"]["cp"] == {"non_mot": 6, "mot": "prohibited"} and by["up-escarpment"]["shifts"]["anti_armour"] == "prohibited"
    assert by["down-escarpment"]["cp"] == {"non_mot": 4, "mot": 8} and by["down-escarpment"]["breakdown"] == 6
    assert by["major-river"]["cp"] == {"non_mot": 8, "mot": "prohibited"} and by["major-river"]["shifts"]["close_assault"] == -6
    assert by["fortification-1"]["kind"] == "fortification" and by["fortification-1"]["shifts"] == {"barrage": -1, "anti_armour": -1, "close_assault": -2}
    assert by["fortification-3"]["shifts"] == {"barrage": -2, "anti_armour": -2, "close_assault": -4}
    assert by["friendly-minefield"]["cp"] == {"non_mot": 1, "mot": 4} and by["friendly-minefield"]["breakdown"] == 0
    assert by["enemy-minefield"]["cp"] == {"non_mot": 4, "mot": "cpa"} and by["enemy-minefield"]["breakdown"] == 2
    assert {int(k) for k in t["footnotes"]} == set(range(1, 14))


def test_errata_e031_track_cost_and_footnote_four():
    e = json.loads((ROOT / "data" / "errata" / "E-031.json").read_text())
    assert e["table"] == "terrain-effects" and e["affects"] == ["8.37"]
    t, by = _table()
    idx = {r["terrain"]: i for i, r in enumerate(t["rows"])}
    paths = {p["path"]: p for p in e["patches"]}
    assert paths[f"/rows/{idx['track']}/cp"]["value"] == "halves-hex-terrain"
    assert paths[f"/rows/{idx['swamp']}/footnotes"]["op"] == "remove"
    assert paths[f"/rows/{idx['major-city']}/footnotes"]["value"] == [4]
