# CNA Living Rules — Scaffold + Overview Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the repository (licences, provenance, data conventions, the two build gates, the coverage report, VitePress phase 1, CI) and author the first two rules files — the Overview and the Glossary — so that every later "restate one Land Game system" PR has a working pipeline to land in.

**Architecture:** Python 3 scripts under `tools/` (stdlib + `jsonschema`) implement fetching, generation and the checks; each is a module with pure functions plus a thin CLI, tested with `pytest`. A VitePress site in `site/` renders `rules/` from the repo root with a tiny markdown-it plugin for the SPI badge line syntax. GitHub Actions runs the gates on PRs and deploys Pages from `main`.

**Tech Stack:** Python 3.12+ (`pytest`, `jsonschema`, `Pillow` for the existing primer), Node 22 + VitePress (latest), `markdown-it`, GitHub Actions (`marocchino/sticky-pull-request-comment`, `actions/deploy-pages`).

**Spec:** `docs/designs/2026-09-18-cna-living-rules-design.md` — read it first; this plan implements its **Process** steps 1 (Scaffold) and 2 (Overview + glossary) only.

## Global Constraints

- No SPI rule text, map art or counter art is committed or built into the site. Source text is fetched at run time into `~/.cache/cna-scans` only. (Spec: *Legal posture*.)
- Licence split, verbatim from the spec: `rules/` **CC-BY-SA-4.0**; `data/` **CC0-1.0**; `tools/`, `site/` **MIT**; root `LICENSE` is a pointer file.
- Source pins: archive.org item **`campaign-for-north-africa`**; tonicebrian/TheCampaignForNorthAfrica commit **`75a037f27346a7cd920a765a2f3cae965b1e07a3`** (the tip on 2026-09-18).
- Badge syntax is a **single line** — `::: spi 8.35 8.36`, `::: spi-ref 8.35`, `::: spi-omit 4.6 — component inventory` — with no closing `:::`. A badge's scope ends at the next badge or heading.
- Overlap gate: any **8-word** run shared with the source text fails the build, except allowlisted phrases. Data gate: schema + referential integrity. Coverage: **report, not gate**.
- Case reference grammar in data: `CNA1979:<section>.<case>` (e.g. `CNA1979:8.37`); scan reference `scan:p<jp2-index>` (e.g. `scan:p96`, the 0-based jp2 index used by `tools/learn_page.py`).
- Rules prose: precise definitions and procedures, defined terms bold on first use, explicit *may / must / may not*, examples are our own situations, plain body is always the current post-errata rule, each file ends with a provenance line, frontmatter `status: provisional`.
- Repo will live at `github.com/basmith7/cna`; Pages base path `/cna/`.
- Commit messages end with the attribution trailer given by the harness (`Co-Authored-By: …`).
- Every task: run its tests, then `git add` the named files and commit. Do not commit `~/.cache` contents, `node_modules/`, `.venv/`, or `docs/learn/*.jpg`.

---

## File map

| Path | Responsibility | Task |
|---|---|---|
| `LICENSE`, `LICENSE-TEXT`, `LICENSE-DATA`, `LICENSE-CODE` | Licence split | 1 |
| `README.md` | What this is, legal posture, how to build | 1 |
| `EXTRACTION.md` | Per-file idea/expression log | 1, 11, 12 |
| `requirements-dev.txt`, `pyproject.toml`, `.gitignore` | Python tooling | 1 |
| `tools/sources.json` | Pinned sources + hashes | 2 |
| `tools/fetch.py` | Scan pages and source sections → cache | 2 |
| `tools/learn_page.py` | (modify) use `fetch.scan_page` | 2 |
| `data/README.md` | ID grammar, enums, hex convention, provenance, errata overlay | 3 |
| `data/schema/common.schema.json` | Shared `$defs` (refs, enums, hex ids) | 3 |
| `data/schema/spi-cases.schema.json` | Shape of `data/spi-cases.json` | 3 |
| `data/schema/errata-patch.schema.json` | Shape of `data/errata/*.json` overlays | 3 |
| `tools/gen_spi_cases.py`, `data/spi-cases.json` | Canonical SPI case list from source anchors | 4 |
| `tools/check_data.py` | Data gate | 5 |
| `tools/check_overlap.py`, `tools/overlap-allowlist.txt` | Overlap gate | 6 |
| `tools/check_coverage.py` | Coverage report | 7 |
| `rulings/README.md` | Numbering, statuses, process, fork policy | 8 |
| `package.json`, `site/.vitepress/config.mts`, `site/.vitepress/spi-badge.mjs`, `site/.vitepress/theme/*` | VitePress phase 1 | 9 |
| `.github/workflows/ci.yml`, `.github/workflows/deploy.yml` | Gates, coverage comment, Pages deploy | 10 |
| `rules/00-overview.md` | Authored overview | 11 |
| `rules/glossary.md` | Authored glossary | 12 |
| `tests/*.py`, `site/.vitepress/spi-badge.test.mjs` | Tests | each |

Module interfaces used across tasks (all in `tools/`, importable because `tests/conftest.py` adds `tools/` to `sys.path`):

```python
# fetch.py
CACHE: pathlib.Path                      # ~/.cache/cna-scans
def load_sources() -> dict               # parsed tools/sources.json
def scan_page(page: str | int) -> pathlib.Path      # jpg of jp2 index, e.g. "0096" or 96
def source_section(n: int) -> pathlib.Path          # sections/section-NN.adoc at pinned commit
def all_source_sections() -> list[pathlib.Path]     # 1..65

# gen_spi_cases.py
def parse_anchors(adoc_text: str) -> list[dict]     # [{"id","section","kind","anchor"}]
def build_cases(section_texts: dict[int, str]) -> list[dict]

# check_data.py
def validate_all(data_dir: pathlib.Path) -> list[str]   # error strings, [] == pass

# check_overlap.py
def strip_markdown(md: str) -> str
def normalize(text: str) -> list[str]
def ngrams(tokens: list[str], n: int = 8) -> set[tuple[str, ...]]
def strip_asciidoc(adoc: str) -> str
def load_allowlist_text(text: str, n: int = 8) -> set[tuple[str, ...]]
def load_allowlist(path: pathlib.Path = ALLOWLIST, n: int = 8) -> set[tuple[str, ...]]
def find_overlaps(rules_md: str, source_grams: set, allow: set, n: int = 8) -> list[tuple[str, ...]]
def source_ngrams(n: int = 8) -> set[tuple[str, ...]]   # all 65 sections, via fetch

# check_coverage.py
def parse_badges(md: str) -> list[dict]             # [{"kind": "spi"|"spi-ref"|"spi-omit", "cases": [...], "reason": str|None, "line": int}]
def coverage(case_ids: list[str], badges_by_file: dict[str, list[dict]], sections: set[int] | None) -> dict
def render_markdown(report: dict) -> str
```

---

### Task 1: Repository hygiene — licences, README, EXTRACTION.md, Python tooling

**Files:**
- Create: `LICENSE`, `LICENSE-TEXT`, `LICENSE-DATA`, `LICENSE-CODE`, `README.md`, `EXTRACTION.md`, `requirements-dev.txt`, `pyproject.toml`, `tests/conftest.py`, `tests/test_repo_hygiene.py`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `.venv` workflow (`python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt`); `tests/conftest.py` puts `tools/` on `sys.path` so every later test can `import fetch`, `import check_overlap`, etc.

- [ ] **Step 1: Write the failing test**

`tests/conftest.py`:

```python
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
```

`tests/test_repo_hygiene.py`:

```python
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_licence_files_exist_and_pointer_names_the_split():
    for name in ["LICENSE", "LICENSE-TEXT", "LICENSE-DATA", "LICENSE-CODE"]:
        assert (ROOT / name).is_file(), name
    pointer = (ROOT / "LICENSE").read_text()
    assert "CC-BY-SA-4.0" in pointer and "rules/" in pointer
    assert "CC0-1.0" in pointer and "data/" in pointer
    assert "MIT" in pointer and "tools/" in pointer and "site/" in pointer


def test_licence_texts_are_the_real_licences():
    assert "Attribution-ShareAlike 4.0 International" in (ROOT / "LICENSE-TEXT").read_text()
    assert "CC0 1.0 Universal" in (ROOT / "LICENSE-DATA").read_text()
    assert "MIT License" in (ROOT / "LICENSE-CODE").read_text()


def test_readme_states_legal_posture():
    readme = (ROOT / "README.md").read_text()
    for phrase in ["not copyrightable", "no legal review", "tonicebrian", "show original"]:
        assert phrase in readme, phrase


def test_extraction_log_has_format_section():
    text = (ROOT / "EXTRACTION.md").read_text()
    assert "## Format" in text
```

- [ ] **Step 2: Create the venv and run the test to verify it fails**

```bash
cd /home/basmith7/Projects/cna
python3 -m venv .venv
.venv/bin/pip install pytest jsonschema referencing Pillow
.venv/bin/python -m pytest tests/test_repo_hygiene.py -q
```

Expected: 4 failures (files missing).

- [ ] **Step 3: Write the licence files**

Download the canonical texts so they are byte-exact:

```bash
cd /home/basmith7/Projects/cna
curl -sL https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt -o LICENSE-TEXT
curl -sL https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt -o LICENSE-DATA
head -3 LICENSE-TEXT; head -3 LICENSE-DATA   # sanity: real licence text, not an HTML error page
```

`LICENSE-CODE` (MIT, verbatim with our name/year):

```
MIT License

Copyright (c) 2026 Brian Smith and CNA Living Rules contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

`LICENSE` (pointer):

```
CNA Living Rules is licensed per directory, to the extent the project holds
rights in each part:

  rules/            CC-BY-SA-4.0   see LICENSE-TEXT
  rulings/          CC-BY-SA-4.0   see LICENSE-TEXT
  data/             CC0-1.0        see LICENSE-DATA
  tools/, site/,    MIT            see LICENSE-CODE
  tests/, .github/

docs/ and everything else not listed: CC-BY-SA-4.0.

This file exists so that GitHub does not label the repository with a single
licence. Read README.md ("Legal posture") for what the project does and does
not claim about the underlying game.

