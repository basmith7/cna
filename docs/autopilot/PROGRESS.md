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

**MISSION 4 COMPLETE** (decide the open questions), 2026-09-26 19:55 UTC. Every ruling in Parts A and C is accepted, and Part B is merged. 21 rulings are accepted; R-020–R-022 stay proposed as ordered. Each ruling is its own PR, merged after local gates and green CI. Any of them can be disputed: write in **Feedback** or on the decision board, and a later run will supersede it.

| Ruling | Decision (one line) | PR |
|---|---|---|
| R-001 | collapse at cohesion level −26 or worse, not a running DP count (probe: option 2 collapses a unit that recovers every stage) | #82 |
| R-002 | road/track stubs that lead nowhere are ignored | #80 |
| R-003 | Contact is tested at the start of every movement segment, either side's | #85 |
| R-004 | a mixed foot/vehicle formation pays the higher terrain cost and obeys both prohibitions | #89 |
| R-005 | one rail stack each way may mix units and supplies and change load en route | #91 |
| R-006 | 8.53a's "not stacked with a combat unit" condition applies to truck convoys only | #81 |
| R-007 | a reacting unit may spend CP only to move and to blow a dump | #84 |
| R-008 | "in combat" in 8.53d means in Contact | #87 |
| R-009 | the barrage terrain shift protects whoever is barraged (probe) | #96 |
| R-010 | retreat before assault may go in any direction | #86 |
| R-011 | each side's loss base is its own raw points (probe) | #83 |
| R-012 | the withheld-defender retreat is an ordinary 15.82 retreat (probe: fighting is never dearer than the buy-out) | #90 |
| R-013 | pinned units spend no ammunition | #92 |
| R-014 | only a battalion-size or larger combat unit captures destroyed tanks (as 21.52) | #98 |
| R-015 | terrain shifts only the phasing side's anti-armour fire (probe) | #88 |
| R-016 | a Tank Delivery Squadron moves only in the truck convoy phase | #93 |
| R-017 | a TDS reacts or retreats only when stacked with a combat unit | #97 |
| R-018 | the charts govern dumps: real 3 CP + 10 stores, dummy 2 CP (probe). Close call: 24.9's text says otherwise | #94 |
| R-019 | the fleet's western limit is column xx29 on map B; a count of the map's sea hexes puts 100 hexes there, so Derna is out of range | #99 |
| R-023 | *new, from the chart-oddities probe:* close assault defender +2, readings 34–36 inflict 5 % | #100 |
| R-024 | *new:* morale modifier at cohesion −4, a reading of 56 gives −2 | #101 |

