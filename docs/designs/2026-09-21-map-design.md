# CNA Map — Design

**Date:** 2026-09-21 (after adversarial review, two rounds)
**Status:** approved design, awaiting implementation plan
**Sub-project:** 2 of N. Sub-project 1 (Living Rules, Land Game) is complete;
see `2026-09-18-cna-living-rules-design.md` for the legal posture and data
conventions this design inherits, and `2026-09-18-map-extraction-spike.md`
for the extraction findings it builds on.

## Goal

Committed, CC0, provenance-carrying hex and hexside terrain data for every
SPI map sheet of *The Campaign for North Africa* (A–E plus Malta), and a
generated schematic map per sheet in our own style, so that:

1. an engine has the map graph (hex terrain, hexside features, named
   places) in the same `data/` conventions as the tables;
2. the primer's Part D (Graziani's Offensive on Map C) can be published
   with no SPI imagery;
3. a future UI has a map that is ours, with every hex addressable by ID.

## Scope

**In:** hex terrain for all six zones; hexside features with up/down for
slopes and escarpments; coast and lake hexsides; named places from the
printed *Summary of Important Locations* plus ports and oases; per-sheet
grid convention; SVG render per sheet; a `/map` site page; Part D published.

**Out (later specs):** port capacities (SPI 55.3, Logistics); airfields and
flying-boat bases (Air); off-map boxes and distances beyond what
`data/tables/off-map-distances.json` already holds; cross-sheet adjacency
(hex IDs are unique across sheets, so a join table can be added without
changing anything here); reading the ~100 unlisted map labels; Malta's
rules; any engine code.

## Sources and legal posture

- **Primary:** Mitch Guthrie's 2021 VASSAL redraw (`CNAv2.1.0.vmod`,
  `tools/sources.json` → `vassal`). Cached at `~/.cache/cna-vassal/`
  (the `.vmod`, the extracted PNG, and — new — `buildFile.xml`). Never
  committed.
- **Second read:** the archive.org scan of the SPI map sheets (jp2 pages
  via `tools/fetch.py pages N`), for resolving every disagreement.
- **Diff only:** Norman Harman's private hex database
  (`tools/sources.json` → `njharman_src`, PR #16, which must merge before
  Part A). It is used to *find* candidate misreads; every difference is
  resolved by looking at the scan or the redraw and recording what was
  seen. His values are never copied, never committed, and never named in a
  committed file — a correction cites the scan crop as its only evidence.
- **Posture:** the same as the tables. Terrain per hex, hexside features and
  place names are game parameters and geographic facts; the compilation
  and the rendering are ours; `data/` is CC0. Committed data carries only
  those facts — no pixel coordinates, no colour-coverage ratios, nothing
  that is a measurement of Guthrie's artwork rather than of the game. No
  legal review has been obtained; `README.md` says so.

## Data (`data/map/`)

All files are JSON, validated by `data/schema/map-*.schema.json` through
`tools/check_data.py`. Provenance is in a file-level `sources` header
(`vassal:CNAv2.1.0`, `scan:p<n>`), not repeated per record; the
`vassal:<module>` form is added to the identifier grammar in
`data/README.md`.

