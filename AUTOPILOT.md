# AUTOPILOT.md — standing orders for unattended runs

Read by `~/Scripts/claude-autopilot.sh`, which cron launches every few hours
when the Claude plan has headroom. Each run is a fresh session with no memory
of the last one; this file plus the journal is the only continuity.

## Mission

Carry out **Process step 3** of `docs/designs/2026-09-18-cna-living-rules-design.md`:
restate the Land Game, one rules file per system, in this order:

1. units & state
2. sequence of play
3. capability points
4. movement
5. stacking & ZOC
6. combat
7. organisation
8. engineering
9. special
10. §32

Each file is its own PR against `main`. Brian reviews and merges; **you never
merge**. Common tables are transcribed into `data/` alongside the file that
first needs them. Rulings are logged as you hit them (`rulings/README.md`).
Every PR must meet the *Review criteria for a rules PR* in the design doc,
including the `EXTRACTION.md` entry, before you mark it ready.

The design and the scaffold plan are already approved: do **not** brainstorm or
write a new spec. Do use TDD for any `tools/` or `site/` change, and read
`rules/00-overview.md`, `rules/glossary.md`, `docs/plans/2026-09-18-scaffold-and-overview.md`
and `EXTRACTION.md` before writing prose so the new file matches their voice,
badge usage and provenance conventions. When step 3 is complete, move to step 4
(site phase 2) and then stop: log `MISSION COMPLETE` in the journal and do nothing further.

## Picking up where the last run left off

In order:

1. `git fetch origin` and `git status`. Abort and log if the tree is dirty on a
   branch you did not create (someone is working here).
2. `gh pr list --state open --label autopilot` — open autopilot PRs.
   - If a PR has review comments from Brian that are not yet addressed, address
     those first, on that branch. That is the highest-priority work.
   - If a PR's file is unfinished (its journal entry says so), continue on that branch.
3. Otherwise start the next file in the order above that has neither a merged
   nor an open PR. Branch `autopilot/<NN>-<slug>` from `origin/main`; if an
   earlier autopilot PR is still open, branch from **its tip** instead and open
   the new PR with `--base` set to that branch (stacked, so `EXTRACTION.md` and
   the sidebar do not conflict; GitHub retargets it to `main` when the base merges).
4. Read `docs/autopilot/JOURNAL.md` (create it if missing) — the last entry
   says exactly what was in flight.

Source text: `.venv/bin/python tools/fetch.py sections` populates `~/.cache/cna-scans`
(needed by the overlap gate). Create `.venv` per the README if missing.

## Working rules

- Keep going until the wall-clock budget in the prompt is nearly spent; do not
  stop early because a "natural" checkpoint arrived.
- Commit small and often, push after every commit. Draft the PR
  (`gh pr create --draft --label autopilot`) as soon as the branch has one commit,
  then `gh pr ready` only when every review criterion passes locally
  (`pytest`, `check_data.py`, `check_overlap.py`, `check_coverage.py` for the
  sections drawn on, `npm run site:build`).
- Never touch `main` directly, never force-push, never rewrite history.
- Never commit anything from `~/.cache`, `node_modules/`, `.venv/`, or SPI text.
- If a gate fails and you cannot fix it within the budget, leave the PR as a
  draft and say why in the journal.
- Commit messages end with the attribution trailer the harness gives you.

## Handing off

Before the budget runs out, append an entry to `docs/autopilot/JOURNAL.md`
and commit it on the working branch:

```
## <UTC timestamp> — <branch>
Done: <what landed, with commit shas>
In flight: <what is half-done and where>
Next: <the first concrete thing the next run should do>
Blocked: <anything only Brian can resolve, or "none">
```

Keep entries under ten lines. The journal is for the next run, not for humans;
Brian reads the PR description, so keep that current too (`gh pr edit --body`).
