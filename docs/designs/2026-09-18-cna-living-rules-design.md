# CNA Living Rules — Design

**Date:** 2026-09-18 (revised after adversarial review and prior-art survey)
**Status:** approved design, awaiting implementation plan
**Sub-project:** 1 of N toward an open-source, self-hostable, rules-enforced online
implementation of *The Campaign for North Africa* (SPI, 1979). This sub-project
produces the rules and core tables an engine will be built against. No engine,
server, or UI work is in scope.

## Goal

A public, reviewed, searchable edition of the CNA **Land Game** rules and its
common tables that:

1. is precise enough to implement a rules-enforcing engine from;
2. folds in SPI's official September 1979 errata;
3. records every gap, contradiction, or ambiguity we resolve, with decision and
   rationale, in a form the community can dispute;
4. is written as our own expression of the mechanics, so it can be openly
   licensed;
5. is published as a static site with full-text search and visual distinction
   between restated rule, errata, and our rulings, with the original SPI text
   viewable beside ours for review.

## Scope

**In:** Land Game §1–32 (self-contained via §32 abstract logistics/air);
the common charts and tables (scan pp. 96–111: CRTs, terrain, weather, fuel
consumption, stacking, initiative, etc.); site; tooling.

**Out (own specs later):** Air Game §33–46; Logistics Game §47–58; scenarios
§59–64 beyond what the Overview needs; OA sheets and reinforcement schedules;
map digitisation; simplification/automation variants; any engine code;
redistributing SPI text, map, or counter art.

## Prior art we build on