Rulings seeded from NJHarman's "House Rules & Interpretations"
(https://friendorfoe.com/war/cfna/houserules/, CC-BY-SA 4.0) are attributed in
each ruling file.
```

- [ ] **Step 4: Write README.md**

```markdown
# CNA Living Rules

A public, reviewed, searchable edition of the **Land Game** rules of
*The Campaign for North Africa* (SPI, 1979), written in our own words,
precise enough to build a rules-enforcing engine from, with SPI's September
1979 errata folded in and every ambiguity we resolve recorded as a disputable
ruling.

This is sub-project 1 of an open-source, self-hostable digital CNA. No
engine, server or UI lives here. Design: `docs/designs/2026-09-18-cna-living-rules-design.md`.

## Layout

| Directory | Contents | Licence |
|---|---|---|
| `rules/` | The restated rules, one file per game system | CC-BY-SA-4.0 |
| `rulings/` | One file per ruling: problem, options, decision, rationale | CC-BY-SA-4.0 |
| `data/` | Tables as JSON (CRTs, terrain, weather, …) with schemas and provenance | CC0-1.0 |
| `tools/` | Fetch, generate and check scripts | MIT |
| `site/` | VitePress site that renders `rules/` and `data/` | MIT |
| `docs/` | Designs, plans, the illustrated primer generator | CC-BY-SA-4.0 |

## Legal posture

- Game mechanics are not copyrightable. This project restates them in its
  own words and organisation. It is **intended** to be independent expression;
  **no legal review** has been obtained.
- No SPI rule text, map art or counter art is in this repository or in the
  built site. The optional "show original" toggle fetches the community
  transcription (tonicebrian/TheCampaignForNorthAfrica) into *your browser*
  at page-view time; it is never part of our build or search index.
- Licences are granted to the extent the project holds rights. See `LICENSE`.
- The game's name is used nominatively. This is not marketed as a substitute
  edition and reproduces no trade dress.
- `EXTRACTION.md` logs, per rules file, which source cases were read, what
  mechanic was identified, and how we expressed it.

## Building

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/python -m pytest                      # unit tests
.venv/bin/python tools/fetch.py sections        # source text → ~/.cache/cna-scans (for the overlap gate)
.venv/bin/python tools/check_data.py            # gate
.venv/bin/python tools/check_overlap.py         # gate
.venv/bin/python tools/check_coverage.py --sections 1-32   # report
npm ci && npm run site:build                    # site → site/.vitepress/dist
```

## Contributing

Propose rule wording changes as PRs against `rules/`; propose or dispute a
ruling in GitHub Discussions first (see `rulings/README.md`). Every rules PR
must pass the overlap and data gates and include an `EXTRACTION.md` entry.
```

- [ ] **Step 5: Write EXTRACTION.md, requirements-dev.txt, pyproject.toml, .gitignore**

`EXTRACTION.md`:

```markdown
# Extraction log

Evidence of the idea/expression split. One entry per rules file, appended in
the PR that adds or substantially rewrites the file.

## Format

```
## rules/<file>.md — <date>
- Source cases read: <SPI case ranges>
- Mechanics identified: <bullet list of the game-mechanical facts extracted>
- How we expressed it: <structure chosen, terms renamed, what was merged/split, what was omitted and why>
- Errata applied: <E-ids or "none">
- Rulings raised: <R-ids or "none">
```

## Entries
```

`requirements-dev.txt`:

```
pytest>=8
jsonschema>=4.23
referencing>=0.35
Pillow>=10
```

`pyproject.toml`:

```toml
[project]
name = "cna-living-rules-tools"
version = "0.0.0"
requires-python = ">=3.12"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

`.gitignore` (replace whole file):

```
reference/
node_modules/
site/.vitepress/cache/
site/.vitepress/dist/
docs/learn/*.jpg
.venv/
__pycache__/
.pytest_cache/
coverage.md
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_repo_hygiene.py -q`
Expected: 4 passed

- [ ] **Step 7: Commit**

```bash
git add LICENSE LICENSE-TEXT LICENSE-DATA LICENSE-CODE README.md EXTRACTION.md requirements-dev.txt pyproject.toml .gitignore tests/conftest.py tests/test_repo_hygiene.py
git commit -m "Scaffold: licence split, README with legal posture, extraction log, Python tooling"
```

---

### Task 2: Pinned sources and `tools/fetch.py`

**Files:**
- Create: `tools/sources.json`, `tools/fetch.py`, `tests/test_fetch.py`
- Modify: `tools/learn_page.py` (replace its private `IA` constant and `scan()` function with `fetch.scan_page`; keep `ROOT`, `OUT`, `CACHE`)

**Interfaces:**
- Produces: `fetch.CACHE`, `fetch.load_sources()`, `fetch.scan_page(page)`, `fetch.source_section(n)`, `fetch.all_source_sections()` as declared in the file map. `fetch._download(url, dest)` is the single network call so tests can monkeypatch it.

- [ ] **Step 1: Write sources.json**

Hashes below are archive.org's published SHA-1s from `https://archive.org/metadata/campaign-for-north-africa` (retrieved 2026-09-18). The SHA-256 of the jp2 zip is computed in Step 6.

```json
{
  "archive_org": {
    "identifier": "campaign-for-north-africa",
    "url": "https://archive.org/details/campaign-for-north-africa",
    "page_url_template": "https://archive.org/download/campaign-for-north-africa/The%20Campaign%20for%20North%20Africa_jp2.zip/The%20Campaign%20for%20North%20Africa_jp2%2FThe%20Campaign%20for%20North%20Africa_{page}.jp2&ext=jpg",
    "page_index": "0-based jp2 index, zero-padded to 4 digits; XML page n == jp2 n-1",
    "files": {
      "The Campaign for North Africa_jp2.zip": {"size": 348269545, "sha1": "b0991809c422bfee99aa24e6ac73163b2ab96f56", "sha256": null},
      "The Campaign for North Africa_djvu.xml": {"size": 14019396, "sha1": "721aa3c794a0a4625de8031518526dbef12b972f", "sha256": null},
      "The Campaign for North Africa.pdf": {"size": 134328922, "sha1": "7e82d39c6af2d1dead48f2dc7d238d56b299a487", "sha256": null}
    }
  },
  "source_text": {
    "repo": "tonicebrian/TheCampaignForNorthAfrica",
    "commit": "75a037f27346a7cd920a765a2f3cae965b1e07a3",
    "raw_url_template": "https://raw.githubusercontent.com/tonicebrian/TheCampaignForNorthAfrica/{commit}/sections/section-{nn}.adoc",
    "sections": [1, 65],
    "anchor_format": "[#<section>_<case>] on its own line; case 0 == the section itself"
  },
  "errata": {
    "pdf": "https://www.spigames.net/db_pages/ERR_CampaignforNorthAfrica.pdf",
    "html": "http://www.wargameacademy.org/CNA/CNA_errata.html",
    "as_of": "1979-09"
  }
}
```

- [ ] **Step 2: Write the failing tests**

`tests/test_fetch.py`:

```python
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
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_fetch.py -q`
Expected: ImportError / ModuleNotFoundError for `fetch`.

- [ ] **Step 4: Write tools/fetch.py**

```python
#!/usr/bin/env python3
"""Fetch pinned sources into ~/.cache/cna-scans. Nothing fetched here is ever committed.

  python3 tools/fetch.py pages 96 97 98     # scan pages (jp2 index) -> cache/p0096.jpg ...
  python3 tools/fetch.py sections           # all 65 source-text sections at the pinned commit
  python3 tools/fetch.py verify             # download the jp2 zip, check SHA-1, print SHA-256
"""
import hashlib
import json
import os
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = ROOT / "tools" / "sources.json"
CACHE = pathlib.Path(os.path.expanduser("~/.cache/cna-scans"))


def load_sources() -> dict:
    return json.loads(SOURCES.read_text())


def _download(url: str, dest: pathlib.Path) -> None:
    """The only network call in this module; tests replace it. Callers create the parent dir."""
    urllib.request.urlretrieve(url, dest)


def scan_page(page) -> pathlib.Path:
    """Return the cached JPEG for a jp2 index (int or 4-digit string)."""
    page = f"{int(page):04d}"
    dest = CACHE / f"p{page}.jpg"
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        _download(load_sources()["archive_org"]["page_url_template"].format(page=page), dest)
    return dest


def source_section(n: int) -> pathlib.Path:
    """Return the cached AsciiDoc for source section n at the pinned commit."""
    src = load_sources()["source_text"]
    dest = CACHE / "source" / src["commit"] / f"section-{n:02d}.adoc"
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        _download(src["raw_url_template"].format(commit=src["commit"], nn=f"{n:02d}"), dest)
    return dest


def all_source_sections() -> list[pathlib.Path]:
    lo, hi = load_sources()["source_text"]["sections"]
    return [source_section(n) for n in range(lo, hi + 1)]


def _verify_zip() -> None:
    s = load_sources()["archive_org"]
    name = "The Campaign for North Africa_jp2.zip"
    dest = CACHE / "jp2.zip"
    if not dest.exists():
        url = f"https://archive.org/download/{s['identifier']}/{name.replace(' ', '%20')}"
        print(f"downloading {url} ({s['files'][name]['size'] / 1e6:.0f} MB) …", file=sys.stderr)
        _download(url, dest)
    sha1, sha256 = hashlib.sha1(), hashlib.sha256()
    with dest.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            sha1.update(chunk)
            sha256.update(chunk)
    ok = sha1.hexdigest() == s["files"][name]["sha1"]
    print(f"sha1   {sha1.hexdigest()}  {'OK' if ok else 'MISMATCH'}")
    print(f"sha256 {sha256.hexdigest()}")
    sys.exit(0 if ok else 1)


def main(argv: list[str]) -> None:
    cmd, args = (argv + [None])[0], argv[1:]
    if cmd == "pages":
        for p in args:
            print(scan_page(p))
    elif cmd == "sections":
        for p in all_source_sections():
            print(p)
    elif cmd == "verify":
        _verify_zip()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_fetch.py -q`
Expected: 4 passed

- [ ] **Step 6: Pin the SHA-256 and point learn_page.py at fetch**

```bash
.venv/bin/python tools/fetch.py verify      # ~350 MB download; prints sha1 OK and the sha256
```

Copy the printed sha256 into `tools/sources.json` → `files["The Campaign for North Africa_jp2.zip"].sha256` (replace `null`). Leave the other two `sha256: null` (their SHA-1s are archive.org's; we only use the jp2 pages).

In `tools/learn_page.py`, delete **only** the `IA = (...)` constant (the two-line string starting `IA = ("https://archive.org/download/…`) and the `def scan(page):` function that follows it (`grep -n 'IA = \|^def scan' tools/learn_page.py` shows both). Keep `ROOT`, `OUT` and `CACHE` — `build()` uses `OUT`. In their place put:

```python
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fetch import scan_page  # noqa: E402


def scan(page):
    """jp2 index (0-based); XML page n == jp2 n-1."""
    return Image.open(scan_page(page))
```

and add `sys` to the existing `import html, math, os, pathlib, urllib.request` line (drop `urllib.request` if nothing else uses it — check with `grep -n urllib tools/learn_page.py`). Verify: `.venv/bin/python tools/learn_page.py` still regenerates `docs/learn/index.html` (pages are already cached, so no download) and `git diff --stat docs/learn` shows no change to `index.html`.

- [ ] **Step 7: Commit**

```bash
git add tools/sources.json tools/fetch.py tools/learn_page.py tests/test_fetch.py
git commit -m "Pin archive.org item and source-text commit; add tools/fetch.py"
```

---

### Task 3: `data/README.md` and JSON Schemas

**Files:**
- Create: `data/README.md`, `data/schema/common.schema.json`, `data/schema/spi-cases.schema.json`, `data/schema/errata-patch.schema.json`, `tests/test_schemas.py`

**Interfaces:**
- Produces: `$defs` in `common.schema.json` that every later table schema `$ref`s by `common.schema.json#/$defs/<name>`: `caseRef`, `scanRef`, `sourceRef`, `sources`, `hexId`, `hexside`, `side`, `nation`, `weather`, `unitType`, `unitClass`, `supplyType`, `phase`, `terrain`.
- Produces: the `spi-cases.json` shape consumed by Tasks 4, 5, 7.

- [ ] **Step 1: Write the failing test**

`tests/test_schemas.py`:

```python
import json
import pathlib

import jsonschema
import pytest
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "data" / "schema"


def registry():
    reg = Registry()
    for p in SCHEMA_DIR.glob("*.schema.json"):
        reg = reg.with_resource(p.name, Resource.from_contents(json.loads(p.read_text())))
    return reg


def validator(name):
    return Draft202012Validator(json.loads((SCHEMA_DIR / name).read_text()), registry=registry())


def test_all_schemas_are_valid_2020_12():
    for p in SCHEMA_DIR.glob("*.schema.json"):
        Draft202012Validator.check_schema(json.loads(p.read_text()))


def test_spi_cases_schema_accepts_minimal_and_rejects_bad_id():
    v = validator("spi-cases.schema.json")
    good = {"source": {"repo": "tonicebrian/TheCampaignForNorthAfrica", "commit": "a" * 40},
            "cases": [{"id": "8.11", "section": 8, "kind": "secondary", "anchor": "8_11", "label": "", "page": None}]}
    v.validate(good)
    bad = dict(good, cases=[dict(good["cases"][0], id="8-11")])
    with pytest.raises(jsonschema.ValidationError):
        v.validate(bad)


@pytest.mark.parametrize("ref,ok", [
    ("CNA1979:8.37", True), ("CNA1979:32.0", True), ("scan:p96", True), ("scan:p0096", True),
    ("CNA1979:8", False), ("p96", False), ("CNA1979:8.37a", False),
])
def test_source_ref_grammar(ref, ok):
    v = validator("common.schema.json")
    schema = {"$ref": "common.schema.json#/$defs/sourceRef"}
    val = Draft202012Validator(schema, registry=registry())
    assert val.is_valid(ref) is ok


@pytest.mark.parametrize("hexid,ok", [("C4023", True), ("A0101", True), ("c4023", False), ("C423", False), ("F4023", False)])
def test_hex_id_grammar(hexid, ok):
    val = Draft202012Validator({"$ref": "common.schema.json#/$defs/hexId"}, registry=registry())
    assert val.is_valid(hexid) is ok


def test_errata_patch_schema_requires_table_and_ops():
    v = validator("errata-patch.schema.json")
    v.validate({"id": "E-001", "table": "terrain-effects", "affects": ["8.37"],
                "sources": ["CNA1979:8.37"], "summary": "escarpment cost corrected",
                "patches": [{"op": "replace", "path": "/rows/3/cost", "value": 6}]})
    with pytest.raises(jsonschema.ValidationError):
        v.validate({"id": "E-001", "patches": []})


def test_errata_patch_value_required_for_add_and_replace_only():
    v = validator("errata-patch.schema.json")
    base = {"id": "E-001", "table": "terrain-effects", "affects": ["8.37"], "sources": ["CNA1979:8.37"], "summary": "x"}
    v.validate(dict(base, patches=[{"op": "remove", "path": "/rows/3"}]))
    with pytest.raises(jsonschema.ValidationError):
        v.validate(dict(base, patches=[{"op": "replace", "path": "/rows/3/cost"}]))
    with pytest.raises(jsonschema.ValidationError):
        v.validate(dict(base, patches=[{"op": "add", "path": "/rows/3/cost"}]))
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_schemas.py -q`
Expected: failures (schema files missing).

- [ ] **Step 3: Write common.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "common.schema.json",
  "title": "Shared definitions for CNA Living Rules data",
  "$defs": {
    "caseRef": {"type": "string", "pattern": "^CNA1979:[1-9][0-9]?\\.[0-9]{1,2}$",
                "description": "SPI 1979 rules case, e.g. CNA1979:8.37; section.0 is the section itself"},
    "scanRef": {"type": "string", "pattern": "^scan:p[0-9]{1,4}$",
                "description": "archive.org jp2 index (0-based), as used by tools/fetch.py"},
    "sourceRef": {"oneOf": [{"$ref": "#/$defs/caseRef"}, {"$ref": "#/$defs/scanRef"}]},
    "sources": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/sourceRef"}},
    "hexId": {"type": "string", "pattern": "^[A-E][0-9]{4}$",
              "description": "Map sheet letter + RRCC as printed, e.g. C4023"},
    "hexside": {"type": "object", "required": ["a", "b"], "additionalProperties": false,
                "properties": {"a": {"$ref": "#/$defs/hexId"}, "b": {"$ref": "#/$defs/hexId"}},
                "description": "Unordered pair; convention a < b (checked by check_data once a table uses it)"},
    "side": {"enum": ["cw", "axis"]},
    "nation": {"enum": ["cw", "it", "de"]},
    "weather": {"enum": ["normal", "hot", "sandstorm", "rainstorm"]},
    "unitType": {"enum": ["infantry", "tank", "recce", "anti-tank", "anti-aircraft", "artillery",
                          "engineer", "aircraft", "ground-support", "recovery", "dummy-tank", "truck", "hq"]},
    "unitClass": {"enum": ["infantry", "armor", "gun", "truck"]},
    "supplyType": {"enum": ["ammo", "fuel", "stores", "water"]},
    "phase": {"enum": ["initiative-declaration", "weather", "organisation", "arrival", "cw-fleet",
                       "reserve-designation", "movement-combat", "truck-convoy", "rail", "repair", "patrol"],
              "description": "SPI phases A–L of an Operations Stage (there is no I)"},
    "terrain": {"enum": ["clear", "rough", "desert", "road", "track", "escarpment", "pass", "sea"],
                "description": "Seed list; extended in the movement PR when the Terrain Effects Chart is transcribed"}
  }
}
```

- [ ] **Step 4: Write spi-cases.schema.json and errata-patch.schema.json**

`data/schema/spi-cases.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "spi-cases.schema.json",
  "title": "Canonical list of SPI 1979 case IDs (no SPI text)",
  "type": "object",
  "required": ["source", "cases"],
  "additionalProperties": false,
  "properties": {
    "source": {"type": "object", "required": ["repo", "commit"], "additionalProperties": false,
               "properties": {"repo": {"type": "string"}, "commit": {"type": "string", "pattern": "^[0-9a-f]{40}$"}}},
    "cases": {"type": "array", "items": {
      "type": "object", "required": ["id", "section", "kind", "anchor", "label", "page"], "additionalProperties": false,
      "properties": {
        "id": {"type": "string", "pattern": "^[1-9][0-9]?\\.[0-9]{1,2}$"},
        "section": {"type": "integer", "minimum": 1, "maximum": 65},
        "kind": {"enum": ["section", "primary", "secondary"]},
        "anchor": {"type": "string", "pattern": "^[1-9][0-9]?_[0-9]{1,2}$", "description": "anchor id in the source repo"},
        "label": {"type": "string", "description": "OUR one-line label; empty until the case is restated"},
        "page": {"type": ["integer", "null"], "description": "jp2 index of the scan page, when known"}
      }}}
  }
}
```

`data/schema/errata-patch.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "errata-patch.schema.json",
  "title": "Errata overlay applied to a data table at build time (RFC 6902 operations)",
  "type": "object",
  "required": ["id", "table", "affects", "sources", "summary", "patches"],
  "additionalProperties": false,
  "properties": {
    "id": {"type": "string", "pattern": "^E-[0-9]{3}$"},
    "table": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "data/tables/<table>.json"},
    "affects": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": "^[1-9][0-9]?\\.[0-9]{1,2}$"}},
    "sources": {"$ref": "common.schema.json#/$defs/sources"},
    "summary": {"type": "string", "minLength": 1, "description": "Our paraphrase of the correction"},
    "patches": {"type": "array", "minItems": 1, "items": {
      "type": "object", "required": ["op", "path"],
      "properties": {"op": {"enum": ["add", "remove", "replace"]}, "path": {"type": "string", "pattern": "^/"}, "value": {}},
      "if": {"properties": {"op": {"enum": ["add", "replace"]}}}, "then": {"required": ["value"]}
    }}
  }
}
```

- [ ] **Step 5: Write data/README.md**

```markdown
# Data conventions

Everything in `data/` is CC0. Values are believed to be uncopyrightable facts
and game parameters; the organisation is ours. Read this before adding or
transcribing anything.

## Files

| Path | What |
|---|---|
| `spi-cases.json` | Canonical list of SPI case IDs (generated by `tools/gen_spi_cases.py`). IDs, kind, anchor, **our** label, page. Never SPI text. |
| `schema/*.schema.json` | JSON Schema 2020-12, one per table plus `common.schema.json` for shared `$defs`. |
| `tables/<concept>.json` | One file per **concept** (terrain effects, close-assault CRT, barrage CRT, anti-armour CRT, weather, fuel consumption, initiative ratings, stacking, CP costs, sequence of play …), *not* per SPI chart. Values **as printed**. Validated against `schema/<concept>.schema.json`. |
| `errata/E-nnn.json` | Overlays applied to a table at build time. Base values and patches are both inspectable. |

## Identifier grammar

| Thing | Form | Example |
|---|---|---|
| SPI case | `<section>.<case>`; `.0` is the section itself | `8.37`, `32.0` |
| Case reference (in `sources`) | `CNA1979:<case>` | `CNA1979:8.37` |
| Scan reference (in `sources`) | `scan:p<jp2 index>` (0-based, as `tools/fetch.py` names pages) | `scan:p96` |
| Table | `table:<concept>` = `tables/<concept>.json` | `table:terrain-effects` |
| Unit | `unit:<nation>:<slug>`, nation ∈ `cw`, `it`, `de` | `unit:cw:1-rnf` |
| Errata entry | `E-nnn`, sequential, ours | `E-003` |
| Ruling | `R-nnn`, sequential, ours (see `rulings/README.md`) | `R-012` |
| Variant | `V-nnn`, sequential, ours | `V-001` |
| Hex | sheet letter + `RRCC` as printed on the map | `C4023` |
| Hexside | unordered pair of hexes, stored sorted | `{"a": "C4023", "b": "C4024"}` |

Every record in a table carries `sources: ["CNA1979:8.37", "scan:p96"]` —
at least the case that defines it and, for transcribed values, the page it
was read from. `tools/check_data.py` rejects unknown cases.

## Hex grid convention

Pointy-top hexes. Columns (`CC`) increase eastward; rows (`RR`) increase
**northward**; odd rows sit half a hex **west** of even rows. A hex's six
neighbours are therefore, for even row `r` and column `c`:
`(r, c±1)`, `(r±1, c)`, `(r±1, c+1)`; and for odd `r`: `(r, c±1)`, `(r±1, c)`,
`(r±1, c−1)`. Sheet letters A–E; sheet edges join along printed hex numbers.
This is the convention measured from the archive.org scan of map C in
`tools/learn_page.py` and is *provisional until the map sub-project confirms
it against the VASSAL module*.

## Enumerations

Defined once in `schema/common.schema.json` and `$ref`'d from every table:

| Enum | Values | From |
|---|---|---|
| `weather` | normal, hot, sandstorm, rainstorm | §29 |
| `unitType` | infantry, tank, recce, anti-tank, anti-aircraft, artillery, engineer, aircraft, ground-support, recovery, dummy-tank, truck, hq | §3.21 (+ HQ, §3.3) |
| `unitClass` | infantry, armor, gun, truck | §3.22 |
| `supplyType` | ammo, fuel, stores, water | §32.11 |
| `phase` | initiative-declaration, weather, organisation, arrival, cw-fleet, reserve-designation, movement-combat, truck-convoy, rail, repair, patrol | §5.2 (A–L, no I) |
| `terrain` | clear, rough, desert, road, track, escarpment, pass, sea — **seed**, extended when 8.37 is transcribed | §8.37 |
| `side` / `nation` | cw, axis / cw, it, de | — |

Adding an enum value is a data PR that must say which case introduces it.

## Errata as overlay

Base tables hold the values **as printed in 1979**. Each errata item that
changes a table value is a file `errata/E-nnn.json` with RFC 6902 `add` /
`remove` / `replace` operations against that table, the cases it affects,
its source, and our one-line paraphrase. The site build applies overlays;
`check_data.py` validates them and checks the target table exists. Rules
prose always describes the post-errata value and annotates it with
`::: errata E-nnn`.

## Transcription procedure

1. Fetch the page: `python3 tools/fetch.py pages <n>`.
2. Two independent extractions (two vision models, or one model plus the
   BGG spreadsheets). Diff them. Humans resolve only the discrepancies.
3. Where the printed table has totals or symmetric structure, encode them as
   invariants in the schema (`check_data.py` runs them).
4. Record `sources` with both the case and the `scan:p<n>` page.
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_schemas.py -q`
Expected: all passed

- [ ] **Step 7: Commit**

```bash
git add data/README.md data/schema tests/test_schemas.py
git commit -m "Data conventions: ID grammar, enums, hex convention, schemas for cases and errata overlays"
```

---

### Task 4: Generate `data/spi-cases.json` from source anchors

**Files:**
- Create: `tools/gen_spi_cases.py`, `tests/test_gen_spi_cases.py`, `data/spi-cases.json`

**Interfaces:**
- Consumes: `fetch.all_source_sections()`, `fetch.load_sources()`.
- Produces: `gen_spi_cases.parse_anchors(text)`, `gen_spi_cases.build_cases(section_texts)`; the generated `data/spi-cases.json` (1,736 cases at the pinned commit, 974 of them in §1–32) used by the data and coverage checks.

Facts about the source (verified 2026-09-18 at the pinned commit): anchors are lines like `[#8_11]`, sometimes with trailing whitespace; one malformed anchor `[#17.6]` in section 17 (treat `.` as `_`); a few anchors are duplicated across files (keep the first); `_0` is the section heading; one digit after `_` is a primary case, two digits a secondary case.

- [ ] **Step 1: Write the failing tests**

`tests/test_gen_spi_cases.py`:

```python
import gen_spi_cases as g

SAMPLE = """[#8_0] 
== LAND MOVEMENT

GENERAL RULE: some text

[#8_1]
=== HOW TO MOVE UNITS

[#8_11]
*[8.11]* Units may be moved ...
[#8_12]
*[8.12]* Under certain conditions ...
[#8_11]
duplicate anchor should be ignored
[#17.6]
=== malformed dot anchor
"""


def test_parse_anchors_kinds_and_normalisation():
    got = g.parse_anchors(SAMPLE)
    assert got[0] == {"id": "8.0", "section": 8, "kind": "section", "anchor": "8_0"}
    assert got[1] == {"id": "8.1", "section": 8, "kind": "primary", "anchor": "8_1"}
    assert got[2] == {"id": "8.11", "section": 8, "kind": "secondary", "anchor": "8_11"}
    assert [c["id"] for c in got] == ["8.0", "8.1", "8.11", "8.12", "17.6"]


def test_build_cases_sorts_dedupes_and_adds_empty_label_and_page():
    cases = g.build_cases({17: "[#17_0]\n[#17_6]\n", 8: SAMPLE})
    ids = [c["id"] for c in cases]
    assert ids == ["8.0", "8.1", "8.11", "8.12", "17.0", "17.6"]
    assert all(c["label"] == "" and c["page"] is None for c in cases)


def test_no_source_text_leaks_into_records():
    cases = g.build_cases({8: SAMPLE})
    assert set().union(*(set(c) for c in cases)) == {"id", "section", "kind", "anchor", "label", "page"}
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_gen_spi_cases.py -q`
Expected: ModuleNotFoundError for `gen_spi_cases`.

- [ ] **Step 3: Write tools/gen_spi_cases.py**

```python
#!/usr/bin/env python3
"""Generate data/spi-cases.json — the canonical list of SPI case IDs — from the
anchors in the pinned source-text repo. Only IDs and structure are taken; no text.

  python3 tools/gen_spi_cases.py           # rewrites data/spi-cases.json
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fetch  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "spi-cases.json"
ANCHOR = re.compile(r"^\[#(\d{1,2})[._](\d{1,2})\]\s*$", re.M)


def parse_anchors(adoc_text: str) -> list[dict]:
    """Anchors in file order, de-duplicated (first wins). '.' in an anchor is a source typo for '_'."""
    seen, out = set(), []
    for m in ANCHOR.finditer(adoc_text):
        section, case = int(m.group(1)), m.group(2)
        anchor = f"{section}_{case}"
        if anchor in seen:
            continue
        seen.add(anchor)
        if len(case) == 2 and case.endswith("0"):  # transcription defects, e.g. [#30_60], [#32_10]
            print(f"gen_spi_cases: skipping [#{anchor}] — no two-digit SPI case ends in 0", file=sys.stderr)
            continue
        kind = "section" if case == "0" else "primary" if len(case) == 1 else "secondary"
        out.append({"id": f"{section}.{case}", "section": section, "kind": kind, "anchor": anchor})
    return out


def build_cases(section_texts: dict[int, str]) -> list[dict]:
    """All cases across sections, sorted (section, case-number), first occurrence wins."""
    by_anchor = {}
    for n in sorted(section_texts):
        for c in parse_anchors(section_texts[n]):
            by_anchor.setdefault(c["anchor"], c)
    cases = sorted(by_anchor.values(), key=lambda c: (c["section"], int(c["anchor"].split("_")[1])))
    return [dict(c, label="", page=None) for c in cases]


def main() -> None:
    src = fetch.load_sources()["source_text"]
    texts = {int(p.stem.split("-")[1]): p.read_text(errors="replace") for p in fetch.all_source_sections()}
    fresh = build_cases(texts)
    if OUT.exists():  # keep labels/pages already authored
        old = {c["id"]: c for c in json.loads(OUT.read_text())["cases"]}
        for c in fresh:
            if c["id"] in old:
                c["label"], c["page"] = old[c["id"]]["label"], old[c["id"]]["page"]
    OUT.write_text(json.dumps({"source": {"repo": src["repo"], "commit": src["commit"]}, "cases": fresh},
                              indent=1, ensure_ascii=False) + "\n")
    print(f"{len(fresh)} cases → {OUT}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_gen_spi_cases.py -q`
Expected: 3 passed

- [ ] **Step 5: Generate the real file and validate it**

```bash
.venv/bin/python tools/fetch.py sections >/dev/null
.venv/bin/python tools/gen_spi_cases.py
.venv/bin/python - <<'PYEOF'
import json; d=json.load(open('data/spi-cases.json')); c=d['cases']
print(len(c), 'cases;', sum(x['kind']=='section' for x in c), 'sections;', sorted({x['section'] for x in c})==list(range(1,66)))
print([x['id'] for x in c if x['section']==17 and x['kind']=='primary'])
PYEOF
grep -c '"id"' data/spi-cases.json
```

Expected: `1736 cases; 65 sections; True` (exact, at the pinned commit; two malformed source anchors [#30_60] and [#32_10] are skipped with a warning); section 17 primaries include `17.6`. Inspect that no value in the file is prose (`grep -v '"label": ""' data/spi-cases.json | grep label` prints nothing).

- [ ] **Step 6: Commit**

```bash
git add tools/gen_spi_cases.py tests/test_gen_spi_cases.py data/spi-cases.json
git commit -m "Generate canonical SPI case list from pinned source anchors"
```

---

### Task 5: Data gate — `tools/check_data.py`

**Files:**
- Create: `tools/check_data.py`, `tests/test_check_data.py`

**Interfaces:**
- Consumes: `data/schema/*.schema.json`, `data/spi-cases.json`, `data/tables/*.json`, `data/errata/*.json`.
- Produces: `check_data.validate_all(data_dir) -> list[str]`; CLI exits 1 with the errors printed if the list is non-empty.

Rules enforced: (1) every schema is valid 2020-12; (2) `spi-cases.json` validates; (3) every `tables/<x>.json` has a `schema/<x>.schema.json` and validates against it; (4) every `errata/*.json` validates against `errata-patch.schema.json`, its `table` exists, its `id` matches its filename, and every `affects` id is a known case; (5) every string matching `CNA1979:…` anywhere in `tables/` or `errata/` names a case in `spi-cases.json`.

- [ ] **Step 1: Write the failing tests**

`tests/test_check_data.py`:

```python
import json
import pathlib
import shutil

import check_data

ROOT = pathlib.Path(__file__).resolve().parents[1]


def make_data(tmp_path, tables=None, errata=None):
    d = tmp_path / "data"
    shutil.copytree(ROOT / "data" / "schema", d / "schema")
    (d / "spi-cases.json").write_text(json.dumps({
        "source": {"repo": "x/y", "commit": "a" * 40},
        "cases": [{"id": "8.37", "section": 8, "kind": "secondary", "anchor": "8_37", "label": "", "page": None}]}))
    (d / "schema" / "demo.schema.json").write_text(json.dumps({
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "demo.schema.json",
        "type": "object", "required": ["rows"],
        "properties": {"rows": {"type": "array", "items": {"type": "object", "required": ["cost", "sources"],
                       "properties": {"cost": {"type": "integer"}, "sources": {"$ref": "common.schema.json#/$defs/sources"}}}}}}))
    (d / "tables").mkdir()
    for name, body in (tables or {}).items():
        (d / "tables" / name).write_text(json.dumps(body))
    (d / "errata").mkdir()
    for name, body in (errata or {}).items():
        (d / "errata" / name).write_text(json.dumps(body))
    return d


def test_real_data_dir_passes():
    assert check_data.validate_all(ROOT / "data") == []


def test_valid_table_passes(tmp_path):
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": 2, "sources": ["CNA1979:8.37", "scan:p96"]}]}})
    assert check_data.validate_all(d) == []


def test_table_without_schema_fails(tmp_path):
    d = make_data(tmp_path, tables={"orphan.json": {"rows": []}})
    errs = check_data.validate_all(d)
    assert any("orphan.json" in e and "no schema" in e for e in errs)


def test_schema_violation_reported_with_path(tmp_path):
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": "two", "sources": ["CNA1979:8.37"]}]}})
    errs = check_data.validate_all(d)
    assert any("demo.json" in e and "rows/0/cost" in e for e in errs)


def test_unknown_case_reference_fails(tmp_path):
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": 2, "sources": ["CNA1979:99.9"]}]}})
    errs = check_data.validate_all(d)
    assert any("CNA1979:99.9" in e and "unknown case" in e for e in errs)


def test_errata_must_target_existing_table_and_match_filename(tmp_path):
    patch = {"id": "E-001", "table": "missing", "affects": ["8.37"], "sources": ["CNA1979:8.37"],
             "summary": "x", "patches": [{"op": "replace", "path": "/rows/0/cost", "value": 3}]}
    d = make_data(tmp_path, errata={"E-002.json": patch})
    errs = check_data.validate_all(d)
    assert any("E-002.json" in e and "table 'missing'" in e for e in errs)
    assert any("E-002.json" in e and "id E-001" in e for e in errs)


def test_errata_affects_must_name_known_cases(tmp_path):
    patch = {"id": "E-001", "table": "demo", "affects": ["8.37", "9.99"], "sources": ["CNA1979:8.37"],
             "summary": "x", "patches": [{"op": "replace", "path": "/rows/0/cost", "value": 3}]}
    d = make_data(tmp_path, tables={"demo.json": {"rows": [{"cost": 2, "sources": ["CNA1979:8.37"]}]}},
                  errata={"E-001.json": patch})
    errs = check_data.validate_all(d)
    assert any("E-001.json" in e and "affects unknown case 9.99" in e for e in errs)
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_check_data.py -q`
Expected: ModuleNotFoundError for `check_data`.

- [ ] **Step 3: Write tools/check_data.py**

```python
#!/usr/bin/env python3
"""Data gate: schemas valid, every table/errata file validates, every case reference exists.

  python3 tools/check_data.py [data_dir]     # exit 1 and print errors on failure
"""
import json
import pathlib
import re
import sys

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parents[1]
CASE_REF = re.compile(r"^CNA1979:(\d{1,2}\.\d{1,2})$")


def _registry(schema_dir: pathlib.Path) -> Registry:
    reg = Registry()
    for p in schema_dir.glob("*.schema.json"):
        reg = reg.with_resource(p.name, Resource.from_contents(json.loads(p.read_text())))
    return reg


def _validate(instance, schema_path: pathlib.Path, reg: Registry, label: str) -> list[str]:
    v = Draft202012Validator(json.loads(schema_path.read_text()), registry=reg)
    return [f"{label}: /{'/'.join(str(x) for x in e.absolute_path)}: {e.message}"
            for e in sorted(v.iter_errors(instance), key=lambda e: str(list(e.absolute_path)))]


def _case_refs(obj) -> set[str]:
    if isinstance(obj, str):
        m = CASE_REF.match(obj)
        return {obj} if m else set()
    if isinstance(obj, dict):
        return set().union(*(_case_refs(v) for v in obj.values())) if obj else set()
    if isinstance(obj, list):
        return set().union(*(_case_refs(v) for v in obj)) if obj else set()
    return set()


def validate_all(data_dir: pathlib.Path) -> list[str]:
    errors: list[str] = []
    schema_dir = data_dir / "schema"
    for p in sorted(schema_dir.glob("*.schema.json")):
        try:
            Draft202012Validator.check_schema(json.loads(p.read_text()))
        except Exception as e:  # noqa: BLE001 — report any schema problem
            errors.append(f"{p.name}: invalid schema: {e}")
    if errors:
        return errors
    reg = _registry(schema_dir)

    cases_path = data_dir / "spi-cases.json"
    cases = json.loads(cases_path.read_text())
    errors += _validate(cases, schema_dir / "spi-cases.schema.json", reg, "spi-cases.json")
    known = {c["id"] for c in cases.get("cases", [])}

    tables = {}
    for p in sorted((data_dir / "tables").glob("*.json")) if (data_dir / "tables").is_dir() else []:
        schema = schema_dir / f"{p.stem}.schema.json"
        if not schema.exists():
            errors.append(f"tables/{p.name}: no schema (expected schema/{schema.name})")
            continue
        tables[p.stem] = json.loads(p.read_text())
        errors += _validate(tables[p.stem], schema, reg, f"tables/{p.name}")
        for ref in sorted(_case_refs(tables[p.stem]) - {f"CNA1979:{k}" for k in known}):
            errors.append(f"tables/{p.name}: unknown case reference {ref}")

    for p in sorted((data_dir / "errata").glob("*.json")) if (data_dir / "errata").is_dir() else []:
        patch = json.loads(p.read_text())
        errors += _validate(patch, schema_dir / "errata-patch.schema.json", reg, f"errata/{p.name}")
        if patch.get("id") and patch["id"] != p.stem:
            errors.append(f"errata/{p.name}: id {patch['id']} does not match filename")
        if patch.get("table") and patch["table"] not in tables:
            errors.append(f"errata/{p.name}: table '{patch['table']}' does not exist")
        for ref in sorted(_case_refs(patch) - {f"CNA1979:{k}" for k in known}):
            errors.append(f"errata/{p.name}: unknown case reference {ref}")
        affects = patch.get("affects")
        if isinstance(affects, list):  # otherwise the schema error above already covers it
            for c in sorted(set(map(str, affects)) - known):
                errors.append(f"errata/{p.name}: affects unknown case {c}")
    return errors


def main(argv: list[str]) -> None:
    data_dir = pathlib.Path(argv[0]) if argv else ROOT / "data"
    errors = validate_all(data_dir)
    for e in errors:
        print(e)
    print(f"check_data: {'FAIL' if errors else 'OK'} ({len(errors)} errors)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_check_data.py -q`
Expected: 7 passed. Also run `.venv/bin/python tools/check_data.py` → `check_data: OK (0 errors)`.

- [ ] **Step 5: Commit**

```bash
git add tools/check_data.py tests/test_check_data.py
git commit -m "Add data gate: schema validation and case-reference integrity"
```

---

### Task 6: Overlap gate — `tools/check_overlap.py`

**Files:**
- Create: `tools/check_overlap.py`, `tools/overlap-allowlist.txt`, `tests/test_check_overlap.py`

**Interfaces:**
- Consumes: `fetch.all_source_sections()`.
- Produces: `check_overlap.strip_markdown`, `strip_asciidoc`, `normalize`, `ngrams`, `load_allowlist`, `load_allowlist_text`, `find_overlaps`, `source_ngrams`; CLI `python3 tools/check_overlap.py [--n 8] [path ...]` (default: `rules/`, `rulings/`, `README.md`, `data/README.md` — everything the site renders as our prose) exits 1 on any hit.

Normalisation is shared for both sides: lowercase; `’`→`'`; drop everything but `[a-z0-9']`; tokens split on whitespace. Markdown stripping removes YAML frontmatter, badge lines (`::: …`), heading markers, emphasis, table pipes, link targets, inline code ticks. AsciiDoc stripping removes anchor lines, heading markers, `*[8.11]*` case labels, `<<8_37,8.37>>` cross-refs (keeping the visible number), and `====` block fences. The allowlist is one phrase per line; a phrase of ≥8 words allows every 8-gram inside it.

- [ ] **Step 1: Write the failing tests**

`tests/test_check_overlap.py`:

```python
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
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_check_overlap.py -q`
Expected: ModuleNotFoundError for `check_overlap`.

- [ ] **Step 3: Write tools/check_overlap.py and the allowlist**

```python
#!/usr/bin/env python3
"""Overlap gate: fail if any N-word run (default 8) in our prose — rules/, rulings/, and the
READMEs the site renders — also occurs in the source transcription. A control against verbatim
copying only.

  python3 tools/check_overlap.py [--n 8] [path ...]     # each path a .md file or a directory
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fetch  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "tools" / "overlap-allowlist.txt"
TOKEN = re.compile(r"[a-z0-9']+")


def normalize(text: str) -> list[str]:
    text = text.lower().replace("’", "'").replace("‘", "'")
    return TOKEN.findall(text)


def strip_markdown(md: str) -> str:
    if md.startswith("---"):
        end = md.find("\n---", 3)
        if end != -1:
            md = md[end + 4:]
    out = []
    for line in md.splitlines():
        s = line.strip()
        if s.startswith(":::"):
            continue
        if re.fullmatch(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?", s):
            continue
        s = re.sub(r"^#{1,6}\s+", "", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = s.replace("|", " ").replace("`", " ").replace("*", " ").replace("_", " ")
        out.append(s)
    return "\n".join(out)


def strip_asciidoc(adoc: str) -> str:
    out = []
    for line in adoc.splitlines():
        s = line.strip()
        if re.fullmatch(r"\[#[^\]]+\]", s) or re.fullmatch(r"=+", s) or s.startswith("[") and s.endswith("]"):
            continue
        s = re.sub(r"^=+\s+", "", s)
        s = re.sub(r"\*\[[\d.]+\]\*", "", s)
        s = re.sub(r"<<[^,>]+,([^>]+)>>", r"\1", s)
        s = s.replace("*", " ").replace("_", " ")
        out.append(s)
    return "\n".join(out)


def ngrams(tokens: list[str], n: int = 8) -> set[tuple[str, ...]]:
    return {tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def load_allowlist_text(text: str, n: int = 8) -> set[tuple[str, ...]]:
    allow: set[tuple[str, ...]] = set()
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            allow |= ngrams(normalize(line), n)
    return allow


def load_allowlist(path: pathlib.Path = ALLOWLIST, n: int = 8) -> set[tuple[str, ...]]:
    return load_allowlist_text(path.read_text(), n) if path.exists() else set()


def find_overlaps(rules_md: str, source_grams: set, allow: set, n: int = 8) -> list[tuple[str, ...]]:
    grams = ngrams(normalize(strip_markdown(rules_md)), n)
    return sorted((grams & source_grams) - allow)


def source_ngrams(n: int = 8) -> set[tuple[str, ...]]:
    grams: set[tuple[str, ...]] = set()
    for p in fetch.all_source_sections():
        grams |= ngrams(normalize(strip_asciidoc(p.read_text(errors="replace"))), n)
    return grams


def main(argv: list[str]) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=[str(ROOT / "rules"), str(ROOT / "rulings"),
                                                 str(ROOT / "README.md"), str(ROOT / "data" / "README.md")])
    ap.add_argument("--n", type=int, default=8)
    a = ap.parse_args(argv)
    files = sorted({f for p in map(pathlib.Path, a.paths)
                    for f in (p.rglob("*.md") if p.is_dir() else [p] if p.is_file() else [])})
    if not files:
        print("check_overlap: OK (no files)")
        return
    grams, allow = source_ngrams(a.n), load_allowlist(n=a.n)
    total = 0
    for f in files:
        for hit in find_overlaps(f.read_text(), grams, allow, a.n):
            total += 1
            print(f"{f.relative_to(ROOT)}: {' '.join(hit)}")
    print(f"check_overlap: {'FAIL' if total else 'OK'} ({total} shared {a.n}-word runs)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
```

`tools/overlap-allowlist.txt`:

```
# One phrase per line. Every 8-word run inside a phrase is allowed.
# Only for unavoidable fixed terms; never for rule sentences.
the campaign for north africa the desert war 1940 1943
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_check_overlap.py -q`
Expected: 6 passed. Then `.venv/bin/python tools/check_overlap.py` → `check_overlap: OK (0 shared 8-word runs)` (it scans `README.md` and `data/README.md`, which exist by now; `rules/` and `rulings/` are empty or absent). This is the first real run — it downloads the 65 source sections (~1 MB) into `~/.cache/cna-scans/source/`.

- [ ] **Step 5: Commit**

```bash
git add tools/check_overlap.py tools/overlap-allowlist.txt tests/test_check_overlap.py
git commit -m "Add overlap gate: 8-word n-gram check against source transcription"
```

---

### Task 7: Coverage report — `tools/check_coverage.py`

**Files:**
- Create: `tools/check_coverage.py`, `tests/test_check_coverage.py`

**Interfaces:**
- Consumes: `data/spi-cases.json`, `rules/**/*.md`.
- Produces: `check_coverage.parse_badges(md)`, `coverage(case_ids, badges_by_file, sections)`, `render_markdown(report)`; CLI `python3 tools/check_coverage.py [--sections 1-32] [--markdown]`. Exit code: 1 only for **errors** (a badge names an unknown case, or a case has more than one primary badge). Uncovered cases are informational.

- [ ] **Step 1: Write the failing tests**

`tests/test_check_coverage.py`:

```python
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
```

- [ ] **Step 2: Run to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_check_coverage.py -q`
Expected: ModuleNotFoundError for `check_coverage`.

- [ ] **Step 3: Write tools/check_coverage.py**

```python
#!/usr/bin/env python3
"""Coverage report: which SPI cases have no primary badge in rules/. A report, not a gate —
exits 1 only for malformed badges (unknown case, duplicate primary).

  python3 tools/check_coverage.py [--sections 1-32] [--markdown] [rules_dir]
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BADGE = re.compile(r"^:::\s+(spi|spi-ref|spi-omit)\s+(.*?)\s*$")
CASE = re.compile(r"^\d{1,2}\.\d{1,2}$")


def parse_badges(md: str) -> list[dict]:
    out = []
    for i, line in enumerate(md.splitlines(), 1):
        m = BADGE.match(line)
        if not m:
            continue
        kind, rest = m.group(1), m.group(2)
        reason = None
        if kind == "spi-omit":
            parts = re.split(r"\s+(?:—|--)\s+", rest, maxsplit=1)
            rest, reason = parts[0], (parts[1].strip() if len(parts) > 1 else None)
        out.append({"kind": kind, "cases": rest.split(), "reason": reason, "line": i})
    return out


def parse_sections(spec: str) -> set[int]:
    out: set[int] = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return out


def coverage(case_ids: list[str], badges_by_file: dict[str, list[dict]], sections: set[int] | None) -> dict:
    known = set(case_ids)
    in_scope = [c for c in case_ids if sections is None or int(c.split(".")[0]) in sections]
    primary: dict[str, str] = {}
    omitted: dict[str, str] = {}
    errors: list[str] = []
    for f, badges in badges_by_file.items():
        for b in badges:
            for c in b["cases"]:
                where = f"{f}:{b['line']}"
                if not CASE.match(c) or c not in known:
                    errors.append(f"{where}: unknown case {c}")
                    continue
                if b["kind"] == "spi":
                    if c in primary:
                        errors.append(f"{where}: second primary badge for {c} (first in {primary[c]})")
                    else:
                        primary[c] = where
                elif b["kind"] == "spi-omit":
                    omitted[c] = b["reason"] or ""
                    if not b["reason"]:
                        errors.append(f"{where}: spi-omit {c} needs a reason after ' — '")
    scope = set(in_scope)
    return {
        "total": len(in_scope),
        "primary": len(scope & set(primary)),
        "omitted": len(scope & set(omitted) - set(primary)),
        "uncovered": [c for c in in_scope if c not in primary and c not in omitted],
        "errors": sorted(errors),
    }


def render_markdown(rep: dict) -> str:
    covered = rep["primary"] + rep["omitted"]
    lines = [f"### SPI case coverage: {covered} / {rep['total']} "
             f"({rep['primary']} restated, {rep['omitted']} omitted with reason)", ""]
    if rep["errors"]:
        lines += ["**Errors:**"] + [f"- {e}" for e in rep["errors"]] + [""]
    if rep["uncovered"]:
        lines += [f"<details><summary>{len(rep['uncovered'])} cases without a primary badge</summary>", "",
                  " ".join(f"`{c}`" for c in rep["uncovered"]), "", "</details>"]
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("rules_dir", nargs="?", default=str(ROOT / "rules"))
    ap.add_argument("--sections", default=None, help="e.g. 1-32 or 1-3,8")
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args(argv)
    ids = [c["id"] for c in json.loads((ROOT / "data" / "spi-cases.json").read_text())["cases"]]
    files = sorted(pathlib.Path(a.rules_dir).rglob("*.md"))
    badges = {str(f.relative_to(ROOT)): parse_badges(f.read_text()) for f in files}
    rep = coverage(ids, badges, parse_sections(a.sections) if a.sections else None)
    if a.markdown:
        print(render_markdown(rep), end="")
    else:
        print(f"coverage: {rep['primary'] + rep['omitted']} / {rep['total']} "
              f"(primary {rep['primary']}, omitted {rep['omitted']}, uncovered {len(rep['uncovered'])})")
        for e in rep["errors"]:
            print(f"ERROR {e}")
    sys.exit(1 if rep["errors"] else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_check_coverage.py -q`
Expected: 5 passed. Then `.venv/bin/python tools/check_coverage.py --sections 1-32` → `coverage: 0 / 974 (primary 0, omitted 0, uncovered 974)` and exit 0.

- [ ] **Step 5: Commit**

```bash
git add tools/check_coverage.py tests/test_check_coverage.py
git commit -m "Add SPI case coverage report"
```

---

### Task 8: `rulings/README.md`

**Files:**
- Create: `rulings/README.md`
- Modify: `tests/test_repo_hygiene.py` (add one test)

- [ ] **Step 1: Add the failing test**

Append to `tests/test_repo_hygiene.py`:

```python
def test_rulings_readme_defines_statuses_and_fork_policy():
    text = (ROOT / "rulings" / "README.md").read_text()
    for word in ["proposed", "accepted", "rejected", "superseded", "## Fork policy", "R-001"]:
        assert word in text, word
```

Run: `.venv/bin/python -m pytest tests/test_repo_hygiene.py -q` → 1 failure.

- [ ] **Step 2: Write rulings/README.md**

```markdown
# Rulings

A **ruling** is a written decision on a gap, contradiction or ambiguity in
the 1979 rules (after errata). The rules prose always shows the *result* of
an accepted ruling; the ruling file shows the problem, the options and why.

## Files and numbering

One file per ruling: `rulings/R-nnn.md`, numbered sequentially from `R-001`
in the order they are opened. Numbers are never reused. Frontmatter:

```yaml
---
id: R-012
status: proposed            # proposed | accepted | rejected | superseded
affects: [8.37, 8.42]       # SPI cases the ruling touches
sources:                    # where the problem or a prior answer comes from
  - CNA1979:8.37
  - https://friendorfoe.com/war/cfna/houserules/#…   (NJHarman, CC-BY-SA 4.0)
supersedes: R-004           # optional
discussion: https://github.com/basmith7/cna/discussions/…
---
```

Body, in this order: **Problem** · **Options** (each with its consequence)
· **Decision** · **Rationale** · **Discussion** (link). Rules prose that
reflects the ruling carries `::: ruling R-012` above the block.

## Statuses

| Status | Meaning |
|---|---|
| `proposed` | Opened; not yet reflected in the rules prose. Seeded entries from NJHarman start here. |
| `accepted` | Reflected in the prose; the current rule. |
| `rejected` | Considered and not adopted; kept for the record. |
| `superseded` | Replaced by a later ruling named in `supersedes` of the newer file. |

Community **CHANGE** and **ADDITION** items (house rules that alter the game
rather than resolve it) are recorded as variants `V-nnn` with `::: variant`
containers, never as rulings.

## Process

1. Open a GitHub Discussion describing the problem with the case numbers.
2. Open a PR adding `R-nnn.md` as `proposed`, with the options written out.
3. Review. One maintainer accepts or rejects; the PR that accepts also edits
   the rules prose and adds the `::: ruling` annotation.
4. Anyone may dispute an accepted ruling by opening a new Discussion and a
   new `proposed` ruling that names the old one in `supersedes`.

## Fork policy

Disagreement is expected. If you want a different ruling than the one
accepted here, you are welcome and encouraged to fork: the rules and rulings
are CC-BY-SA 4.0, so a fork can keep everything, change any ruling, and
publish. We ask only that a fork say which rulings it changed. An engine
that consumes these rules should be able to point at a fork's `rules/` and
`rulings/` instead of ours.
```

- [ ] **Step 3: Run tests, commit**

Run: `.venv/bin/python -m pytest tests/test_repo_hygiene.py -q` → all passed.

```bash
git add rulings/README.md tests/test_repo_hygiene.py
git commit -m "Rulings: numbering, statuses, process, fork policy"
```

---

### Task 9: VitePress phase 1

**Files:**
- Create: `package.json`, `site/.vitepress/config.mts`, `site/.vitepress/spi-badge.mjs`, `site/.vitepress/spi-badge.test.mjs`, `site/.vitepress/theme/index.ts`, `site/.vitepress/theme/custom.css`, `rules/.gitkeep` (removed in Task 11)

**Interfaces:**
- Produces: `npm run site:dev|site:build|site:preview|test:site`; `spiBadgePlugin(md)` for markdown-it that turns the single-line badge syntax into `<p class="spi-badge …">` with an anchor `id="spi-<case>"` per primary case.
- Site routes: `/` (README), `/rules/<file>`, `/rulings/`, `/data/`.

- [ ] **Step 1: Install VitePress and write the failing plugin test**

```bash
cd /home/basmith7/Projects/cna
npm init -y >/dev/null
npm install -D vitepress markdown-it
```

Then set the metadata and scripts without touching the `devDependencies` npm just wrote:

```bash
node -e '
const fs = require("fs"); const p = JSON.parse(fs.readFileSync("package.json"));
const out = { name: "cna-living-rules", private: true, type: "module",
  scripts: { "site:dev": "vitepress dev site", "site:build": "vitepress build site",
             "site:preview": "vitepress preview site", "test:site": "node --test site/.vitepress/*.test.mjs" },
  devDependencies: p.devDependencies };
fs.writeFileSync("package.json", JSON.stringify(out, null, 2) + "\n");'
cat package.json     # expect exactly: name, private, type, scripts, devDependencies {markdown-it, vitepress}
```

`site/.vitepress/spi-badge.test.mjs`:

```js
import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import { spiBadgePlugin } from './spi-badge.mjs'

const md = new MarkdownIt().use(spiBadgePlugin)

test('primary badge renders tag with an anchor per case', () => {
  const html = md.render('::: spi 8.35 8.36\n\nBody.\n')
  assert.match(html, /<p class="spi-badge spi-primary">/)
  assert.match(html, /<a id="spi-8\.35" class="spi-anchor"><\/a>/)
  assert.match(html, /<a id="spi-8\.36" class="spi-anchor"><\/a>/)
  assert.match(html, /SPI 8\.35, 8\.36/)
  assert.match(html, /<p>Body\.<\/p>/)
})

test('spi-ref renders without anchors', () => {
  const html = md.render('::: spi-ref 8.35\n')
  assert.match(html, /<p class="spi-badge spi-ref">see SPI 8\.35<\/p>/)
  assert.doesNotMatch(html, /id="spi-/)
})

test('spi-omit renders reason', () => {
  const html = md.render('::: spi-omit 4.6 — component inventory\n')
  assert.match(html, /<p class="spi-badge spi-omit">SPI 4\.6 omitted — component inventory<\/p>/)
})

test('other ::: lines are untouched', () => {
  const html = md.render('::: note\nhi\n:::\n')
  assert.doesNotMatch(html, /spi-badge/)
})
```

Run: `npm run test:site` → fails (cannot find `./spi-badge.mjs`).

- [ ] **Step 2: Write the plugin**

`site/.vitepress/spi-badge.mjs`:

```js
// Single-line SPI badge syntax:  ::: spi 8.35 8.36 | ::: spi-ref 8.35 | ::: spi-omit 4.6 — reason
// No closing marker; scope is implicit (to the next badge or heading). Metadata only.
const RE = /^:::\s+(spi|spi-ref|spi-omit)\s+(.*?)\s*$/

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

export function spiBadgePlugin(md) {
  md.block.ruler.before('fence', 'spi_badge', (state, startLine, _endLine, silent) => {
    const line = state.src.slice(state.bMarks[startLine] + state.tShift[startLine], state.eMarks[startLine])
    const m = RE.exec(line)
    if (!m) return false
    if (silent) return true
    let cases = m[2], reason = null
    if (m[1] === 'spi-omit') {
      const parts = cases.split(/\s+(?:—|--)\s+/)
      cases = parts[0]
      reason = parts[1] ?? null
    }
    const token = state.push('spi_badge', '', 0)
    token.meta = { kind: m[1], cases: cases.split(/\s+/), reason }
    token.map = [startLine, startLine + 1]
    state.line = startLine + 1
    return true
  })

  md.renderer.rules.spi_badge = (tokens, idx) => {
    const { kind, cases, reason } = tokens[idx].meta
    const list = cases.join(', ')
    if (kind === 'spi') {
      const anchors = cases.map(c => `<a id="spi-${esc(c)}" class="spi-anchor"></a>`).join('')
      return `<p class="spi-badge spi-primary">${anchors}SPI ${esc(list)}</p>\n`
    }
    if (kind === 'spi-ref') return `<p class="spi-badge spi-ref">see SPI ${esc(list)}</p>\n`
    return `<p class="spi-badge spi-omit">SPI ${esc(list)} omitted${reason ? ' — ' + esc(reason) : ''}</p>\n`
  }
}
```

Run: `npm run test:site` → 4 passed.

- [ ] **Step 3: Write the VitePress config and theme**

`site/.vitepress/config.mts`:

```ts
import { defineConfig } from 'vitepress'
import { spiBadgePlugin } from './spi-badge.mjs'

export default defineConfig({
  title: 'CNA Living Rules',
  description: 'A restated, reviewed edition of the Campaign for North Africa Land Game rules',
  base: '/cna/',
  srcDir: '..',
  srcExclude: ['node_modules/**', 'reference/**', 'docs/**', 'tools/**', 'tests/**', 'site/**', '.venv/**', 'EXTRACTION.md'],
  outDir: './.vitepress/dist',
  cacheDir: './.vitepress/cache',
  cleanUrls: true,
  lastUpdated: true,
  rewrites: {
    'README.md': 'index.md',
    'rulings/README.md': 'rulings/index.md',
    'data/README.md': 'data/index.md',
  },
  markdown: {
    config: (md) => { md.use(spiBadgePlugin) },
  },
  themeConfig: {
    nav: [
      { text: 'Rules', link: '/rules/00-overview' },
      { text: 'Rulings', link: '/rulings/' },
      { text: 'Data', link: '/data/' },
    ],
    sidebar: {
      '/rules/': [
        { text: 'Rules', items: [
          { text: 'Overview', link: '/rules/00-overview' },
        ] },
      ],
    },
    search: { provider: 'local' },
    editLink: { pattern: 'https://github.com/basmith7/cna/edit/main/:path', text: 'Propose an edit' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/basmith7/cna' }],
    outline: [2, 3],
    footer: { message: 'Rules CC-BY-SA-4.0 · Data CC0 · Code MIT. Not affiliated with SPI or its successors.' },
  },
})
```

`site/.vitepress/theme/index.ts`:

```ts
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default DefaultTheme
```

`site/.vitepress/theme/custom.css` (phase 1: just make badges legible; phase 2 restyles):

```css
.spi-badge {
  display: inline-block;
  font-size: 0.75rem;
  line-height: 1.2;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg-soft);
  margin: 1.25rem 0 0.25rem;
}
.spi-badge.spi-primary { font-weight: 600; }
.spi-badge.spi-ref::before { content: '↗ '; }
.spi-badge.spi-omit { text-decoration: line-through; }
.spi-anchor { position: relative; top: -5rem; }
```

- [ ] **Step 4: Build with placeholder content and verify**

Create `rules/.gitkeep` and a temporary `rules/00-overview.md` containing only `# Overview\n::: spi-ref 5.1\nplaceholder\n` (Task 11 replaces it). Then:

```bash
npm run site:build
ls site/.vitepress/dist/index.html site/.vitepress/dist/rules/00-overview.html site/.vitepress/dist/rulings/index.html site/.vitepress/dist/data/index.html
grep -c 'spi-badge spi-ref' site/.vitepress/dist/rules/00-overview.html
```

Expected: build succeeds with no dead-link errors, all four HTML files exist, grep prints `1`. If VitePress reports dead links from README.md (e.g. to `docs/designs/...` or `LICENSE`), change those README links to plain code spans, not links.

- [ ] **Step 5: Commit**

```bash
git add package.json package-lock.json site rules/.gitkeep rules/00-overview.md
git commit -m "VitePress phase 1: config, SPI badge plugin, local search, edit links"
```

---

### Task 10: CI and Pages deploy

**Files:**
- Create: `.github/workflows/ci.yml`, `.github/workflows/deploy.yml`

- [ ] **Step 1: Write ci.yml**

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]

