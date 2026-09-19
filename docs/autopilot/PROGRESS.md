# Autopilot progress

Human-facing journal for the unattended runs (see `AUTOPILOT.md`). The
autopilot rewrites **Status** and **Next steps** at the end of every run and
the cron script appends to **Runs and quota**. The only section a human
writes is **Feedback**.

## Feedback

Write anything here: corrections, priorities, "stop doing X", questions.
The next run reads this section first, acts on it, and moves each item to
*Addressed* with a one-line reply. Leave the list empty when there's nothing.

- 2026-09-19 (Brian): **New orders — mission 2** in `AUTOPILOT.md` (Parts A, B, C, D, in that order). The `MISSION COMPLETE` below is mission 1; ignore it. Policy for Part B is in `ATTRIBUTION.md` and `rulings/README.md`; I have contacted NJHarman and quoting under CC-BY-SA proceeds without waiting for a reply.

## Addressed

- (none yet)

## Status

Mission 1 (rules files 1–10 and site phase 2): all merged, PRs #2–#13.

| Part | What | State | PR |
|---|---|---|---|
| A | close the 30-case Land Game coverage gap (§1, §2, §4, 17.2) | not started | — |
| B | seed rulings from NJHarman (CORRECTION / CLARIFICATION / INTERPRETATION, Land Game topics) | not started | — |
| C | chart sheet tables into `data/tables/`, cross-checked against Clay Stone | not started | — |
| D | publish the primer (Parts A–C) as the site's *Learn* page; Part D of the primer waits for the map | not started | — |

## Next steps

Start Part A (`autopilot/a-coverage-gap`). See `AUTOPILOT.md` for the full orders.

Still for Brian: click one *Original text* block on the deployed site to confirm the viewer works in a browser.

## Runs and quota

Weekly and 5-hour figures are plan utilisation (%) as reported by the usage endpoint, sampled just before and just after the run. Cost is the list-price equivalent the CLI reports.

| Started (Phoenix) | Minutes | Weekly before→after | 5h before→after | Cost | Turns | Result |
|---|---|---|---|---|---|---|
| 2026-09-18 21:15 | 2 | 51→51 | 25→26 | $0.81 | 12 | smoke test; opened #2 |
| 2026-09-18 21:29 | 8 | 52→53 | 28→33 | $3.52 | 49 | §6.2 + §17 restated, R-001, #2 marked ready; CI overlap gate red on R-001 |
| 2026-09-18 21:39 | 11 | 52→53 | 30→35 | $4.60 | 63 | opened #3–#6 (sequence, CP, movement, stacking) as a stacked chain; ran on stale orders, did not merge |
| 2026-09-18 21:51 | 10 | 52→53 | 32→33 | $2.16 | 44 | Run complete with ~4 min to spare; everything is committed and pushed, working tree clean. **Landed this run** - Fixed red CI on #2 (cherry-picked the R-001 rew |
| 2026-09-19 03:23 | 32 | 54→55 | 5→9 | $16.33 | 118 | **MISSION COMPLETE** — steps 3 and 4 are done and on `main`; the Pages deploy is green. This run merged six PRs, each after local gates and green CI: / PR / Fil |
| 2026-09-19 06:23 | 0 | 55→55 | 0→0 | $0.28 | 3 | Nothing to do this run. `MISSION COMPLETE` is already logged in the journal and PROGRESS.md (steps 3 and 4 done, all 11 PRs merged), the **Feedback** section is |
