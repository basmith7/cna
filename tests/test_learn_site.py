"""learn_page.py --site: the primer's Parts A-C as a VitePress page with no SPI material."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import learn_page as lp  # noqa: E402


def test_site_markdown_has_parts_a_to_c_and_no_crops():
    md = lp.site_markdown()
    assert md.startswith("---\ntitle: Learn\n")
    assert '<div class="learn">' in md
    assert "Part A" in md and "Part B" in md and "Part C" in md
    assert "<img" not in md and "graziani" not in md  # no SPI crops, no Map C
    assert 'data-table="barrage-results"' in md and 'data-table="close-assault-results"' in md
    assert "Part D" in md and "map sub-project" in md  # the one-paragraph note
    assert "\n\n" not in md.split("---\n", 2)[2]  # no blank lines: keeps markdown-it from re-entering the HTML block


def test_site_css_is_scoped_under_learn():
    css = lp.scoped_css()
    for rule in re.findall(r"^([^{}\n]+)\{", css, flags=re.M):
        for sel in rule.split(","):
            assert sel.strip().startswith(".learn"), sel
    assert "body{" not in css


def test_case_numbers_become_rule_links():
    out = lp.link_cases("see [8.37] and [15.79, 12.6] but not [99.99]")
    assert '<a href="rules/40-movement#spi-8.37">8.37</a>' in out  # relative: raw HTML is not base-prefixed by VitePress
    assert "60-combat" in out and "[99.99]" in out


def test_svg_text_is_not_linked():
    out = lp.link_cases('<svg><text>[8.37]</text></svg> [8.37]')
    assert out.count("<a ") == 1


def test_committed_site_page_is_current():
    assert (ROOT / "site" / "learn.md").read_text() == lp.site_markdown(), "site/learn.md is stale: run tools/learn_page.py --site"
