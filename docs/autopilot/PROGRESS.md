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

**MISSION 2 COMPLETE** (2026-09-20), with one item only Brian can close: SPI 20.67, the Axis Replacement Point Type Limitations Chart, is not printed on either player chart set or the shared sheet in the archive.org scan (every chart heading on jp2 111–178 was listed) — if your copy has it, say where in Feedback.

Mission 1 (rules files 1–10 and site phase 2): all merged, PRs #2–#13.

| Part | What | State | PR |
|---|---|---|---|
| A | close the 30-case Land Game coverage gap (§1, §2, §4, 17.2) | **merged** — §1–32 coverage 974/974 | #17 |
| B | seed rulings from NJHarman (CORRECTION / CLARIFICATION / INTERPRETATION, Land Game topics) | **merged** — R-002–R-019 (18 proposed rulings), `rulings/register.md` generated, 5 items recorded as not imported | #18, #20–#26 |
| C | chart sheet tables into `data/tables/`, cross-checked | **merged** — 33 tables, every one cross-checked cell by cell against a second scan with 0 differences; three errata overlays (E-008, E-012, E-025) plus E-014 and E-031 added this run. Only 20.67 outstanding (see above) | #27–#55 |
| D | publish the primer (Parts A–C) as the site's *Learn* page | **merged** — `/learn` in the nav, sidebar A/B/C, tables from `data/`, case links into the rules; Part D of the primer stays local until the map is redrawn | #56, #57 |

## Next steps

Nothing queued for the autopilot. For Brian:

- **Look at `/learn` on the deployed site in both colour schemes.** The primer keeps its own light panels with explicit text colours, so in dark mode it is a light island rather than themed; if you want it themed, the CSS is `CSS` in `tools/learn_page.py` (scoped under `.learn` by `scoped_css()`).
- **Formation charts (19.31–19.33) deserve a glance** — they are symbol grids and two spots were read with less confidence (noted in `data/tables/formation-organisation.json`): the 5th Light's second infantry battalion, and which Ramcke battalion is the heavy-weapons one.
- **Chart vs rules-text disagreements**, kept as printed and noted in the tables, the rules pointer paragraphs and `EXTRACTION.md` — candidates for rulings, none opened: 24.17 temporary repair facility 50 fuel + 250 stores / 1 stage vs 24.82's 150 fuel + 250 stores / 3 stages; facility rebuild 10 fuel + 50 stores vs 24.84's 30 + 50; real dump 10 stores vs 20 (R-018); 27.91 guarded dump raided on a total **≥** the guards' defence (chart) vs **>** (27.5x text).
- **E-025 reading, please check:** the errata says the Weather Table is "completely backwards". Applied as: each season's game-turn bands swap with the opposite season's (turns 1–12 → autumn); weather dice ranges stay with their season names. `data/errata/E-025.json` is the one file to change.
- **Cross-check sources:** Clay Stone's PDFs are the rules only, no charts. Chart-sheet and player-set tables were checked against the Discord 300 dpi *Shared / Axis / Commonwealth Charts.pdf*; the two rulebook-page charts (8.37 Terrain Effects, 8.89 off-map distances — found on jp2 69–70, not the chart sheet) against the Discord converted rulebook scan. If you want a different second source, say so.
- **Three printed oddities** (both scans agree, not in the 1979 errata), kept as printed and declared in `known_gaps` / notes: close assault attacker −2 / 20 % reads "13-18"; close assault defender +2 has no cell for 34–36; Morale Modifier −4 has no cell for 56. They want rulings.
- R-012 (15.29) and R-018 (dump cost) are the seeded rulings where printed text and sensible reading pull apart; R-019 needs a hex count on the map.
- Click one *Original text* block on the deployed site to confirm the viewer works in a browser.

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
