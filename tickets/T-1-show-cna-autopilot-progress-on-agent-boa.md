---
id: T-1
title: Show CNA autopilot progress on agent-board
status: todo
priority: medium
labels: []
depends: []
created: 2026-10-04T04:25:55Z
updated: 2026-10-04T04:25:55Z
---
Brian wants to follow the unattended autopilot's CNA progress on agent-board, not in `docs/autopilot/PROGRESS.md`.

## Done when
- [ ] The cna board has a ticket for each mission (Missions 1–4 together, Mission 5 on its own) and one for the open questions only Brian's printed copy can answer
- [ ] `AUTOPILOT.md` tells every run to keep its mission ticket current on the board (status, Status summary, Done-when ticks) and to open a ticket when a new mission starts
- [ ] A helper (`tools/board_ticket.py`) creates, updates and ticks tickets through the board's HTTP API, and a run doesn't fail when the board is down
- [ ] Merged to main, so the next cron run reads the new orders
