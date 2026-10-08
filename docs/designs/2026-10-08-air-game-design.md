# The Air Game: Design

**Date:** 2026-10-08
**Sub-project:** 3 of the digital CNA roadmap (Air Game rules).
**Status:** Part 0 (this spec and its plan). Written by the autopilot as
Mission 7 Part 0 under the delegation of 2026-09-26: every decision below is
Claude's, is cheap to reverse, and can each be reversed with one PR.

## Goal

Restate SPI's Air Game (§33–47) the way Mission 5 restated the Logistics
Game: in our own words, precise enough to build an engine from, with errata
folded in, every chart as data, and every ambiguity recorded as a ruling and
then decided.

This serves **the goal** in `AUTOPILOT.md` directly: it is the last module
the rulebook lacks. When it lands every SPI section is covered, and an
engine can build any combination of the three games (Land alone, Land with
Logistics, Land with Air, all three) from this repository without opening
the SPI books. For cna-engine it is optional work: every scenario is
already playable with the Air Game abstracted (§32 and §58), so the engine's
critical path does not wait on this mission, and this repo keeps answering
the engine's requests first, every run.

## Scope

**In:** §33–47, 431 cases (by `rules/coverage.md`):

| SPI | Subject | Cases |
|---|---|---|
| 33 | Air Game sequence of play | 1 (plus the long procedural text) |
| 34 | The aircraft: fighters, bombers, flying boats, transports; characteristics; reinforcements and withdrawals | 45 |
| 35 | Squadron ground support units (SGSUs) | 20 |
| 36 | Air facilities: airfields, landing strips, flying-boat basins, off-map facilities | 15 |
| 37 | Flight: mechanics, restrictions, emergency flight, distance charts | 21 |
| 38 | Aircraft maintenance: readying, refuelling, refitting, arming | 27 |
| 39 | Missions in general, combined, aborted, night; mission summary | 27 |
| 40 | Fighter combat: pilots, CAP, scramble, strafing, flak suppression | 52 |
| 41 | Bombing missions: land support, night, air bombardment, convoys, torpedoes, Tripoli | 60 |
| 42 | Non-combat missions: transfer, reconnaissance, transport, airdrop, convoy reconnaissance | 39 |
| 43 | Axis Italian and Aegean air bases | 12 |
| 44 | Malta: bases, raids, invasion, strategic raids, construction | 25 |
| 45 | Air-to-air combat | 34 |
| 46 | Anti-aircraft fire | 20 |
| 47 | Abstract logistics for the Air Game (played without the Logistics Game) | 33 |

Also in scope: the charts printed in these sections as `data/tables/*.json`
(aircraft characteristics, distance charts, scramble, strafing, air
bombardment, TacAir kill, maneuver adjustment, AA combat results, flak
adjustment, Malta construction, air reinforcements and withdrawals);
NJHarman's house rules on air topics, seeded as rulings and variants (his
notes touch about 19 air cases, including the CAP conflict between 40.24 and
41.63 and Malta CAP in 39.5); and deciding every air ruling.

**Out:**
- The scenarios' air set-ups. They are already data where the scans print
  them (`data/scenarios/`, Mission 6); this mission only checks that every
  aircraft type they name has a characteristics row, and adds it if not.
- Per-pilot or per-plane figures printed only on counters. Where a rule
  needs one, the rule names the variable and `data/README.md` records where
  it is expected from, as Mission 5 did.
- Engine work.

## Decisions