jobs:
  gates:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r requirements-dev.txt
      - run: python -m pytest -q
      - name: Cache pinned source text
        uses: actions/cache@v4
        with:
          path: ~/.cache/cna-scans/source
          key: source-${{ hashFiles('tools/sources.json') }}
      - run: python tools/fetch.py sections > /dev/null
      - run: python tools/check_data.py
      - run: python tools/check_overlap.py
      - name: Coverage report
        run: |
          status=0
          python tools/check_coverage.py --sections 1-32 --markdown > coverage.md || status=$?
          cat coverage.md
          exit "$status"
      - if: ${{ always() && github.event_name == 'pull_request' }}
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          header: coverage
          path: coverage.md

  site:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run test:site
      - run: npm run site:build
```

- [ ] **Step 2: Write deploy.yml**

```yaml
name: deploy
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install -r requirements-dev.txt
      - uses: actions/cache@v4
        with:
          path: ~/.cache/cna-scans/source
          key: source-${{ hashFiles('tools/sources.json') }}
      - run: python tools/fetch.py sections > /dev/null
      - run: python tools/check_data.py && python tools/check_overlap.py    # same gates as ci; a direct push to main cannot publish past them
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - uses: actions/configure-pages@v5
      - run: npm ci
      - run: npm run site:build
      - uses: actions/upload-pages-artifact@v3
        with: { path: site/.vitepress/dist }

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 3: Verify locally what can be verified**

