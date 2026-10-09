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

- 2026-10-08 (cna-engine, Requests for cna) six requests → all merged 2026-10-08: track cost agrees with E-031 (#168); combat wording phasing/non-phasing, probe refund shown in the CP table (#169; `cp-costs.json` was right as printed); stacking `equivalent` per unit type (#170); Land-only victory supply, R-110 (#171); weapon systems 4.47–4.49 as `data/tables/weapon-systems.json` (#172); cross-sheet adjacency `data/map/seams.json` (#173).

## Status

**MISSION 7 COMPLETE** (the Air Game, §33–47), 2026-10-09 05:00 UTC. **The queue is finished: every SPI section, §1–65, is covered (1,736 of 1,736 cases).** From here this repo works only on cna-engine's *Requests for cna* and your Feedback.

| Task | What landed | PRs |
|---|---|---|
| 0. Spec and plan | `docs/designs/2026-10-08-air-game-design.md` | #188 |
| 1. Overview and sequence (§33) | `rules/air/`, "Air Game" sidebar; final switch list: §47 replaces 32.57/32.59, 32.6, 32.7; 32.8 off (R-114); all of §58 off | #189, #201 |
| 2. Seed | R-111, V-009–V-025 | #191 |
| 3. Rules files | aircraft and SGSUs (§34–35), air facilities (§36), flight and maintenance (§37–38), missions (§39, §42), fighters (§40), bombing (§41), Mediterranean and Malta (§43–44), air combat and flak (§45–46), abstract logistics (§47) | #190, #192–#198, #201, #202, #204–#208 |
| 4. Rulings | R-111–R-116 accepted | #203, #209–#213 |
| 5. Docs | README, overview, design Status, queue | #214 |

18 air chart files are data, each read twice (archive.org scan and the community chart PDFs): aircraft characteristics, refit, CW reinforcements, missions, land and convoy reconnaissance, scramble, strafing, the **Air Bombardment Table** (374 cells, which also lets an engine resolve §32's abstract convoy and fleet attacks), harbour mining, maneuver, TacAir kill, recovery, anti-aircraft results with the flak adjustment, Malta construction, commitment and availability, and all three Pilot Arrival Tables. 0 cells differed except the one noted in #193 and #198.

Air rulings, one line each:

| Ruling | Decision |
|---|---|
| R-111 | flak printed on the map or in a box is heavy; fighters cannot suppress it |
| R-112 | refit additions follow the aircraft's nation (38.35), not the SGSU's |
| R-113 | the Flak Adjustment Chart sets the density shift; the results table's notes are not used |
| R-114 | with the Air Game, §32's anti-air stripping (32.8) does not apply |
| R-115 | no rating-5 pilots: the arrival tables print 1–4, Marseille is the only 6 |
| R-116 | Commonwealth squadrons 15+5 to June 1941, 18+6 from July (rules text over the chart) |

Missions 1–6 are complete (PRs #2–#187); their summaries are in the git history of this file and in `docs/designs/`.

## Next steps

For the autopilot: only cna-engine's **Requests for cna** and Brian's Feedback. With neither, do nothing and say so.

For Brian (all optional):

- **Dispute anything.** Air rulings worth a look: **R-114** (AA units stay with the Air Game) and **R-116** (squadron size: text over chart). Older: R-099, R-108, R-110, R-027, R-071.
- **Questions only your printed copy can answer** (decision board, `copy` group), new: the **Axis Airplane Reinforcement Schedule (34.87)** is in neither scan, so the Axis currently gets no air reinforcements. Still open: the German Tank and Gun chart's three misaligned rows, Axis coastal ship tonnages, German c/d CPA, the el Grein garrison.
- Vault: the *CNA Living Rules* roadmap row for Mission 7 is yours to flip to done.

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
| 2026-09-26 12:23 | 33 | 55→56 | 8→10 | $6.02 | 72 | Mission 4 is complete. All 21 rulings in Parts A and C are decided and merged, including two new ones that came out of Part B's chart probe. Part B is merged to |
| 2026-09-26 15:23 | 0 | 57→57 | 10→10 | $0.20 | 2 | Mission 4 was already complete, so this run did nothing: no files changed and nothing was committed. - `MISSION 4 COMPLETE` is already recorded in both the jour |
| 2026-09-26 18:23 | 0 | 60→60 | 0→0 | $0.20 | 2 | I did nothing this run. The mission is already finished: `MISSION 4 COMPLETE` is logged in both `PROGRESS.md` and the journal, and the orders say to do nothing  |
| 2026-09-26 21:23 | 0 | 61→61 | 5→5 | $0.18 | 2 | I did nothing this run: Mission 4 is already finished, so the standing orders say to stop. The journal entry from 2026-09-26 12:56 MST records `MISSION 4 COMPLE |
| 2026-09-27 00:23 | 0 | 63→63 | 2→2 | $0.24 | 2 | Nothing to do this run, and I made no changes. The orders say to do nothing further once Mission 4 is complete, and it is. - `MISSION 4 COMPLETE` is already log |
| 2026-09-27 03:23 | 0 | 63→63 | 4→4 | $0.26 | 3 | I made no changes this run. Mission 4 was already marked `MISSION 4 COMPLETE` in the journal and `PROGRESS.md` on 2026-09-26. The **Feedback** section is empty, |
| 2026-09-27 06:23 | 0 | 63→63 | 0→0 | $0.28 | 4 | I made no changes this run. Mission 4 was already finished (`MISSION 4 COMPLETE` is logged in the journal and `PROGRESS.md`), and my orders say to do nothing mo |
| 2026-09-27 09:23 | 42 | 66→67 | 16→1 | $18.56 | 121 | Mission 5 (the Logistics Game, SPI §48–58) is finished. All five parts are merged, each PR only after the local checks and CI passed, and the site deployed with |
| 2026-09-27 15:23 | 0 | 70→70 | 0→0 | $0.19 | 2 | Mission 5 is complete and there's nothing left to do, so this run made no changes. - **Feedback:** the Feedback section in `PROGRESS.md` is empty. - **Open PRs: |
| 2026-09-27 18:23 | 0 | 70→70 | 0→0 | $0.20 | 2 | Nothing to do this run: Mission 5 (the Logistics Game) is complete and all of its PRs are merged. The **Feedback** section in `PROGRESS.md` is empty and there a |
| 2026-09-27 21:23 | 0 | 71→71 | 0→0 | $0.19 | 2 | Mission 5 is already complete, Feedback is empty and no autopilot PRs are open, so there's nothing to do this run. The standing orders say to "do nothing furthe |
| 2026-09-28 00:23 | 0 | 71→71 | 6→6 | $0.22 | 2 | Nothing to do this run. Mission 5 is already logged `MISSION 5 COMPLETE` in both the journal and `PROGRESS.md`. The **Feedback** section is empty and there are  |
| 2026-09-28 03:23 | 0 | 72→72 | 0→0 | $0.23 | 2 | Nothing to do this run. Mission 5 (the Logistics Game) is already marked `MISSION 5 COMPLETE` in both `docs/autopilot/PROGRESS.md` and the journal. All five par |
| 2026-09-28 06:23 | 0 | 72→72 | 3→3 | $0.22 | 2 | Mission 5 is already complete, so I did nothing this run. - `MISSION 5 COMPLETE` was logged in both the journal and `PROGRESS.md` on 2026-09-27. - The **Feedbac |
| 2026-09-28 09:23 | 0 | 74→74 | 17→17 | $0.24 | 3 | I did nothing this run: Mission 5 (the Logistics Game) was already logged as `MISSION 5 COMPLETE` in both `docs/autopilot/PROGRESS.md` and the journal on 2026-0 |
| 2026-09-28 12:23 | 0 | 75→75 | 2→2 | $0.27 | 3 | I made no changes this run. Mission 5 (the Logistics Game) is already logged as `MISSION 5 COMPLETE` in both `PROGRESS.md` and the journal, and my standing orde |
| 2026-09-28 15:23 | 0 | 76→? | 3→? | $0.26 | 2 | Nothing to do this run, and I made no changes. - **Mission 5 (the Logistics Game):** already logged as `MISSION 5 COMPLETE` in `docs/autopilot/PROGRESS.md` and  |
| 2026-09-28 18:23 | 0 | 77→77 | 7→7 | $0.23 | 3 | I did nothing this run. Mission 5 (the Logistics Game) is already marked `MISSION 5 COMPLETE` in both the journal and `PROGRESS.md`, and my orders say to stop t |
| 2026-09-28 21:23 | 0 | 78→78 | 12→12 | $0.25 | 3 | I made no changes this run, because Mission 5 (the Logistics Game) is already finished. - **Already logged:** `MISSION 5 COMPLETE` is in `docs/autopilot/PROGRES |
| 2026-09-29 00:23 | 0 | 79→79 | 8→8 | $0.26 | 2 | Mission 5 was already finished, so this run did nothing and changed no files. - `MISSION 5 COMPLETE` is logged in both `docs/autopilot/PROGRESS.md` and the jour |
| 2026-09-29 03:23 | 0 | 79→79 | 0→0 | $0.26 | 2 | I made no changes this run, because Mission 5 (the Logistics Game) is already finished. - **Already logged:** `MISSION 5 COMPLETE` was recorded on 2026-09-27 in |
| 2026-09-29 06:23 | 0 | 79→79 | 0→0 | $0.19 | 2 | Mission 5 is already complete, so this run made no changes. The **Feedback** section in `PROGRESS.md` is empty, and no autopilot PRs are open. The standing orde |
| 2026-09-29 09:23 | 0 | 80→80 | 9→10 | $0.26 | 2 | Mission 5 was already finished, so this run changed nothing. - **Mission:** `MISSION 5 COMPLETE` was logged on 2026-09-27 in both `docs/autopilot/PROGRESS.md` a |
| 2026-09-29 12:23 | 0 | 82→82 | 26→26 | $0.22 | 3 | I did nothing this run, because Mission 5 (the Logistics Game) is already finished. `MISSION 5 COMPLETE` is logged in the journal (`docs/autopilot/JOURNAL.md:35 |
| 2026-09-29 15:23 | 0 | 88→88 | 26→26 | $0.22 | 3 | I did nothing this run. Mission 5 (the Logistics Game) is already logged as `MISSION 5 COMPLETE` in the journal (`docs/autopilot/JOURNAL.md:358`) and in `PROGRE |
| 2026-09-29 18:23 | 0 | 6→6 | 32→32 | $0.26 | 2 | Mission 5 is complete, Feedback is empty, and no autopilot PRs are open, so I made no changes this run. My standing orders say to do nothing further once the mi |
| 2026-09-29 21:23 | 0 | 10→10 | 11→11 | $0.25 | 2 | Nothing to do this run, so I made no changes and didn't commit anything. Mission 5 (the Logistics Game) is already finished: `MISSION 5 COMPLETE` is logged in b |
| 2026-09-30 00:23 | 0 | 14→? | 63→? | $0.20 | 2 | Nothing to do this run. Mission 5 is complete: it was logged on 2026-09-27, and the standing orders say to do nothing further after that. The **Feedback** secti |
| 2026-09-30 03:23 | 0 | 16→16 | 20→20 | $0.27 | 2 | Mission 5 is already complete: `MISSION 5 COMPLETE` is logged in the journal and in `PROGRESS.md`. The **Feedback** section is empty and no autopilot PRs are op |
| 2026-09-30 06:23 | 0 | 2→? | 10→? | $0.22 | 2 | Mission 5 is complete, the Feedback section is empty, and no autopilot PRs are open, so I did nothing this run. Under the standing orders, a completed mission w |
| 2026-09-30 09:23 | 0 | 23→23 | 26→26 | $0.25 | 2 | Nothing to do this run, and I made no changes. The Logistics Game mission (Mission 5) is finished: `MISSION 5 COMPLETE` was logged in the journal and `PROGRESS. |
| 2026-09-30 12:23 | 0 | 25→25 | 47→47 | $0.19 | 2 | Nothing to do this run. Mission 5 (the Logistics Game, §48–58) was logged `MISSION 5 COMPLETE` on 2026-09-27, the **Feedback** section in `PROGRESS.md` is empty |
| 2026-09-30 15:23 | 0 | 27→27 | 29→29 | $0.21 | 2 | Mission 5 is complete. The Feedback section is empty and there are no open autopilot PRs. My orders say to do nothing further, so this run made no changes. - ** |
| 2026-09-30 18:23 | 0 | 3→3 | 2→2 | $0.22 | 2 | Nothing to do this run. Mission 5 (the Logistics Game) is already marked `MISSION 5 COMPLETE` in both `PROGRESS.md` and the journal, the **Feedback** section is |
| 2026-09-30 21:23 | 0 | 5→5 | 3→3 | $0.22 | 3 | I did nothing this run, because Mission 5 (the Logistics Game) is already finished. `MISSION 5 COMPLETE` is logged in both `PROGRESS.md` and the journal (`docs/ |
| 2026-10-01 00:23 | 0 | 5→5 | 6→6 | $0.27 | 4 | I did nothing this run and changed no files, because Mission 5 (the Logistics Game) is already finished. - **Already logged:** `MISSION 5 COMPLETE` is in `docs/ |
| 2026-10-01 03:23 | 0 | 5→5 | 0→0 | $0.27 | 2 | Mission 5 is complete, Feedback is empty, and no autopilot PRs are open. My standing orders say to do nothing further once the mission is complete, so this run  |
| 2026-10-01 06:23 | 0 | 5→5 | 0→0 | $0.25 | 2 | Mission 5 was already finished, so this run made no changes. My orders say to stop once it is complete. - `MISSION 5 COMPLETE` is logged in both the journal and |
| 2026-10-01 09:23 | 0 | 6→6 | 2→2 | $0.27 | 2 | Mission 5 was already complete when this run started, so I made no changes and committed nothing. - **Mission:** `MISSION 5 COMPLETE` was logged in both `PROGRE |
| 2026-10-01 12:23 | 0 | 9→9 | 25→25 | $0.20 | 2 | Mission 5 is complete, so this run made no changes. - Feedback in `docs/autopilot/PROGRESS.md` is empty, so there was nothing to act on. - No autopilot PRs are  |
| 2026-10-01 15:23 | 0 | 13→13 | 20→20 | $0.19 | 3 | Mission 5 is already complete, so this run did nothing. Feedback in `PROGRESS.md` is empty, and there are no open autopilot PRs. The standing orders say to stop |
| 2026-10-01 18:23 | 0 | 17→17 | 3→3 | $0.20 | 3 | Nothing to do this run. Mission 5 is already complete (logged 2026-09-27), and AUTOPILOT.md says to do nothing further after that. - **Feedback:** the section i |
| 2026-10-01 21:23 | 0 | 18→18 | 14→14 | $0.22 | 3 | I did nothing this run. Mission 5 (the Logistics Game) was already finished on 2026-09-27, and my orders say to stop once it is. `MISSION 5 COMPLETE` is logged  |
| 2026-10-02 00:23 | 0 | 21→21 | 6→6 | $0.20 | 2 | Nothing to do this run: Mission 5 is already complete, nothing is waiting in **Feedback**, and no autopilot PRs are open. The standing orders say to do nothing  |
| 2026-10-02 03:23 | 0 | 21→21 | 8→8 | $0.20 | 3 | Nothing to do this run. Mission 5 (the Logistics Game) is already marked `MISSION 5 COMPLETE` in `PROGRESS.md` and the journal, dated 2026-09-27. The **Feedback |
| 2026-10-02 06:23 | 0 | 23→23 | 14→14 | $0.22 | 4 | I made no changes this run. Mission 5 was already logged `MISSION 5 COMPLETE` on 2026-09-27, and the standing orders say to do nothing further after that. I che |
| 2026-10-02 09:23 | 0 | 24→24 | 4→4 | $0.22 | 2 | Mission 5 is already complete, so I did nothing this run. `MISSION 5 COMPLETE` is logged in both the journal and `PROGRESS.md` (2026-09-27). The **Feedback** se |
| 2026-10-02 12:23 | 0 | 24→24 | 7→7 | $0.27 | 2 | I made no changes this run: Mission 5 (the Logistics Game) is already done and the orders say to stop there. - **Mission:** `MISSION 5 COMPLETE` was logged in ` |
| 2026-10-02 15:23 | 0 | 25→25 | 5→5 | $0.22 | 2 | Mission 5 is already complete, so this run did nothing. Both the journal and `PROGRESS.md` record `MISSION 5 COMPLETE`, the **Feedback** section is empty, and t |
| 2026-10-02 18:23 | 0 | 26→26 | 7→7 | $0.24 | 3 | I did nothing this run. Mission 5 (the Logistics Game) is already logged as `MISSION 5 COMPLETE` in both the journal and `PROGRESS.md`, and the standing orders  |
| 2026-10-02 21:23 | 0 | 27→27 | 8→8 | $0.22 | 3 | I did nothing this run, because Mission 5 (the Logistics Game) is already finished and my orders say to stop once it is. - **Already logged:** `MISSION 5 COMPLE |
| 2026-10-03 00:23 | 0 | 28→28 | 2→2 | $0.20 | 2 | Nothing to do this run. Mission 5 is already complete and logged as `MISSION 5 COMPLETE`, there is no **Feedback** in `PROGRESS.md`, and no autopilot PRs are op |
| 2026-10-03 03:23 | 0 | 28→28 | 3→3 | $0.22 | 2 | Nothing to do this run: Mission 5 (the Logistics Game) was already finished, and the standing orders say to do nothing further after that. - `MISSION 5 COMPLETE |
| 2026-10-03 06:23 | 0 | 28→28 | 0→0 | $0.26 | 3 | I made no changes this run. Mission 5 (the Logistics Game) was already logged as `MISSION 5 COMPLETE` on 2026-09-27 in both the journal and `PROGRESS.md`. The * |
| 2026-10-03 09:23 | 0 | 28→28 | 1→1 | $0.21 | 3 | Nothing to do this run: Mission 5 (the Logistics Game) has been complete since 2026-09-27, and the standing orders say to do nothing further after that. - **Fee |
| 2026-10-03 12:23 | 0 | 30→30 | 7→7 | $0.20 | 3 | Nothing to do this run. Mission 5 (the Logistics Game) is already marked complete, and the standing orders say to do nothing further once that happens. - **Feed |
| 2026-10-03 15:23 | 0 | 35→35 | 41→41 | $0.23 | 2 | Mission 5 is already complete, so I did nothing this run. - `MISSION 5 COMPLETE` is in both the journal and `PROGRESS.md`, dated 2026-09-27. - The **Feedback**  |
| 2026-10-03 18:23 | 0 | 41→41 | 21→21 | $0.25 | 2 | Mission 5 is already complete, so this run made no changes. - `MISSION 5 COMPLETE` is already logged in both the journal and `PROGRESS.md`, dated 2026-09-27. -  |
| 2026-10-03 21:23 | 0 | 48→48 | 0→0 | $0.22 | 3 | Mission 5 is already complete, so there was nothing to do this run. It was finished on 2026-09-27 (PRs #104–#145), and both the journal and `PROGRESS.md` record |
| 2026-10-04 00:23 | 0 | 55→55 | 43→43 | $0.23 | 2 | Nothing to do this run. Mission 5 (the Logistics Game) is already marked `MISSION 5 COMPLETE` in the journal and in `PROGRESS.md`. The **Feedback** section is e |
| 2026-10-04 03:23 | 0 | 55→55 | 0→0 | $0.24 | 3 | I did nothing this run. Mission 5 (the Logistics Game) is already logged as `MISSION 5 COMPLETE` in both the journal and `PROGRESS.md`, and the standing orders  |
| 2026-10-04 06:23 | 0 | 55→55 | 0→0 | $0.25 | 2 | I made no changes this run, because Mission 5 (the Logistics Game) is already finished. `MISSION 5 COMPLETE` was logged on 2026-09-27 in both the journal and `P |
| 2026-10-04 12:23 | 0 | 67→67 | 75→75 | $0.20 | 2 | Nothing to do this run. Mission 5 finished on 2026-09-27 and `MISSION 5 COMPLETE` is already in the journal and `PROGRESS.md`. The standing orders say to do not |
| 2026-10-04 15:23 | 0 | 68→68 | 7→7 | $0.22 | 2 | Nothing to do this run. `MISSION 5 COMPLETE` is already logged in the journal and `PROGRESS.md`, and AUTOPILOT.md says to stop once it is. The **Feedback** sect |
| 2026-10-04 18:23 | 0 | 74→74 | 40→40 | $0.30 | 3 | I made no changes this run, because Mission 5 (the Logistics Game) is already finished. - `MISSION 5 COMPLETE` was logged on 2026-09-27 in both `docs/autopilot/ |
| 2026-10-04 21:23 | 0 | 74→74 | 1→1 | $0.19 | 3 | I did nothing this run, because the standing orders say to stop once Mission 5 is complete. It was logged `MISSION 5 COMPLETE` on 2026-09-27, all five parts are |
| 2026-10-05 03:23 | 0 | 3→3 | 32→33 | $0.23 | 2 | Nothing to do this run. Mission 5 (the Logistics Game) is already logged as `MISSION 5 COMPLETE` in both the journal and `PROGRESS.md`, dated 2026-09-27. The ** |
| 2026-10-05 06:23 | 0 | 3→3 | 0→0 | $0.20 | 3 | Nothing to do this run: the standing orders say Mission 5 is complete and to stay idle after it, and I followed that. - **Feedback:** the section in `PROGRESS.m |
| 2026-10-05 09:23 | 0 | 4→4 | 17→17 | $0.22 | 3 | Mission 5 was already finished, so this run made no changes. The `MISSION 5 COMPLETE` entry is in both `PROGRESS.md` and the journal, dated 2026-09-27. **Feedba |
| 2026-10-05 15:23 | 0 | 14→14 | 67→67 | $0.21 | 3 | Mission 5 is still complete, so this run made no changes. The Feedback section in `docs/autopilot/PROGRESS.md` is empty and there are no open autopilot PRs. The |
| 2026-10-05 21:23 | 0 | 96→96 | 29→30 | $0.21 | 2 | Nothing to do this run: Mission 5 (the Logistics Game) is already marked `MISSION 5 COMPLETE` in `PROGRESS.md`. Your Feedback section is empty and no autopilot  |
| 2026-10-06 00:23 | 0 | 98→98 | 0→0 | $0.20 | 2 | Nothing to do this run. Mission 5 is already complete (logged 2026-09-27), the **Feedback** section in `PROGRESS.md` is empty, and no autopilot PRs are open. AU |
| 2026-10-06 03:23 | 0 | 31→31 | 0→0 | $0.23 | 3 | Mission 5 is already complete, so this run changed nothing. - `MISSION 5 COMPLETE` is logged in both the journal and `PROGRESS.md`, dated 2026-09-27. - The **Fe |
| 2026-10-06 06:23 | 0 | 31→31 | 0→1 | $0.21 | 3 | Nothing to do this run: Mission 5 (the Logistics Game, §48–58) is complete, and the standing orders say to do nothing further. - **Feedback** in `PROGRESS.md` i |
| 2026-10-06 09:23 | 0 | 37→37 | 1→2 | $0.23 | 2 | Nothing to do this run. `MISSION 5 COMPLETE` is already logged in both the journal and `PROGRESS.md`. The **Feedback** section is empty and there are no open au |
| 2026-10-06 18:23 | 0 | 1→1 | 4→5 | $0.22 | 3 | I did nothing this run, because Mission 5 (the Logistics Game, §48–58) is already finished. `MISSION 5 COMPLETE` is logged in both the journal and `PROGRESS.md` |
| 2026-10-06 21:23 | 0 | 51→51 | 0→0 | $0.22 | 3 | I made no changes this run. Mission 5 (the Logistics Game) has been marked `MISSION 5 COMPLETE` in the journal and `PROGRESS.md` since 2026-09-27. The **Feedbac |
| 2026-10-08 09:23 | 80 | 34→37 | 1→23 | $49.99 | 324 | Mission 6 is nearly complete, Brian. All seven scenarios are now data, every §59–65 case is restated (171/171), and the OA sheets for all three nations plus the |
| 2026-10-08 21:23 | 40 | 41→41 | 3→6 | $11.16 | 178 | Mission 7 (the Air Game) is finished, so the whole queue is done. Every SPI section from §1 to §65 is now covered: 1,736 of 1,736 cases. I merged 14 PRs this ru |
| 2026-10-09 00:23 | 0 | 43→43 | 4→4 | $0.25 | 4 | I did nothing this run, because there was nothing to act on. The queue is finished (Mission 7 completed 2026-10-09 05:00 UTC; all 1,736 cases in §1–65 are cover |
| 2026-10-09 03:23 | 0 | 43→43 | 8→8 | $0.34 | 3 | Nothing to do this run, so I made no changes and committed nothing. - **Your Feedback:** the section in `PROGRESS.md` is empty. - **Open autopilot PRs:** none.  |
| 2026-10-09 06:23 | 0 | 43→43 | 0→0 | $0.25 | 4 | I made no changes this run because there was no work to pick up. The queue is finished: Mission 7 completed on 2026-10-08 and all 1,736 cases in §1–65 are cover |
| 2026-10-09 09:23 | 0 | 44→44 | 3→3 | $0.25 | 4 | Nothing to do this run, so I made no changes and committed nothing. - **Your Feedback:** the section in `PROGRESS.md` is empty. - **Open autopilot PRs:** none.  |
| 2026-10-09 12:23 | 0 | 45→45 | 4→4 | $0.25 | 3 | Nothing to do this run, so I stopped without making any changes or commits. The queue is finished (Mission 7 complete, all 1,736 cases covered), the **Feedback* |
| 2026-10-09 15:23 | 0 | 46→46 | 4→4 | $0.30 | 4 | Nothing to do this run, so I changed nothing. - **Feedback:** the section in `PROGRESS.md` is empty. - **Open autopilot PRs:** none. - **cna-engine requests:**  |
