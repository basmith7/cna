"""Maximum Attachment Chart (SPI 19.5): per nation and parent type, how many battalion-equivalent
units may be attached and what restrictions apply."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_rows_by_nation_and_key_values():
    t = json.loads((ROOT / "data" / "tables" / "max-attachments.json").read_text())
    by = {(r["nation"], r["parent"]): r for r in t["rows"]}
    assert len(by) == len(t["rows"]) == 20
    assert by[("cw", "armour-division")]["turns"] == {"from": 1, "to": 67} and by[("cw", "armour-division")]["max_units"] == 2
    assert by[("cw", "armour-division-late")]["turns"] == {"from": 68, "to": None} and by[("cw", "armour-division-late")]["max_units"] == 3
    assert by[("de", "armour-division")]["alternatives"] == [{"brigades": 1, "units": 1}, {"brigades": 0, "units": 4}]
    assert by[("it", "battalion")]["max_units"] == 0
    assert by[("cw", "selby-force")]["restrictions"] == {"tank": 0, "recce": 0, "infantry": 3}
    assert t["free_company_equivalents"] == 2