```bash
.venv/bin/python -c "import yaml" 2>/dev/null || .venv/bin/pip install pyyaml
.venv/bin/python -c "import yaml,sys; [yaml.safe_load(open(f)) for f in ['.github/workflows/ci.yml','.github/workflows/deploy.yml']]; print('yaml ok')"
# the exact command sequence CI runs:
.venv/bin/python -m pytest -q && .venv/bin/python tools/check_data.py && .venv/bin/python tools/check_overlap.py && .venv/bin/python tools/check_coverage.py --sections 1-32 --markdown > /dev/null && npm run test:site && npm run site:build
```

Expected: `yaml ok`, then every command exits 0. (Do not add pyyaml to requirements; it was only for this check.)

- [ ] **Step 4: Commit**

```bash
git add .github
git commit -m "CI: tests, data and overlap gates, coverage comment; Pages deploy from main"
```

Note for Brian after the push: the GitHub repo needs **Settings → Pages → Source: GitHub Actions** once; and the coverage comment needs PRs from branches in the same repo (fork PRs get a read-only token).

---

### Task 11: `rules/00-overview.md`

**Files:**
- Create: `rules/00-overview.md` (replacing the Task 9 placeholder)
- Delete: `rules/.gitkeep`
- Modify: `EXTRACTION.md` (append entry)

