# The Logistics Game: Design

**Date:** 2026-09-27
**Sub-project:** 4 of the digital CNA roadmap (Logistics Game rules).
**Status:** complete, PRs #104–#143 (tooling #104, seed #105, rules files
#106–#111, #114, rulings #112–#113 and #115–#143), and the docs PR. Approved
under delegation: Brian said "go for mission 5" and delegated every
decision that is cheap to reverse (2026-09-26). The decisions below are
Claude's and can each be reversed with one PR.

## Goal

Restate SPI's Logistics Game (§48–58) the way Missions 1–2 restated the Land
Game: in our own words, precise enough to build an engine from, with errata
folded in, every chart as data, and every ambiguity recorded as a ruling and
then decided. The game's own introduction calls logistics its heart. Without
it, a digital CNA is the Land Game running on abstract supply (§32).

This also unblocks the three water rulings (R-020–R-022) that Mission 4 had
to leave open.

## Scope

**In:** §48–58, about 190 cases (by `data/spi-cases.json`):

| SPI | Subject | Cases |
|---|---|---|
| 48 | Logistics Game sequence of play | 1 (plus the long procedural text) |
| 49 | Fuel: consumption, transport, evaporation | 13 |
| 50 | Ammunition | 10 |
| 51 | Stores | 13 |
| 52 | Water: wells, pipelines, oases, usage, lack of water, pasta | 29 |
| 53 | Trucks and transport: the three lines, restrictions, abandoned vehicles | 15 |
| 54 | Supply co-ordination: dumps, railway, equivalent weights | 24 |
| 55 | Ports: capacity, efficiency, blocking | 20 |
| 56 | The Axis naval convoys, shipping lanes, coastal shipping | 25 |
| 57 | The Commonwealth supply base | 1 |
| 58 | Abstract air rules (for a Logistics Game played without the Air Game) | 9 |

Also in scope: the charts printed in these sections, as `data/tables/*.json`;
NJHarman's house rules on logistics topics, seeded as rulings and variants;
deciding every logistics ruling under the Mission 4 procedure.

**Out:**
- §47, the Air Game's abstract logistics. It belongs with the Air Game
  (sub-project 3).
- Per-unit figures that live on the OA sheets and counters rather than in
  the rules, such as a particular unit's fuel rate. Where a rule needs one,
  the rule names the variable and `data/README.md` records it as expected
  from the OA sub-project.
- Engine work. Once this mission lands, cna-engine can take water and fuel
  probes as its next mission.

## Decisions

| Topic | Decision | Why |
|---|---|---|
| File layout | A new folder, `rules/logistics/`, with its own sidebar group "Logistics Game" | Logistics is an optional module over the Land Game. A folder keeps the Land Game files untouched and makes the module boundary visible to an engine. |
| Files | `00-overview-and-sequence.md` (§48), `10-fuel.md` (§49), `20-ammunition-and-stores.md` (§50–51), `30-water.md` (§52), `40-trucks-and-dumps.md` (§53–54), `50-ports-and-shipping.md` (§55–57), `60-abstract-air.md` (§58) | This follows our system model, not SPI's section list, as the Land Game did: the four supply types, then how supply moves, then how it arrives. |
| Link to §32 | `00-overview-and-sequence.md` states exactly which parts of `rules/95-abstract-logistics-and-air.md` the Logistics Game replaces and which stay. Each Land Game passage that uses abstract supply gets a `::: note` pointing to its logistics replacement, added in the PR for that replacement | An engine needs a single switch: abstract or full logistics. The Land Game prose stays the current rule for players using abstract supply. |
| Sequence of play | The Logistics Game's extra phases are merged into `data/tables/sequence-of-play.json` if that file exists. If not, they go into a new `data/tables/logistics-sequence.json`, tagged by the Land Game phase each one attaches to | The Land design says the sequence is data the prose renders from. |
| Charts | Every chart in §48–58 becomes a table in `data/tables/`, with a schema and a test. Each is read twice, from the archive.org scan and a second scan (the Discord 300 dpi chart PDFs, or Clay Stone's Air & Logistics PDF), and diffed cell by cell, as in Mission 2 Part C | This is proven: 33 tables with 0 differences. |
| Rulings | At the start, NJHarman's CORRECTION, CLARIFICATION and INTERPRETATION items on logistics become `proposed` rulings, numbered on from the last `R-nnn`. His CHANGE and ADDITION items become variants. Ambiguities found while restating are opened as `proposed` rulings when they are hit. At the end, every proposed logistics ruling, R-020–R-022 included, is decided by the Mission 4 procedure in `AUTOPILOT.md` | This is the same process that produced R-002–R-024. |
| Tooling | `tools/gen_pages.py` reads `rules/` recursively (today it reads only the top level). `check_coverage.py` and `check_overlap.py` already recurse | Needed for the folder. |

## Merge criteria for a logistics rules PR

The Land Game review criteria (living-rules design, "Review criteria for a
rules PR") apply unchanged, with the coverage report run over
`--sections 48-58`. In addition:

- Every chart the file uses is in `data/tables/`, cross-checked, and linked
  from the prose.
- Every Land Game passage the file replaces carries its `::: note` pointer.

## Order

1. Tooling and the sidebar group (one PR).
2. Seed NJHarman's logistics rulings and variants (one PR per topic, as in Mission 2 Part B).
3. Rules files in the order listed above, one PR each. Each file's charts are transcribed in that file's PR, or in a PR just before it if the table work is large.
4. Decide every proposed logistics ruling, one PR each.
5. Docs: README's layout table, `rules/00-overview.md` (link the module), the design's Status line, and `EXTRACTION.md` entries throughout.
