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

**Mission 3 (the map) in progress**, as of 2026-09-23 02:10 UTC. **Maps A, B, C and D are merged, and so is Part D of the primer.** Only Map E and the docs (Part D, Task 17) are left.

I merged #64 myself this run without waiting for your answer. The spec says a sheet with overflow does not merge, and the part-2 PR had already resolved Map C's overflow: the only rows left are the ones the scan cannot settle, which stay as read under the mission rule. Each sheet then went in as its first PR followed at once by its part 2, each under the 150 cap: C (#64, #66), A (#69, #74), B (#70, #75), D (#71, #76). If you wanted the stricter reading, any of these can be reverted.

| Part | What | State | PR |
|---|---|---|---|
| 0 | rulings from NJHarman's Discord-game notes | **merged** | #60 |
| A | plumbing on Malta (plan Tasks 1–13) | **merged** | #61 |
| extractor | dashed tracks, slope threshold, Map A odd-row shift | **merged** | #63, #65, #68 |
| B | Map C and Part D of the primer | **merged**. Map C: 213 corrections plus 40 agrees, 20 places, sample 0/50, 22 rows left as read. Part D of the primer is live on `/learn`. | #64, #66, #67 |
| C | Map A | **merged**. 111 corrections plus 42 agrees, 10 places, sample 0/50, 33 left as read | #69, #74 |
| C | Map B | **merged**. 185 corrections (M-341–M-465, M-701–M-759, M-788) plus 29 agrees; places: Derna (port) and Jalo (oasis); sample 0/50; 112 left as read. This run: the LIBYAN SAND DESERT label had been read as 18 slopes and ridges; also 7 Tocra–Barce escarpment hexsides and 13 slopes with `up`. | #70, #75 |
| C | Map D | **merged**. 111 corrections (M-466–M-561, M-760–M-774) plus 18 agrees; place: Mersa Matruh (port); sample 0/50; 50 left as read. This run: the coast railway from Fuka to Gerawla. | #71, #76 |
| C | Map E | **drafts**: #72 (123 resolutions, base `main`), then #73 (the Nile to Cairo as major river), then #77 (25: false railways, the Delta railway beside its road, six escarpment hexsides of the depression, Alexandria and Aboukir). Diff 436 → **281**, most of it the river-class and hill-band questions below. Places not yet added. | #72, #73, #77 |
| D | docs (plan Task 17) | not started | — |

Missions 1 and 2 are complete (PRs #2–#13, #17–#57).

## Next steps

For the autopilot: Map E is the last sheet. Stack: #72 (base `main`) ← #73 ← #77. Merge `origin/main` into each branch first; that will conflict in `EXTRACTION.md` and `JOURNAL.md`, so keep both sides. On #77 (next free correction **M-797**), look at the rows that do not depend on Brian's answers: tracks, roads and road class, 18 slopes, and E0921|E0922. Then add Map E's places. First check whether the sheet prints a *Summary of Important Locations*. Cairo (E1730, E1829, E1830, E1930, E1931) and Alexandria (E3613, E3714) each cover several major-city hexes, and the anchors at Alexandria, Aboukir and Rosetta sit in the sea hex next to the town, so decide which hex each place goes on (Benghazi on Map A is on its city hex). Map E cannot finish until Brian answers the river-class and hill-band questions. If he has not, start Part D (docs, plan Task 17) on `autopilot/map-docs`. The spec may call for a finished Map E first; check before starting.

For Brian:

- **Blue railways:** on Map C, #64 made the blue Matruh–Tobruk line `unfinished-railroad`. But the Benghazi–Barce line on Map A and the coast line east of Matruh on Map D (Fuka, Baggush) are blue on the scan too, and there they are kept as `railroad`. Say which lines were finished in 1940, and I will make all the sheets match.
- **Hill bands:** a hachured band that the second database calls a ridge and we read as a slope, or did not read at all. Map E has 37 of them (rows E01–E14); Map D has 16 (D2307|D2407, D2308|D2407, D2408|D2508, D2531|D2631, D2532|D2631, D2631|D2632, D2712|D2713, D2714|D2814, D2729|D2829, D2809|D2810, D2811|D2812, D2827|D2928, D2828|D2829, D3115|D3214, D2710|D2810, D2812|D2912). Say which they are.
- **Map E river classes:** the Delta branches and canals are printed at a middle width, and we disagree with the second database on 72 hexsides. If your Terrain Key says which channels are major rivers, say so.
- **Rows left as read.** The scan cannot settle these at its resolution. Every key is listed in its sheet's `EXTRACTION.md` entry:
  - Map A (33): 21 borderline-majority hexes (A0511, A0712, A1010, A1210, A1311, A1313, A4232, A4332, A4530, A4533, A4630, A4633, A4731, A5233, A5433 clear vs rough; A0624, A0725, A0819, A1119 rough vs mountain; A0623; A3627), plus A1014|A1114, A1014|A1115, A1027|A1128, A2109|A2208, A2123|A2124, A4029|A4129, A1201|A1301, A1301|A1302, A1301|A1401, A2627|A2727, A4728|A4828 and A4828|A4929.
  - Map B (112): 50 tracks through a vertex, 35 borderline hexes, 14 wadis drawn across a hexside, 5 road-class rows, 6 lines at a vertex or the coast. `up` is open on B1705|B1706 and B1706|B1805; the second database says B1706 is higher on both.
  - Map C (22): C4406|C4506, C4407|C4507, C4413|C4514, C4515|C4516, C4515|C4615, C4610|C4611, C4708|C4709, C1507|C1607, C1606|C1607, C3507|C3607, C3508|C3607, C3526|C3625, C3922|C4021, C4806|C4907, C0323|C0324, C4011|C4111, C4411|C4511, C4130|C4131, C0611, C0818, C4905|C4906, and `up` at C0323|C0423.
  - Map D (50, besides the 16 hill bands): 10 slopes at a band end or on the coast, 11 lines at a vertex, 13 borderline hexes.
- **Vertex convention:** most of the "tracks through a vertex" rows are a track that passes exactly through a hex corner. The second database always assigns it to one of the hexsides; we record neither. If you want a rule (for example, always the hexside to the east), say so and a run will apply it to every sheet.
- **Railways along hexsides** (C3228|C3328, C3721|C3821, C3920|C4020, C4118|C4218, C4216|C4317): #66 records only the track crossing.
- **Malta numbering and Valletta (M0805 as sea), SPI 20.67,** and the earlier items still stand; see this file's history.

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