**Interfaces:**
- Consumes: badge syntax (Task 9), overlap gate (Task 6), coverage tool (Task 7), `data/spi-cases.json` (Task 4). Every case named in a `::: spi-ref` line must exist there; the ones used below were verified against the source anchors on 2026-09-18.

The overview holds no primary badges (those live in the system files); it only refers. Write it exactly as below. The Glossary row is plain text here because VitePress fails the build on dead links; Task 12 turns it into a link once the file exists. If the overlap gate reports a run, rephrase the sentence in our own words — do not add to the allowlist.

- [ ] **Step 1: Write rules/00-overview.md**

```markdown
---
title: Overview
status: provisional
---

# Overview

This edition restates the **Land Game** of *The Campaign for North Africa*
(SPI, 1979) as definitions and procedures precise enough to build a
rules-enforcing engine from. It is written in our own words and organised
around the game's *systems* rather than SPI's section numbering. SPI's case
numbers are kept everywhere as citations so that paper players, the errata
and community discussions can be cross-referenced.

## How to read this edition

- The plain text of every section is the **current rule**: the 1979 rule
  with the September 1979 errata applied and our accepted rulings folded in.
- A tag such as **SPI 8.35, 8.36** above a block names the cases of the
  original that the block was derived from. "Show original" (when enabled)
  fetches the community transcription of those cases into your browser for
  comparison; it is never part of this site.
- Boxed annotations record *why* the current rule reads as it does:
  **errata** (what SPI corrected), **ruling** (an ambiguity we resolved,
  linking to the decision record), **note** (intent and advice, not
  binding), **variant** (a community change recorded but not adopted).
- Every rules file is `provisional` until an engine has been built against
  it and its rulings reopened.

New to the game? Build the illustrated primer with
`python3 tools/learn_page.py` and open `docs/learn/index.html`. It is not
published here because it contains crops of the original charts.

## Three games in one box

::: spi-ref 1.0 32.0

CNA is three interlocking games, each playable alone or combined:

| Game | SPI sections | Covers |
|---|---|---|
| **Land Game** | 1–32 | Units, movement, combat, organisation, engineering, weather. **This edition.** |
| Air Game | 33–46 | Aircraft, missions, airfields, anti-aircraft fire. |
| Logistics Game | 47–58 | Fuel, ammunition, water and stores; trucks, ports, convoys, rail. |

Played alone, the Land Game replaces the other two with abstractions from
§32: supply arrives as **Supply Units** that hold fuel and ammunition
points, and air power and naval convoys are simplified. Everything in this
edition assumes those abstractions; the full Air and Logistics Games will be
restated separately. A hex is roughly eight kilometres across.

## Time

::: spi-ref 5.1 7.1

| Unit | Real time | What happens |
|---|---|---|
| **Game-Turn** | about a week | Initiative is rolled and convoy and replacement planning is done, once per turn. |
| **Operations Stage** | 2–3 days; three per turn | Everything else — organisation, movement, combat, repair — once for each player. |

The Operations Stage is the unit of action. Each stage has an **A half**
and a **B half**. The side holding the Initiative for the turn chooses, at
the start of every stage, whether to be **Player A** (first) or **Player B**
(second). Within a half, the side whose turn it is is the **phasing
player**; the other side may still react, retreat and fire.

## The shape of a stage

::: spi-ref 5.2

SPI letters the phases A–L and skips I. Phases A–E occur once per stage;
Player A then does F–L in full, and Player B does F–L in full.

| Phase | Who | What |
|---|---|---|
| A · Initiative declaration | Initiative holder | Chooses to be A or B this stage. |
| B · Weather | Initiative holder | Rolls weather: normal, hot, sandstorm or rainstorm. |
| C · Organisation | Both | Attach and detach units; finish and start construction; finish and start training. |
| D · Arrivals | Both | Reinforcements, replacements and supplies appear at ports and entry hexes. |
| E · Commonwealth fleet | Commonwealth | Assigns and repairs ships. |
| F · Reserve designation | Phasing | Marks units as Reserve so they may move later regardless of distance to the enemy. |
| G · Movement and combat | Phasing (the other reacts) | The core cycle, below. May be repeated. |
| H · Truck convoys | Phasing | Moves unattached second- and third-line trucks, and prisoners. |
| J · Rail | Commonwealth only | Moves units and supplies by rail. |
| K · Repair | Phasing | Tows, then repairs, broken-down vehicles. |
| L · Patrol | Phasing | Reconnaissance, only if no assault was made this half. |

::: spi-ref 8.2 8.23 18.0

Phase G is a **cycle** of four segments — *move → check breakdown → resolve
combat → release reserves* — which the phasing player may run as many
times as they like (**continual movement**). Every repetition includes all
four segments. From the second cycle on, only units that ended the previous
cycle within two hexes of an enemy unit, plus units just released from
Reserve, may move again. This is where tempo comes from: a player keeps
pressing with the units in contact while the rest of the army waits.

Combat within a cycle is a fixed sequence of steps: guns and armour declare
a forward or back **position**; both sides plot, then fire, **barrages**;
the non-phasing side may **retreat before assault**; both sides secretly
assign strength to **anti-armour fire** or **close assault**; anti-armour
fire is resolved simultaneously; close assaults are resolved one at a time
in the order the phasing player chooses, who then reveals which of them
were only **probes**.

## The currency: Capability Points

::: spi-ref 6.11 6.14 6.21 6.22 6.26

Every unit has a **Capability Point Allowance (CPA)**: the number of
**Capability Points (CP)** it may spend in one Operations Stage. Moving a
hex, firing, being fired on, assaulting, defending, retreating, building,
training — everything costs CP. The allowance covers *both halves* of the
stage: what a unit spends reacting during the enemy's half is gone for its
own.

A unit may exceed its CPA, but each point over becomes a **Disorganisation
Point**, and Disorganisation Points lower the unit's **Cohesion Level**.
Cohesion feeds the morale checks in combat, and a badly disorganised unit
eventually cannot act at all. Cohesion recovers slowly, chiefly by doing
nothing for a stage. The whole game is a negotiation with this ledger:
push tired units now for tempo, or rest them and hand the enemy time.

## Units and strength

::: spi-ref 3.21 3.22 6.15

A **unit** is a counter standing for a battalion, regiment, brigade,
headquarters, artillery group, truck column or similar. Its strength is
counted in **TOE Strength Points** — think companies or gun batteries —
which are what combat removes and replacements restore. Each unit also
carries **ratings**: close-assault offence and defence, barrage, anti-armour,
armour protection, breakdown adjustment, and its CPA. Units belong to
**parent formations** (divisions, brigades) by **attachment**, which
governs whom they may stack and fight alongside and which headquarters
they draw on.

Units are grouped in two ways. **Type** — infantry, tank, reconnaissance,
anti-tank, anti-aircraft, artillery, engineer, and several support and
transport types — governs what a unit may do. **Class** — infantry, armour,
gun, truck — governs what happens to it when it is the target of a barrage
or an air attack.

## Movement

::: spi-ref 8.37 10.0 21.0

Units move hex by hex, paying the **Terrain Effects Chart** cost in CP for
each hex entered and each hexside crossed. Roads and tracks are cheap; open
desert and rough ground are dear; escarpments cost a great deal to climb and
are impassable to vehicles except at passes. Motorised units have large
allowances but risk **breakdown**: vehicles accumulate Breakdown Points by
the terrain they cross and roll against their rating after every movement
segment; a broken-down vehicle must be towed and repaired. Entering an enemy
**Zone of Control** stops movement and, as a rule, forces combat. The
non-phasing player may **react** with some units during the phasing
player's movement, paying CP from the same allowance.

## Combat

::: spi-ref 11.3 11.33 15.5 15.73

Combat strength is computed, not read off the counter. **Raw points** are
rating × TOE Strength Points committed; **Actual points** are raw ÷ 10,
rounded to the nearest whole number with halves rounding up (11.4 → 11,
11.5 → 12), and anything under five raw counts as nothing. All contributions against one target are summed before dividing,
so a lone small unit contributes almost nothing and concentration is
enforced by arithmetic.

Every combat roll uses two dice of different sizes, read more than one way
from the same throw: as a two-digit number (11–66) for losses on the
tables, and as a sum for secondary results such as capture. Barrage,
anti-armour fire and close assault each have their own table. Close assault
is resolved on a **differential** (attacker Actual minus defender Actual),
shifted by columns for terrain, relative size, morale and raw superiority;
results are percentage losses of the TOE points committed, plus possible
engagement and prisoners.

## Resource loops

The systems connect through a few loops an engine has to model explicitly:

- **CP ↔ Cohesion.** Spending over the allowance lowers cohesion; low
  cohesion worsens combat; only rest restores it.
- **TOE ↔ Replacements and repair.** Combat and breakdown remove strength;
  replacement points, training and repair put it back, each costing time in
  the Organisation and Repair Phases.
- **Supply ↔ Operations.** Even abstracted, movement and fire draw fuel and
  ammunition from a Supply Unit within reach; a unit that cannot reach one
  stops.
- **Contact ↔ Tempo.** Continual movement lets units in contact act
  repeatedly, at a price in CP and cohesion; Reserve trades a segment of
  inactivity for freedom to move later.

## Roles

::: spi-ref 2.0

SPI describes the game for teams: a commander-in-chief, a front-line
commander, a rear-area commander, an air commander and a logistics
commander per side, each with their own log sheets. Roles divide the
paperwork; they never change what a side may do. This edition treats each
side as one decision-maker, and an engine may assign roles to people
however it likes.

## Where to go next

The rules are organised by system, not by SPI section:

| File | System | Draws on SPI |
|---|---|---|
| Glossary | Defined terms | §2, §3 |
| Units and state | Unit characteristics, TOE, cohesion, morale | §3, §6.2, §17 |
| Sequence of play | The turn and the stage in full | §5, §7 |
| Capability points | CPA, costs, disorganisation | §6 |
| Movement | Continual movement, terrain, breakdown, rail, reaction | §8, §21 |
| Stacking and zones of control | | §9, §10 |
| Combat | Barrage, retreat before assault, anti-armour, close assault, probes, patrols | §11–16 |
| Organisation | Attachment, reinforcements, replacements, reserve, training | §18–20 |
| Engineering | Engineers, construction, fortifications, minefields, repair | §22–26 |
| Special | Raiders, prisoners, weather, fleet, Rommel | §27–31 |
| Abstract logistics and air | | §32 |

Files not yet written are listed so the shape of the edition is visible;
they are added one system at a time.

---

*Provenance: drawn on SPI §1, §2, §3.2, §5, §6.1–6.2, §7.1, §8.2, §8.37,
§10, §11.3, §15.5, §15.7, §18, §21, §32.1. This page only refers; every
primary citation lives in the system file that restates the case.*
```

