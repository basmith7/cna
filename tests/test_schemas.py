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


def test_all_schemas_are_valid_2020_12():
    for p in SCHEMA_DIR.glob("*.schema.json"):
        Draft202012Validator.check_schema(json.loads(p.read_text()))


def test_spi_cases_schema_accepts_minimal_and_rejects_bad_id():
    v = validator("spi-cases.schema.json")
    good = {"source": {"repo": "tonicebrian/TheCampaignForNorthAfrica", "commit": "a" * 40},
            "cases": [{"id": "8.11", "section": 8, "kind": "secondary", "anchor": "8_11", "label": "", "page": None}]}
    v.validate(good)
    bad = dict(good, cases=[dict(good["cases"][0], id="8-11")])
    with pytest.raises(jsonschema.ValidationError):
        v.validate(bad)


@pytest.mark.parametrize("ref,ok", [
    ("CNA1979:8.37", True), ("CNA1979:32.0", True), ("scan:p96", True), ("scan:p0096", True),
    ("CNA1979:8", False), ("p96", False), ("CNA1979:8.37a", False),
])
def test_source_ref_grammar(ref, ok):
    v = validator("common.schema.json")
    schema = {"$ref": "common.schema.json#/$defs/sourceRef"}
    val = Draft202012Validator(schema, registry=registry())
    assert val.is_valid(ref) is ok


@pytest.mark.parametrize("hexid,ok", [("C4023", True), ("A0101", True), ("c4023", False), ("C423", False), ("F4023", False)])
def test_hex_id_grammar(hexid, ok):
    val = Draft202012Validator({"$ref": "common.schema.json#/$defs/hexId"}, registry=registry())
    assert val.is_valid(hexid) is ok


def test_errata_patch_schema_requires_table_and_ops():
    v = validator("errata-patch.schema.json")
    v.validate({"id": "E-001", "table": "terrain-effects", "affects": ["8.37"],
                "sources": ["CNA1979:8.37"], "summary": "escarpment cost corrected",
                "patches": [{"op": "replace", "path": "/rows/3/cost", "value": 6}]})
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"id": "E-001", "patches": []})


def test_errata_patch_value_required_for_add_and_replace_only():
    v = validator("errata-patch.schema.json")
    base = {"id": "E-001", "table": "terrain-effects", "affects": ["8.37"], "sources": ["CNA1979:8.37"], "summary": "x"}
    v.validate(dict(base, patches=[{"op": "remove", "path": "/rows/3"}]))
    with pytest.raises(jsonschema.ValidationError):
        v.validate(dict(base, patches=[{"op": "replace", "path": "/rows/3/cost"}]))
    with pytest.raises(jsonschema.ValidationError):
        v.validate(dict(base, patches=[{"op": "add", "path": "/rows/3/cost"}]))
