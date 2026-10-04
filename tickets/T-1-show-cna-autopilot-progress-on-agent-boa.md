---
id: T-1
title: Show CNA autopilot progress on agent-board
status: doing
priority: medium
labels: []
depends: []
created: 2026-10-04T04:25:55Z
updated: 2026-10-04T04:27:21Z
kind: build
risk: low
riskReason: Docs and a small helper script; the autopilot keeps PROGRESS.md, so nothing is lost if the board writes fail
size: medium
---
Brian wants to follow the unattended autopilot's CNA progress on agent-board, not in `docs/autopilot/PROGRESS.md`.

## Done when
- [x] The cna board has a ticket for each mission (Missions 1–4 together, Mission 5 on its own) and one for the open questions only Brian's printed copy can answer
- [x] `AUTOPILOT.md` tells every run to keep its mission ticket current on the board (status, Status summary, Done-when ticks) and to open a ticket when a new mission starts
- [x] A helper (`tools/board_ticket.py`) creates, updates and ticks tickets through the board's HTTP API, and a run doesn't fail when the board is down
- [ ] Merged to main, so the next cron run reads the new orders
