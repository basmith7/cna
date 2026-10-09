---
id: T-1
title: Show CNA autopilot progress on agent-board
status: todo
priority: medium
labels: []
depends: []
created: 2026-10-04T04:25:55Z
updated: 2026-10-04T04:47:46Z
kind: build
risk: low
riskReason: Docs and a small helper script; the autopilot keeps PROGRESS.md, so nothing is lost if the board writes fail
size: medium
---
Brian wants to follow the unattended autopilot's CNA progress on agent-board, not in `docs/autopilot/PROGRESS.md`.

**On hold (2026-10-03):** Brian: "let's hold off for now, the current process is working." The cron autopilot keeps running unchanged.

**State:** Board seeded (T-2 Missions 1–4, T-3 Mission 5, T-4 printed-copy questions). Commit `afb873e` on branch `idea/agent-1` (not merged) adds `tools/board_ticket.py` (board HTTP helper, exits 0 when the board is down), a "The board" section and handoff step 3 in `AUTOPILOT.md`, and a pointer in `PROGRESS.md`. pytest passes (211).

**Bigger idea, discussed and parked:** autopilot work becomes tickets, with automation still driving it. Recommended shape: the cron keeps its quota check but, when on pace, presses Build it on the next ready cna ticket (`POST /api/build`) instead of running `claude -p`. Board agents build and `merge_ticket`. Missions become a parent ticket with one child per plan task. Auto-build stays off for cna so pacing stays in the cron. Needs a cna `AGENTS.md` holding the gates and ruling procedure from `AUTOPILOT.md`, since `merge_ticket` merges to main without a PR (whether it waits for GitHub CI is unconfirmed). Alternatives: board auto-build alone (no quota pacing), or the cron using tickets as its queue.

## Done when
- [x] The cna board has a ticket for each mission (Missions 1–4 together, Mission 5 on its own) and one for the open questions only Brian's printed copy can answer
- [x] `AUTOPILOT.md` tells every run to keep its mission ticket current on the board (status, Status summary, Done-when ticks) and to open a ticket when a new mission starts
- [x] A helper (`tools/board_ticket.py`) creates, updates and ticks tickets through the board's HTTP API, and a run doesn't fail when the board is down
- [ ] Merged to main, so the next cron run reads the new orders
