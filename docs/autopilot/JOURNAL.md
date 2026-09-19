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