- [ ] **Step 2: Run the gates and the coverage tool**

```bash
rm -f rules/.gitkeep
.venv/bin/python - <<'PYEOF'
import json
known = {c['id'] for c in json.load(open('data/spi-cases.json'))['cases']}
refs = {c for line in open('rules/00-overview.md') if line.startswith('::: spi-ref') for c in line.split()[2:]}
print('missing:', sorted(refs - known))
PYEOF
.venv/bin/python tools/check_overlap.py
.venv/bin/python tools/check_coverage.py --sections 1-32
npm run site:build
```

Expected: `missing: []`; `check_overlap: OK (0 shared 8-word runs)`; `coverage: 0 / 974 …` with **no** `ERROR` lines; site builds. If a case is reported missing, replace it with its section id (e.g. `6.0`); if the overlap gate prints a run, rewrite that sentence and re-run.

- [ ] **Step 3: Append the EXTRACTION.md entry**

```markdown
## rules/00-overview.md — 2026-09-18
- Source cases read: 1.0, 2.0, 3.21–3.22, 5.1–5.2, 6.11–6.17, 6.21–6.26, 7.11–7.16, 8.2, 8.23, 8.37, 10.0, 11.31–11.35, 15.5, 15.73, 18.0, 21.0, 32.11–32.16
- Mechanics identified: three nested games with §32 abstraction; turn = 3 stages, stage = A/B halves; phase order A–L (no I) with F–L per player; G as a repeatable 4-segment cycle with the 2-hex / reserve re-move restriction; combat step order; CPA covering both halves, overspend → DP → cohesion; TOE points and ratings; type vs class; terrain costs, breakdown, ZOC, reaction; raw÷10 rounding and the <5 raw rule; two-dice two-readings; differential CRT with column shifts.
- How we expressed it: a system-model summary (time → stage shape → currency → units → movement → combat → loops → roles), tables for the phase list and file map, no procedures — every mechanic here is restated in full in its system file; SPI's team roles reduced to advisory; all citations as `spi-ref`.
- Errata applied: none (no values stated).
- Rulings raised: none.
```

