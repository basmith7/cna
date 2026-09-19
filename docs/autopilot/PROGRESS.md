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
| 6 | combat | draft, not yet written | #8 |
| 7 | organisation | not started | |
| 8 | engineering | not started | |
| 9 | special | not started | |
| 10 | §32 | not started | |
| — | site phase 2 | not started | |

## Next steps

- File 6, combat (`rules/60-combat.md`): branch `autopilot/60-combat` and draft PR #8 opened; nothing written yet. Source is ~14 800 words across SPI §11–§16, so expect two or three runs.
- Pending data tables that need the chart sheet scanned (not in `~/.cache/cna-scans`): Terrain Effects Chart (8.37, incl. stacking ceilings), Off-Map Distance Chart (8.89), initiative ratings, unit basic stacking point values (9.4, counter sheet). **Brian:** can you capture the chart sheet, or extend `tools/fetch.py` to get it?
- Lesson from this run: earlier runs stacked PRs on each other's branches; deleting a merged base auto-closed the next PR. All PRs now target `main`.

## Runs and quota

Weekly and 5-hour figures are plan utilisation (%) as reported by the usage endpoint, sampled just before and just after the run. Cost is the list-price equivalent the CLI reports.

| Started (UTC) | Minutes | Weekly before→after | 5h before→after | Cost | Turns | Result |
|---|---|---|---|---|---|---|
| 2026-09-19 04:15 | 2 | 51→51 | 25→26 | $0.81 | 12 | smoke test; opened #2 |
| 2026-09-19 04:29 | 8 | 52→53 | 28→33 | $3.52 | 49 | §6.2 + §17 restated, R-001, #2 marked ready; CI overlap gate red on R-001 |
| 2026-09-19 04:39 | 11 | 52→53 | 30→35 | $4.60 | 63 | opened #3–#6 (sequence, CP, movement, stacking) as a stacked chain; ran on stale orders, did not merge |
| 2026-09-19 04:51 | 10 | 52→53 | 32→33 | $2.16 | 44 | Run complete with ~4 min to spare; everything is committed and pushed, working tree clean. **Landed this run** - Fixed red CI on #2 (cherry-picked the R-001 rew |
