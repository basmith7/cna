# Scenarios and OA Sheets Implementation Plan

> **For agentic workers:** follow this plan task by task, one PR per task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restate SPI §59–65 in `rules/scenarios/`, with every scenario
set-up, OA sheet, characteristics chart and reinforcement schedule as data,
starting with one complete Land Game scenario (Graziani's Offensive).

**Architecture:** The Mission 5 pipeline (source text, our prose with
`::: spi` badges, the overlap gate, the coverage report, `EXTRACTION.md`,
charts as JSON with a schema and a test), plus three new kinds of data:
`data/scenarios/`, `data/oa/` and unit-level tables.

**Tech Stack:** Python 3.12 tools (`tools/`), pytest, VitePress site, JSON
Schema 2020-12.

**Spec:** `docs/designs/2026-10-08-scenarios-and-oa-design.md`. Where this
plan and the spec disagree, follow the spec.

## Global Constraints

- No SPI text in the repo or on the site. Data holds values, ids and our own
  one-line notes; prose is our own words, citing case numbers.
- Every PR passes: `pytest`, `check_data.py`, `check_overlap.py` (with and
  without arguments), `check_coverage.py --sections <sections drawn on>`,
  `tools/gen_pages.py` (no diff left over), `npm run test:site`,
  `npm run site:build`.
- Values **as printed**, read from the scan (not the OCR source text), each
  read twice and diffed. Disagreements the scan cannot settle stay as read,
  go in the file's `notes` and in the `copy` group of
  `docs/autopilot/decisions.json`.
- Unit ids follow `data/README.md`: `unit:<nation>:<slug>`, nation ∈ `cw`,
  `it`, `de`. Slugs are lower-case ASCII, from the counter abbreviation
  (`unit:it:62-marmarica-div-hq`, `unit:cw:1-rnf`).
- Keys are `snake_case`; enums are closed. cna-engine reads these files with
  serde, so no field may need parsing from free text.

## Review Focus

1. **Every unit placed exists.** `check_data.py` resolves every `unit:` id in
   `data/scenarios/` and the schedule against `data/oa/`.
2. **Every hex and place exists** in `data/map/`.
3. **Printed totals match.** Where SPI prints a total (truck points, supply
   points, plane counts, TOE), a test sums the data and compares.
4. **The abstraction blocks replace, never add**, unless SPI says "in
   addition"; the test for each scenario names which.
5. **OCR is not a source.** Any hex or name that differs from the source
   text's OCR is logged in `EXTRACTION.md` with the scan page.

---

## Part 1: Graziani's Offensive, complete

All of Part 1 merges before Part 2 starts.

### Task 1.1: Tooling, schemas, sidebar, frontier

**Files:**
- Create: `data/schema/scenario.schema.json`, `data/schema/oa.schema.json`,
  `data/schema/reinforcement-schedule.schema.json`
- Modify: `tools/check_data.py` (validate `data/scenarios/*.json` and
  `data/oa/*.json`; resolve `unit:`, hex, `place` and `extends` references)
- Modify: `tests/test_check_data.py`
- Modify: `site/.vitepress/config.mts` (sidebar group "Scenarios")
- Modify: `data/map/` (frontier: region membership `libya` / `egypt` per
  hex, derived from the printed frontier on Maps C and D, checked against the
  scan; schema and builder changes as needed)
- Modify: `data/README.md` (the new folders and identifiers)

- [ ] Write failing tests: a scenario naming an unknown unit, an unknown hex,
  an unknown place, an `extends` to a missing scenario; each must fail
  `check_data.py`. A minimal valid scenario and OA file must pass.
- [ ] Write the schemas (shape in the spec's Decisions table) and the checks.
- [ ] Add the frontier; test that Sollum (C4021) is in Egypt and Fort Capuzzo
  (C4020) in Libya, read from the scan.
- [ ] Gates, PR `autopilot/s-tooling`.

### Task 1.2: Unit characteristics and weapon systems

**Files:**
- Create: `data/tables/unit-characteristics.json`, `data/tables/weapon-systems.json`
  and their schemas and tests
- Modify: `EXTRACTION.md`

- [ ] Read 4.46a/b/c (jp2 132–133, 136, 166–170) and 4.47–4.49 (jp2 137–139,
  171–172) twice; diff; record.
- [ ] Test: every ID code used by `data/oa/` has a characteristics row (runs
  once Task 1.3 lands; skip if no OA yet).
- [ ] Gates, PR `autopilot/s-characteristics`.

### Task 1.3: OA sheets for Graziani's Offensive

**Files:**
- Create: `data/oa/it.json`, `data/oa/cw.json` (only the formations §60.31,
  §60.41 and the Game-Turn 1–6 arrivals name); tests

- [ ] List the formations named in §60.31, §60.41 and the schedule rows for
  Game-Turns 1–6.
- [ ] Read each OA sheet (Commonwealth jp2 115–131, Italian jp2 146–160)
  twice; diff; record.
- [ ] Test: each formation's units sum to the TOE the sheet prints, where it
  prints one.
- [ ] Gates, PR `autopilot/s-oa-graziani`.

### Task 1.4: Reinforcement schedule through Game-Turn 6

**Files:**
- Create: `data/tables/reinforcement-schedule.json` (Game-Turns 1–6, both
  sides) and schema test

- [ ] Read 4.43a (jp2 113–114) and 4.43b (jp2 144–145) twice for Game-Turns
  1–6; diff; record. Add any OA sheets the rows name that Task 1.3 lacks.
- [ ] Gates, PR `autopilot/s-schedule-gt1-6`.

### Task 1.5: The scenario file and the rules prose

**Files:**
- Create: `data/scenarios/grazianis-offensive.json`,
  `data/scenarios/italian-campaign.json` (`extends`)
- Create: `rules/scenarios/00-reading-scenarios.md` (§59),
  `rules/scenarios/10-the-italians.md` (§60)
- Create: `tests/test_scenarios.py`
- Modify: `EXTRACTION.md`

- [ ] Transcribe §60.31–60.47, §60.5–60.7 and §60.92–60.93 from the scan
  (jp2 pages of §60 in the rulebook) into the scenario file; victory
  conditions §60.81–60.82 as structured objectives (`hold` a place or hex,
  with the supply condition as a named enum value).
- [ ] Test: printed totals (§60.33, §60.34, §60.43, §60.44 and the §60.92
  tables) sum correctly; every §59.12 heading (a–h) has its block.
- [ ] Write the two rules files; open `proposed` rulings for what the data
  cannot say.
- [ ] Add `59-60` to the CI coverage `--sections` in `.github/workflows/ci.yml`
  (each later rules PR adds its own section).
- [ ] Gates (`--sections 59,60`), PR `autopilot/s-the-italians`.
- [ ] After merge: a line in `PROGRESS.md` telling cna-engine Part 1 has
  landed (scenario id and file paths).

## Part 2: Seed NJHarman's scenario items

### Task 2.1

- [ ] Find NJHarman's items on §59–65 (`~/.cache/cna-scans/njharman-clean.txt`
  and the Discord notes). CORRECTION / CLARIFICATION / INTERPRETATION become
  `proposed` rulings from R-094; CHANGE / ADDITION become variants from V-006.
- [ ] Gates, PR `autopilot/s-seed`.

## Part 3: The other scenario groups, and the rest of the OA

One PR per bullet, each preceded by a data PR for the OA sheets and schedule
rows it needs if those are large:

- [ ] Task 3.1 `20-desert-fox.md` (§61) with `rommels-arrival.json` and its campaign.
- [ ] Task 3.2 `30-crusader.md` (§62) with its scenario file(s).
- [ ] Task 3.3 `40-el-alamein.md` (§63) with `the-last-chance.json` and `the-long-retreat.json`.
- [ ] Task 3.4 the remaining OA sheets (all three nations) and the full
  reinforcement schedule.
- [ ] Task 3.5 `50-campaign-game.md` (§64; §65 `spi-omit`) with the campaign
  game file(s).
- [ ] Task 3.6 the per-unit figures listed in `data/README.md` under *Values
  expected from the OA sub-project*, where the scans print them; the rest go
  to the `copy` group.

## Part 4: Decide every new ruling

- [ ] One PR per ruling, branch `autopilot/ruling-r-nnn`, by the standing
  procedure in `AUTOPILOT.md`.

## Part 5: Docs

- [ ] README layout table, `rules/00-overview.md` (link the Scenarios group),
  the design's Status line, `EXTRACTION.md`, and the queue in `AUTOPILOT.md`
  (Mission 6 `done`, Mission 7 `next`). Log `MISSION 6 COMPLETE`.
