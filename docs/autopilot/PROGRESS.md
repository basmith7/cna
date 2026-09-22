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

**Mission 3 (the map) in progress**: 2026-09-22 22:56 UTC. Parts 0 and A are merged, and so are both extractor PRs. Map C and Part D of the primer are finished as three stacked drafts. **Brian: merge #64** (`gh pr ready 64 && gh pr merge 64 --merge`) **or say in Feedback that the cap should not block it.** After that the next run retargets #66 and #67 to `main` and merges them in turn. They stay drafts until then, so that no run merges #66 into #64 and pushes #64 over the 150 cap.

Missions 1 and 2 are complete (PRs #2–#13, #17–#57). 20.67 is still the one item only Brian can close (see *Next steps*).

| Part | What | State | PR |
|---|---|---|---|
| 0 | rulings from NJHarman's Discord-game notes | **merged** — R-020 (well draws per stage), R-021 (sweetening attempts), R-022 (52.51 vehicles vs guns); R-007/R-013/R-018 gained the notes as a second source; air/Malta/CHANGE items listed as not imported in `EXTRACTION.md` | #60 |
| A | plumbing on Malta (plan Tasks 1–13) | **merged** — `map_geom`, schemas, `sheets.json` (Map A shifts odd rows *east*), extractor cache-first/ids/clip/coast/raw, `map_build`, `check_data` map gate, `map_render` + `/map` page + golden, CI gates, `data/README.md`, EXTRACTION entry; Malta: 63 hexes, 17 corrections (the redraw's title box), 6 places | #61 |
| extractor | dashed-track detection; slope band threshold (own PRs, every raw regenerated) | **merged** — Map C diff 470 → 297 (#63) → 262 (#65); Malta corrections re-resolved (+M-018, M-019); `map_diff.py` and Map C raw + render landed with #63 | #63, #65 |
| B | Map C: diff, ≤150 resolutions, `up`, places, 50-hex sample, Part D of the primer | **three stacked drafts, all gates green** — #64: 149 resolutions (116 corrections M-020–M-135 + 33 agrees), 20 places, sample 0/50, at the cap. #66 (base #64): 100 more (93 corrections M-140–M-232 + 7 agrees): 60 missed track crossings, 5 railway hexsides that are tracks, the coastal slope west of Tobruk with `up`, 6 false railway reads removed; Map C diff 155 → **62**, of which **22 left as read** (see below). #67 (base #66): Task 15, Part D of the primer on our own Map C render | #64, #66, #67 (drafts) |
| C | Maps A, B, D, E | **Map A drafted** — #68 (extractor: Map A's odd-row shift is `west` in the printed numbering; 169 hexsides failed adjacency with `east`) merged; #69 (draft, base #66): raw, 103 corrections M-233–M-335 + 25 agrees = 128 resolutions, 10 places, sample 0/50, 66 rows left (21 borderline terrain majorities, 45 hexside). B, D, E not started | #68, #69 (draft) |
| D | docs | not started | — |

## Next steps

For the autopilot: if #64 has merged, retarget #66 to `main` (`gh pr edit 66 --base main`), run the gates, then mark it ready and merge it once CI is green; then do the same for #67. After that comes Part C, Map A, on `autopilot/map-a` (Task 16 = Task 14 steps 14.3–14.8). If #64 has not merged: Map A is #69, stacked on #66. Its second PR and Map B can stack the same way (next free correction is M-336). Merge order once #64 is in: #66, then #67 and #69.

For Brian:

- **Map C rows left as read (22)**: the scan cannot settle these at its resolution. Your copy might:
  - ridge or slope in the El Adem–Tobruk ridge country: C4406|C4506, C4407|C4507, C4413|C4514, C4515|C4516, C4515|C4615, C4610|C4611, C4708|C4709
  - wadis that the redraw draws on the hexside but the scan prints just inside the hex: C1507|C1607, C1606|C1607, C3507|C3607, C3508|C3607
  - where an escarpment band ends: C3526|C3625, C3922|C4021, C4806|C4907
  - lines that pass through a hex vertex: tracks at C0323|C0324 and C4011|C4111, the railway at C4411|C4511, and the road at C4130|C4131, where it changes from unfinished to finished at the vertex
  - from #64: C0611 (clear or sand), C0818 (clear or salt-marsh), C4905|C4906 (coast road or track), and `up` at C0323|C0423 (our band-side convention says C0323 is higher; the second database says C0423, a rough hill ringed by hachures)
- **Railways along hexsides:** in five places the railway runs along a hexside to its vertex instead of crossing it (C3228|C3328, C3721|C3821, C3920|C4020, C4118|C4218, C4216|C4317). #66 records only the track crossing there. Tell me if you would rather the railway counted as crossing.
- **Malta numbering:** the printed inset has no hex numbers, so `M` hexes carry the VASSAL module's numbering. Norman's code uses a different origin. Say if you want it changed.
- **Valletta** (`M0805`) reads as sea: it is a `feature` place with `port: true` on a sea hex.
- **Unfinished railroad:** the whole Matruh–Capuzzo–Tobruk line is blue on the scan. If part of it should be a finished railroad in 1940, say which stretch.
- **SPI 20.67:** not printed in the archive.org scan. If your copy has it, say where.
- The earlier items (Learn page dark mode, formation charts 19.31–19.33, and others) still stand. See the 2026-09-20 entry in this file's git history.

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