| Topic | Decision | Why |
|---|---|---|
| File layout | A new folder, `rules/air/`, with its own sidebar group "Air Game", as `rules/logistics/` has | The Air Game is an optional module. A folder keeps the Land and Logistics files untouched and makes the module boundary visible. |
| Files (each under about 70 cases) | `00-overview-and-sequence.md` (§33, 1), `10-aircraft-and-sgsus.md` (§34–35, 65), `20-air-facilities.md` (§36, 15), `30-flight-and-maintenance.md` (§37–38, 48), `40-missions.md` (§39 and §42, 66), `50-fighters.md` (§40, 52), `60-bombing.md` (§41, 60), `70-air-combat-and-flak.md` (§45–46, 54), `80-mediterranean-and-malta.md` (§43–44, 37), `90-abstract-logistics.md` (§47, 33) | Our system model, not SPI's section order: what flies, where from, how it flies and is kept flying, what it does, how it fights, then the theatre and the logistics fallback. §42 joins §39 because both are mission rules with no combat. |
| The switch from §32 and §58 | `00-overview-and-sequence.md` states exactly which parts of `rules/95-abstract-logistics-and-air.md` (§32) and `rules/logistics/60-abstract-air.md` (§58) the Air Game replaces and which stay, as one list an engine can implement as one switch. Expected from a first reading: all of §58; from §32 the air parts (convoy and fleet attack by abstract air, the anti-air modifications, limited intelligence where air reconnaissance replaces it); §32's supply-unit rules stay unless §47 replaces them. The list is settled in Task 3.1 from the text, and each replaced passage gets a `::: note` pointer in the PR that replaces it | `AUTOPILOT.md` asks for exactly this, so the engine has one switch. The Land and Logistics prose stays the current rule for players without the Air Game. |
| §47 | `90-abstract-logistics.md` restates §47 as the supply rules of a Land-and-Air game without the Logistics Game, and says how it differs from §32 (depots, air-facility supply), not as a copy of §32 | §47 and §32 overlap heavily; restating only the differences keeps one source for each rule. Mission 5 left §47 out on purpose for this mission. |
| Sequence of play | No new table. `data/tables/logistics-sequence.json` (48.0) is already the full three-game sequence with an `air_game_only` flag on every air step; §33's Land-and-Air sequence is the same list without the Logistics Game's own steps. Task 1 adds a `logistics_game_only` flag (stores expenditure, water distribution, attrition) and checks the §33 order against it, so one table serves all four combinations of modules | One sequence, filtered by two switches, cannot drift apart the way two copies could. |
| Charts | Every chart in §33–47 becomes a table in `data/tables/`, with a schema and a test, read twice (archive.org scan and the community 300 dpi chart PDFs, or Clay Stone's Air & Logistics PDF) and diffed cell by cell | Proven in Missions 2, 5 and 6: hundreds of cells, few differences, each resolved or sent to the `copy` group. |
| Aircraft identity | Aircraft types get ids `aircraft:<nation>:<slug>`; the characteristics table and the air reinforcement schedule key on them, and scenario air set-ups are checked against them by `check_data.py` | One id per type lets scenarios, reinforcements and charts agree, as `unit:` ids do for land units. |
| Rulings | NJHarman's CORRECTION, CLARIFICATION and INTERPRETATION items on air become `proposed` rulings, numbered on from the last `R-nnn`; CHANGE and ADDITION items become variants. Ambiguities found while restating are opened when hit. All are decided at the end by the standing procedure | Same process as Missions 2, 5 and 6. |
| Tooling | None expected: `gen_pages.py`, `check_coverage.py` and `check_overlap.py` already read subfolders. Task 1 only adds the sidebar group and extends CI coverage to `33-47` as files land | Mission 5 did the subfolder work. |

## Merge criteria for an air rules PR

The Land Game review criteria (living-rules design) apply unchanged, with
the coverage report run over the sections the file draws on (0 uncovered).
In addition:

- Every chart the file uses is in `data/tables/`, cross-checked, linked from
  the prose, with its cross-check count in `EXTRACTION.md`.
- Every §32 or §58 passage the file replaces carries its `::: note` pointer,
  and the overview's replacement list names it.
- No rules file over about 70 cases.

## Order

0. This spec and plan (one PR).
1. Sidebar group "Air Game" and the overview stub (one PR, with the first
   rules file if an empty group breaks the build, as in Mission 6).
2. Seed NJHarman's air items as rulings and variants (one PR).
3. Rules files in the order of the Files row, one PR each; each file's
   charts in its own PR or one just before it. Plan for several runs.
4. Decide every proposed air ruling, one PR each.
5. Docs: README, `rules/00-overview.md` (the Air Game row stops saying
   "restated separately"), this Status line, the queue in `AUTOPILOT.md`
   (Mission 7 `done`), and `MISSION 7 COMPLETE`. After that the rulebook is
   done and the autopilot works only on cna-engine's requests and Brian's
   feedback.
