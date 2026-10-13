# 02 Table pages

Contract: every `data/tables/<name>.json` has a readable page at `/tables/<name>`,
plus `/tables/` index grouped by the rules page that cites it.

Seam `tools/tables_page.py`:
- `apply_errata(table, patches) -> (table, marks)` RFC-6902 add/remove/replace on a copy;
  `marks` are the patched pointer paths with errata id.
- `render_table(name, table, errata, cited_by) -> str` markdown. Shape rules:
  list of objects → grid (columns = union of keys in first-seen order, `sources`
  column dropped and shown as a small per-page sources line); object whose values
  are all objects → matrix (rows = outer keys, columns = inner keys); scalar →
  "Label: value" line; list of scalars → inline list. Cell formatting: null → "—",
  `{from,to}` → "a–b", consecutive int list → "a–b", nested object → "k: v; …".
  Keys humanised (`cw_percent` → "CW percent"; known abbreviations kept upper).
  Patched cells carry a superscript errata link. Notes render as a list.
- `render_index(tables, cited_by) -> str`, `sidebar(…) -> list` (written to
  `site/.vitepress/tables-sidebar.json`).
- `cited_by` comes from scanning `rules/**/*.md` for `data/tables/<name>.json`.
- Called from `gen_pages.py`; output `site/tables/*.md`, rewrite `site/tables/:t` → `tables/:t`.
- Tests (pytest): fixture table covering each shape and every errata op; every leaf
  value of each real table (after errata) appears in its page; index lists all 72.
- Visual: close-assault-results, terrain-effects, unit-characteristics, index; desktop
  and mobile; wide tables scroll horizontally inside their own box.
- Delegated: exact humanising dictionary, page intro wording.

Added from the risk-first draft:
- Pivot CRTs: when a table has a `columns` list of `{id,…}` and its rows carry a
  `column` key (barrage, breakdown), show rows × column ids with the remaining value
  field in the cell, instead of one line per cell. Other row fields form the row label.
- `footnotes` dict → numbered list; `known_gaps` → a "Known gaps" callout.
- Measure the local search index (`dist/assets/chunks/@localSearchIndex*`) before and
  after; if it grows past ~1 MB, set `search: false` on the largest tables.