| File | Content |
|---|---|
| `sheets.json` | Per sheet (`A`–`E`, `M` for Malta): printed row/column bounds and the odd-row offset direction (`odd_rows_shift: "west"`/`"east"`). The extractor derives this from VASSAL's `vDescend`/`hOff`/`stagger` per zone; the README's single global rule is replaced by "see `sheets.json`". |
| `raw/<sheet>.json` | The extractor's read, regenerated only by `map_extract.py`. Same fields as the final files, no more. Committed so CI can verify the final files without the PNG. |
| `corrections/M-nnn.json` | One hand correction each: `target` (`hex`/`hexside`/`place`), `key`, RFC 6902 patches as in `errata/E-nnn.json`, `seen` (what the scan showed: `scan:p<n>`, crop coordinates, a sentence), `superseded: true` when a later extractor run makes it moot. `map_build.py` errors if a live correction's `old` no longer matches raw. |
| `hexes.json` | One record per hex: `id` (`C4023`; Malta `M` + `RRCC` after clipping the zone's partial hexes to the printed range), `sheet`, `terrain` (the existing `terrain` enum from `common.schema.json`: clear, gravel, salt-marsh, heavy-vegetation, rough, mountain, delta, desert, major-city, swamp, sea; `village-bir-oasis` is **not** used here), `settlement` (`null` / `major-city` / `village` / `bir` / `oasis`), `coastal` (bool). |
| `hexsides.json` | One record per hexside that carries a feature: `a`, `b` (sorted; `b: null` plus `side` for a sheet-edge hexside), `features` (list of: escarpment, ridge, slope, wadi, major-river, minor-river, road, unfinished-road, railroad, unfinished-railroad, track, coast, lake), `up` (hex ID of the higher side for escarpment/slope; `null` allowed in raw, not in a merged sheet — see gates). |
| `places.json` | `id` (slug), `hex`, `name`, `kind` (major-city, village, bir, oasis, feature), `port` (bool). Source: the printed *Summary of Important Locations* (54 entries) plus every port and oasis on the map. |

Rules the schema encodes (checked by `check_data.py`):

- every `hexsides.a`/`b` and `places.hex` exists in `hexes.json`;
- every `(a, b)` pair is adjacent under the sheet's convention in `sheets.json`
  (edge records with `b: null` are skipped);
- a hex with a non-null `settlement` has at most one place; every place's hex
  has a matching `settlement`;
- `up` ∈ {`a`, `b`} when present; `coast` implies both hexes are land and
  `coastal`;
- `pass` is not stored: it is where a track crosses an escarpment hexside
  (`rules/40-movement.md`, *Escarpments*), derivable.

Lake hexes (the palette cannot tell lake from sea) are set by correction.
Oases are not detected by the extractor; they come from the printed page and
corrections.

## Tools (`tools/`)

| Tool | Does | Needs the cache? |
|---|---|---|
| `map_extract.py` (exists) | `.vmod` → `build/map/raw-<sheet>.json` + review crops. First-run fixes, landed **before any correction exists**: cache `buildFile.xml` and read it from the cache; heavy-vegetation second green; clip zone-edge partial hexes; a `coast` hexside detector (midpoint sample majority sea, both hexes land); `up` from the band side, `null` when undeterminable; emit only game-fact fields. Frozen after Part A; any later change is its own PR that regenerates every `raw/` file and re-resolves conflicts. | yes |
| `map_build.py` (new) | `raw/` + `corrections/` → `hexes.json`, `hexsides.json`, `places.json`. `--check` fails if the committed files differ from the rebuild (runs in CI: needs no PNG). | no |
| `map_diff.py` (new) | our final data vs the NJHarman DB → `build/map/diff-<sheet>.md` (hex, ours, his, a crop path). Skips with a note when the cache lacks his files. Only counts leave `build/`. | yes |
| `map_sample.py` (new) | seeded random sample of N hexes per sheet → crops from the scan and the redraw + a checklist; the filled checklist's misread count goes to `EXTRACTION.md`. | yes |
| `map_render.py` (new) | `data/map/` → `site/public/map/<sheet>.svg` (committed; `--check` in CI), and `--region <hex list>` for inlined crops. Deterministic output (fixed float format, sorted keys) so byte comparison is stable. | no |

`build/` is added to `.gitignore` in Part A's first commit, with a hygiene
test that nothing under `build/`, and no raster under `data/` or
`site/public/map/`, is tracked. `requirements-dev.txt` gains `numpy`.

## Rendering

One SVG per sheet, ours in every respect: own palette (declared once in the
tool, with a legend element), pointy-top hex polygons with the printed hex
number, terrain as flat fill by class, hexside features as strokes
(escarpment/slope with a tick on the down side; rivers, wadis, roads,
tracks, rail by stroke style), settlements as symbols, place labels from
`places.json`. Each hex is `<polygon id="C4023" class="terrain-clear">`; each
hexside `<path class="slope" data-a data-b data-up>`. No SPI or Guthrie
artwork or text is rendered or embedded.

Tests: every hex ID appears exactly once as a polygon and nothing else has
an ID; every hexside path references an adjacent pair; neighbouring polygons
share an edge within 0.01 px (this also tests `sheets.json`); the file is
well-formed XML; a golden snapshot for Malta; `--check` messages name the
regenerate command.

## Verification and merge gates

Every sheet PR passes `pytest`, `check_data.py`, `map_build.py --check`,
`map_render.py --check`, `check_overlap.py` and the site build, and its
`EXTRACTION.md` entry records:

- NJHarman diff count for the sheet and the resolution of each: a correction
  citing the scan, or `agrees with the redraw; his DB differs` naming the crop
  file and the observed class. **Cap 150 resolutions per PR**; overflow is a
  documented stop with the remaining count in `PROGRESS.md`, not a merge.
- Zero `up: null` on escarpment and slope hexsides, or an explicit allowlist
  with a reason each.
- The 50-hex sample checklist result (misreads / 50). This measures
  extractor-vs-redraw agreement plus a coarse scan sanity check, not an error
  rate against SPI's map.
- The SVG viewed next to the scan for the sheet.

Part A additionally establishes the slope/escarpment side convention: check
hexsides whose direction the rules or scenario text fix (Halfaya Pass C3922,
the Sollum escarpment C4021) and record the convention in `data/README.md`.

## Site and primer

- `/map`: one section per sheet with `<img src="/map/<sheet>.svg">`, the
  legend, a *how this was made* paragraph and the legal note; `Map` in the
  top nav.
- Part D of the primer: `map_render.py --region` renders the Graziani area of
  Map C with the deployment overlay computed from hex IDs; `learn_page.py
  --site` inlines it and Part D is published. The existing "no `<img>`, no
  `graziani`" site test is updated to allow the rendered region.

## Order of work (autopilot mission 3)

0. **Precondition (Brian):** merge PR #16 (`njharman_src` entry) and PR #58.
1. **Part A — plumbing on Malta.** `.gitignore` + hygiene test; extractor
   fixes and freeze; `sheets.json`; schemas and enums; `map_build.py`;
   `map_render.py` with the Malta golden; `/map` page with Malta;
   side-convention check on Map C hexsides; `data/README.md` updates. Malta
   retires plumbing risk only — no escarpment, slope, river, road or rail.
2. **Part B — Map C.** Diff, corrections, sample, render, Part D published.
   Every real extraction problem surfaces here; size it accordingly.
3. **Part C — Maps A, B, D, E**, one PR each, same gates.
4. **Part D — docs.** README, this design's status, vault roadmap.

## Review criteria for a map PR

- Gates above green; `EXTRACTION.md` entry present with counts.
- No file under `build/`, no raster, no NJHarman value in a committed file
  (counts in `EXTRACTION.md` are fine).
- Corrections cite the scan; none cite the diff.
- `raw/` changed only by an extractor PR.
