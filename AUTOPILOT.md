# AUTOPILOT.md — standing orders for unattended runs

Read by `~/Scripts/claude-autopilot.sh`, which cron launches every few hours
when the Claude plan has headroom. Each run is a fresh session with no memory
of the last one; this file plus the journal is the only continuity.

## Mission

**Mission 5, issued 2026-09-27: the Logistics Game (§48–58).** Missions 1–4
are done; their `COMPLETE` entries in the journal and `PROGRESS.md` are not a
reason to idle.

Two documents govern this mission. Read both before touching anything:

- **Spec:** `docs/designs/2026-09-27-logistics-game-design.md`
- **Plan:** `docs/plans/2026-09-27-logistics-game.md`. Follow it task by
  task. Where the plan and the spec disagree, follow the spec and say so in
  the journal.

The delegation of 2026-09-26 still stands: decide anything cheap to reverse
yourself. Anything Brian writes in **Feedback** wins. Bring him only
questions of fact that need his printed copy: add them to the `copy` group
of `docs/autopilot/decisions.json` and to **Next steps**, and leave the data
as read.

Parts, in order (plan task numbers):

1. **Tooling** (Task 1), one PR.
2. **Seed NJHarman's logistics items** (Task 2), one PR.
3. **Rules files** (Tasks 3–9), one PR per file, in the plan's order.
4. **Decide every logistics ruling** (Task 10), R-020–R-022 included, one
   PR each, by the procedure below.
5. **Docs** (Task 11), one PR.

When all five are merged, log `MISSION 5 COMPLETE` in the journal and
`PROGRESS.md` and do nothing further.

### How to decide a ruling

1. Read the ruling file, the rules prose for every case in `affects`, and
   every ruling already `accepted`.
2. Choose, in this order of preference: the reading the printed text
   supports, unless the ruling's Rationale shows it produces an exploit or
   contradicts another rule; then consistency with accepted rulings; then
   whichever is simpler for an engine to implement.
3. Fill in **Decision** ("Option N." plus one sentence) and **Rationale**
   (why, in our own words; cite a probe's finding where there is one, linked
   to `probes/<id>.json` in cna-engine at its commit). Set
   `status: accepted`. Edit the rules prose to show the result, with
   `::: ruling R-nnn` above the block. Run `tools/gen_pages.py`.
4. One PR per ruling, branch `autopilot/ruling-r-nnn`. Merge it once the
   gates below are green.

### Gates for every PR

All green locally before `gh pr ready`: `pytest`, `check_data.py`,
`check_overlap.py` (with and without arguments), `tools/gen_pages.py` (no
diff left over), `npm run test:site`, `npm run site:build`. Never commit
anything under `build/`. Add `check_coverage.py --sections` for the sections the PR draws on
(0 uncovered).

## Picking up where the last run left off

You are in a dedicated clone owned by the autopilot (not Brian's checkout), on
`main`, freshly reset to `origin/main`. In order:

1. Read `docs/autopilot/PROGRESS.md`. Its **Feedback** section is Brian's
   voice: act on every item first, then move it to **Addressed** with a
   one-line reply. If an item changes the mission, it wins over this file.
   Items from the decision board (`tools/decisions_page.py`) name a ruling
   id or a `docs/autopilot/decisions.json` id: once an answer lands, drop
   that entry from `decisions.json`. A new question for Brian goes into
   `decisions.json` as well as **Next steps**.
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