| Source | What | How we use it |
|---|---|---|
| [archive.org scan](https://archive.org/details/campaign-for-north-africa), item `campaign-for-north-africa` | 192 pp: rules, charts, OA, counters, 5 maps (~150 dpi) | Authority for tables and maps. Pin identifier + file SHA-256 in `tools/sources.json`. Not committed; `~/.cache/cna-scans`. |
| [tonicebrian/TheCampaignForNorthAfrica](https://github.com/tonicebrian/TheCampaignForNorthAfrica) | Verbatim transcription, all 65 sections, AsciiDoc, one anchor per case (`[#8_37]`) | The **source text** for side-by-side review. We do not make our own transcription. |
| [Clay Stone's 2021 errata-integrated PDFs](https://friendorfoe.com/d/CfNA/) | Re-typeset Land / Air & Logistics / Scenarios with errata applied | Cross-check when transcription and errata disagree. |
| [SPI errata, Sept 1979](https://www.spigames.net/db_pages/ERR_CampaignforNorthAfrica.pdf) ([HTML](http://www.wargameacademy.org/CNA/CNA_errata.html)) | Official corrections | Applied as errata entries, paraphrased, cited by item. |
| [NJHarman's House Rules & Interpretations](https://friendorfoe.com/war/cfna/houserules/) | ~7,500 words, tagged CORRECTION / CLARIFICATION / INTERPRETATION / CHANGE / ADDITION; CC-BY-SA 4.0; updated 2025-07 | Seed for the rulings log, with attribution. CORRECTION/CLARIFICATION/INTERPRETATION become `proposed` rulings; CHANGE/ADDITION are recorded as variants, not adopted. |
| [dills122/sandtable](https://github.com/dills122/sandtable) | Active C# engine, same 1979+errata posture, cites rules as `CNA1979:8.22` | Peer consumer of our case IDs; not a dependency. |
| VASSAL module v2.1.0 (Mitch Guthrie, 2021) | Homogeneous vector-style redraw of all five maps as one 14310×4632 PNG; `buildFile.xml` carries exact hex geometry (`dx=72.95 dy=85.25`, sideways), per-sheet zone polygons and numbering offsets | **Source for the map sub-project.** `tools/map_extract.py` maps hex IDs to pixels from `buildFile.xml` and classifies terrain by sampling hex centres and hexside midpoints; only the derived terrain data is committed, the PNG is cached like the scans. |
| Michael Miller's `CNA-Hex-Database-20150117.csv` | Hand-built hex/hexside terrain data (link dead) | Cross-check for the extractor if it resurfaces; not a dependency. |
| BGG files (OOB xlsx 2010, Sequence of Play 2008, CRT analysis 2026) | Community aids | Cross-checks only. |

## Legal posture

Stated plainly in `README.md` and not asserted beyond this:

- Game mechanics are not copyrightable. This project restates them in its own
  words and organisation. It is **intended** to be independent expression; no
  legal review has been obtained.
- No SPI rule text, map art, or counter art is in this repository or in the
  built site. The original text shown by the "show original" toggle is loaded
  in the reader's browser from tonicebrian's repository and is never part of
  our build or search index.
- Licences are granted *to the extent the project holds rights*: `rules/`
  CC-BY-SA-4.0; `data/` CC0-1.0 (values believed to be uncopyrightable facts
  and game parameters; the compilation is our own organisation); `tools/`,
  `site/` MIT. Root `LICENSE` is a pointer file explaining the split so GitHub
  does not label the repo as a single licence.
- Nominative use of the game's name only; no trade dress. Not marketed as a
  substitute edition.
- `EXTRACTION.md` keeps a short log per section: source cases read → mechanic
  identified → how we expressed it. Evidence of the idea/expression split.
- Both repos of interest live under the same GitHub account; GitHub's
  repeat-infringer policy is account-level. We accept that; a mirror of `cna`
  off GitHub is part of the self-hosting story later.

## Repository layout

```
rules/                    # organised by OUR system model, not SPI's TOC
  00-overview.md          # authored: turn, roles, nested games, resource loops
  glossary.md             # authored
  10-units-and-state.md   # unit characteristics, TOE, cohesion, morale enums  (SPI §3, §6.2, §17)
  20-sequence-of-play.md  # (§5, §7)
  30-capability-points.md # (§6)
  40-movement.md          # continual movement, terrain, breakdown, rail, reaction (§8, §21)
  50-stacking-and-zoc.md  # (§9, §10)
  60-combat.md            # system, barrage, RBA, anti-armor, close assault, probes, patrols (§11–16)
  70-organisation.md      # attachment, reinforcements, replacements, reserve, training (§18–20)
  80-engineering.md       # engineers, construction, fortifications, minefields, repair (§22–26)
  90-special.md           # raiders, prisoners, weather, fleet, Rommel (§27–31)
  95-abstract-logistics-and-air.md  # (§32)
rulings/
  R-001.md …              # one file per ruling, frontmatter: id, status, affects, sources
  README.md               # numbering, statuses, process
data/
  README.md               # ID grammar, enums, coordinate convention, provenance
  schema/*.json           # JSON Schema per dataset
  tables/*.json           # one file per concept (not per SPI chart); each carries source refs
  spi-cases.json          # canonical list of SPI case IDs, page, our one-line label — no SPI text
tools/
  sources.json            # archive.org identifier + file hashes; tonicebrian pinned commit
  fetch.py                # scans → ~/.cache/cna-scans
  check_coverage.py       # which SPI cases have no badge (report, not gate)
  check_overlap.py        # 8-word n-gram overlap vs source text (gate)
  check_data.py           # schema + referential integrity (gate)
  learn_page.py           # illustrated primer (docs/learn)
site/                     # VitePress
docs/designs/             # this file and later designs
docs/learn/               # primer output (scan crops git-ignored)
EXTRACTION.md · README.md · LICENSE (pointer) · LICENSE-TEXT · LICENSE-DATA · LICENSE-CODE
```

## Rules text

### Organisation

Files follow **our system model** (above), not SPI's section list. Within a
file, headings, order, grouping, merging and splitting are chosen for
readability and precision. Completeness is defined by our model: every state
variable, phase, and procedure an engine needs is specified. SPI's case list
is a *checklist* against that, not the structure.

### The `spi` badge (join key)

Each rule block is preceded by a block marker naming the SPI cases it draws
on:

```markdown
::: spi 8.35 8.36
```

- Rendered as a small tag (**SPI 8.35–8.36**). Metadata only — the citation
  for paper-rules players, and the key used by "show original".
- A badge opens a scope that ends at the next badge or heading. Exactly one
  badge per SPI case is **primary** (gets the anchor `#spi-8.35`); further
  mentions use `::: spi-ref 8.35`. Rulings link to the primary anchor.
- Cases that are pure commentary or component description may be marked
  `::: spi-omit 4.6 — component inventory` so the coverage report is honest.
- `tools/check_coverage.py` reports SPI cases (from `data/spi-cases.json`)
  with no primary badge. It is a report, not a build gate.

### Writing rules

- Restate as precise definitions and procedures: defined terms bold on first
  use, numbered steps, tables for anything tabular, explicit *may / must /
  may not*. Examples use **our own situations**, not SPI's with new numbers.
- The plain body is always the **current rule** — post-errata, post-ruling.
  Errata and ruling containers annotate what changed and why; they are never
  an alternative rule body.
- `tools/check_overlap.py` fails the build on any 8-word run shared with the
  source text (excluding a small allowlist of unavoidable terms). This is a
  control for verbatim copying only.
- Each file ends with a provenance line naming the SPI sections drawn on.
- Each section is `provisional` (frontmatter) until an engine has consumed it;
  the engine sub-project is expected to reopen rulings.

### Provenance containers

| Container | Meaning |
|---|---|
| *(plain body)* | The current rule, our words. |
| `::: errata E-12` | Annotation: what SPI's Sept 1979 errata changed here, paraphrased, cited by item. |
| `::: ruling R-012` | Annotation: this block reflects our ruling; links to `rulings/R-012.md`. |
| `::: note` | Non-binding: designer intent, why, play advice. |
| `::: variant V-003` | A community CHANGE/ADDITION we record but do not adopt (e.g. NJHarman). |
| *(generated)* `original` | Collapsed block, **client-side only**: fetched at page view from tonicebrian's repo for the cases in the enclosing badge; excluded from SSR and search; hidden if the fetch fails; can be disabled by one config flag. |

A build step generates a **"Changes from the original"** page (all errata and
rulings by file) and the coverage report.

### Rulings

`rulings/R-nnn.md`, frontmatter `id, status, affects: [8.37, 8.42], sources,
supersedes`, body: Problem · Options · Decision · Rationale · Discussion link.
Statuses: `proposed`, `accepted`, `rejected`, `superseded`. Seeded from
NJHarman's CORRECTION/CLARIFICATION/INTERPRETATION entries (attributed,
CC-BY-SA), each as `proposed` until reviewed. Community disputes via GitHub
Discussions → PR. One maintainer accepts; a fork policy is written in
`rulings/README.md` so disagreement has a non-hostile exit.

## Data

- `data/README.md` **first**, before any transcription: stable ID grammar
  (`unit:cw:1-rnf`, `table:terrain-effects`, hex `C4023` = sheet + RRCC as
  printed), enums (terrain, weather, unit class, supply type, phase), and the
  hexside convention (for the later map spec).
- One JSON file per **concept** (terrain effects, close-assault CRT, barrage
  CRT, anti-armor CRT, weather, fuel consumption, initiative ratings,
  stacking, CP costs …), not one per SPI chart. Each record carries
  `sources: ["CNA1979:8.37", "scan:p69"]`.
- **Errata as overlay**: base values as printed plus `errata/*.json` patches
  applied at build; both are inspectable.
- JSON Schema per file; `tools/check_data.py` validates schema and
  referential integrity in CI (gate).
- Transcription from page images: two independent extractions (two
  vision models, or model vs the BGG spreadsheets) diffed; humans resolve
  discrepancies only; row/column totals captured as invariants where the
  table has them. Provenance is page + table name.
- Sequence of play is a data file (`data/tables/sequence-of-play.json`) that
  the prose renders from.

## Site

- VitePress in `site/`, sourcing `rules/` and rendering `data/` tables.
- Phase 1: stock theme, local search, `editLink`, sidebar. Phase 2 (once
  content exists): provenance container styling, badges, changes page,
  coverage page, client-side original viewer.
- PR checks: site builds, overlap gate, data gate, coverage report posted as a
  comment. Deploy to GitHub Pages on merge to `main` only.

## Process

1. **Scaffold** — repo hygiene (licences, README with legal posture,
   `EXTRACTION.md`), `tools/sources.json` with pinned archive item + hashes
   and tonicebrian commit, `data/README.md` + schemas, `data/spi-cases.json`
   (generated from tonicebrian's anchors — IDs and our labels only), VitePress
   phase 1, CI with the two gates and the coverage report.
2. **Overview + glossary** — authored from what we already learned; the top
   of the tree. `docs/learn` primer links from it.
3. **Restate the Land Game** in this order, one PR each, Brian reviews:
   units & state → sequence of play → capability points → movement → stacking
   & ZOC → combat → organisation → engineering → special → §32. Common tables
   transcribed alongside the file that first needs them. Rulings logged as
   hit; NJHarman seed imported at the start of step 3.
4. **Site phase 2** once ≥3 files exist.
5. **Outreach** in parallel with 1: NJHarman (rulings upstreaming, hex CSV as cross-check),
   Dylan Steele (case-ID citation target).

Air, Logistics, scenarios, OA, map: separate specs after 3 is done.

## Review criteria for a rules PR

- Every SPI case for the sections drawn on is primary-badged, `spi-ref`'d, or
  `spi-omit`'ed with a reason (coverage report clean for those sections).
- Overlap gate passes.
- Every errata item touching those cases is applied and annotated.
- Every ambiguity found has a `proposed` ruling file.
- Examples are our own situations.
- `EXTRACTION.md` has an entry for the file.
- Site builds; the file is in the sidebar and search.
