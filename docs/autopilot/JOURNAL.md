# Autopilot journal

One entry per run, newest last. For the next run, not for humans.

## 2026-09-19T04:15Z — autopilot/10-units-and-state
Done: branch created from origin/main; journal started.
In flight: rules/10-units-and-state.md (SPI §3, §6.2, §17) — not yet written.
Next: create .venv (README), fetch sections, read §3/§6.2/§17 from ~/.cache/cna-scans, write the file, run gates, draft PR.
Blocked: none

## 2026-09-19T04:17Z — autopilot/10-units-and-state
Done: PR #2 (draft). rules/10-units-and-state.md first draft covering SPI §3 only (types, classes, HQ 3.3x, characteristics 3.5, parenthesised ratings, type notes). .venv + section cache set up (not committed). Overlap gate passes after wording fixes.
In flight: §6.2 (CPA ratings, raw→actual, <5 raw rule) and §17 (cohesion/DP/RP) not yet restated; no data/ tables yet; no EXTRACTION.md entry; coverage not checked; spi-omit for 3.1 glossary and colour cases not yet added.
Next: read section-06.adoc (§6.2x) and section-17.adoc from ~/.cache/cna-scans/source/<commit>/, add "Capability point ratings" and "Cohesion" sections, badge 3.1 as spi-omit (glossary), run check_coverage --sections 3,6,17, add EXTRACTION entry, sidebar entry in site/, then gh pr ready.
Blocked: none

