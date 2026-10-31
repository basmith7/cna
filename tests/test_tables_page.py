import json
import pathlib
import re

import pytest
import tables_page as tp

ROOT = pathlib.Path(__file__).resolve().parents[1]

FIXTURE = {
    "table": "test-chart",
    "sources": ["CNA1979:8.37", "scan:p69"],
    "notes": ["Read across, then down"],
    "footnotes": {"1": "only on Tuesdays"},
    "known_gaps": [{"side": "defender", "readings": [34, 35, 36]}],
    "hot_weather_extra": 2,
    "columns": [{"id": "1-2", "min": 1, "max": 2}, {"id": "3-4", "min": 3, "max": 4}],
    "rows": [
        {"class": "infantry", "column": "1-2", "dice": {"from": 11, "to": 53}, "sources": ["CNA1979:12.6"]},
        {"class": "infantry", "column": "3-4", "dice": {"from": 11, "to": 44}, "sources": ["CNA1979:12.6"]},
        {"class": "armor", "column": "1-2", "dice": None, "sources": ["CNA1979:12.6"]},
    ],
    "losses": {"50": {"-1": None, "+1": {"from": 11, "to": 15}}, "40": {"-1": {"from": 16, "to": 16}, "+1": None}},
    "pool": {"arrive_turns_later": 2, "rows": [{"item": "light|truck", "total": 835, "units": ["unit:cw:a", "x"]}]},
}


def test_errata_ops_and_marks():
    patches = [{"id": "E-900", "summary": "a fix", "patches": [
        {"op": "replace", "path": "/losses/50/+1", "value": {"from": 12, "to": 15}},
        {"op": "add", "path": "/rows/0/footnotes", "value": [4]},
        {"op": "remove", "path": "/rows/2"},
    ]}]
    out, marks = tp.apply_errata(FIXTURE, patches)
    assert out["losses"]["50"]["+1"] == {"from": 12, "to": 15}
    assert out["rows"][0]["footnotes"] == [4] and len(out["rows"]) == 2
    assert FIXTURE["losses"]["50"]["+1"] == {"from": 11, "to": 15}          # input untouched
    assert set(marks.values()) == {"E-900"}
    page = tp.render_table("test-chart", FIXTURE, patches, [])
    assert "12–15 <a class=\"errata-mark\"" in page and "E-900" in page


def test_shapes_render_as_people_read_them():
    page = tp.render_table("test-chart", FIXTURE, [], [("Combat", "/rules/60-combat")])
    assert 'title: "Test chart"' in page.splitlines()[:4]
    assert "Used in [Combat](/rules/60-combat)." in page
    # pivot: one row per class, one column per column id, dice in the cell
    assert "| Class | 1-2 | 3-4 |" in page
    assert "| infantry | 11–53 | 11–44 |" in page and "| armor | — | — |" in page
    # matrix: outer keys are rows, inner keys columns
    assert "|  | -1 | +1 |" in page and "| **50** | — | 11–15 |" in page and "| **40** | 16 | — |" in page
    # scalars, nested sections, escaping, int runs, sources
    assert "- **Hot weather extra:** 2" in page
    assert "### Table" in page and "light\\|truck" in page
    assert "dice readings 34–36 (side defender)" in page and "only on Tuesdays" in page
    assert "Sources: SPI 8.37 · scan page 69" in page
    assert page.index("## Table") < page.index("## Columns") < page.index("## Notes")


def _rendered_leaves(node, key=None):
    """Every value a page must show, as tp formats it (sources and pivot column keys are metadata)."""
    if key in ("sources", "column", "notes", "footnotes", "table"):
        return
    if tp._leafish(node) and key is not None:
        if isinstance(node, list) and len(node) > 4:   # may be spread across the chart's columns
            yield from (tp.fmt(x, key) for x in node)
        else:
            yield tp.fmt(node, key)
        return
    items = node.items() if isinstance(node, dict) else ((key, x) for x in node)
    for k, v in items:
        yield from _rendered_leaves(v, k)


@pytest.mark.parametrize("path", sorted((ROOT / "data" / "tables").glob("*.json")), ids=lambda p: p.stem)
def test_every_value_appears_on_its_page(path):
    pages = tp.targets(ROOT)
    page = pages[ROOT / "site" / "tables" / f"{path.stem}.md"]
    table = json.loads(path.read_text())
    errata = [json.loads(p.read_text()) for p in sorted((ROOT / "data" / "errata").glob("E-*.json"))]
    data, _ = tp.apply_errata(table, [e for e in errata if e["table"] == path.stem])
    text = re.sub(r'<span class="wrap">(.*?)</span>', r"\1", page)
    missing = [v for v in _rendered_leaves(data) if re.sub(r'<span class="wrap">(.*?)</span>', r"\1", tp.cell(v)) not in text]
    assert not missing, missing[:5]
    for n in data.get("notes", []):
        assert tp.prose(n) in page


def test_index_lists_every_table_once():
    index = tp.targets(ROOT)[ROOT / "site" / "tables" / "index.md"]
    names = sorted(p.stem for p in (ROOT / "data" / "tables").glob("*.json"))
    linked = re.findall(r"\]\(/tables/([\w-]+)\)", index)
    assert sorted(linked) == names
