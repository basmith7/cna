# AUTOPILOT.md — standing orders for unattended runs

Read by `~/Scripts/claude-autopilot.sh`, which cron launches every few hours
when the Claude plan has headroom. Each run is a fresh session with no memory
of the last one; this file plus the journal is the only continuity.

## Mission

**Mission 3, issued 2026-09-21: the map sub-project.** Missions 1 and 2 are
done; the `MISSION COMPLETE` / `MISSION 2 COMPLETE` entries in the journal
and `PROGRESS.md` refer to them and are not a reason to idle.

Two documents govern this mission — read both before touching anything:

- **Spec:** `docs/designs/2026-09-21-map-design.md` — what, why, the legal
  posture, the merge gates.
- **Plan:** `docs/plans/2026-09-21-map.md` — how, task by task with tests.
  Follow it in order; each task's steps are the unit of work. Where the plan
  and this file disagree, the plan wins; where the plan and the spec
  disagree, say so in the journal and follow the spec.

Precondition: PR #16 (`njharman_src` in `tools/sources.json`) must be on
`main`. If it is not, do Part A anyway (it does not need the diff) and stop
before Part B with a note in `PROGRESS.md` **Next steps**.

### Part A — plumbing on Malta (plan Tasks 1–13, one PR)

Branch `autopilot/map-a-malta`. Everything in `tools/`, `data/schema/`,
`data/map/sheets.json`, the extractor changes, `map_build.py`,
`map_render.py`, the `/map` page, `data/README.md`. After Task 6 the
extractor is frozen: any later change to `tools/map_extract.py` is its own
PR that regenerates every `data/map/raw/*.json`.

### Part B — Map C and Part D of the primer (plan Tasks 14–15, two PRs)

Branch `autopilot/map-c`, then `autopilot/learn-part-d`. Task 14's first
run also writes `map_diff.py` and `map_sample.py`. Hard limits: **150 diff
resolutions per PR**; a sheet does not merge with `up: null` on a slope or
escarpment hexside unless the `EXTRACTION.md` entry allowlists it with a
reason; the 50-hex sample is not optional.

### Part C — Maps A, B, D, E (plan Task 16, one PR per sheet)

Branches `autopilot/map-<letter>`, in the order A, B, D, E. Same procedure
and limits as Map C.

### Part D — docs (plan Task 17, one PR)

Branch `autopilot/map-docs`.

### Rules specific to this mission

- **Never commit** anything under `build/`, any `.png` / `.jpg` / `.npy` /
  `.csv` under `data/` or `site/public/map/`, `buildFile.xml`, or any file
  from `~/.cache/cna-njharman/`. Check `git show --stat HEAD` before every
  push. The hygiene test enforces part of this; you enforce the rest.
- **NJHarman's database is diff-only.** A correction file cites the scan
  (`seen`) and never the diff; `EXTRACTION.md` states counts only.
- Committed map data carries game facts only — no pixel coordinates, no
  coverage ratios.
- If the scan resolution is too low to decide a hex or hexside, leave it
  as the extractor read it, list the key in `PROGRESS.md` **Next steps**,
  and move on; Brian will look at his copy.
- Gates for every map PR, all green locally before `gh pr ready`:
  `pytest`, `check_data.py`, `map_build.py --check`, `map_render.py --check`,
  `check_overlap.py` (with and without arguments), `npm run test:site`,
  `npm run site:build`.

When Parts A–D are all merged: log `MISSION 3 COMPLETE` in the journal and
`PROGRESS.md` and do nothing further.

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
3. Otherwise start the next unfinished part of the mission, in order.
   Branch `autopilot/<part>-<slug>` from `origin/main` (e.g.
   `autopilot/a-coverage-gap`, `autopilot/b-rulings-combat`,
   `autopilot/c-terrain-effects`).
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
## <timestamp, local time> — <branch>
Done: <what landed, with commit shas>
In flight: <what is half-done and where>
Next: <the first concrete thing the next run should do>
Blocked: <anything only Brian can resolve, or "none">
```

Keep entries under ten lines. The journal is for the next run, not for humans;
Brian reads the PR description, so keep that current too (`gh pr edit --body`).
