import json
import pathlib

import fetch


def test_load_sources_pins_commit_and_identifier():
    s = fetch.load_sources()
    assert s["archive_org"]["identifier"] == "campaign-for-north-africa"
    assert s["source_text"]["commit"] == "75a037f27346a7cd920a765a2f3cae965b1e07a3"


def test_scan_page_downloads_once_into_cache(tmp_path, monkeypatch):
    calls = []

    def fake_download(url, dest):
        calls.append(url)
        pathlib.Path(dest).write_bytes(b"jpg")

    monkeypatch.setattr(fetch, "CACHE", tmp_path)
    monkeypatch.setattr(fetch, "_download", fake_download)
    p1 = fetch.scan_page(96)
    p2 = fetch.scan_page("0096")
    assert p1 == p2 == tmp_path / "p0096.jpg"
    assert len(calls) == 1
    assert "North%20Africa_0096.jp2" in calls[0]


def test_source_section_is_cached_under_commit(tmp_path, monkeypatch):
    calls = []

    def fake_download(url, dest):
        calls.append(url)
        pathlib.Path(dest).write_text("[#8_0]\n== LAND MOVEMENT\n")

    monkeypatch.setattr(fetch, "CACHE", tmp_path)
    monkeypatch.setattr(fetch, "_download", fake_download)
    p = fetch.source_section(8)
    assert p == tmp_path / "source" / "75a037f27346a7cd920a765a2f3cae965b1e07a3" / "section-08.adoc"
    assert p.read_text().startswith("[#8_0]")
    fetch.source_section(8)
    assert len(calls) == 1
    assert calls[0].endswith("/75a037f27346a7cd920a765a2f3cae965b1e07a3/sections/section-08.adoc")


def test_all_source_sections_covers_1_to_65(tmp_path, monkeypatch):
    monkeypatch.setattr(fetch, "CACHE", tmp_path)
    monkeypatch.setattr(fetch, "_download", lambda url, dest: pathlib.Path(dest).write_text("x"))
    paths = fetch.all_source_sections()
    assert len(paths) == 65
    assert paths[0].name == "section-01.adoc" and paths[-1].name == "section-65.adoc"
