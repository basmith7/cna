import check_coverage as cc

MD = """# Title
::: spi 8.35 8.36
body
::: spi-ref 8.35
::: spi-omit 4.6 — component inventory
::: spi-omit 4.7 -- second reason
"""


def test_parse_badges():
    b = cc.parse_badges(MD)
    assert b[0] == {"kind": "spi", "cases": ["8.35", "8.36"], "reason": None, "line": 2}
    assert b[1] == {"kind": "spi-ref", "cases": ["8.35"], "reason": None, "line": 4}
    assert b[2] == {"kind": "spi-omit", "cases": ["4.6"], "reason": "component inventory", "line": 5}
    assert b[3] == {"kind": "spi-omit", "cases": ["4.7"], "reason": "second reason", "line": 6}


def test_parse_badges_tolerates_up_to_three_leading_spaces():
    b = cc.parse_badges("  ::: spi 8.35\n")
    assert b[0] == {"kind": "spi", "cases": ["8.35"], "reason": None, "line": 1}


def test_coverage_counts_primary_omit_and_uncovered():
    ids = ["4.6", "4.7", "8.35", "8.36", "8.37", "33.1"]
    rep = cc.coverage(ids, {"rules/a.md": cc.parse_badges(MD)}, sections={4, 8})
    assert rep["total"] == 5 and rep["primary"] == 2 and rep["omitted"] == 2
    assert rep["uncovered"] == ["8.37"]
    assert rep["errors"] == []


def test_coverage_errors_on_duplicate_primary_and_unknown_case():
    badges = {"rules/a.md": cc.parse_badges("::: spi 8.35\n"), "rules/b.md": cc.parse_badges("::: spi 8.35 9.99\n")}
    rep = cc.coverage(["8.35"], badges, sections=None)
    assert any("8.35" in e and "primary" in e for e in rep["errors"])
    assert any("9.99" in e and "unknown" in e for e in rep["errors"])


def test_render_markdown_mentions_counts_and_uncovered():
    rep = cc.coverage(["8.35", "8.37"], {"rules/a.md": cc.parse_badges("::: spi 8.35\n")}, sections=None)
    out = cc.render_markdown(rep)
    assert "1 / 2" in out and "8.37" in out


def test_parse_sections_arg():
    assert cc.parse_sections("1-3,8") == {1, 2, 3, 8}
