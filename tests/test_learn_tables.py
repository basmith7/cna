"""JSON -> HTML renderer for the combat tables the Learn page shows (Part D of the mission)."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import learn_tables as lt  # noqa: E402


def test_load_applies_errata_overlays():
    base = json.loads((ROOT / "data" / "tables" / "close-assault-results.json").read_text())
    t = lt.load_table("close-assault-results")
    assert base["losses"]["defender"]["10"]["+4"] == {"from": 24, "to": 45}   # as printed
    assert t["losses"]["defender"]["10"]["+4"] == {"from": 34, "to": 45}      # E-008 applied


def test_barrage_html_shape():
    h = lt.render("barrage-results")
    assert h.startswith('<div class="learn-table" data-table="barrage-results">')
    assert 'spi-ref' in h and '12.6' in h and 'data/tables/barrage-results.json' in h
    assert h.count("<table") == 4  # one per target class
    assert "<th>1–2</th>" in h and "<th>17+</th>" in h
    # infantry, 5-6 column: no effect 11-41, pinned 42-65, lose 1 on 66
    assert "<td>11–41</td>" in h and "<td>42–65</td>" in h and "<td>66</td>" in h
    assert "no effect" in h and "pinned" in h and "lose 1" in h


def test_anti_armour_html_shape():
    h = lt.render("anti-armour-results")
    assert h.count("<table") == 1
    assert "<th>0</th>" in h and "<th>16+</th>" in h
    assert "<th>11</th>" in h and "<th>65</th>" in h
    assert "<td>—</td>" in h  # a blank cell renders as a dash
    assert "<td>22</td>" in h and "<td>32</td>" in h
