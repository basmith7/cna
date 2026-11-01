# AGENTS.md: invariants and gotchas

What the code and the other docs don't tell you. Unattended-run orders and the PR gates are
in `AUTOPILOT.md`; setup and legal posture in `README.md`; `data/` conventions (id grammar,
hex grid, enums, errata and map-correction overlays, transcription) in `data/README.md`;
ruling format, numbering and lifecycle in `rulings/README.md`.

## The engine contract

- cna-engine pins this repo as the `vendor/cna` submodule, and its `cna-data` crate reads
  `data/` with serde. Renaming or removing a field or an enum value breaks it, and so does
  adding an enum value: its enums have no catch-all. Adding a field is safe except inside a
  scenario's placements, unit entries and `motorisation` block, which it parses with
  `deny_unknown_fields`. The break shows at the engine's next `vendor/cna` bump, so name
  any such change in the PR body.
- A ruling's option numbers are the engine's switch values: `crates/cna-rules/src/ruleset.rs`
  numbers each variant as the ruling numbers its options, and defaults to the accepted
  Decision. Renumber nothing in a ruling the engine models; a changed Decision needs the
  matching default changed in the engine.

## Coverage badges

`check_coverage.py` counts a case as covered by its one primary `::: spi` badge, or by
`::: spi-omit <case> — <reason>`. `::: spi-ref` is a cross-reference and counts for
nothing. A second primary badge for the same case is an error.

## Map changes

- A hex or hexside fix is a `data/map/corrections/M-nnn.json` (format in `data/README.md`),
  then run, in order: `tools/map_build.py`, `tools/map_seams.py`, `tools/map_render.py`
  (add `--golden` for a Malta change) and `tools/learn_page.py --site`, whose Part D
  draws Map C. Commit everything they rewrite. CI's gates fail on stale
  `hexes.json`/`hexsides.json` and SVGs; pytest fails on stale `seams.json`,
  `tests/golden/M.svg` and `site/learn.md`.
- `site/map.md`, `site/public/map/*.svg` and `site/learn.md` are generated but carry no
  "do not edit" header.
- `map_geom.is_adjacent` is same-sheet only; `map_geom.distance` counts across sheet seams.
  For adjacency across a seam, read `data/map/seams.json`.

## Site

The site's `srcDir` is the repo root: a new top-level markdown file is published as a page
unless `site/.vitepress/config.mts` lists it in `srcExclude`.

## `main`

Every push to `main` deploys the site, and the cron script commits quota rows to
`docs/autopilot/PROGRESS.md` on `main` between runs: branch from a freshly fetched
`origin/main`.
