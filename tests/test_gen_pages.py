import json
import pathlib

import gen_pages as gp

RULES_A = """---
title: Alpha
---
# Alpha
::: spi 8.35 8.36
body
::: errata E-001 — 8.35: the plus was a times
::: spi-omit 8.37 — chart
::: ruling R-001 — cohesion level, not DP count
::: variant V-001 — San Giorgio as a live gun battery
"""
RULES_B = """---
title: Beta
---
# Beta
::: spi 9.11
::: errata E-002
"""
RULING = """---
id: R-001
status: accepted
affects: [8.35]
sources:
  - CNA1979:8.35
---
# R-001 — Threshold
"""
VARIANT = """---
id: V-001
status: recorded
affects: [30.17, 55.25]
sources:
  - CNA1979:30.17
---
# V-001 — San Giorgio
"""


def _repo(tmp_path: pathlib.Path) -> pathlib.Path:
    (tmp_path / "rules").mkdir()
    (tmp_path / "rules" / "10-alpha.md").write_text(RULES_A)
    (tmp_path / "rules" / "20-beta.md").write_text(RULES_B)
    (tmp_path / "rulings").mkdir()
    (tmp_path / "rulings" / "R-001.md").write_text(RULING)
    (tmp_path / "rulings" / "V-001.md").write_text(VARIANT)
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "spi-cases.json").write_text(json.dumps({"cases": [
        {"id": "8.35", "section": 8}, {"id": "8.36", "section": 8}, {"id": "8.37", "section": 8},
        {"id": "9.11", "section": 9}, {"id": "9.12", "section": 9}]}))
    return tmp_path


def test_collect_annotations_reads_errata_and_ruling_badges(tmp_path):
    repo = _repo(tmp_path)
    ann = gp.collect_annotations(repo / "rules")
    assert ann["rules/10-alpha.md"]["title"] == "Alpha"
    assert ann["rules/10-alpha.md"]["errata"] == [("E-001", "8.35: the plus was a times")]
    assert ann["rules/10-alpha.md"]["rulings"] == [("R-001", "cohesion level, not DP count")]
    assert ann["rules/10-alpha.md"]["variants"] == [("V-001", "San Giorgio as a live gun battery")]
    assert ann["rules/20-beta.md"]["errata"] == [("E-002", "")]


def test_render_changes_groups_by_file_and_lists_ruling_status(tmp_path):
    repo = _repo(tmp_path)
    md = gp.render_changes(repo)
    assert "## [Alpha](./10-alpha.md)" in md
    assert "**E-001** — 8.35: the plus was a times" in md
    assert "[R-001](../rulings/R-001.md)" in md
    assert "| [R-001](../rulings/R-001.md) | accepted | 8.35 |" in md
    assert "[V-001](../rulings/V-001.md) — San Giorgio as a live gun battery" in md
    assert "| [V-001](../rulings/V-001.md) | recorded | 30.17, 55.25 |" in md
    assert md.index("Alpha") < md.index("Beta")


def test_render_coverage_has_a_row_per_section_with_file_links(tmp_path):
    repo = _repo(tmp_path)
    md = gp.render_coverage(repo)
    assert "| 8 | [Alpha](./10-alpha.md) | 2 | 1 | 0 | 100 % |" in md
    assert "| 9 | [Beta](./20-beta.md) | 1 | 0 | 1 | 50 % |" in md
    assert "`9.12`" in md


def test_write_pages_is_idempotent_and_reports_staleness(tmp_path):
    repo = _repo(tmp_path)
    assert gp.write_pages(repo) is True          # first run wrote something
    assert gp.write_pages(repo) is False         # second run: nothing changed
    assert (repo / "rules" / "changes.md").exists()
    assert (repo / "rules" / "coverage.md").exists()


def test_committed_pages_are_current():
    root = pathlib.Path(__file__).resolve().parents[1]
    assert gp.render_changes(root) == (root / "rules" / "changes.md").read_text(), \
        "rules/changes.md is stale: run tools/gen_pages.py"
    assert gp.render_coverage(root) == (root / "rules" / "coverage.md").read_text(), \
        "rules/coverage.md is stale: run tools/gen_pages.py"
