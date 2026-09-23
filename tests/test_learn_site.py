"""learn_page.py --site: the primer's Parts A-C as a VitePress page with no SPI material."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import learn_page as lp  # noqa: E402


def test_site_markdown_has_parts_a_to_d_and_no_crops():
    md = lp.site_markdown()
    assert md.startswith("---\ntitle: Learn\n")
    assert '<div class="learn">' in md
    assert "Part A" in md and "Part B" in md and "Part C" in md
    assert "<img" not in md and "graziani" not in md  # no SPI crops; the map is inline SVG from data/map
    assert 'data-table="barrage-results"' in md and 'data-table="close-assault-results"' in md
    assert "Part D" in md and 'class="cna-map"' in md and 'id="C4021"' in md
    assert 'class="overlay"' in md and "Sidi Barrani" in md
    assert "\n\n" not in md.split("---\n", 2)[2]  # no blank lines: keeps markdown-it from re-entering the HTML block


def test_part_d_region_covers_the_frontier():
    ids = lp.part_d_region()
    assert {"C4021", "C3922", "C4321", "C4131", "C3019"} <= set(ids)
    assert all(i[0] == "C" for i in ids)


def test_part_d_units_are_on_map_c_land():
    import map_render
    data = map_render.MapData.load(ROOT / "data")
    for hid, label, side in lp.PART_D_UNITS:
        assert side in ("it", "cw"), hid
        assert data.hexes[hid]["terrain"] != "sea", (hid, label)


def test_site_css_is_scoped_under_learn():
    css = lp.scoped_css()
    for rule in re.findall(r"^([^{}\n]+)\{", css, flags=re.M):
        for sel in rule.split(","):
            if sel.startswith("@media"):
                continue
            assert re.match(r"(\.dark )?\.learn", sel.strip()), sel
    assert "body{" not in css
    assert ">" not in css  # Vue's template compiler escapes it to &gt; inside an inline <style>, killing the rule


def test_site_page_owns_its_layout():
    """The primer is a 1240px two-column design; VitePress's 688px doc column squeezed the notes into a
    strip beside the map and its hard-coded light colours were unreadable in dark mode."""
    md = lp.site_markdown()
    assert md.startswith("---\ntitle: Learn\nlayout: page\n")
    css = lp.scoped_css()
    assert ".dark .learn{" in css                        # dark-scheme palette
    assert "svg{" in css and "max-width:100%" in css     # maps scale to the column instead of overflowing it
    assert "flex-wrap:wrap" in css                       # map and note stack on narrow viewports
    for hard in ("#fff", "#666", "#222", "#444"):        # every fixed light-scheme colour goes through a variable
        assert f":{hard}" not in css.replace(f",{hard})", ""), hard


def test_case_numbers_become_rule_links():
    out = lp.link_cases("see [8.37] and [15.79, 12.6] but not [99.99]")
    assert '<a href="rules/40-movement#spi-8.37">8.37</a>' in out  # relative: raw HTML is not base-prefixed by VitePress
    assert "60-combat" in out and "[99.99]" in out


def test_svg_text_is_not_linked():
    out = lp.link_cases('<svg><text>[8.37]</text></svg> [8.37]')
    assert out.count("<a ") == 1


def test_committed_site_page_is_current():
    assert (ROOT / "site" / "learn.md").read_text() == lp.site_markdown(), "site/learn.md is stale: run tools/learn_page.py --site"
