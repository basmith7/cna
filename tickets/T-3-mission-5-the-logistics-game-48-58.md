---
id: T-3
title: "Mission 5: the Logistics Game (§48–58)"
status: todo
labels:
  - autopilot
depends: []
created: 2026-10-04T04:26:05Z
updated: 2026-10-04T04:26:05Z
---
**Complete** 2026-09-27 17:05 UTC. Spec `docs/designs/2026-09-27-logistics-game-design.md`, plan `docs/plans/2026-09-27-logistics-game.md`.

| Part | What landed | PRs |
|---|---|---|
| 1. Tooling | `rules/` read recursively, *Logistics Game* sidebar group, CI coverage over 1-32,48-58 | #104 |
| 2. Seed | NJHarman's logistics items: R-025–R-027, V-002–V-005 | #105 |
| 3. Rules files | `rules/logistics/`, seven files, 160 of 160 cases covered, 12 charts as data | #106–#111, #114 |
| 4. Rulings | 32 logistics rulings accepted, R-020–R-022 included | #112–#113, #115–#143, #145 |
| 5. Docs | README, overview link, OA variables, design Status | #144 |

Worth a look (each is one PR to reverse): **R-027** Tobruk starts the campaigns at level 2, not the scenarios' 7; **R-071** Logistics Game rail runs carry units or supplies, never both; **R-040/R-042** fuel in tanks evaporates each turn but not in hot weather. Every ruling's one-liner is in `docs/autopilot/PROGRESS.md`.

## Done when
- [x] 1. Tooling merged
- [x] 2. Seed merged
- [x] 3. Rules files merged
- [x] 4. Every logistics ruling decided and merged
- [x] 5. Docs merged
