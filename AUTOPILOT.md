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

Each file is its own PR against `main`. **You merge your own PRs** (merge
commit, `gh pr merge --merge --delete-branch`) once every review criterion
passes locally and CI is green (`gh pr checks --watch`). Nobody else will
merge them: "ready for review" is not a state this project has. A PR whose
CI is red is the first thing to fix in any run, before new work. Brian does not
review PRs; he reads `docs/autopilot/PROGRESS.md` and leaves feedback there. Common tables are transcribed into `data/` alongside the file that
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

You are in a dedicated clone owned by the autopilot (not Brian's checkout), on
`main`, freshly reset to `origin/main`. In order:

1. Read `docs/autopilot/PROGRESS.md`. Its **Feedback** section is Brian's
   voice: act on every item first, then move it to **Addressed** with a
   one-line reply. If an item changes the mission, it wins over this file.
2. `gh pr list --state open --label autopilot` — if an autopilot PR is open,
   its file is unfinished: check out that branch, read the last entry of
   `docs/autopilot/JOURNAL.md` on it, and continue. If its gates and CI
   already pass, merge it and move on.
3. Otherwise start the next file in the order above that has no merged PR.
   Branch `autopilot/<NN>-<slug>` from `origin/main`.
4. `docs/autopilot/JOURNAL.md` is the machine-to-machine handoff (below);
   `PROGRESS.md` is for Brian. Keep both.

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

Before the budget runs out, do both of these:

**1. Update `docs/autopilot/PROGRESS.md` on `main`** (commit directly to main
and push, it is a doc): rewrite the **Status** table and **Next steps** so a
human can see where things stand in thirty seconds, and file any replies under
**Addressed**. Do not touch **Runs and quota**; the cron script fills it.

**2. Append an entry to `docs/autopilot/JOURNAL.md`** and commit it on the
working branch:

```
## <timestamp, America/Phoenix> — <branch>
Done: <what landed, with commit shas>
In flight: <what is half-done and where>
Next: <the first concrete thing the next run should do>
Blocked: <anything only Brian can resolve, or "none">
```

Keep entries under ten lines. The journal is for the next run, not for humans;
Brian reads the PR description, so keep that current too (`gh pr edit --body`).
