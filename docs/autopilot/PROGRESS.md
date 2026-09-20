# Autopilot progress

Human-facing journal for the unattended runs (see `AUTOPILOT.md`). The
autopilot rewrites **Status** and **Next steps** at the end of every run and
the cron script appends to **Runs and quota**. The only section a human
writes is **Feedback**.

## Feedback

Write anything here: corrections, priorities, "stop doing X", questions.
The next run reads this section first, acts on it, and moves each item to
*Addressed* with a one-line reply. Leave the list empty when there's nothing.


## Addressed

- 2026-09-19 (Brian) mission 2 orders → acted on 2026-09-20: Part A merged (#17), Part B merged (#18, #20–#26: R-002–R-019 plus the generated `rulings/register.md`); Part C combat CRTs merged (#27, #28). Quoting policy followed as written; three quotes elide NJHarman's own quotation of a printed SPI sentence (noted in each footnote) because the overlap gate flags them.

## Status

Mission 1 (rules files 1–10 and site phase 2): all merged, PRs #2–#13.

| Part | What | State | PR |
|---|---|---|---|
| A | close the 30-case Land Game coverage gap (§1, §2, §4, 17.2) | **merged** — §1–32 coverage 974/974 | #17 |
| B | seed rulings from NJHarman (CORRECTION / CLARIFICATION / INTERPRETATION, Land Game topics) | **merged** — R-002–R-019 (18 proposed rulings, one PR per topic), `rulings/register.md` generated, 5 items recorded as not imported in `EXTRACTION.md` | #18, #20–#26 |
| C | chart sheet tables into `data/tables/`, cross-checked | nearly done — 32 tables captured (this run added 13: 8.37 **Terrain Effects** + E-031, 8.89, 24.17, 24.18, 27.91, 27.92, 30.46, 30.6, 20.66 + E-014 overlay, 20.78 A/B/C, 32.46/32.47, 32.59, 32.66). Left: 19.31–19.33 Formation Organisation Charts (symbol grids, jp2 134 / 173 / 174) and 20.67 Type Limitations Chart (not located) | #27–#54 |
| D | publish the primer (Parts A–C) as the site's *Learn* page; Part D of the primer waits for the map | not started | — |

## Next steps

Part C: the three Formation Organisation Charts (19.31 Commonwealth jp2 134, 19.32 Italian jp2 173, 19.33 German jp2 174) are grids of unit symbols — capturable but need a careful legend read; then 20.67 if it turns up (search the Axis chart set pages jp2 150–178). Then Part D.

**Found this run:** the Terrain Effects Chart (8.37) and the 8.89 distance chart are *rulebook* pages (jp2 69–70), not chart-sheet pages — that is why no chart-sheet search found them. The TEC is in with the SPI errata applied as overlay E-031 (footnote 4 → Major City; a track halves the hex cost rather than costing 1 CP). Cross-check for those two was the Discord OCR-converted rulebook scan (an independent scan); Clay Stone's PDF prints "see Charts and Tables" plus the errata text in place of the chart.

**Chart vs rules-text disagreements** (kept as printed in the data, noted in the rules pointer paragraphs and `EXTRACTION.md`; candidates for rulings, none opened):
- 24.17 Construction Chart: temporary repair facility **50 fuel + 250 stores in 1 stage** vs 24.82's 150 fuel + 250 stores over 3 stages; facility rebuild **10 fuel + 50 stores** vs 24.84's 30 fuel + 50 stores; real dump 10 stores vs 20 (already R-018).
- 27.91 Desert Raider Raids: a guarded dump is raided if the two-dice total is **≥** the guards' raw close-assault defence (chart) vs **>** (27.5x text).

**E-025 reading, please check:** the errata says the Weather Table is "completely backwards". Applied as: each season's game-turn bands swap with the opposite season's (turns 1–12 → autumn, matching the September 1940 start); weather dice ranges stay with their season names. One overlay file (`data/errata/E-025.json`) to change if you read it differently.

**Cross-check sources, please note:** Clay Stone's PDFs at friendorfoe.com/d/CfNA/ are the *rules* only — no chart sheet. Chart-sheet tables were cross-checked cell by cell against the Discord 300 dpi *Shared / Axis / Commonwealth Charts.pdf*; the two rulebook-page charts against the Discord converted rulebook scan. Every table this run: 0 cells differ. If you want a different second source, say so in Feedback.

**Three printed oddities** (both scans agree, none in the 1979 errata), kept as printed and declared in `known_gaps` / notes: close assault CRT attacker −2 / 20 % reads "13-18" (17–18 are not readings, so 13–16); close assault defender +2 has no cell for readings 34–36; Morale Modifier level −4 has no cell for reading 56. They want rulings.

For Brian, if you have a minute: R-012 (15.29 withhold-and-retreat) and R-018 (dump cost) are the two seeded rulings where the printed text and the sensible reading pull apart; R-019 needs a hex count on the map (Alexandria → row xx24 vs xx29).

Still for Brian: click one *Original text* block on the deployed site to confirm the viewer works in a browser.

## Runs and quota

Weekly and 5-hour figures are plan utilisation (%) as reported by the usage endpoint, sampled just before and just after the run. Cost is the list-price equivalent the CLI reports.

| Started | Minutes | Weekly before→after | 5h before→after | Cost | Turns | Result |
|---|---|---|---|---|---|---|
| 2026-09-18 21:15 | 2 | 51→51 | 25→26 | $0.81 | 12 | smoke test; opened #2 |
| 2026-09-18 21:29 | 8 | 52→53 | 28→33 | $3.52 | 49 | §6.2 + §17 restated, R-001, #2 marked ready; CI overlap gate red on R-001 |
| 2026-09-18 21:39 | 11 | 52→53 | 30→35 | $4.60 | 63 | opened #3–#6 (sequence, CP, movement, stacking) as a stacked chain; ran on stale orders, did not merge |
| 2026-09-18 21:51 | 10 | 52→53 | 32→33 | $2.16 | 44 | Run complete with ~4 min to spare; everything is committed and pushed, working tree clean. **Landed this run** - Fixed red CI on #2 (cherry-picked the R-001 rew |
| 2026-09-19 03:23 | 32 | 54→55 | 5→9 | $16.33 | 118 | **MISSION COMPLETE** — steps 3 and 4 are done and on `main`; the Pages deploy is green. This run merged six PRs, each after local gates and green CI: / PR / Fil |
| 2026-09-19 06:23 | 0 | 55→55 | 0→0 | $0.28 | 3 | Nothing to do this run. `MISSION COMPLETE` is already logged in the journal and PROGRESS.md (steps 3 and 4 done, all 11 PRs merged), the **Feedback** section is |
| 2026-09-19 18:23 | 67 | 61→62 | 16→26 | $53.39 | 314 | Run complete with ~22 minutes to spare; everything is merged and pushed, tree clean, no open autopilot PRs. **Landed this run (PRs #17–#42, all merged after gre |