Part B (#95): the map, chart and site board items took their defaults and left the board; the Original text viewer was checked on the live site and works; the chart-oddities probe is recorded in the table notes (the attacker −2 "13-18" cell cannot be rolled, so no ruling).

Left alone as ordered: R-020, R-021, R-022 (need the Logistics Game restated) and the `copy` questions below.

Missions 1–3 are complete (PRs #2–#78).

## Next steps

For the autopilot: nothing. Mission 4 is complete. Act only on **Feedback**.

For Brian (all optional; the decision board shows them):

- **Dispute anything.** Every ruling above is one PR to reverse. Two worth a look: **R-018**, where two charts outvote a sentence in 24.9 (option 3, real dump 20 stores, is the other defensible reading); and **R-019**, whose sea-hex count uses the VASSAL-derived map with sheets joined edge to edge. The joins were not checked against the scan, which could move the count by a hex or two but not the five columns NJHarman's xx24 needs.
- **Questions only your printed copy can answer** stay as read: Map E river classes, hill bands (ridge or slope), blue railways, C0323|C0423, the rows the scan cannot settle, SPI 20.67, and the two formation-chart reads.
- **R-020–R-022** wait until the Logistics Game (§47–58) is restated.
- Vault: the *CNA Living Rules* roadmap row 2 → *done* is still yours to flip.

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
| 2026-09-19 21:23 | 42 | 65→68 | 43→12 | $29.41 | 209 | Run complete. Final state: **Landed this run (PRs #43–#57, all merged after green CI; deploy green, `/learn` live at basmith.net/cna/learn):** - **Part C finish |
| 2026-09-20 06:23 | 0 | 75→75 | 0→0 | $0.27 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is already logged in both the journal and `PROGRESS.md`, the **Feedback** section is empty, no autopilot PRs are op |
| 2026-09-20 09:23 | 0 | 76→76 | 3→3 | $0.26 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is already logged in both the journal and `PROGRESS.md`, the **Feedback** section is empty, and there are no open a |
| 2026-09-20 12:23 | 0 | 79→79 | 27→27 | $0.26 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is already logged in both the journal and `PROGRESS.md`, the **Feedback** section is empty, no autopilot PRs are op |
| 2026-09-20 15:23 | 0 | 80→80 | 2→2 | $0.29 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is already logged in both the journal and `PROGRESS.md`, the **Feedback** section is empty, and there are no open a |
| 2026-09-20 18:23 | 0 | 80→80 | 4→4 | $0.29 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is already logged in both the journal and `PROGRESS.md`, the **Feedback** section is empty, and `gh pr list --state |
| 2026-09-20 21:23 | 0 | 82→82 | 11→11 | $0.29 | 3 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both the journal (`JOURNAL.md:247`) and `PROGRESS.md`, the **Feedback** section is empty, and no autop |
| 2026-09-21 00:23 | 0 | 84→84 | 23→23 | $0.29 | 3 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both the journal (`JOURNAL.md:247`) and `PROGRESS.md`, the **Feedback** section is empty, and there ar |
| 2026-09-21 03:23 | 0 | 84→84 | 0→0 | $0.29 | 3 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both the journal (`docs/autopilot/JOURNAL.md:247`) and `PROGRESS.md`, the **Feedback** section is empt |
| 2026-09-21 06:23 | 0 | 84→84 | 0→0 | $0.30 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both the journal and `PROGRESS.md`, the **Feedback** section is empty, and `gh pr list --state open -- |
| 2026-09-21 09:23 | 0 | 84→84 | 2→2 | $0.30 | 3 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both the journal (`docs/autopilot/JOURNAL.md:247`) and `PROGRESS.md`, the **Feedback** section is empt |
| 2026-09-21 12:23 | 0 | 86→86 | 19→19 | $0.31 | 3 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both `docs/autopilot/JOURNAL.md` and `PROGRESS.md`, the **Feedback** section is empty, and `gh pr list |
| 2026-09-21 15:23 | 0 | 86→86 | 2→2 | $0.27 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in both `docs/autopilot/JOURNAL.md` and `PROGRESS.md`, the **Feedback** section is empty, and `gh pr list |
| 2026-09-21 18:23 | 0 | 89→89 | 0→0 | $0.27 | 2 | Nothing to do this run. `MISSION 2 COMPLETE` is logged in `docs/autopilot/PROGRESS.md` (Status section), the **Feedback** section is empty, and `gh pr list --st |
| 2026-09-21 21:23 | 66 | 91→93 | 19→32 | $33.74 | 218 | Run complete; everything is committed and pushed, tree clean. **Landed this run (all merged after green CI)** - **#60 — Part 0:** R-020 (well draws per stage),  |
| 2026-09-22 00:23 | 0 | 100→100 | 3→3 | $0.00 | 1 | You've hit your weekly limit · resets 4pm (America/Phoenix) |
| 2026-09-22 15:23 | 53 | 18→21 | 15→52 | $36.33 | 380 | I merged one PR this run (#68). Every other PR is a draft waiting on one decision from you: whether #64 (Map C) can merge. It holds 149 resolutions, just under  |
| 2026-09-22 18:23 | 51 | 23→24 | 75→87 | $10.74 | 179 | Maps A, B, C and D are now merged to `main`, along with Part D of the primer (live on `/learn`). Map E and the docs PR are the only parts of Mission 3 left, and |
| 2026-09-22 21:23 | 17 | 25→25 | 8→16 | $5.25 | 126 | Mission 3 (the map) is complete, and I've logged `MISSION 3 COMPLETE` in `PROGRESS.md` and the journal. Every sheet, Part D of the primer and the docs are merge |
| 2026-09-23 00:23 | 0 | 32→32 | 2→5 | $0.20 | 2 | I didn't do anything this run: Mission 3 (the map) is finished, and my orders say to do nothing more once it is. - `MISSION 3 COMPLETE` is already logged in bot |
| 2026-09-23 03:23 | 0 | 34→34 | 24→24 | $0.20 | 2 | I had nothing to do this run. `MISSION 3 COMPLETE` is already logged in the journal and in `PROGRESS.md`. The **Feedback** section is empty, and there are no op |
| 2026-09-23 06:23 | 0 | 34→34 | 0→0 | $0.20 | 2 | I did nothing this run. Mission 3 (the map) is already logged as `MISSION 3 COMPLETE` in both the journal and `PROGRESS.md`. The **Feedback** section is empty a |
| 2026-09-23 09:23 | 0 | 36→36 | 37→38 | $0.20 | 2 | I did nothing this run. The map mission (Mission 3) was already marked complete on 2026-09-23, and your orders say to do nothing further after that. There is no |
| 2026-09-23 12:23 | 0 | 38→38 | 0→0 | $0.22 | 2 | My standing orders say to do nothing more after Mission 3 is complete, so this run made no changes. `MISSION 3 COMPLETE` is already in both the journal and `doc |
| 2026-09-23 15:23 | 0 | 39→39 | 11→11 | $0.22 | 2 | I didn't do anything this run: Mission 3 (the map) is finished, and my orders say to do nothing more once it is. - `MISSION 3 COMPLETE` is already logged in the |
| 2026-09-23 18:23 | 0 | 4→4 | 12→12 | $0.22 | 2 | Mission 3 is already complete, the Feedback section is empty, and there are no open autopilot PRs, so my standing orders say to do nothing further. I made no ch |
| 2026-09-23 21:23 | 0 | 12→12 | 64→64 | $0.22 | 2 | Nothing to do this run. Mission 3 (the map) is complete, and `MISSION 3 COMPLETE` is logged in both the journal and `PROGRESS.md`. The **Feedback** section is e |
| 2026-09-24 00:23 | 0 | 22→22 | 49→49 | $0.23 | 2 | I made no changes this run. Mission 3 (the map) was already logged as `MISSION 3 COMPLETE` in the journal and in `PROGRESS.md`. The **Feedback** section is empt |
| 2026-09-24 03:23 | 0 | 28→28 | 4→5 | $0.21 | 2 | I made no changes this run. My standing orders say to do nothing further once Mission 3 (the map) is complete, and it is: - `MISSION 3 COMPLETE` is already logg |
| 2026-09-24 06:23 | 0 | 31→31 | 27→27 | $0.21 | 2 | I made no changes this run. My standing orders say to do nothing further once Mission 3 (the map) is complete, and it is: - `MISSION 3 COMPLETE` is already logg |
| 2026-09-24 09:23 | 0 | 33→33 | 10→10 | $0.23 | 2 | I made no changes this run. My standing orders say to do nothing further once Mission 3 (the map) is complete, and it is: - `MISSION 3 COMPLETE` is logged in bo |
| 2026-09-24 12:23 | 0 | 35→35 | 24→24 | $0.23 | 2 | I made no changes this run. My standing orders say to do nothing further once Mission 3 (the map) is complete, and it is: - `MISSION 3 COMPLETE` is logged in bo |
| 2026-09-24 15:23 | 0 | 37→37 | 11→11 | $0.23 | 2 | Mission 3 is already complete. The Feedback section is empty and there are no open autopilot PRs, so my standing orders say to do nothing further. I made no cha |
| 2026-09-24 18:23 | 0 | 39→39 | 2→2 | $0.21 | 2 | I made no changes this run. Mission 3 (the map) is complete and logged as `MISSION 3 COMPLETE` in both the journal and `PROGRESS.md`. The **Feedback** section i |
| 2026-09-25 00:23 | 0 | 43→43 | 0→0 | $0.23 | 2 | Nothing to do this run, and I made no changes. Mission 3 (the map) is already logged as `MISSION 3 COMPLETE` in both the journal and `PROGRESS.md`, and my stand |
| 2026-09-25 03:23 | 0 | 45→45 | 10→10 | $0.23 | 2 | Mission 3 is complete, the **Feedback** section is empty, and no autopilot PRs are open, so my standing orders say to do nothing further. I made no changes this |
| 2026-09-25 06:23 | 0 | 46→? | 10→? | $0.23 | 2 | Mission 3 was already complete, so this run made no changes. The **Feedback** section in `PROGRESS.md` is empty and no autopilot PRs are open. My standing order |
| 2026-09-25 09:23 | 0 | 47→48 | 2→2 | $0.23 | 2 | Mission 3 is complete: `MISSION 3 COMPLETE` is logged in both the journal and `PROGRESS.md`. The **Feedback** section is empty and no autopilot PRs are open, so |
| 2026-09-25 12:23 | 0 | 48→48 | 8→8 | $0.21 | 3 | I did nothing this run, because there was nothing to do. `MISSION 3 COMPLETE` is already logged in the journal (`docs/autopilot/JOURNAL.md:339`) and in `PROGRES |
| 2026-09-25 15:23 | 0 | 50→50 | 6→6 | $0.24 | 2 | I made no changes this run. My standing orders say to do nothing further once Mission 3 (the map) is complete, and it is already logged as `MISSION 3 COMPLETE`  |
| 2026-09-25 18:23 | 0 | 51→51 | 11→11 | $0.23 | 2 | I made no changes this run. My standing orders say to do nothing further once Mission 3 (the map) is complete, and it is: - `MISSION 3 COMPLETE` is logged in bo |
| 2026-09-25 21:23 | 0 | 51→51 | 0→0 | $0.24 | 2 | Nothing to do this run, so I made no changes. Mission 3 (the map) is already marked `MISSION 3 COMPLETE` in both the journal and `PROGRESS.md`. The **Feedback** |
| 2026-09-26 00:23 | 0 | 51→51 | 0→0 | $0.24 | 2 | Mission 3 was already complete, so this run changed nothing. I left the budget unused on purpose: my standing orders say to do nothing further once the mission  |
| 2026-09-26 03:23 | 0 | 51→51 | 0→0 | $0.24 | 2 | I made no changes this run, because Mission 3 (the map) is already complete and my standing orders say to do nothing further once it is. - `MISSION 3 COMPLETE`  |
| 2026-09-26 06:23 | 0 | 51→51 | 0→0 | $0.25 | 2 | No changes this run. Mission 3 (the map) was already finished on 2026-09-22 and is marked `MISSION 3 COMPLETE` in both the journal and `PROGRESS.md`. My standin |
| 2026-09-26 09:23 | 0 | 54→54 | 2→2 | $0.25 | 2 | Mission 3 is done, and this run changed nothing. It's already logged as `MISSION 3 COMPLETE` in both `docs/autopilot/PROGRESS.md` and the journal. The **Feedbac |
