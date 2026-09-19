# Autopilot progress

Human-facing journal for the unattended runs (see `AUTOPILOT.md`). The
autopilot rewrites **Status** and **Next steps** at the end of every run and
the cron script appends to **Runs and quota**. The only section a human
writes is **Feedback**.

## Feedback

Write anything here: corrections, priorities, "stop doing X", questions.
The next run reads this section first, acts on it, and moves each item to
*Addressed* with a one-line reply. Leave the list empty when there's nothing.

- (none)

## Addressed

- (none yet)

## Status

| # | File | State | PR |
|---|---|---|---|
| 1 | units & state | **merged** | #2 |
| 2 | sequence of play | **merged** | #7 (was #3; auto-closed when its stacked base branch was deleted) |
| 3 | capability points | **merged** | #4 |
| 4 | movement | **merged** | #5 |
| 5 | stacking & ZOC | **merged** | #6 |
| 6 | combat | **merged** | #8 |
| 7 | organisation | in progress | #9 (draft) |
| 8 | engineering | not started | |
| 9 | special | not started | |
| 10 | §32 | not started | |
| — | site phase 2 | not started | |

## Next steps

- File 6, combat (`rules/60-combat.md`, SPI §11–§16) merged in the 03:23 run, with the Sept 1979 errata for those sections applied (E-001–E-010, indexed in `data/errata/INDEX.md`) and the site now rendering `::: errata` / `::: ruling` badges.
- File 7, organisation: branch `autopilot/70-organisation`, draft PR #9; being written in the same run.
- Pending data tables that need the chart sheet scanned (not in `~/.cache/cna-scans`): Terrain Effects Chart (8.37, incl. stacking ceilings), Off-Map Distance Chart (8.89), initiative ratings, unit basic stacking point values (9.4), and now all combat tables — Barrage Results (12.6), Anti-Armour CRT (14.6), Close Assault CRT (15.79, errata E-008 waiting on it), Prisoners Captured (15.89), Patrol Survival / Reconnaissance / Objective Loss (16.6–16.8). **Brian:** can you capture the chart sheet, or extend `tools/fetch.py` to get it?
- Convention decision this run (revisit if you disagree): prose-only errata are annotated inline with `::: errata E-nnn — paraphrase` and listed in `data/errata/INDEX.md`; only table-changing items also get an `E-nnn.json` overlay.

## Runs and quota

Weekly and 5-hour figures are plan utilisation (%) as reported by the usage endpoint, sampled just before and just after the run. Cost is the list-price equivalent the CLI reports.

| Started (Phoenix) | Minutes | Weekly before→after | 5h before→after | Cost | Turns | Result |
|---|---|---|---|---|---|---|
| 2026-09-18 21:15 | 2 | 51→51 | 25→26 | $0.81 | 12 | smoke test; opened #2 |
| 2026-09-18 21:29 | 8 | 52→53 | 28→33 | $3.52 | 49 | §6.2 + §17 restated, R-001, #2 marked ready; CI overlap gate red on R-001 |
| 2026-09-18 21:39 | 11 | 52→53 | 30→35 | $4.60 | 63 | opened #3–#6 (sequence, CP, movement, stacking) as a stacked chain; ran on stale orders, did not merge |
| 2026-09-18 21:51 | 10 | 52→53 | 32→33 | $2.16 | 44 | Run complete with ~4 min to spare; everything is committed and pushed, working tree clean. **Landed this run** - Fixed red CI on #2 (cherry-picked the R-001 rew |
