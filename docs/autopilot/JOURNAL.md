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

## 2026-09-19 03:26 (Phoenix) — autopilot/60-combat
Done: §11–§14 restated in rules/60-combat.md (incl. §32 addenda 14.15, 14.27 and the 12.0/12.23/12.46/14.0 clarifications); coverage 11–14 = 109/109; overlap OK.
In flight: §15 close assault (6 841 words) and §16 patrols not started. Anchors promised in the file: #gun-losses, #forced-retreats, #dummy-tank-formations — must exist when §15/§16 land. Sidebar entry, EXTRACTION entry not written. Barrage (12.6) and anti-armour (14.6) CRTs spi-omit pending chart sheet.
Next: read section-15.adoc, restate; then §16; sidebar; EXTRACTION; gates; gh pr ready; merge.
Blocked: chart sheet (CRTs) — Brian.

## 2026-09-19 03:33 (Phoenix) — autopilot/60-combat
Done: rules/60-combat.md complete (§11–§16 + §32 addenda + errata E-001–E-010); data/tables/assault-size-shifts.json; data/errata/INDEX.md (E-id registry); spi-badge.mjs renders ::: errata / ::: ruling (tests); sidebar; EXTRACTION; 50-stacking links #forced-retreats. Coverage 11–16 209/209, all gates + CI green. PR #8 ready and merged this run.
In flight: none.
Next: file 7 = organisation (check section list — likely SPI §19 attach/detach, §20 replacements?, §21 repair? read 00-overview file map first). Branch autopilot/70-organisation from origin/main, --base main. Sidebar regex already lists 70-organisation.
Blocked: chart sheet capture for all CRTs (12.6, 14.6, 15.79, 15.89, 16.6–16.8) plus earlier tables — Brian.

## 2026-09-19 03:35 (Phoenix) — autopilot/70-organisation
Done: branch from origin/main (5b1d8d0); draft PR opened. Nothing written.
In flight: rules/70-organisation.md — SPI §19 organisation/reorganisation (3 770 words), §20 reinforcements/replacements/CW withdrawals (2 743). §18 reserve already lives in 50-stacking-and-zoc; §17.3 training in 10-units-and-state.
Next: read section-19/20.adoc; write in the 60-combat style (errata badges via data/errata/INDEX.md, next id E-011); sidebar; EXTRACTION; gates; gh pr ready; merge.
Blocked: chart sheet — Brian.

## 2026-09-19 03:37 (Phoenix) — autopilot/70-organisation
Done: rules/70-organisation.md complete (§19–§20, §32 addenda, errata E-011–E-016); data/tables/replacement-training.json + schema; sidebar; EXTRACTION. Coverage 19–20 111/111; all gates green locally. PR #9 ready; merging this run if CI green.
In flight: none.
Next: file 8 = engineering (SPI §22–§26: check word counts — 22: 1 900, 23: 409, 24: 2 746, 25: 360, 26: 616). Branch autopilot/80-engineering from origin/main. Next errata id E-017. §21 (breakdown/repair) is mapped to movement/special per 00-overview — confirm before writing.
Blocked: chart sheet — Brian.

## 2026-09-19 03:38 (Phoenix) — autopilot/80-engineering
Done: branch from origin/main (1efe45b); draft PR opened. Nothing written.
In flight: rules/80-engineering.md — SPI §22–§26 (engineers, construction, fortifications, minefields, repair). §21 breakdown/repair: 00-overview maps it to Movement, 40-movement points breakdown at Special; decide and note in EXTRACTION.
Next: read section-22..26.adoc; write; sidebar; EXTRACTION; gates; ready; merge. Next errata id E-017.
Blocked: chart sheet — Brian.

## 2026-09-19 03:41 (Phoenix) — autopilot/80-engineering
Done: rules/80-engineering.md complete (§22–§26, §32 additions 23.15/24.79, errata E-017–E-022); sidebar; EXTRACTION. Coverage 22–26 147/147; gates green locally. PR #10 ready; merging this run if CI green.
In flight: none.
Next: file 9 = special (SPI §27–§31 raiders, prisoners, weather, fleet, Rommel; plus §21 breakdown — 40-movement points breakdown at 90-special, 00-overview maps §21 to movement; put §21 in special and say so). Branch autopilot/90-special from origin/main. Next errata id E-023 (errata for 21.12 exists: Italian M13/40 BAR).
Blocked: chart sheet — Brian.
