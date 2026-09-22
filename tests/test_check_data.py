import json
import pathlib
import shutil

import check_data

ROOT = pathlib.Path(__file__).resolve().parents[1]


def make_data(tmp_path, tables=None, errata=None):
    d = tmp_path / "data"
    shutil.copytree(ROOT / "data" / "schema", d / "schema")
    (d / "spi-cases.json").write_text(json.dumps({
        "source": {"repo": "x/y", "commit": "a" * 40},
        "cases": [{"id": "8.37", "section": 8, "kind": "secondary", "anchor": "8_37", "label": "", "page": None}]}))
    (d / "schema" / "demo.schema.json").write_text(json.dumps({
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "demo.schema.json",
        "type": "object", "required": ["rows"],
        "properties": {"rows": {"type": "array", "items": {"type": "object", "required": ["cost", "sources"],
                       "properties": {"cost": {"type": "integer"}, "sources": {"$ref": "common.schema.json#/$defs/sources"}}}}}}))
    (d / "tables").mkdir()
    for name, body in (tables or {}).items():
        (d / "tables" / name).write_text(json.dumps(body))
    (d / "errata").mkdir()
    for name, body in (errata or {}).items():
        (d / "errata" / name).write_text(json.dumps(body))
    return d


def test_real_data_dir_passes():
    assert check_data.validate_all(ROOT / "data") == []


def test_valid_table_passes(tmp_path):
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": 2, "sources": ["CNA1979:8.37", "scan:p96"]}]}})
    assert check_data.validate_all(d) == []


def test_table_without_schema_fails(tmp_path):
    d = make_data(tmp_path, tables={"orphan.json": {"rows": []}})
    errs = check_data.validate_all(d)
    assert any("orphan.json" in e and "no schema" in e for e in errs)


def test_schema_violation_reported_with_path(tmp_path):
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": "two", "sources": ["CNA1979:8.37"]}]}})
    errs = check_data.validate_all(d)
    assert any("demo.json" in e and "rows/0/cost" in e for e in errs)


def test_unknown_case_reference_fails(tmp_path):
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": 2, "sources": ["CNA1979:99.9"]}]}})
    errs = check_data.validate_all(d)
    assert any("CNA1979:99.9" in e and "unknown case" in e for e in errs)


def test_errata_must_target_existing_table_and_match_filename(tmp_path):
    patch = {"id": "E-001", "table": "missing", "affects": ["8.37"], "sources": ["CNA1979:8.37"],
             "summary": "x", "patches": [{"op": "replace", "path": "/rows/0/cost", "value": 3}]}
    d = make_data(tmp_path, errata={"E-002.json": patch})
    errs = check_data.validate_all(d)
    assert any("E-002.json" in e and "table 'missing'" in e for e in errs)
    assert any("E-002.json" in e and "id E-001" in e for e in errs)


def test_errata_affects_must_name_known_cases(tmp_path):
    patch = {"id": "E-001", "table": "demo", "affects": ["8.37", "9.99"], "sources": ["CNA1979:8.37"],
             "summary": "x", "patches": [{"op": "replace", "path": "/rows/0/cost", "value": 3}]}
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": 2, "sources": ["CNA1979:8.37"]}]}},
                  errata={"E-001.json": patch})
    errs = check_data.validate_all(d)
    assert any("E-001.json" in e and "affects unknown case 9.99" in e for e in errs)


def test_malformed_table_json_fails(tmp_path):
    d = make_data(tmp_path, tables={})
    (d / "tables" / "demo.json").write_text("{not json")
    errs = check_data.validate_all(d)
    assert any("demo.json" in e and "invalid JSON" in e for e in errs)
    assert not any("Traceback" in e or "JSONDecodeError" in str(type(e)) for e in errs)


def test_malformed_spi_cases_json_fails(tmp_path):
    d = make_data(tmp_path)
    (d / "spi-cases.json").write_text("{not json")
    errs = check_data.validate_all(d)
    assert any("spi-cases.json" in e and "invalid JSON" in e for e in errs)


def test_spi_cases_wrong_shape_fails_closed(tmp_path):
    d = make_data(tmp_path)
    (d / "spi-cases.json").write_text(json.dumps(["not", "a", "dict"]))
    errs = check_data.validate_all(d)
    assert any("spi-cases.json" in e and "expected an object" in e for e in errs)


def test_spi_cases_missing_id_fails_closed(tmp_path):
    d = make_data(tmp_path)
    (d / "spi-cases.json").write_text(json.dumps({
        "source": {"repo": "x/y", "commit": "a" * 40},
        "cases": [{"section": 8, "kind": "secondary", "anchor": "8_37", "label": "", "page": None}]}))
    errs = check_data.validate_all(d)
    assert any("spi-cases.json" in e and "missing 'id'" in e for e in errs)


def make_map(d, hexes, sides, places):
    (d / "map" / "raw").mkdir(parents=True); (d / "map" / "corrections").mkdir()
    (d / "map" / "sheets.json").write_text((ROOT / "data" / "map" / "sheets.json").read_text())
    (d / "map" / "hexes.json").write_text(json.dumps({"sources": ["vassal:CNAv2.1.0"], "hexes": hexes}))
    (d / "map" / "hexsides.json").write_text(json.dumps({"sources": ["vassal:CNAv2.1.0"], "hexsides": sides}))
    (d / "map" / "places.json").write_text(json.dumps({"sources": ["scan:p187"], "places": places}))


H = lambda i, **kw: {"id": i, "sheet": i[0], "terrain": "clear", "settlement": None, "coastal": False, **kw}
S = lambda a, b, **kw: {"key": f"{a}|{b}", "a": a, "b": b, "side": None, "features": ["slope"], "up": None, **kw}


def test_map_valid_passes(tmp_path):
    d = make_data(tmp_path)
    make_map(d, [H("C4023", settlement="village", coastal=True), H("C4024", coastal=True)],
             [S("C4023", "C4024", up="C4023"),
              {"key": "C4023|W", "a": "C4023", "b": None, "side": "W", "features": ["coast"], "up": None}],
             [{"id": "sollum", "hex": "C4023", "name": "Sollum", "kind": "village", "port": True}])
    assert check_data.validate_all(d) == []


def test_map_referential_errors(tmp_path):
    d = make_data(tmp_path)
    make_map(d, [H("C4023"), H("C4025")],
             [S("C4023", "C4025"), S("C4023", "C4099")],
             [{"id": "x", "hex": "C4023", "name": "X", "kind": "village", "port": False}])
    errs = "\n".join(check_data.validate_all(d))
    assert "not adjacent" in errs and "C4099" in errs and "settlement" in errs


def test_map_up_must_be_an_endpoint(tmp_path):
    d = make_data(tmp_path)
    make_map(d, [H("C4023"), H("C4024")], [S("C4023", "C4024", up="C4025")], [])
    assert any("up" in e for e in check_data.validate_all(d))
