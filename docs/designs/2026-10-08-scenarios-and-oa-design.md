# Scenarios and OA Sheets: Design

**Date:** 2026-10-08
**Sub-project:** 5 of the digital CNA roadmap (scenarios and OA sheets).
**Status:** complete, PRs #146–#186 (spec #146; Part 1 Graziani's Offensive
#147–#151, #153; seed #152; Part 3 scenarios, OA sheets and schedule #154–#160,
#162, Task 3.6 #184; Part 4 rulings R-094–R-109 #161, #163–#167, #174–#182, #186;
docs). Also R-110 (#171) and the weapon-systems chart (#172) from
cna-engine's requests. Written by the autopilot as
Mission 6 Part 0 under the delegation of 2026-09-26: every decision below is
Claude's, is cheap to reverse, and can each be reversed with one PR. The
order (one small scenario first) is Brian's, from the *Path to a playable
game* agreed on 2026-10-07.

## Goal

Restate SPI's scenario sections (§59–65) and turn the scenario set-ups, the
organisation (OA) sheets and the reinforcement schedules into data, so that
an engine can load a scenario and place every unit without opening the SPI
books.

This is how the mission serves **the goal** (a self-hostable digital CNA two
players can play in a browser): the rulebook so far says how units move and
fight, but not which units exist, where they start, what their ratings are or
when they arrive. Without that no game can start. cna-engine's Mission 2
(headless game state for one small scenario) is built on Part 1 of this
mission, so Part 1 is one scenario, complete, merged before anything else.

## The first scenario: Graziani's Offensive

Part 1 is **Graziani's Offensive** (§60.22), played as the Land Game only
(§60.92). Why this one:

- **It is the shortest.** Game-Turns 1–6, eighteen OpStages. Rommel's
  Arrival (§61) runs Game-Turns 26–38; Crusader and El Alamein are longer
  still.
- **Its set-up is self-contained.** Every starting unit is listed by hex in
  §60.31 and §60.41. Rommel's Arrival instead places "all German units
  scheduled before Game-Turn 26", so it needs the whole Axis reinforcement
  schedule up to then.
- **It needs neither the Air Game nor the Logistics Game.** §60.92 gives its
  Land-Game-only adjustments (supply units and motorisation points instead
  of dumps and trucks), and the abstract rules for both are already restated
  (§32 in `rules/95-abstract-logistics-and-air.md`).
- **It shares its set-up with the Italian Campaign** (§60.23), so the second
  scenario of the group is almost free.

Its cost is size: two Italian armies and the Western Desert Force start on the
map, about 200 counters. The designer recommends Rommel's Arrival as the
quick game; it is short in units, not in turns or dependencies, so it comes
second.

## Scope

**In:** §59–65, about 170 cases (by `data/spi-cases.json`):

| SPI | Subject | Cases |
|---|---|---|
| 59 | Introduction: reading a set-up, initial air, trucks and supply, abstractions | 30 |
| 60 | Group One, the Italians: Graziani's Offensive, the Italian Campaign | 32 |
| 61 | Group Two, the Desert Fox: Rommel's Arrival and its campaign | 25 |
| 62 | Group Three, Operation Crusader | 27 |
| 63 | Group Four, El Alamein: The Last Chance, The Long Retreat | 38 |
| 64 | Group Five, the campaign game | 18 |
| 65 | Designer's notes and bibliography | 1 |

Also in scope, as data:

- **Scenario set-ups**: every unit, truck, supply dump, air facility, plane
  and pilot a scenario lists, with its placement, per game module (Land, Air,
  Logistics) where the scenario lists them separately.
- **OA sheets**: the Commonwealth, Italian and German organisation charts
  (4.43, 4.45b, 4.45c in the chart sets): every counter, its formation, its
  parent, its ID code, its TOE and weapon systems, its arrival and its basic
  morale.
- **Unit characteristics** (4.46a/b/c) and **weapon systems** (4.47–4.49):
  the per-ID-code CPA and ratings, and the per-weapon ratings, that the
  Land Game rules name as "read from the OA sheet".
- **Reinforcement and withdrawal schedules** (4.43a, 4.43b).
- The per-unit figures `data/README.md` lists as expected from the OA
  sub-project (fuel rates, fuel capacities, coastal ship tonnage) where the
  scans print them.
- NJHarman's items on scenarios, seeded as rulings and variants; every new
  ruling decided.

**Out:**

- The Air Game rules (§33–47). Air set-ups are recorded as data, because
  they are facts of the scenario, but nothing here explains them; Mission 7
  does.
- Engine work. cna-engine reads these files; it does not live here.
- Scenarios of our own. §59 invites players to invent them; we don't.

## Decisions

| Topic | Decision | Why |
|---|---|---|
| File layout | A new folder `rules/scenarios/` and sidebar group "Scenarios": `00-reading-scenarios.md` (§59), `10-the-italians.md` (§60), `20-desert-fox.md` (§61), `30-crusader.md` (§62), `40-el-alamein.md` (§63), `50-campaign-game.md` (§64) | One file per scenario group, as SPI organises them; the folder follows `rules/logistics/`. |
| §65 | `spi-omit`ted from `50-campaign-game.md` with a reason (designer's notes and bibliography: commentary, no rules) | The coverage report must still account for it. |
| Prose versus data | The rules files state each scenario's length, special rules, initiative, construction state, abstractions and victory conditions in prose. Long listings (deployments, planes, trucks, supply, fleets) live **only** in `data/scenarios/<slug>.json`; the prose links to them and states the rules for reading them | A listing is a fact table; restating it as prose adds nothing and invites overlap with SPI's wording. |
| Scenario data | `data/scenarios/<slug>.json`, schema `scenario.schema.json`. One file per scenario; scenarios that share a set-up (Graziani / Italian Campaign) share it by `extends: "scenario:<slug>"` and override only what differs | An engine loads one file and gets one game. |
| Scenario shape | Top level: `id`, `group`, `start` and `end` (`{game_turn, opstage}`), `initiative`, `construction`, `victory`, `sides.{axis,cw}`. Each side has `deployments[]`, `trucks`, `supply`, `air`, `fleet`, `reinforcements` and `special`. A deployment is `{placement, units[], trucks}`. Module-specific content is keyed by the game it belongs to (`land`, `air`, `logistics`) and the abstraction cases (§60.9 etc.) are separate keys (`abstractions.land_only` and so on), each **replacing** a named block as SPI's text does | Mirrors §59.12's list (a–h), so the data can be checked against the printed headings; the abstraction blocks give an engine one switch per module, as Mission 5 did for §32. |
| Placement grammar | `{"hexes": [...]}`, `{"place": "<places.json id>"}`, `{"box": "tripoli"}`, `{"within": {"of": "<hex>", "hexes": n}}`, `{"region": "libya" \| "egypt" \| ...}`, `{"sheets": ["A","B"]}`, plus optional `not_within` and `stacking` notes. Anything the grammar cannot say goes in `constraint` as our own sentence and opens a ruling | Closed, serde-friendly variants; nothing an engine has to parse from prose. |
| Countries | "Anywhere in Libya / Egypt" needs the frontier. Task 1.1 adds it to the map data as region membership derived from the printed frontier, checked against the scan like any map correction | The map has no border today; it is a fact of the map, not of the scenario. |
| Unit references | Scenario units are `unit:<nation>:<slug>` ids that must exist in `data/oa/<nation>.json`; a listed parent stands for its whole OA sheet unless `less`, `assigned`, `detached`, `attached` or `consists_of` say otherwise (§59.2's indicators) | `check_data.py` can then prove every placed unit exists. |
| OA data | `data/oa/cw.json`, `data/oa/it.json`, `data/oa/de.json`, schema `oa.schema.json`: `formations[]` (one per OA sheet: name, basic morale, notes) each with `units[]` (id, name, abbreviation, ID code, parent, TOE and weapon systems, arrival, notes). Values as printed | The OA sheet is SPI's unit of organisation; the engine flattens it. |
| Characteristics | `data/tables/unit-characteristics.json` (per nation, per ID code) and `data/tables/weapon-systems.json` (tanks, guns, AA by nation) | They are charts; they follow the `data/tables/` rules. |
| Reinforcements | `data/tables/reinforcement-schedule.json`: rows `{side, game_turn, opstage, units[], trucks, notes}`, units as OA ids | Rows by OpStage, as printed. |
| Order of the OA | Part 1 transcribes only the OA sheets, characteristics rows and schedule rows Graziani's Offensive needs (its set-up, and arrivals through Game-Turn 6). The rest follows in Part 3 | Brian's order: one scenario complete before anything else. |
| Reading scans | Every value is read twice (two independent vision reads of the archive.org scan, or one of it and one of the Discord 300 dpi chart PDFs) and diffed; the cross-check count goes in `EXTRACTION.md` | The method behind the map and the 45 tables. |
| What the scans cannot settle | Stays as read, listed in the file's `notes`, and goes to the `copy` group of `docs/autopilot/decisions.json` for Brian's printed copy | Standing orders. |
| OCR slips in the source text | Hex numbers and names in the source text are OCR (e.g. `13714` for D3714, `BS526` for B5526). The data records the reading of the scan, never the OCR, and notes each correction in `EXTRACTION.md` | The scan is the authority. |
| Rulings | NJHarman's scenario items are seeded at the start (rulings for corrections and clarifications, variants for changes). Ambiguities found later open `proposed` rulings numbered on from R-093; every one is decided by the standing procedure | Same process as Missions 2–5. |

## Merge criteria

The rules-PR criteria of the living-rules design apply, with
`check_coverage.py --sections 59-65` over the files written so far. In
addition:

- **Data PRs:** the new schema validates every file; `check_data.py` proves
  every `unit:` id in a scenario or schedule exists in `data/oa/`, every hex
  exists in `data/map/hexes.json`, every `place` exists in
  `data/map/places.json`, and every `sources` case exists.
- **Scenario PRs:** a test loads the scenario and checks it against the
  printed totals where SPI prints them (truck points, supply points, plane
  counts), and that every listed hex of §59.12 (a–h) has a block in the file.
- **Cross-check:** every transcribed value was read twice; disagreements are
  either resolved from the scan or listed in `notes` and in `decisions.json`.

## Order

1. **Graziani's Offensive, complete** (several PRs, all merged before step 2):
   tooling and schemas, the frontier, the characteristics and weapon tables,
   the OA sheets its units need, the schedule through Game-Turn 6, the
   scenario file (with the Italian Campaign as an `extends`), and
   `rules/scenarios/00-reading-scenarios.md` and `10-the-italians.md`.
   Tell cna-engine it can start: a line in this repo's `PROGRESS.md`.
2. Seed NJHarman's scenario items.
3. The remaining rules files (§61–64), one PR each with its scenario files,
   each preceded by the OA sheets and schedule rows it needs; then the rest
   of the OA sheets and schedules, so that the campaign game (§64) can load.
4. Decide every new ruling, one PR each.
5. Docs: README, overview links, this Status line, the queue in
   `AUTOPILOT.md`.