## 2026-09-19T04:42Z — autopilot/10-units-and-state
Done: finished the file. §6.2 (Cohesion) + §17 (Morale/Training/Voluntary surrender) restated; §3 omit-badges added; ruling R-001 (−26 threshold); sidebar entry; ignoreDeadLinks for future rules files; EXTRACTION entry. All gates pass (pytest 60, check_data, check_overlap, site:build). Committed + pushed; marking PR #2 ready.
In flight: none for file 1.
Next: file 2 = sequence of play (SPI §5, §7). Branch autopilot/20-sequence-of-play from origin/main once #2 merges (or stack on #2's tip if still open; --base autopilot/10-units-and-state). Coverage for §6.1/6.3 stays open — it belongs to file 3 (capability points, §6).
Blocked: none (Brian merges #2).

## 2026-09-19T04:41Z — autopilot/20-sequence-of-play
Done: branch created from tip of autopilot/10-units-and-state (stacked; PR #2 still open, no review comments).
In flight: rules/20-sequence-of-play.md (SPI §5, §7) — not yet written.
Next: read section-05/07 from ~/.cache/cna-scans/source/<commit>/, write the file matching 10-units-and-state.md conventions, sidebar entry, EXTRACTION entry, gates, draft PR --base autopilot/10-units-and-state.
Blocked: none

## 2026-09-19T04:42Z — autopilot/20-sequence-of-play
Done: rules/20-sequence-of-play.md complete (§5 + §7), sidebar, EXTRACTION entry; coverage 12/12, overlap OK, pytest 60, site builds. PR #3 marked ready (stacked on #2). Also fixed an overlap-gate hit in rulings/R-001.md on the #2 branch (pushed) — rulings/ is now scanned.
In flight: none for file 2.
Next: file 3 = capability points (SPI §6.1, §6.3 — §6.2 already in file 1). Branch autopilot/30-capability-points from tip of autopilot/20-sequence-of-play, --base autopilot/20-sequence-of-play while #3 is open.
Blocked: none (Brian merges #2, #3). Initiative Ratings Chart (7.2) needs the chart sheet captured before data/ transcription.

## 2026-09-19T04:43Z — autopilot/30-capability-points
Done: rules/30-capability-points.md prose complete (§6.1, §6.3 table inline), sidebar, EXTRACTION entry; overlap OK, coverage §6 20/20, pytest 60, site builds. PR #4 (draft, --base autopilot/20-sequence-of-play).
In flight: data/tables/cp-costs.json + data/schema/cp-costs.schema.json not written (design says tables go to data/ with the file that first needs them). check_data.py may need a loader for tables/ — check with a failing test first (TDD).
Next: write schema+table for CP costs (sources CNA1979:6.3, scan page from fetch.py), point the file's table at it, run check_data, then gh pr ready 4. Then file 4 = movement (§8) stacked on this branch.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:45Z — autopilot/30-capability-points
Done: data/tables/cp-costs.json + data/schema/cp-costs.schema.json (c90c89b); all gates pass; PR #4 marked ready (stacked on #3). Note: check_overlap scans only git-tracked files — run it after `git add`, not before.
In flight: none for file 3.
Next: file 4 = movement (SPI §8, plus Terrain Effects Chart → data/tables/terrain-effects.json; extend common.schema terrain enum). Branch autopilot/40-movement from tip of autopilot/30-capability-points, --base autopilot/30-capability-points while #4 is open.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:46Z — autopilot/40-movement
Done: branch from tip of autopilot/30-capability-points; rules/40-movement.md is a commented skeleton mapping SPI §8.1–8.9 to sections (no badges yet, so §8 coverage is 0 — expected).
In flight: file 4 (movement, §8, 658 source lines) — nothing restated yet.
Next: read section-08.adoc in full; restate 8.1–8.2 first (they are cited by 00-overview and 20-sequence-of-play), then 8.3 with the terrain-effects table + schema (extend common.schema terrain enum), then 8.4–8.9. Add sidebar entry, EXTRACTION entry. Remember: `git add` before check_overlap (it scans tracked files only). Open draft PR --base autopilot/30-capability-points.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:47Z — autopilot/40-movement
Done: §8.1–§8.8 restated in rules/40-movement.md (ba7936a + this commit); sidebar entry; overlap OK; site builds. PR #5 draft (--base autopilot/30-capability-points). Coverage §8: 69/80.
In flight: file 4. Remaining: 8.9 motorised/trucks (559–658; anchor #trucks is linked from 30-capability-points). Terrain Effects Chart: data/tables/terrain-effects.json + schema not started (chart sheet not in cache — check tools/fetch.py for chart pages; if unavailable, keep 8.37 spi-omit and say so in EXTRACTION). Remove the HTML skeleton comment at the top of the file when done. EXTRACTION entry not written.
Next: restate 8.9 (source lines 559–658), then EXTRACTION entry, then gates and gh pr ready 5.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:50Z — autopilot/40-movement
Done: rules/40-movement.md complete (§8.1–8.9), EXTRACTION entry, sidebar; coverage §8 80/80, overlap OK, pytest 60, check_data OK, site builds. PR #5 marked ready (stacked on #4). Terrain Effects Chart (8.37) + Off-Map Distance Chart (8.89) NOT transcribed — chart sheet not in ~/.cache/cna-scans (spi-omit, flagged in PR body).
In flight: none for file 4.
Next: file 5 = stacking & ZOC (SPI §9, §10, §18 reserve). Branch autopilot/50-stacking-and-zoc from tip of autopilot/40-movement, --base autopilot/40-movement while #5 is open. Anchors already linked from other files: #reserve, #roads. Check tools/fetch.py for a way to fetch the chart sheet pages for the pending data tables.
Blocked: chart sheet capture (Brian / fetch.py) for terrain-effects, off-map-distances, initiative-ratings tables.

## 2026-09-19T04:51Z — autopilot/50-stacking-and-zoc
Done: branch from tip of autopilot/40-movement; draft PR opened. Nothing written.
In flight: rules/50-stacking-and-zoc.md (SPI §9 stacking, §10 ZOC, §18 reserve) — not started. Must provide anchors #reserve and #roads (linked from 40-movement).
Next: read section-09/10/18.adoc, write the file in the 10/20/40 style, sidebar, EXTRACTION, gates (git add before check_overlap), gh pr ready.
Blocked: none new.

## 2026-09-19T04:58Z — autopilot/50-stacking-and-zoc
Done: merged #2 (16507d1, after cherry-picking R-001 fix 444f014), #7 (=#3 recreated against main after base-branch deletion auto-closed it; 9371b7b), #4, #5. Files 1–4 are on main. Retargeted #6 to main and merged origin/main into this branch.
In flight: rules/50-stacking-and-zoc.md still not started (this run spent its 15 min unwinding the PR stack).
Next: write rules/50-stacking-and-zoc.md (SPI §9, §10, §18) with anchors #reserve and #roads; sidebar; EXTRACTION; gates; gh pr ready; merge. Do NOT stack PRs on other PR branches again — always --base main.
Blocked: chart sheet capture (terrain-effects, off-map-distances, initiative-ratings tables) still needs Brian.

## 2026-09-19T05:01Z — autopilot/50-stacking-and-zoc
Done: rules/50-stacking-and-zoc.md complete (§9 5a2bb8b, §10 53bfefe, §18 + EXTRACTION b8f2848); sidebar; all gates green locally and in CI; PR #6 ready and being merged this run.
In flight: none.
Next: file 6 = combat (SPI §11–§16?, check section list). Branch autopilot/60-combat from origin/main, --base main. Sidebar regex already lists 60-combat.
Blocked: chart/counter sheet capture for 8.37 stacking ceilings, 9.4 SP table, terrain-effects, off-map-distances, initiative-ratings — Brian.

## 2026-09-19T05:03Z — autopilot/60-combat
Done: branch from origin/main (4b6662c); draft PR opened. Nothing written yet.
In flight: rules/60-combat.md — SPI §11 combat system, §12 anti-armour, §13 barrage, §14 retreat before assault, §15 close assault, §16 patrols/recon (~6 sections; check word count, may need two runs). Sidebar regex already includes 60-combat; add sidebar entry after 50.
Next: read section-11..16.adoc; write in the 40/50 style; CRT tables to data/ with schema; anchors other files reference: 50 links "combat (SPI 15.82)" for stand-and-take-losses, 10.31 probe; gates; EXTRACTION; gh pr ready; merge.
Blocked: none new.

## 2026-09-19 03:26 — autopilot/60-combat
Done: §11–§14 restated in rules/60-combat.md (incl. §32 addenda 14.15, 14.27 and the 12.0/12.23/12.46/14.0 clarifications); coverage 11–14 = 109/109; overlap OK.
In flight: §15 close assault (6 841 words) and §16 patrols not started. Anchors promised in the file: #gun-losses, #forced-retreats, #dummy-tank-formations — must exist when §15/§16 land. Sidebar entry, EXTRACTION entry not written. Barrage (12.6) and anti-armour (14.6) CRTs spi-omit pending chart sheet.
Next: read section-15.adoc, restate; then §16; sidebar; EXTRACTION; gates; gh pr ready; merge.
Blocked: chart sheet (CRTs) — Brian.

## 2026-09-19 03:33 — autopilot/60-combat
Done: rules/60-combat.md complete (§11–§16 + §32 addenda + errata E-001–E-010); data/tables/assault-size-shifts.json; data/errata/INDEX.md (E-id registry); spi-badge.mjs renders ::: errata / ::: ruling (tests); sidebar; EXTRACTION; 50-stacking links #forced-retreats. Coverage 11–16 209/209, all gates + CI green. PR #8 ready and merged this run.
In flight: none.
Next: file 7 = organisation (check section list — likely SPI §19 attach/detach, §20 replacements?, §21 repair? read 00-overview file map first). Branch autopilot/70-organisation from origin/main, --base main. Sidebar regex already lists 70-organisation.
Blocked: chart sheet capture for all CRTs (12.6, 14.6, 15.79, 15.89, 16.6–16.8) plus earlier tables — Brian.

## 2026-09-19 03:35 — autopilot/70-organisation
Done: branch from origin/main (5b1d8d0); draft PR opened. Nothing written.
In flight: rules/70-organisation.md — SPI §19 organisation/reorganisation (3 770 words), §20 reinforcements/replacements/CW withdrawals (2 743). §18 reserve already lives in 50-stacking-and-zoc; §17.3 training in 10-units-and-state.
Next: read section-19/20.adoc; write in the 60-combat style (errata badges via data/errata/INDEX.md, next id E-011); sidebar; EXTRACTION; gates; gh pr ready; merge.
Blocked: chart sheet — Brian.

## 2026-09-19 03:37 — autopilot/70-organisation
Done: rules/70-organisation.md complete (§19–§20, §32 addenda, errata E-011–E-016); data/tables/replacement-training.json + schema; sidebar; EXTRACTION. Coverage 19–20 111/111; all gates green locally. PR #9 ready; merging this run if CI green.
In flight: none.
Next: file 8 = engineering (SPI §22–§26: check word counts — 22: 1 900, 23: 409, 24: 2 746, 25: 360, 26: 616). Branch autopilot/80-engineering from origin/main. Next errata id E-017. §21 (breakdown/repair) is mapped to movement/special per 00-overview — confirm before writing.
Blocked: chart sheet — Brian.

## 2026-09-19 03:38 — autopilot/80-engineering
Done: branch from origin/main (1efe45b); draft PR opened. Nothing written.
In flight: rules/80-engineering.md — SPI §22–§26 (engineers, construction, fortifications, minefields, repair). §21 breakdown/repair: 00-overview maps it to Movement, 40-movement points breakdown at Special; decide and note in EXTRACTION.
Next: read section-22..26.adoc; write; sidebar; EXTRACTION; gates; ready; merge. Next errata id E-017.
Blocked: chart sheet — Brian.

## 2026-09-19 03:41 — autopilot/80-engineering
Done: rules/80-engineering.md complete (§22–§26, §32 additions 23.15/24.79, errata E-017–E-022); sidebar; EXTRACTION. Coverage 22–26 147/147; gates green locally. PR #10 ready; merging this run if CI green.
In flight: none.
Next: file 9 = special (SPI §27–§31 raiders, prisoners, weather, fleet, Rommel; plus §21 breakdown — 40-movement points breakdown at 90-special, 00-overview maps §21 to movement; put §21 in special and say so). Branch autopilot/90-special from origin/main. Next errata id E-023 (errata for 21.12 exists: Italian M13/40 BAR).
Blocked: chart sheet — Brian.

## 2026-09-19 03:43 — autopilot/90-special
Done: branch from origin/main; draft PR opened. Nothing written.
In flight: rules/90-special.md — SPI §21 (breakdown, 2 684 words), §27 raiders (3 062), §28 prisoners (896), §29 weather (820), §30 fleet (2 073), §31 Rommel (280).
Next: read sections; write; sidebar; EXTRACTION; gates; ready; merge. Next errata id E-023.
Blocked: chart sheet — Brian.

## 2026-09-19 03:47 — autopilot/90-special
Done: rules/90-special.md complete (§21, §27–§31, §32 addenda, errata E-023–E-030); data/tables/breakdown-adjustments.json + seasons.json with schemas; sidebar; EXTRACTION. Coverage 21,27–31 196/196; gates green locally. PR #11 ready; merging this run if CI green.
In flight: none. Note for a later tidy: 00-overview's file map lists §21 under Movement; it now lives in Special.
Next: file 10 = §32 abstract logistics and air (rules/95-abstract-logistics-and-air.md; sidebar regex already lists it; several other files link to it). Branch autopilot/95-abstract-logistics-and-air. Next errata id E-031. The §32 addenda block (lines ~470–620 of section-32.adoc) has already been folded into files 6–9 — badge only the 32.x cases there.
Blocked: chart sheet — Brian.

## 2026-09-19 03:48 — autopilot/95-abstract-logistics-and-air
Done: branch from origin/main; draft PR opened. Nothing written.
In flight: rules/95-abstract-logistics-and-air.md — SPI §32 (32.1–32.x rules only; the addenda block at the end is already folded into files 1–9 case by case). Also fix 00-overview file map (§21 → Special) in this PR.
Next: read section-32.adoc lines 1–470; write; sidebar; EXTRACTION; gates; ready; merge. Then step 4 (site phase 2) — read the design doc for what that means.
Blocked: chart sheet — Brian.

## 2026-09-19 03:49 — autopilot/95-abstract-logistics-and-air
Done: rules/95-abstract-logistics-and-air.md complete (§32 + 3.61–3.62); ::: note container in spi-badge.mjs (tests 11 pass); 00-overview file map fixed; 10-units 3.61/3.62 → spi-ref; sidebar; EXTRACTION. Coverage §32 61/61. PR #12 ready; merging this run if CI green. Step 3 of the design is then COMPLETE.
In flight: none.
Next: step 4 = site phase 2 — read docs/designs/2026-09-18-cna-living-rules-design.md for its definition (likely: "Changes from the original" page, coverage report page, client-side `original` blocks). Do it with TDD on site/ and tools/. Then log MISSION COMPLETE.
Blocked: chart sheet — Brian.

## 2026-09-19 03:53 — autopilot/site-phase-2
Done: tools/gen_pages.py (TDD, 5 tests) → rules/changes.md + rules/coverage.md (committed; test fails when stale); R-001 now a ::: ruling badge; original viewer: site/.vitepress/original.mjs (helpers, 4 tests), theme/OriginalViewer.vue (doc-after slot, DOM attach, fetch on open, remove on failure), themeConfig.original flag; data-cases attr on primary badges; sidebar "Provenance" group. All gates green locally. PR #13.
In flight: PR #13 to mark ready + merge. The Vue DOM attach is verified only by build + helper tests + a node fetch smoke test (no browser here) — say so in the PR body.
Next: after merge, log MISSION COMPLETE in journal and PROGRESS; stop.
Blocked: chart sheet — Brian.

## 2026-09-19 03:56 — main
Done: PR #13 (site phase 2) merged; main CI and Pages deploy green. Steps 3 and 4 complete.
In flight: none.
Next: nothing — orders say stop after step 4. Open items for Brian are listed in PROGRESS.md (chart sheet capture, NJHarman seed, browser check of the original viewer).
Blocked: none for the autopilot.

MISSION COMPLETE

## 2026-09-19 — main (Brian)
Done: mission 2 orders written to AUTOPILOT.md; ATTRIBUTION.md, README legal posture, rulings/README.md quoting convention; tools/sources.json gained djvu_xml_url and an empty chart_pages map.
In flight: none.
Next: Part A — autopilot/a-coverage-gap.
Blocked: none.

## 2026-09-19 18:27 — autopilot/a-coverage-gap
Done: Part A in one commit — omit blocks for §1, §2, §4 (incl. 4.4, missing from the orders' list) in 00-overview; 4.25 + 4.42 restated in 70-organisation, 4.26 in 50-stacking; 17.2 omitted; coverage.md regenerated; EXTRACTION entry. Coverage §1–32: 974/974. PR #17.
In flight: PR #17 marked ready; merge when CI green.
Next: Part B — fetch njharman.html to ~/.cache/cna-scans, read ATTRIBUTION.md + rulings/README.md, first topic PR (footnote plugin is already wired — package.json, config.mts, footnote.test.mjs exist from V-001).
Blocked: none.

## 2026-09-19 18:58 — autopilot/c-close-assault-crt
Done: Part A merged (#17). Part B merged: register page + R-002 (#18), R-003–R-005 (#20), R-006–R-008 (#21), R-009 (#22), R-010–R-013 (#23), R-014–R-015 (#24), R-016–R-018 (#25), R-019 (#26); seed complete, EXTRACTION table lists every item. Part C: 12.6 + 14.6 merged (#27); 15.79 + E-008 overlay in PR #28 (ready, CI pending at handoff).
In flight: PR #28 — merge if green. Clay Stone's PDFs have NO chart sheet; cross-checks used the Discord 300 dpi "Shared Charts.pdf" (cache) instead — say so in every EXTRACTION entry.
Next: Part C continues per rules file — Shared Charts.pdf contact sheet (pdftoppm -r 60) shows where each table is: p1 6.3 CP costs + 15.53 + 16.6; p2 7.2, 9.4, 12.6; p3 14.6, 15.89, 16.7, 16.8, 27.93; p4 15.79; p5 17.4 morale, 17.6 training, 40.8, 52.8; p6 19.5, 39.5, 29.61 weather; p7 21.38 breakdown, 22.15, 20.3; p8 22.44, 22.8, 27.91, 29.7; p9 24.17 construction; p10 24.18 demolition, 35.23, 38.31, 45.6; p11 40.4, 42.27, 41.39, 45.4, 45.5, 46.41, 49.19; p12 41.5; p13 46.3, 50.2, 58.5; p14 52.7, 54.12, 54.17, 54.2; p15 54.5, 55.3; p16 index. Terrain Effects Chart 8.37 is NOT in that PDF (it is on the map or the player-specific sheets) — search the djvu XML. Start with 90-special (21.38 breakdown, 29.6/29.7 weather + E-025) or 40-movement (8.37 via djvu XML).
Blocked: none. Lesson: never `--delete-branch` a merged PR while a stacked PR still targets it (GitHub auto-closes the stacked PR); retarget first.

## 2026-09-19 19:03 — autopilot/c-chart-pages
Done: #28 (15.79 + E-008) merged. This branch: weather.json + E-025 overlay (jp2 100), sources.json chart_pages for the whole shared sheet (jp2 95–110). PR #29.
In flight: PR #29 — merge if green. Then continue 90-special: 29.7 foul weather (jp2 102), 21.38 breakdown (jp2 101), 27.91/27.93 raids (jp2 102/97), 30.46 chariot (not on shared sheet — search djvu for "CHARIOT": jp2 40/41/43 are rules text; may be on a player sheet).
Next: fetch pages already cached (95, 99–104); Discord "Shared Charts.pdf" pages = jp2 − 94 (p1=95 … p16=110) for cross-checks; `pdftoppm -r 150 -f N -l N -png`. Each table: test first, then JSON + schema, then badge + EXTRACTION entry with "0 of N cells differ".
Blocked: Terrain Effects Chart (8.37) location — not on the shared sheet; not found in djvu titles. May be on the map or the CW/Axis chart sets (Discord Axis/Commonwealth Charts.pdf are in the cache — check their contact sheets).

## 2026-09-19 19:18 — main
Done: Part C this run — #27 (12.6, 14.6), #28 (15.79 + E-008 overlay), #29 (29.61 + E-025 overlay, chart_pages map), #30 (29.7, 21.38), #31 (15.89, 16.7, 16.8, 27.93), #32 (16.6), #33 (22.8, 22.44; E-017 prose-only), #34 (17.6), #35 (17.4). 15 tables, all cross-checked cell by cell against Discord "Shared Charts.pdf" (Clay Stone's PDFs have no charts). 91 tests.
In flight: none; working tree clean, all PRs merged.
Next: remaining pending-capture omits, in this order: 24.17 construction (jp2 103) + 24.18 demolition (jp2 104) for 80-engineering; 19.5 maximum attachment (jp2 100) + 20.3 replacement conversion (jp2 101) for 70-organisation (text-valued tables — design a shape first); 27.91 desert raider (jp2 102, per-target procedure list); then the player-sheet tables (19.3, 20.66, 20.78, 27.92, 30.46, 30.59) — check the Discord Axis/Commonwealth Charts.pdf contact sheets; 8.37 / 8.89 still unlocated. Then Part D.
Blocked: none. Reminders: run check_overlap on untracked files explicitly (`check_overlap.py rulings/ data/`) — the no-arg run only sees tracked files; Discord page = jp2 − 94; never --delete-branch under a stacked PR.

## 2026-09-19 19:23 — main
Done: after the 19:18 entry, four more PRs merged: #36 (cp-costs 6.3 cross-checked, 0 diffs), #37 (assault-size-shifts 15.53 cross-checked, missing 3 SP vs 2 SP = 0 row added), #38 (7.2 initiative ratings), #39 (9.4 stacking point values). 94 tests. Tree clean.
In flight: none.
Next: 24.17 construction (jp2 103) + 24.18 demolition (jp2 104) — text-valued rows (item / situation / unit required / stages / restrictions): design a schema with enums for unit-required and restate restrictions as our own short flags, never the chart's sentences. Then 19.5 max attachment (jp2 100), 20.3 replacement conversion (jp2 101), 27.91 desert raider (jp2 102). Then player-sheet tables; 8.37/8.89 still unlocated. Then Part D.
Blocked: none.

## 2026-09-19 19:26 — main
Done: #40 merged (20.3 replacement conversion + E-012 overlay). 18 chart tables captured this run; 96 tests; tree clean; no open autopilot PRs.
In flight: none.
Next: 19.5 maximum attachment (jp2 100, upper half; matrix of parent type × attachable type — check the crop first) and 24.17/24.18 construction & demolition (jp2 103/104; text-valued: item / unit required / stages / restrictions → enums + our own flags). Then 27.91 desert raider (jp2 102). Then player-sheet tables; 8.37/8.89 unlocated. Then Part D.
Blocked: none.

## 2026-09-19 19:28 — main
Done: #41 merged (19.5 max attachments). 19 chart tables captured this run, 97 tests, tree clean, no open autopilot PRs.
In flight: none.
Next: 24.17 construction (jp2 103) + 24.18 demolition (jp2 104, printed sideways — rotate +90, not -90) for 80-engineering; 27.91 desert raider (jp2 102); then player-sheet tables (19.3x, 20.66, 20.78, 27.92, 30.46, 30.59) via Discord Axis/Commonwealth Charts.pdf contact sheets; 8.37/8.89 unlocated. Then Part D.
Blocked: none.

## 2026-09-19 19:30 — main
Done: #42 merged — R-018 rewritten with the real 24.17 / 6.3 figures (dummy dump 2 CP on both charts vs 3 CP in 24.9; stores 10 vs 20). Final state: PRs #17–#42 all merged, 97 tests, tree clean.
In flight: none.
Next: 24.17 construction chart (jp2 103, sideways; restrictions column is prose — model as enums/flags, never the chart's sentences) + 24.18 demolition (jp2 104). Then 27.91, player-sheet tables, 8.37/8.89 search. Then Part D.
Blocked: none.

## 2026-09-19 21:27 — autopilot/c-construction-demolition
Done: branch opened; jp2 103 (construction, sideways: rotate -90) and 104 (demolition, upright) read and matched against Discord Shared Charts p9/p10.
In flight: construction.json + demolition.json with schemas and tests; badge 24.17/24.18 in 80-engineering; EXTRACTION entry.
Next: finish this PR, then 27.91 desert raider (jp2 102), then player-sheet tables.
Blocked: none. Note: chart says temporary repair facility 50 fuel + 250 stores / 1 stage, rebuild 10 fuel + 50 stores; rules prose (24.8x) says 150 fuel + 250 stores / 3 stages and 30 fuel + 50 stores — record as a chart-vs-rules discrepancy for Brian.

## 2026-09-19 21:51 — main
Done: 12 PRs merged this run, all after green CI: #43 (24.17 + 24.18), #44 (27.91), #45 (8.37 TEC + E-031 — a RULEBOOK page, jp2 69), #46 (27.92, jp2 140), #47 (20.78 A/B/C, jp2 140), #48 (20.66 + E-014 overlay, jp2 175), #49 (30.46, jp2 176), #50 (30.6 fleet schedule, jp2 141), #51 (32.46/32.47), #52 (32.66, jp2 176), #53 (8.89, jp2 70), #54 (32.59, jp2 107, headed 58.5). 32 tables, 116 tests, tree clean, no open autopilot PRs.
In flight: none.
Next: Part C's last items — 19.31/19.32/19.33 Formation Organisation Charts (jp2 134 / 173 / 174; symbol grids: read the counter-symbol legend first, model rows as parent → list of {count, type, size, turns}); 20.67 unlocated (scan Axis set jp2 150–178 contact sheet). Then Part D (learn_page.py --site).
Blocked: none. Lessons: run `check_overlap.py` with NO args too (CI's run) — EXTRACTION.md phrasing tripped it once; when stacking PRs, `gh pr edit N --base main` after the base merges, never --delete-branch; jp2 103 needs rotate(-90), 104 and 107 are as printed / +90 respectively — just view the raw page first.

## 2026-09-19 21:57 — autopilot/c-formation-cw
Done: branch opened for 19.31 (Commonwealth Formation Organisation Chart, jp2 134 / Discord CW p24 at 220 dpi — legend on the lower half of the page).
In flight: formation-organisation.json (rows = parent formation × organisation type × turns → components with count / unit slug / alternatives; a missing printed count is stored as count 1 with count_printed false).
Next: if this lands, add 19.32 (jp2 173) and 19.33 (jp2 174) rows to the same file, then badge 19.3 19.31 19.32 19.33 together.
Blocked: none.

## 2026-09-19 22:00 — autopilot/d-table-renderer
Done: Part C complete bar 20.67 (not printed on either player chart set — djvu headings for jp2 111–178 checked). Starting Part D with the smallest TDD piece: tools/learn_tables.py, a JSON→HTML renderer for the CRTs (errata overlays applied, spi-ref badge), not yet wired into learn_page.py.
In flight: renderer for barrage (12.6) and anti-armour (14.6); close-assault (15.79, nested losses/sums) next.
Next: finish close-assault rendering; then learn_page.py --site writing site/learn.md (Parts A–C, SVGs inline, CSS scoped under .learn, case numbers → rule links via data/spi-cases.json + check_coverage badge index), stale-check pytest, nav + sidebar, README/00-overview edits.
Blocked: none.

## 2026-09-19 22:05 — main
Done: after the 21:51 entry, #55 (19.31–19.33 formation charts, 37 rows), #56 (learn_tables.py renderer, TDD), #57 (learn_page.py --site → site/learn.md at /learn, nav + sidebar, case links, scoped CSS, README/00-overview) all merged after green CI. 33 tables, 129 tests, tree clean, no open autopilot PRs. 20.67 is not printed anywhere in the scan (djvu headings jp2 111–178 checked) — left to Brian.
In flight: none.
Next: nothing — Parts A–D are merged. If Brian answers on 20.67 or the Learn page's dark-mode styling in Feedback, act on that.
Blocked: none.

MISSION 2 COMPLETE
