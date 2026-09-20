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
| C | chart sheet tables into `data/tables/`, cross-checked | in progress — the three combat CRTs (12.6, 14.6, 15.79) merged with E-008 applied; other sheets next | #27, #28 |
| D | publish the primer (Parts A–C) as the site's *Learn* page; Part D of the primer waits for the map | not started | — |

## Next steps

Part C continues, one PR per rules file: locate each remaining chart-sheet table in the archive.org scan (djvu XML search → `chart_pages`), transcribe, cross-check, badge. Then Part D.

**Cross-check source, please note:** Clay Stone's PDFs at friendorfoe.com/d/CfNA/ are the *rules* only — they contain no chart sheet ("See Charts and Tables"). The three CRTs were cross-checked cell by cell against the Discord 300 dpi *Shared Charts.pdf* instead (0 cells differ in all three). If you want a different second source, say so in Feedback.

**Two printed oddities in the close assault CRT** (both scans agree, neither in the 1979 errata): attacker −2 / 20 % reads "13-18" (17–18 are not readings, so 13–16); defender +2 has no cell for readings 34–36. Both are kept as printed and declared in the data file; they want rulings.

For Brian, if you have a minute: R-012 (15.29 withhold-and-retreat) and R-018 (dump cost, 24.9 vs the Construction Chart) are the two seeded rulings where the printed text and the sensible reading pull apart; R-019 needs a hex count on the map (Alexandria → row xx24 vs xx29).

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
