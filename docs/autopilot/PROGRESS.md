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
| 1 | units & state | ready for review | #2 |
| 2 | sequence of play | not started | |
| 3 | capability points | not started | |
| 4 | movement | not started | |
| 5 | stacking & ZOC | not started | |
| 6 | combat | not started | |
| 7 | organisation | not started | |
| 8 | engineering | not started | |
| 9 | special | not started | |
| 10 | §32 | not started | |
| — | site phase 2 | not started | |

## Next steps

- Review/merge #2 (units & state) — all gates pass, ruling R-001 opened.
- Then start file 2, sequence of play (SPI §5, §7): branch `autopilot/20-sequence-of-play`.

## Runs and quota

Weekly and 5-hour figures are plan utilisation (%) as reported by the usage endpoint, sampled just before and just after the run. Cost is the list-price equivalent the CLI reports.

| Started (UTC) | Minutes | Weekly before→after | 5h before→after | Cost | Turns | Result |
|---|---|---|---|---|---|---|
| 2026-09-19 04:15 | 2 | 51→51 | 25→26 | $0.81 | 12 | smoke test; opened #2 |
| 2026-09-19 04:29 | 8 | 52→53 | 28→33 | $3.52 | 49 | §6.2 + §17 restated, R-001, #2 marked ready; CI overlap gate red on R-001 |
