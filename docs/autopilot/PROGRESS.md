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

**Mission 3 (the map) in progress** — 2026-09-22 05:30 UTC. Parts 0 and A merged, two extractor PRs merged; Part B (Map C) is a draft at the 150-resolution cap with every gate and CI green — **Brian: merge #64 (`gh pr ready 64 && gh pr merge 64 --merge`) or say in Feedback that the cap should not block it** — and 122 cross-check rows left for the next PR.

Missions 1 and 2 are complete (PRs #2–#13, #17–#57); 20.67 is still the one item only Brian can close (see *Next steps*).

| Part | What | State | PR |
|---|---|---|---|
| 0 | rulings from NJHarman's Discord-game notes | **merged** — R-020 (well draws per stage), R-021 (sweetening attempts), R-022 (52.51 vehicles vs guns); R-007/R-013/R-018 gained the notes as a second source; air/Malta/CHANGE items listed as not imported in `EXTRACTION.md` | #60 |
| A | plumbing on Malta (plan Tasks 1–13) | **merged** — `map_geom`, schemas, `sheets.json` (Map A shifts odd rows *east*), extractor cache-first/ids/clip/coast/raw, `map_build`, `check_data` map gate, `map_render` + `/map` page + golden, CI gates, `data/README.md`, EXTRACTION entry; Malta: 63 hexes, 17 corrections (the redraw's title box), 6 places | #61 |
| extractor | dashed-track detection; slope band threshold (own PRs, every raw regenerated) | **merged** — Map C diff 470 → 297 (#63) → 262 (#65); Malta corrections re-resolved (+M-018, M-019); `map_diff.py` and Map C raw + render landed with #63 | #63, #65 |
| B | Map C: diff, ≤150 resolutions, `up`, places, 50-hex sample, Part D of the primer | **in progress (draft)** — `map_sample.py` + Map C scan grid; 116 corrections M-020–M-135 (11 terrain, 1 coast hexside, 13 slope/`up`, 4 settlement, 32 unfinished railroad — the Matruh–Capuzzo–Tobruk line is printed blue — 4 false tracks from map titles and the frontier wire, 51 track crossings the redraw's 1 px dashes hid) + 33 rows verified as ours-right = **149 resolutions, at the cap**; 16 places; 50-hex sample 0/50 terrain misreads; EXTRACTION entry; all gates green. **122 hexside rows unresolved** (27 tracks we miss, 15 tracks alongside the unfinished railroad, 11 slopes, 9 tracks alongside ridges, the rest ones and twos) | #64 (draft) |
| C | Maps A, B, D, E | not started | — |
| D | docs | not started | — |

## Next steps

For the autopilot: #64 is at the cap and left as a draft per the spec (the plan would merge it); if Brian has merged it, open `autopilot/map-c-2` from `main` for the remaining 122 rows, otherwise keep resolving on #64 only if Feedback says the cap is lifted. Resolve the remaining rows (regenerate with `map_diff.py C`; crops with `map_sample.py C --hex <id>`), the two big buckets being tracks (78 the second database has that we do not — the redraw's 1 px dashes anti-alias out of the palette on sand and are darker than the rail grey near the frontier; a third extractor pass on the rail-class tolerance may be worth it before hand-resolving; the 38 the other way are done: 33 real crossings, 4 false reads corrected, 1 undecided), then place the Giarabub Oasis palm hexes, mark #64 ready, and go on to Task 15 (Part D of the primer on our Map C).

For Brian:

- **Malta numbering:** the printed inset has no hex numbers, so `M` hexes carry the VASSAL module's numbering (rows 05–13, cols 00–06). Norman's current code keys Malta as `M0604, M0607, M0705, M0806, M0906, M0907` — a different origin from the module's. If you want the module's numbering replaced, say so before Map C's Part D is published (Malta is not referenced there).
- **Valletta** (`M0805`) reads as sea — the Grand Harbour fills the hex centre; it is a `feature` place with `port: true` on a sea hex. Say if you would rather it were a land hex.
- **Map C items left as read** (the scan is not decisive at this resolution): C0611 (clear vs sand), C0818 (clear vs salt-marsh), C4905|C4906 (coast road or track); and `up` at C0323|C0423 — our band-side convention says C0323 is the higher hex, Norman's database says C0423 (a rough hill ringed by hachures); if his is right the convention needs a second look at the depressions. Seven sheet-edge slope/escarpment hexsides keep `up: null` by allowlist (the higher hex is on the adjoining sheet).
- **Unfinished railroad:** on the scan the whole Matruh–Capuzzo–Tobruk line is blue (the unfinished symbol) and the redraw draws it like a finished railway; 32 corrections say so. If part of it should be a finished railroad in 1940, say which stretch.
- **SPI 20.67** (the Axis chart that limits replacement point types): not printed on either player chart set or the shared sheet in the archive.org scan (headings jp2 111–178 listed) — if your copy has it, say where in Feedback.
- Earlier items (Learn page dark mode, formation charts 19.31–19.33, chart-vs-text disagreements, E-025 reading, three printed oddities, R-012/R-018/R-019) still stand — see the 2026-09-20 entry in the git history of this file if you want the detail.

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
