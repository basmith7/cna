import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import decisions_page as dp  # noqa: E402

RULING = """---
id: R-099
status: proposed
affects: [1.1, 2.2]
---

# R-099 — Can a unit fly?

## Problem

Text says *no*.[^a]

> quoted **thing**

[^a]: A footnote.

## Options

1. **Never** (NJHarman). Consequence: none.
2. **Always.** It
   wraps onto a second line.

## Decision

None yet — proposed.

## Rationale

Option 1 is cleaner.
"""


def test_parse_ruling_reads_options_and_sections():
    r = dp.parse_ruling(RULING)
    assert r["id"] == "R-099"
    assert r["title"] == "Can a unit fly?"
    assert r["affects"] == "1.1, 2.2"
    assert [o["label"] for o in r["options"]] == ["Never", "Always."]
    assert "wraps onto a second line" in r["options"][1]["html"]
    assert "<blockquote>" in r["problem"] and "<em>no</em>" in r["problem"]
    assert "[^a]" not in r["problem"] and "A footnote" not in r["problem"]
    assert "cleaner" in r["rationale"]


def test_only_proposed_rulings_are_open(tmp_path):
    (tmp_path / "rulings").mkdir()
    (tmp_path / "rulings" / "R-099.md").write_text(RULING)
    (tmp_path / "rulings" / "R-100.md").write_text(RULING.replace("R-099", "R-100").replace("proposed", "accepted", 1))
    assert [r["id"] for r in dp.open_rulings(tmp_path)] == ["R-099"]


def test_every_repo_ruling_that_is_open_has_options():
    for r in dp.open_rulings(ROOT):
        assert len(r["options"]) >= 2, r["id"]


def test_build_writes_self_contained_page(tmp_path):
    out = tmp_path / "decisions.html"
    dp.build(ROOT, out)
    html = out.read_text()
    assert "R-020" in html and "map-hill-bands" in html
    assert "<script>" in html
    assert 'src="http' not in html and "<link" not in html and "@import" not in html


PROBE = {
    "id": "R-020", "kind": "line", "question": "Fight or withhold",
    "rules_commit": "abc", "engine_commit": "see git log",
    "x": {"label": "Column", "values": ["-1", "0", "+1"]},
    "y": {"label": "Loss %", "values": []},
    "series": [
        {"option": None, "label": "Fight", "values": [6.0, 6.9, 7.1]},
        {"option": 2, "label": "Stay, pay 30 %", "values": [30.0, 30.0, 30.0]},
    ],
    "finding": "Fighting is <always> cheaper.",
}


def test_probe_chart_is_drawn_into_its_ruling(tmp_path):
    import json
    probes = tmp_path / "probes"
    probes.mkdir()
    (probes / "R-020.json").write_text(json.dumps(PROBE))
    (probes / "chart-oddities.json").write_text(json.dumps(PROBE | {"id": "chart-oddities", "kind": "bar"}))
    out = tmp_path / "d.html"
    dp.build(ROOT, out, probes)
    html = out.read_text()
    assert html.count("<svg") == 2
    assert "Fighting is &lt;always&gt; cheaper." in html
    assert "Stay, pay 30 %" in html


def test_probe_for_unknown_id_is_ignored(tmp_path):
    import json
    probes = tmp_path / "probes"
    probes.mkdir()
    (probes / "R-999.json").write_text(json.dumps(PROBE | {"id": "R-999"}))
    out = tmp_path / "d.html"
    dp.build(ROOT, out, probes)
    assert "<svg" not in out.read_text()


def test_copy_group_comes_first():
    groups, items = dp._items(ROOT)
    assert list(groups)[0] == "copy"
