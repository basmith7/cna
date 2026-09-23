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

**MISSION 3 COMPLETE** (the map), 2026-09-23 04:40 UTC. All five sheets, Part D of the primer and the docs are merged; `/map` shows every sheet. The design's Status line lists the PRs.

This run merged Map E (#72, #73, #77) and the docs (#78). Map E went in the way Maps C and D did: once every row had been looked at, with the rows the scan cannot settle left as read and listed in its `EXTRACTION.md` entry. That includes the Delta river classes, which wait on your answer below. Revert any of them if you wanted Map E held.

| Part | What | State | PR |
|---|---|---|---|
| 0 | rulings from NJHarman's Discord-game notes | **merged** | #60 |
| A | plumbing on Malta (plan Tasks 1–13) | **merged** | #61 |
| extractor | dashed tracks, slope threshold, Map A odd-row shift | **merged** | #63, #65, #68 |
| B | Map C and Part D of the primer | **merged**. 213 corrections plus 40 agrees, 20 places, sample 0/50, 22 rows left as read. | #62, #64, #66, #67 |
| C | Map A | **merged**. 111 corrections plus 42 agrees, 10 places, sample 0/50, 33 left as read | #69, #74 |
| C | Map B | **merged**. 185 corrections plus 29 agrees, 2 places, sample 0/50, 112 left as read | #70, #75 |
| C | Map D | **merged**. 111 corrections plus 18 agrees, 1 place, sample 0/50, 50 left as read | #71, #76 |
| C | Map E | **merged**. 244 corrections (M-562–M-697, M-775–M-882) plus 13 agrees; 12 places; sample 0/50; diff 436 → 207, all left as read (134 of them river rows). This run: 17 slopes of the hill rings; 15 Delta railway crossings read as track; 7 roads read as unfinished; and 42 hill bands on rough ground as **ridge**, because the band straddles each hexside, the extraction's own ridge rule. | #72, #73, #77 |
| D | docs (plan Task 17) | **merged**: README data row and legal note, overview link to `/map`, design Status | #78 |

Missions 1 and 2 are complete (PRs #2–#13, #17–#57).

## Next steps

For the autopilot: nothing. Mission 3 is complete. Act only on **Feedback**.

For Brian: each answer below is one small correction PR across the sheets, and the next run will make it.

- **Map E river classes.** The Delta branches and canals are printed at a middle width, and we disagree with the second database on 72 hexsides (38 major→minor, 34 minor→major). A further 62 rows are the Fayum lake shore (the second database codes it as river), the Nile running through a hex, or a winding channel the second database puts on the next hexside. If your Terrain Key says which channels are major rivers, say so.
- **Hill bands: ridge or slope?** On Map E this run recorded 42 bands as ridge. The band lies on both sides of each hexside, which is the extractor's rule for a ridge. Measured the same way (dark on both sides), 9 of Map D's 16 open hill-band rows are ridges: D2408|D2508, D2531|D2631, D2532|D2631, D2631|D2632, D2729|D2829, D2811|D2812, D2827|D2928, D2828|D2829, D2812|D2912 (D3115|D3214 is borderline). The other 6 are one-sided, so they stay slopes. Say whether the printed Terrain Key agrees, and a run will set Map D to match.
- **Blue railways:** on Map C, #64 made the blue Matruh–Tobruk line `unfinished-railroad`. But the Benghazi–Barce line on Map A and the coast line east of Matruh on Map D (Fuka, Baggush) are blue on the scan too, and there they are kept as `railroad`. Say which lines were finished in 1940, and a run will make all the sheets match.
- **Vertex convention:** most rows left as read on every sheet are a track, road or railway passing exactly through a hex corner. The second database always assigns it to one of the hexsides; we record neither. If you want a rule (for example, always the hexside to the east), say so.
- **Places:** the extractor's reference list puts Amiriya at E2212, but the scan prints it at E3212, which is where `places.json` has it. Maps B and D carry only their ports and oases (Derna, Jalo, Mersa Matruh); the villages from the scenario references (Barce, Gazala, Fuka, Sidi Haneish and others) are not in `places.json` yet. Say if you want them.
- **Rows left as read.** The scan cannot settle these at its resolution. Every key is in its sheet's `EXTRACTION.md` entry: A 33, B 112, C 22, D 50, E 207.
- **Railways along hexsides** (C3228|C3328, C3721|C3821, C3920|C4020, C4118|C4218, C4216|C4317): #66 records only the track crossing.
- **Malta numbering and Valletta (M0805 as sea), SPI 20.67,** and the earlier items still stand; see this file's history.
- Vault: the plan leaves the *CNA Living Rules* roadmap row 2 → *done* in your vault to you.

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
