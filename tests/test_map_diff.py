import json
import pathlib
import pytest

import map_diff as md
import map_render as mr

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHEETS = {"C": {"zone": "Map C", "odd_rows_shift": "west", "rows": [1, 51], "cols": [1, 33]}}


def ours():
    hexes = {i: {"id": i, "sheet": "C", "terrain": "clear", "settlement": None, "coastal": False} for i in ("C4021", "C4022", "C3921")}
    sides = [{"key": "C3921|C4021", "a": "C3921", "b": "C4021", "side": None, "features": ["escarpment"], "up": "C3921"}]
    return mr.MapData(SHEETS, hexes, sides, [])


def theirs():
    return {"C4021": "clear", "C4022": "clear", "C3921": "clear"}, {"C3921|C4021": {"escarpment": "C3921"}}


def test_identical_inputs_have_no_diff():
    assert md.diff_sheet("C", ours(), theirs()) == []


def test_terrain_and_missing_hexside_each_make_one_row():
    t, s = theirs()
    t["C4022"] = "rough"
    s["C4021|C4022"] = {"track": None}
    d = md.diff_sheet("C", ours(), (t, s))
    assert [(x["kind"], x["key"]) for x in d] == [("hexside", "C4021|C4022"), ("hex", "C4022")]


def test_up_disagreement_is_its_own_kind():
    t, s = theirs()
    s["C3921|C4021"] = {"escarpment": "C4021"}
    d = md.diff_sheet("C", ours(), (t, s))
    assert d == [{"kind": "up", "key": "C3921|C4021", "ours": "C3921", "theirs": "C4021"}]


def test_maps_use_our_enums():
    common = json.loads((ROOT / "data" / "schema" / "common.schema.json").read_text())["$defs"]
    assert set(md.CODE_MAP.values()) <= set(common["mapTerrain"]["enum"])
    assert set(md.FEATURE_MAP.values()) <= set(common["hexsideFeature"]["enum"])


def test_normaliser():
    assert md.normalise_id("Map C 4023") == "C4023" and md.normalise_id("c4023") == "C4023"
    with pytest.raises(ValueError):
        md.normalise_id("Z4023")


def test_load_from_literal_module(tmp_path):
    (tmp_path / "mapterrain.py").write_text(
        "from .x import Y\nterrain = {'C4021': 0, 'C3921': 4, 'C9999': 11}\n"
        "slopes = {'C4021': ['C3921'], 'C3921': ['C4021']}\nescarpments = {'C4022': ['C3922']}\n"
        "roads = {'C4021': ['C4022']}\ncoast = set(['C4021'])\n")
    terrain, sides = md.load_njharman(tmp_path)
    assert terrain == {"C4021": "clear", "C3921": "rough"}
    assert sides["C3921|C4021"] == {"ridge": None}
    assert sides["C3922|C4022"] == {"escarpment": "C3922"} and sides["C4021|C4022"] == {"road": None}


def test_main_skips_without_cache(monkeypatch, capsys):
    monkeypatch.setattr(md, "NJ_DATA", pathlib.Path("/nonexistent"))
    assert md.main([]) == 0
    assert "diff skipped" in capsys.readouterr().out
