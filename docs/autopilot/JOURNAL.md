# Autopilot journal

One entry per run, newest last. For the next run, not for humans.

## 2026-09-19T04:15Z — autopilot/10-units-and-state
Done: branch created from origin/main; journal started.
In flight: rules/10-units-and-state.md (SPI §3, §6.2, §17) — not yet written.
Next: create .venv (README), fetch sections, read §3/§6.2/§17 from ~/.cache/cna-scans, write the file, run gates, draft PR.
Blocked: none

## 2026-09-19T04:17Z — autopilot/10-units-and-state
Done: PR #2 (draft). rules/10-units-and-state.md first draft covering SPI §3 only (types, classes, HQ 3.3x, characteristics 3.5, parenthesised ratings, type notes). .venv + section cache set up (not committed). Overlap gate passes after wording fixes.
In flight: §6.2 (CPA ratings, raw→actual, <5 raw rule) and §17 (cohesion/DP/RP) not yet restated; no data/ tables yet; no EXTRACTION.md entry; coverage not checked; spi-omit for 3.1 glossary and colour cases not yet added.
Next: read section-06.adoc (§6.2x) and section-17.adoc from ~/.cache/cna-scans/source/<commit>/, add "Capability point ratings" and "Cohesion" sections, badge 3.1 as spi-omit (glossary), run check_coverage --sections 3,6,17, add EXTRACTION entry, sidebar entry in site/, then gh pr ready.
Blocked: none

## 2026-09-19T04:42Z — autopilot/10-units-and-state
Done: finished the file. §6.2 (Cohesion) + §17 (Morale/Training/Voluntary surrender) restated; §3 omit-badges added; ruling R-001 (−26 threshold); sidebar entry; ignoreDeadLinks for future rules files; EXTRACTION entry. All gates pass (pytest 60, check_data, check_overlap, site:build). Committed + pushed; marking PR #2 ready.
In flight: none for file 1.
Next: file 2 = sequence of play (SPI §5, §7). Branch autopilot/20-sequence-of-play from origin/main once #2 merges (or stack on #2's tip if still open; --base autopilot/10-units-and-state). Coverage for §6.1/6.3 stays open — it belongs to file 3 (capability points, §6).
Blocked: none (Brian merges #2).

## 2026-09-19T04:41Z — autopilot/20-sequence-of-play
Done: branch created from tip of autopilot/10-units-and-state (stacked; PR #2 still open, no review comments).
In flight: rules/20-sequence-of-play.md (SPI §5, §7) — not yet written.
Next: read section-05/07 from ~/.cache/cna-scans/source/<commit>/, write the file matching 10-units-and-state.md conventions, sidebar entry, EXTRACTION entry, gates, draft PR --base autopilot/10-units-and-state.
Blocked: none

## 2026-09-19T04:42Z — autopilot/20-sequence-of-play
Done: rules/20-sequence-of-play.md complete (§5 + §7), sidebar, EXTRACTION entry; coverage 12/12, overlap OK, pytest 60, site builds. PR #3 marked ready (stacked on #2). Also fixed an overlap-gate hit in rulings/R-001.md on the #2 branch (pushed) — rulings/ is now scanned.
In flight: none for file 2.
Next: file 3 = capability points (SPI §6.1, §6.3 — §6.2 already in file 1). Branch autopilot/30-capability-points from tip of autopilot/20-sequence-of-play, --base autopilot/20-sequence-of-play while #3 is open.
Blocked: none (Brian merges #2, #3). Initiative Ratings Chart (7.2) needs the chart sheet captured before data/ transcription.

## 2026-09-19T04:43Z — autopilot/30-capability-points
Done: rules/30-capability-points.md prose complete (§6.1, §6.3 table inline), sidebar, EXTRACTION entry; overlap OK, coverage §6 20/20, pytest 60, site builds. PR #4 (draft, --base autopilot/20-sequence-of-play).
In flight: data/tables/cp-costs.json + data/schema/cp-costs.schema.json not written (design says tables go to data/ with the file that first needs them). check_data.py may need a loader for tables/ — check with a failing test first (TDD).
Next: write schema+table for CP costs (sources CNA1979:6.3, scan page from fetch.py), point the file's table at it, run check_data, then gh pr ready 4. Then file 4 = movement (§8) stacked on this branch.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:45Z — autopilot/30-capability-points
Done: data/tables/cp-costs.json + data/schema/cp-costs.schema.json (c90c89b); all gates pass; PR #4 marked ready (stacked on #3). Note: check_overlap scans only git-tracked files — run it after `git add`, not before.
In flight: none for file 3.
Next: file 4 = movement (SPI §8, plus Terrain Effects Chart → data/tables/terrain-effects.json; extend common.schema terrain enum). Branch autopilot/40-movement from tip of autopilot/30-capability-points, --base autopilot/30-capability-points while #4 is open.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:46Z — autopilot/40-movement
Done: branch from tip of autopilot/30-capability-points; rules/40-movement.md is a commented skeleton mapping SPI §8.1–8.9 to sections (no badges yet, so §8 coverage is 0 — expected).
In flight: file 4 (movement, §8, 658 source lines) — nothing restated yet.
Next: read section-08.adoc in full; restate 8.1–8.2 first (they are cited by 00-overview and 20-sequence-of-play), then 8.3 with the terrain-effects table + schema (extend common.schema terrain enum), then 8.4–8.9. Add sidebar entry, EXTRACTION entry. Remember: `git add` before check_overlap (it scans tracked files only). Open draft PR --base autopilot/30-capability-points.
Blocked: none (Brian merges #2, #3, #4 in order).

## 2026-09-19T04:47Z — autopilot/40-movement
Done: §8.1–§8.6 restated in rules/40-movement.md (ba7936a + this commit); sidebar entry; overlap OK; site builds. PR #5 draft (--base autopilot/30-capability-points). Coverage §8: 50/80.
In flight: file 4. Remaining: 8.7 rail (433–485), 8.8 Tripoli/Tunisia (486–558), 8.9 motorised/trucks (559–658; anchor #trucks is linked from 30-capability-points). Terrain Effects Chart: data/tables/terrain-effects.json + schema not started (chart sheet not in cache — check tools/fetch.py for chart pages; if unavailable, keep 8.37 spi-omit and say so in EXTRACTION). Remove the HTML skeleton comment at the top of the file when done. EXTRACTION entry not written.
Next: restate 8.7–8.9 in order, then EXTRACTION entry, then gates and gh pr ready 5.
Blocked: none (Brian merges #2, #3, #4 in order).
