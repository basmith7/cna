import pathlib

import pytest

import check_overlap as co

ROOT = pathlib.Path(__file__).resolve().parents[1]

INVENTED_SOURCE_SENTENCE = "a convoy halts when its lead vehicle reaches the first hex of soft sand"


def test_normalize_lowercases_and_strips_punctuation():
    assert co.normalize("Zones of Control, Terrain; (Fuel) — “Breakdown’s”") == \
        ["zones", "of", "control", "terrain", "fuel", "breakdown's"]


def test_strip_markdown_removes_frontmatter_badges_and_syntax():
    md = "---\ntitle: X\nstatus: provisional\n---\n# Heading\n::: spi 8.35 8.36\nSome **bold** and `code` and [a link](./x.md).\n| a | b |\n|---|---|\n| c | d |\n"
    assert co.normalize(co.strip_markdown(md)) == ["heading", "some", "bold", "and", "code", "and", "a", "link", "a", "b", "c", "d"]


def test_strip_asciidoc_removes_anchors_labels_and_xrefs():
    adoc = "[#8_11]\n*[8.11]* Units may be moved (see <<8_34,8.34>>).\n====\nnote\n====\n"
    assert co.normalize(co.strip_asciidoc(adoc)) == ["units", "may", "be", "moved", "see", "8", "34", "note"]


def test_strip_asciidoc_keeps_bracketed_prose():
    adoc = "[note]\n[#8_11]\n[This bracketed sentence is real prose]\n====\n"
    assert co.normalize(co.strip_asciidoc(adoc)) == ["this", "bracketed", "sentence", "is", "real", "prose"]


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
    grams = co.ngrams(co.normalize(INVENTED_SOURCE_SENTENCE))
    assert co.find_overlaps("A unit moves hex by hex along a path it chooses.", grams, allow=set()) == []


def test_main_scans_py_files_without_markdown_stripping(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(co, "source_ngrams",
                         lambda n=8: co.ngrams(co.normalize(INVENTED_SOURCE_SENTENCE), n))
    pyfile = tmp_path / "sample.py"
    pyfile.write_text("# a convoy halts when its lead vehicle reaches nowhere in particular\n")
    with pytest.raises(SystemExit) as e:
        co.main([str(pyfile)])
    assert e.value.code == 1
    out = capsys.readouterr().out
    assert "sample.py" in out
    assert "convoy" in out


def test_main_accepts_relative_path_argument(monkeypatch):
    monkeypatch.setattr(co, "source_ngrams", lambda n=8: set())
    monkeypatch.chdir(ROOT)
    with pytest.raises(SystemExit) as e:
        co.main(["tests"])
    assert e.value.code == 0


def test_default_scope_files_covers_python_and_markdown(monkeypatch):
    files = co.default_scope_files()
    rel = {str(f.relative_to(ROOT)) for f in files}
    assert "tools/check_overlap.py" in rel
    assert "README.md" in rel
    assert not any(r.startswith("LICENSE") for r in rel)
    assert "package-lock.json" not in rel
    assert "tools/overlap-allowlist.txt" not in rel


def test_source_ngrams_exits_on_degraded_corpus(tmp_path, monkeypatch):
    empty = tmp_path / "section-01.adoc"
    empty.write_text("")
    monkeypatch.setattr(co.fetch, "all_source_sections", lambda: [empty])
    with pytest.raises(SystemExit) as e:
        co.source_ngrams()
    assert e.value.code == 1


def test_source_ngrams_exits_when_total_tokens_too_low(tmp_path, monkeypatch):
    small = tmp_path / "section-01.adoc"
    small.write_text("a few words of source text here")
    monkeypatch.setattr(co.fetch, "all_source_sections", lambda: [small])
    with pytest.raises(SystemExit) as e:
        co.source_ngrams()
    assert e.value.code == 1
