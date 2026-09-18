# CNA Living Rules — Design

**Date:** 2026-09-18
**Status:** approved design, awaiting implementation plan
**Sub-project:** 1 of N for an open-source, self-hostable, rules-enforced online
implementation of *The Campaign for North Africa* (SPI, 1979). This sub-project
produces the rules and data the game engine will be built against. No engine,
server, or UI work is in scope here.

## Goal

A public, reviewed, searchable edition of the CNA rules and game data that:

1. is precise enough to implement a rules-enforcing engine from;
2. folds in SPI's official September 1979 errata;
3. records every gap, contradiction, or ambiguity we resolve, with the decision
   and rationale, in a way the community can dispute;
4. can be openly licensed — which means it is **our own expression** of the
   mechanics, not a transcription of SPI's text;
5. is published as a static site on GitHub Pages with full-text search and
   visual distinction between original rule, errata, and our rulings.

## Non-goals

- Simplification or automation variants (planned as a later ruleset layer).
- Verbatim transcription of SPI text (copyright; not ours to license).
- Redistributing SPI map or counter art.
- Community rules from the cna-group forum / "CNA Computer System" — not
  publicly available; if they surface, they slot in as patches (see Rulings).
- Any engine, server, or client code.

## Sources

| Source | Use |
|---|---|
| [archive.org scan](https://archive.org/details/campaign-for-north-africa) — 192 pp: Land Rules (1–47), Air & Logistics Rules + scenarios (48–90), countersheets (91–95, 182–187), common charts (96–111), Commonwealth charts/OA (112–143), Axis charts/OA (144–181), 5 map sections (188–192) | Primary spec. OCR text is good for rules prose, useless for tables; tables come from page images. |
| [SPI errata, Sept 1979](https://www.spigames.net/db_pages/ERR_CampaignforNorthAfrica.pdf) (clean HTML at [Wargame Academy](http://www.wargameacademy.org/CNA/CNA_errata.html)) | Applied inline. Includes three missing Italian division OA sheets and reinforcement omissions. |
| BGG files (OOB spreadsheet 2010, Sequence of Play 2008, CRT analysis 2026) | Cross-checks for data transcription; not authoritative. |
| MOVES magazine Q&A (1979–81) | Later pass if located; treated as errata with a `source` note. |

Scans and OCR text are **not committed** (`reference/` is git-ignored); tools
fetch them from archive.org.

## Licensing

- `rules/` text: CC-BY-SA-4.0.
- `data/`: CC0-1.0 (game data are facts/numbers).
- `tools/`, `site/`: MIT.
- Repo README states the copyright position: mechanics are not copyrightable;
  text is our restatement; no SPI text, map, or counter art is included.

## Repository layout

Single repo, `cna`, intended to become the monorepo for later sub-projects.

```
rules/                  # one markdown file per SPI section
  00-index.md
  01-introduction.md … 32-abstract-logistics-and-air.md   (Land Game)
  33-… 46-…                                              (Air Game)
  47-… 58-…                                              (Logistics Game)
  59-… 64-…                                              (Scenarios)
  rulings.md            # R-001 … resolved ambiguities
  glossary.md           # generated from §3 + terms introduced elsewhere
data/
  README.md             # schemas, provenance conventions
  units/                # characteristics charts (CW, German, Italian; land & air)
  oa/                   # organization-at-arrival sheets, one file per parent formation
  reinforcements/       # land & air schedules, withdrawals, replacement pools
  tables/               # CRTs, terrain effects, weather, fuel consumption, etc.
  map/                  # hex terrain, hexsides, named locations, per map sheet A–E
tools/                  # fetch + extraction scripts (python); committed, throwaway-grade
site/                   # VitePress: config, theme, custom containers
docs/superpowers/specs/ # this and later designs
.github/workflows/pages.yml
LICENSE                 # MIT (tools, site)
LICENSE-TEXT            # CC-BY-SA-4.0 (rules)
LICENSE-DATA            # CC0-1.0 (data)
```

## Rules text

### Structure

- One file per SPI numbered section, filename `NN-kebab-title.md`.
- Every SPI case keeps its number as a heading anchor so it is citable and
  cross-referenceable to the original:

  ```markdown
  ## [8.3] Terrain Effects on Movement
  ### [8.37] Terrain Effects Chart
  ```

- Within a case the rule is **restated as a precise definition or procedure**:
  defined terms in bold on first use, numbered steps for procedures, tables for
  anything tabular, explicit "may / must / may not". SPI's examples are
  re-done with our own numbers. Redundant restatements across sections are
  replaced with a cross-link.
- If we split or merge cases for clarity, the SPI numbers are preserved in the
  heading (`## [8.35–8.36] …`) so nothing is un-findable.
- Each file ends with a provenance line:
  `*Source: SPI 1979 Land Game Rules, pp. 13–15; errata Sept 1979.*`

### Provenance markup

Three custom VitePress containers, rendered with distinct colour and label:

| Container | Meaning |
|---|---|
| *(plain body)* | Our restatement of the original rule. |
| `::: errata` | Rule as changed by SPI errata. Quotes the errata point briefly and states the corrected rule. |
| `::: ruling R-012` | Our resolution of a gap or contradiction. Body states the rule as we play it; links to `rulings.md#R-012`. |
| `::: note` | Non-binding commentary: designer intent, why a rule exists, play advice. |

A build step scans containers to generate a **"Changes from the original"** page
listing every errata and ruling by section.

### Rulings log

`rules/rulings.md`, one entry per issue:

```markdown
## R-012 — Track cost when entering a hex by road *(accepted)*
**Affects:** [8.37], [8.42]
**Problem:** … (what the original says, why it is ambiguous/contradictory)
**Options:** 1. … 2. …
**Decision:** …
**Rationale:** …
**Discussion:** <link to GitHub Discussion>
```

Status is `proposed` until the maintainer accepts; the site renders both.
Community disputes go through GitHub Discussions/Issues → PR.

## Data

- Every table from the Charts & Tables booklets becomes one JSON or CSV file
  (JSON for nested/structured, CSV for flat tables). Schema for each documented
  in `data/README.md`.
- Every record carries `source_page` (scan page number) and, if changed by
  errata, `errata: true` with a `note`.
- Transcription is from page images: vision-model-assisted extraction into the
  schema, then human verification against the image. OCR text is not used for
  tables.
- Map: for each of the five sheets, a hex table (`hex_id`, terrain, features,
  named location) and a hexside table (escarpments, roads, tracks, rail, wadis,
  coastline). Derived by hand/vision from the scans; SPI map art is not
  committed.
- Errata data changes (missing Italian OA sheets, reinforcement omissions,
  map D escarpment 2228/2328) are applied in data and flagged.

## Site

- VitePress in `site/`, sourcing `rules/` and rendering `data/` tables.
- Local full-text search (built-in MiniSearch).
- Sidebar: Land Game / Air Game / Logistics Game / Scenarios / Rulings /
  Changes from original / Data / About & licensing.
- Custom theme: the three provenance containers styled distinctly (colour bar +
  label); a legend on every page footer.
- `editLink` on every page → GitHub edit → PR (wiki-style contribution with
  review).
- Deploy: GitHub Actions on push to `main` → GitHub Pages.
- Later: Vue components for interactive CRT lookups and a hex viewer can be
  embedded without changing the content model.

## Process

1. **Scaffold**: repo, licences, VitePress with containers and deploy, `tools/`
   fetch script for OCR text and page images, `data/README.md` schemas.
2. **Land Game §1–32**, in order, a few sections per PR. For each section:
   clean OCR → apply errata → restate → flag ambiguities as `proposed` rulings
   → Brian reviews → merge. §32 (abstract logistics & air) makes the Land Game
   self-contained, so this is the first milestone at which an engine could be
   started.
3. **Land data**: unit characteristics, OA sheets, reinforcements, common
   tables, map hexes.
4. **Air Game §33–46** and air data.
5. **Logistics Game §47–58** and logistics data.
6. **Scenarios §59–64** (mostly data: setups, supply levels).
7. MOVES Q&A pass, if issues are located.

## Review criteria for a section PR

- Every SPI case number in that section is present as an anchor.
- No sentence is a copy of SPI text (spot-check).
- Every errata item touching the section is applied and marked.
- Every ambiguity found has a ruling entry (`proposed` is fine).
- Site builds; the section appears in search and the sidebar.
