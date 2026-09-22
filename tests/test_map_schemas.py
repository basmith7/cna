import json
import pathlib
import jsonschema
import pytest
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "data" / "schema"


def registry():
    reg = Registry()
    for p in SCHEMA_DIR.glob("*.schema.json"):
        reg = reg.with_resource(p.name, Resource.from_contents(json.loads(p.read_text())))
    return reg


def validator(name):
    return Draft202012Validator(json.loads((SCHEMA_DIR / name).read_text()), registry=registry())


def ok(ref, inst):
    return not list(Draft202012Validator({"$ref": f"common.schema.json#/$defs/{ref}"}, registry=registry()).iter_errors(inst))


HEX = {"id": "C4023", "sheet": "C", "terrain": "clear", "settlement": None, "coastal": False}
SIDE = {"key": "C4023|C4024", "a": "C4023", "b": "C4024", "side": None, "features": ["slope"], "up": "C4023"}


def test_hex_id_accepts_malta_and_common_source_accepts_vassal():
    assert ok("hexId", "M0304") and ok("hexId", "C4023") and not ok("hexId", "Z0304")
    assert ok("sourceRef", "vassal:CNAv2.1.0") and not ok("sourceRef", "vassal:")


def test_hexes_schema():
    v = validator("map-hexes.schema.json")
    doc = {"sources": ["vassal:CNAv2.1.0"], "hexes": [HEX]}
    v.validate(doc)
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"sources": ["vassal:CNAv2.1.0"], "hexes": [{**HEX, "terrain": "village-bir-oasis"}]})
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"sources": ["vassal:CNAv2.1.0"], "hexes": [{**HEX, "x": 12}]})


def test_hexsides_schema_allows_edge_and_nullable_up():
    v = validator("map-hexsides.schema.json")
    v.validate({"sources": ["vassal:CNAv2.1.0"], "hexsides": [SIDE, {**SIDE, "key": "C4023|W", "b": None, "side": "W", "up": None}]})
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"sources": ["vassal:CNAv2.1.0"], "hexsides": [{**SIDE, "features": ["river"]}]})


def test_places_schema():
    v = validator("map-places.schema.json")
    v.validate({"sources": ["scan:p187"], "places": [{"id": "sollum", "hex": "C4021", "name": "Sollum", "kind": "village", "port": True}]})
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"sources": ["scan:p187"], "places": [{"id": "Sollum", "hex": "C4021", "name": "Sollum", "kind": "village", "port": True}]})


def test_correction_schema():
    v = validator("map-correction.schema.json")
    v.validate({"id": "M-001", "target": "hex", "key": "M0304", "before": HEX,
                "patches": [{"op": "replace", "path": "/terrain", "value": "rough"}],
                "seen": {"scan": "scan:p187", "crop": [100, 200, 60, 60], "note": "tan fill, not clear"},
                "superseded": False})
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"id": "M-001", "target": "hex", "key": "M0304", "before": HEX, "patches": [],
                    "seen": {"scan": "scan:p187", "crop": [0, 0, 1, 1], "note": "x"}, "superseded": False})


def test_sheets_file_validates_and_names_six_sheets():
    validator("map-sheets.schema.json").validate(json.loads((ROOT / "data" / "map" / "sheets.json").read_text()))
    sheets = json.loads((ROOT / "data" / "map" / "sheets.json").read_text())["sheets"]
    assert set(sheets) == set("ABCDEM")