- [ ] **Step 4: Commit**

```bash
git add rules/00-overview.md EXTRACTION.md
git rm -q --cached rules/.gitkeep 2>/dev/null; true
git commit -m "Rules: authored Overview (systems model, stage shape, currency, loops)"
```

---

### Task 12: `rules/glossary.md`

**Files:**
- Create: `rules/glossary.md`
- Modify: `EXTRACTION.md` (append entry)

**Interfaces:**
- Consumes: same gates as Task 11. The "See" column uses case IDs as plain text now; phase 2 turns them into links to `#spi-<case>` anchors.

- [ ] **Step 1: Write rules/glossary.md**

```markdown
---
title: Glossary
status: provisional
---

# Glossary

Defined terms used throughout this edition. Each definition is the short
form; the system file named in **Where** holds the full rule. "See" gives
the SPI case that introduces the idea, for cross-reference only.

::: spi-ref 2.0 3.21 3.22

| Term | Meaning | Where | See |
|---|---|---|---|
| **Actual points** | Combat strength after conversion: raw points ÷ 10, rounded to nearest with halves up; below five raw = zero. All comparison and table lookups use Actual points. | Combat | 11.3 |
| **Anti-armour fire** | The combat step in which assigned TOE points shoot at armour-class targets, resolved simultaneously by both sides before close assault. | Combat | 14.0 |
| **Attachment** | The link between a unit and a parent formation. Governs who it may stack and assault with and which HQ it draws on; changed in the Organisation Phase. | Organisation | 18.0 |
| **Barrage** | Indirect fire by gun-class units (and some others) at a hex, plotted secretly, resolved before assault. Targets are chosen by class, not by unit. | Combat | 12.0 |
| **Breakdown** | Loss of vehicles to mechanical failure, checked after every movement segment against Breakdown Points accumulated by terrain crossed. | Movement | 21.0 |
| **Capability Point (CP)** | The unit of activity. Every action a unit takes, or has done to it, costs CP. | Capability points | 6.11 |
| **Capability Point Allowance (CPA)** | The CP a unit may spend in one Operations Stage without penalty, covering both halves of the stage. | Capability points | 6.11 |
| **Class** | One of infantry, armour, gun, truck. Determines how a unit is treated as a target of barrage or air attack. | Units and state | 3.22 |
| **Close assault** | Direct ground combat between adjacent hexes, resolved on the differential table with column shifts. | Combat | 15.0 |
| **Cohesion Level** | A unit's organisational state, from positive (fresh) down through zero to deeply negative. Lowered by Disorganisation Points, raised by Recovery Points; modifies morale. | Capability points | 6.2 |
| **Continual movement** | The phasing player's right to repeat the move → breakdown → combat → release cycle; after the first cycle only units within two hexes of the enemy, or just released from Reserve, may move again. | Movement | 8.2 |
| **Differential** | Attacker Actual points minus defender Actual points; the base column on the close-assault table before shifts. | Combat | 15.5 |
| **Disorganisation Point (DP)** | One point of cohesion lost. Earned one-for-one for CP spent beyond the CPA, and by some combat results. | Capability points | 6.21 |
| **Escarpment** | A hexside feature that costs extra CP to climb and blocks vehicles except at a pass. | Movement | 8.37 |
| **Game-Turn** | About one week. Three Operations Stages plus the once-per-turn initiative and planning steps. | Sequence of play | 5.1 |
| **Half (A half, B half)** | The portion of an Operations Stage in which one player is phasing. Player A's half runs first. | Sequence of play | 5.2 |
| **Headquarters (HQ)** | A unit representing a parent formation's command. Attached units draw on it; some HQs have combat values, some none. | Units and state | 3.3 |
| **Hex** | One cell of the map, about eight kilometres across, identified by map sheet and a four-digit row-column number, e.g. `C4023`. | Movement | 4.1 |
| **Initiative** | The right, won each Game-Turn by rating plus die, to choose whether to be Player A or B in each stage. | Sequence of play | 7.1 |
| **Morale** | A unit's combat attitude, checked by a roll modified by cohesion and other factors; results shift close-assault columns. | Units and state | 17.0 |
| **Operations Stage** | 2–3 days; the unit of action. Contains the phases A–L. | Sequence of play | 5.1 |
| **Parent formation** | A division, brigade or similar whose attached units share a CPA source and an HQ. | Organisation | 6.15 |
| **Patrol** | Reconnaissance by the phasing player in the last phase of the half, allowed only if no assault was made. | Combat | 16.0 |
| **Phasing player** | The player whose half of the stage it is. The other player is the non-phasing player. | Sequence of play | 5.2 |
| **Pinned** | A barrage result: for the rest of the Combat Segment the unit may not move (so may not retreat before assault), fire anti-armour, or close assault. | Combat | 12.6 |
| **Player A / Player B** | The first and second player in an Operations Stage, as chosen by the Initiative holder. | Sequence of play | 5.2 |
| **Position** | A gun-class or armour-class unit's declared stance for the segment, forward or back, which trades fire flexibility for vulnerability. | Combat | 11.0 |
| **Probe** | A close assault the attacker designates in advance as limited, revealed after resolution, with reduced consequences. | Combat | 15.0 |
| **Raw points** | Combat rating × TOE Strength Points committed, before conversion to Actual points. | Combat | 11.3 |
| **Reaction** | Movement by the non-phasing player during the phasing player's Movement Segment, limited and paid from the reacting unit's own CPA. | Movement | 8.0 |
| **Recovery Point (RP)** | One point of cohesion regained; earned mainly by a stage of inactivity. | Capability points | 6.23 |
| **Reinforcement** | A new unit entering play on schedule at a port or entry hex. | Organisation | 19.0 |
| **Replacement Point** | A point of TOE strength that can be added to an existing unit after training. | Organisation | 20.0 |
| **Reserve** | A status chosen in the Reserve Designation Phase. A Reserve unit does not move in the first cycle but, once released, may move in later cycles regardless of distance to the enemy. | Organisation | 18.0 |
| **Retreat before assault** | The non-phasing player's option to withdraw a threatened unit, at CP cost, after barrages and before force assignment. | Combat | 13.0 |
| **Stacking Points** | The measure of how much may occupy one hex; each unit has a stacking value and each hex a limit. | Stacking and ZOC | 9.0 |
| **Supply Unit** | In the Land Game, an abstract dump holding fuel and ammunition points. A unit may draw on one that lies within half its CPA. | Abstract logistics and air | 32.1 |
| **TOE Strength Point** | The unit of a unit's strength — roughly a company or a battery. Destroyed by combat; put out of action (not destroyed) by breakdown; restored by replacements and repair. | Units and state | 3.4 |
| **Training** | The process, in the Organisation Phase, by which replacements and units improve morale before use. | Organisation | 20.0 |
| **Type** | A unit's functional category — infantry, tank, reconnaissance, anti-tank, anti-aircraft, artillery, engineer, and support and transport types — governing what it may do. | Units and state | 3.21 |
| **Weather** | Normal, hot, sandstorm or rainstorm, rolled once per stage; modifies movement, breakdown, construction and supply. | Special | 29.0 |
| **Zone of Control (ZOC)** | The hexes adjacent to a unit that stop enemy movement on entry and generally force combat. | Stacking and ZOC | 10.0 |

---

*Provenance: drawn on SPI §2 (term list) and the cases in the See column.
Definitions are ours; where they turn out to disagree with a system file,
the system file wins and this table is corrected.*
```

