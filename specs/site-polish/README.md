# Site polish: make CNA Living Rules feel finished

## Next Agent Prompt

Status (2026-10-12): slices 01–05 built on branch `pm/polish` (PR labelled `pm`). What
remains is follow-up work filed as GitHub issues (label `pm`); pick from those rather than
reopening this spec. If you change a table page, edit `tools/tables_page.py` and run
`tools/gen_pages.py`; never edit `site/tables/*.md` by hand. Update this section before you
end a pass.

- [x] 01 Home page and nav: `slices/01-home.md`
- [x] 02 Table pages: `slices/02-tables.md`
- [x] 03 Prose links to tables: `slices/03-table-links.md`
- [x] 04 Map viewer: `slices/04-map-viewer.md` (built by a delegated pass; sizes and touch fixed after review)
- [x] 05 Small polish: `slices/05-polish.md`

Evidence: before/after shots in `~/Projects/cna-pm-shots/{before,after}/` (not committed).

## Goal

A newcomer who opens http://basmith.net/cna/ understands within one screen what this
is (a free, plain-language restatement of SPI's *The Campaign for North Africa*),
where to start (Learn, then the Overview), and how to find a rule (search, the rules
sidebar, the tables). Nothing visible should read as a developer artefact or as
unfinished.

## What browsing the site found (2026-10-12, `~/Projects/cna-pm-shots/before/`)

1. The home page is the developer README: directory layout, licences, build commands.
2. None of the 72 tables in `data/tables/` is shown anywhere. Prose says
   "`data/tables/barrage-results.json`"; the Data nav opens developer conventions.
3. The map sheets are squeezed into the text column; hex numbers and place names are
   unreadable, with no zoom.
4. The rulings register wraps ids as "R-/001"; `spi-omit` badges are struck through
   and read as an error.

## Non-goals and firewalls

- No change to data values, JSON schemas, rulings' decisions or rule wording.
  Rules files are not edited at all (links come from a render-time plugin).
- No SPI text, map art or counter art. Table pages show only what the JSON holds.
- No new npm or pip dependencies.
- `README.md` stays the repository readme for GitHub; the site gets its own home.
- No backward compatibility shims: old URLs `/data/` stay (data conventions page);
  nothing else moves.

## Single owners (invariants)

- **Table presentation** has one owner: `tools/tables_page.py` (pure functions; errata
  application lives here and nowhere else in Python). It is run by `tools/gen_pages.py`,
  so the existing "gen_pages leaves no diff" gate and `tests/test_gen_pages.py` cover it.
- **Table sidebar and index** come from the same generator (it writes a JSON sidebar
  file the config imports), never a hand-kept list.
- **Map page markup** stays owned by `tools/map_render.py::render_page`; the viewer
  behaviour lives in one Vue component with its maths in a pure module.
- **Table links in prose**: one markdown-it rule in `site/.vitepress/table-links.mjs`.

## Gates (every slice)

`.venv/bin/python -m pytest -q`, `tools/check_data.py`, `tools/check_overlap.py` and
`tools/check_overlap.py site/tables` (after slice 02), `tools/gen_pages.py` (no diff),
`tools/map_render.py --check`, `npm run test:site`, `npm run site:build`.
Visual gate: screenshot-critique on every changed page shot (unprimed), and
compare-screenshots against the matching `before/` shot.

## Decisions taken without Brian (reversible)

Recorded in the PR's choices list; the main ones: Python-generated committed table
pages rather than VitePress dynamic routes (matches `gen_pages`/`map_render`/`learn_page`,
searchable, diff-gated); errata applied on display with a mark; nav "Data" becomes
"Tables"; prose links via render plugin, not by editing rules files.

Drafts: three blind drafts (fewest-slices, risk-first on a second model, seam-quality) agreed on the five slices; the risk-first draft preferred JS dynamic routes (CI's site job runs Node only). Committed Python output still works there since the pages are in git.

Alternative considered: VitePress dynamic routes (`[table].paths.mjs`) — no committed
generated files, but a second generator language and no diff gate. Rejected for one owner.
