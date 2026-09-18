import pathlib

import check_overlap as co

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_normalize_lowercases_and_strips_punctuation():
    assert co.normalize("Zones of Control, Terrain; (Fuel) — “Breakdown’s”") == \
        ["zones", "of", "control", "terrain", "fuel", "breakdown's"]


def test_strip_markdown_removes_frontmatter_badges_and_syntax():
    md = "---\ntitle: X\nstatus: provisional\n---\n# Heading\n::: spi 8.35 8.36\nSome **bold** and `code` and [a link](./x.md).\n| a | b |\n|---|---|\n| c | d |\n"
    assert co.normalize(co.strip_markdown(md)) == ["heading", "some", "bold", "and", "code", "and", "a", "link", "a", "b", "c", "d"]


def test_strip_asciidoc_removes_anchors_labels_and_xrefs():
    adoc = "[#8_11]\n*[8.11]* Units may be moved (see <<8_34,8.34>>).\n====\nnote\n====\n"
    assert co.normalize(co.strip_asciidoc(adoc)) == ["units", "may", "be", "moved", "see", "8", "34", "note"]


def test_ngrams():
    assert co.ngrams(list("abcde"), 3) == {("a", "b", "c"), ("b", "c", "d"), ("c", "d", "e")}
    assert co.ngrams(list("ab"), 3) == set()


def test_find_overlaps_reports_shared_8_word_runs_and_honours_allowlist():
    source = "the terrain effects chart lists all costs for entering each hex and crossing hexsides"
    grams = co.ngrams(co.normalize(source))
    rules = "Our text: the terrain effects chart lists all costs for entering each hex, unlike theirs."
    hits = co.find_overlaps(rules, grams, allow=set())
    assert ("the", "terrain", "effects", "chart", "lists", "all", "costs", "for") in hits
    allow = co.load_allowlist_text("the terrain effects chart lists all costs for entering each hex\n")
    assert co.find_overlaps(rules, grams, allow=allow) == []


def test_find_overlaps_clean_text_has_no_hits():
    grams = co.ngrams(co.normalize("units are moved one at a time or in stacks tracing a path of contiguous hexes"))
    assert co.find_overlaps("A unit moves hex by hex along a path it chooses.", grams, allow=set()) == []