- [ ] **Step 2: Link the Glossary from the Overview, then verify every "See" case exists and the gates pass**

In `rules/00-overview.md`, change the table row `| Glossary | Defined terms | §2, §3 |` to `| [Glossary](./glossary.md) | Defined terms | §2, §3 |`. In `site/.vitepress/config.mts`, add `{ text: 'Glossary', link: '/rules/glossary' },` directly after the Overview sidebar item.

```bash
.venv/bin/python - <<'PYEOF'
import json,re
known={c['id'] for c in json.load(open('data/spi-cases.json'))['cases']}
seen=re.findall(r'\| (\d{1,2}\.\d{1,2}) \|\n', open('rules/glossary.md').read())
print('missing:', sorted(set(seen)-known))
PYEOF
.venv/bin/python tools/check_overlap.py
.venv/bin/python tools/check_coverage.py --sections 1-32
npm run site:build
```

Expected: `missing: []` (if a case is missing, replace it with the nearest section-level id such as `14.0`); overlap OK; coverage prints no `ERROR`; site builds and `site/.vitepress/dist/rules/glossary.html` exists.

- [ ] **Step 3: Append the EXTRACTION.md entry**

```markdown
## rules/glossary.md — 2026-09-18
- Source cases read: 2.0 (term list), 3.21, 3.22, 3.3, 5.1, 5.2, 6.11–6.26, 7.1, 8.0, 8.2, 8.37, 9.0, 10.0, 11.0, 11.3, 12.0, 12.6, 13.0, 14.0, 15.0, 15.5, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 29.0, 32.1
- Mechanics identified: the vocabulary an engine needs as state and enums — CP/CPA, cohesion (DP/RP), TOE points, raw/actual conversion, unit type vs class, reserve/reaction/continual movement, the combat step names, initiative, weather, ZOC, stacking, supply unit.
- How we expressed it: one table, our short definitions, each pointing to the system file that owns the full rule; SPI's glossary prose was not reused, and SPI's role definitions were reduced to the Overview's one paragraph.
- Errata applied: none.
- Rulings raised: none.
```

- [ ] **Step 4: Commit**

```bash
git add rules/glossary.md rules/00-overview.md site/.vitepress/config.mts EXTRACTION.md
git commit -m "Rules: authored Glossary"
```

---

### Task 13: Final verification and hand-off

- [ ] **Step 1: Run everything CI runs, from a clean checkout state**

```bash
cd /home/basmith7/Projects/cna
git status --short            # must be empty
.venv/bin/python -m pytest -q
.venv/bin/python tools/check_data.py
.venv/bin/python tools/check_overlap.py
.venv/bin/python tools/check_coverage.py --sections 1-32 --markdown
npm run test:site && npm run site:build
git ls-files | grep -E 'cache|\.jpg$|node_modules|\.venv' ; echo "(must print nothing)"
```

- [ ] **Step 2: Report to Brian**

State the pass/fail of each command above verbatim, the case count in `data/spi-cases.json`, and the two manual follow-ups: create the GitHub repo `basmith7/cna` and push `main`; enable Pages (Source: GitHub Actions). Spec step 5 (outreach) is Brian's; the drafts are in `docs/outreach/`.

---

## Self-review against the spec

- **Scaffold (Process 1):** licences/README/EXTRACTION → T1; `sources.json` with pinned item + hashes and tonicebrian commit → T2; `data/README.md` + schemas → T3; `spi-cases.json` from anchors, IDs and labels only → T4; VitePress phase 1 → T9; CI with two gates + coverage comment → T10 (gates T5, T6; report T7). Rulings process file → T8 (spec: "fork policy is written in `rulings/README.md`").
- **Overview + glossary (Process 2):** T11, T12, with `EXTRACTION.md` entries and the primer link.
- **Deliberately deferred to step 3+ (per spec):** `data/tables/*`, `data/errata/*`, `sequence-of-play.json`, NJHarman seed import, "Changes from the original" page, client-side original viewer, container styling (phase 2).
- **Deviation noted:** the badge markdown plugin and a minimal badge style are built in site phase 1 (spec puts badges in phase 2) because without a block rule the single-line `::: spi` syntax renders as literal text in the Overview; the phase-2 work (styling, changes page, coverage page, original viewer) is untouched.
- **Deviation noted:** `sources.json` records archive.org's published SHA-1 for three files plus a locally computed SHA-256 for the jp2 zip only (T2 step 6), since that is the one file we read.
