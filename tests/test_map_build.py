import json
import pathlib
import shutil
import pytest

import map_build as mb

ROOT = pathlib.Path(__file__).resolve().parents[1]
HEX = {"id": "M0304", "sheet": "M", "terrain": "clear", "settlement": None, "coastal": False}
SIDE = {"key": "M0304|M0305", "a": "M0304", "b": "M0305", "side": None, "features": ["slope"], "up": None}


def make(tmp_path, corrections=()):
    d = tmp_path / "data"
    shutil.copytree(ROOT / "data" / "schema", d / "schema")
    (d / "map" / "raw").mkdir(parents=True)
    (d / "map" / "corrections").mkdir()
    (d / "map" / "sheets.json").write_text((ROOT / "data" / "map" / "sheets.json").read_text())
    (d / "map" / "raw" / "M.json").write_text(json.dumps({"sources": ["vassal:CNAv2.1.0"], "sheet": "M", "hexes": [HEX], "hexsides": [SIDE]}))
    for i, c in enumerate(corrections, 1):
        (d / "map" / "corrections" / f"M-{i:03d}.json").write_text(json.dumps({"id": f"M-{i:03d}", "superseded": False,
            "seen": {"scan": "scan:p187", "crop": [0, 0, 1, 1], "note": "t"}, **c}))
    return d


def test_build_without_corrections_equals_raw(tmp_path):
    hexes, sides = mb.build(make(tmp_path))
    assert hexes["hexes"] == [HEX] and sides["hexsides"] == [SIDE]
    assert hexes["sources"] == ["vassal:CNAv2.1.0"]


def test_replace_and_set_up(tmp_path):
    d = make(tmp_path, [
        {"target": "hex", "key": "M0304", "before": HEX, "patches": [{"op": "replace", "path": "/terrain", "value": "rough"}]},
        {"target": "hexside", "key": "M0304|M0305", "before": SIDE, "patches": [{"op": "replace", "path": "/up", "value": "M0305"}]}])
    hexes, sides = mb.build(d)
    assert hexes["hexes"][0]["terrain"] == "rough" and sides["hexsides"][0]["up"] == "M0305"


def test_add_and_remove_whole_records(tmp_path):
    new = {"key": "M0304|W", "a": "M0304", "b": None, "side": "W", "features": ["coast"], "up": None}
    d = make(tmp_path, [
        {"target": "hexside", "key": "M0304|W", "before": None, "patches": [{"op": "add", "path": "", "value": new}]},
        {"target": "hexside", "key": "M0304|M0305", "before": SIDE, "patches": [{"op": "remove", "path": ""}]}])
    _, sides = mb.build(d)
    assert sides["hexsides"] == [new]


def test_stale_before_fails_with_the_correction_id(tmp_path):
    d = make(tmp_path, [{"target": "hex", "key": "M0304", "before": {**HEX, "terrain": "desert"},
                         "patches": [{"op": "replace", "path": "/terrain", "value": "rough"}]}])
    with pytest.raises(mb.CorrectionError, match="M-001"):
        mb.build(d)


def test_superseded_is_skipped_even_if_stale(tmp_path):
    d = make(tmp_path, [{"target": "hex", "key": "M0304", "before": {**HEX, "terrain": "desert"}, "superseded": True,
                         "patches": [{"op": "replace", "path": "/terrain", "value": "rough"}]}])
    hexes, _ = mb.build(d)
    assert hexes["hexes"][0]["terrain"] == "clear"


def test_check_reports_stale_committed_files(tmp_path):
    d = make(tmp_path)
    assert mb.check(d) != []            # nothing written yet
    mb.write(d)
    assert mb.check(d) == []
    (d / "map" / "hexes.json").write_text("{}")
    assert any("hexes.json" in e for e in mb.check(d))


def test_real_data_is_current():
    assert mb.check(ROOT / "data") == [], "run: .venv/bin/python tools/map_build.py"
