# AUTOPILOT.md — standing orders for unattended runs

Read by `~/Scripts/claude-autopilot.sh`, which cron launches every few hours
when the Claude plan has headroom. Each run is a fresh session with no memory
of the last one; this file plus the journal is the only continuity.

## Mission

**Mission 4, issued 2026-09-26: decide the open questions.** Missions 1–3
are done; their `COMPLETE` entries in the journal and `PROGRESS.md` are not a
reason to idle.

On 2026-09-26 Brian delegated every decision that is cheap to reverse. A
ruling is cheap to reverse: anyone can dispute and supersede it
(`rulings/README.md`), and in the engine it is one switch. The policy is the
last section of the cna-engine spec,
<https://github.com/basmith7/cna-engine/blob/main/docs/designs/2026-09-26-engine-probes-design.md>.
The one exception: anything Brian writes in **Feedback** about a ruling or a
board item wins.

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

### Part A: interpretive rulings (one PR each)

R-002, R-003, R-004, R-005, R-006, R-007, R-008, R-010, R-013, R-014, R-016,
R-017, R-019. For R-019 the map now exists (`data/map/`): count the sea hexes,
then decide.

### Part B: board defaults (one PR, `autopilot/board-defaults`)

Apply these, then delete each item from `docs/autopilot/decisions.json`:

- `map-vertex`: record neither (no data change).
- `map-rail-along-hexside`: keep only the track crossing (no data change).
- `map-villages`: no; the scenarios sub-project will add them.
- `map-malta-numbering`: keep the VASSAL numbering.
- `map-valletta`: stays a sea hex with a port.
- `chart-e025`: the current reading stands.
- `chart-vs-text`: leave the disagreements as noted in the tables; cna-engine
  slice 4 probes them with R-018.
- `site-learn-dark`: keep the light island.
- `site-original-text`: check it yourself. Load a rules page on the deployed
  site in headless Chrome (`/usr/bin/google-chrome`) and click one *Original
  text* block. If it works, delete the item. If it is broken, fix it in its own
  PR.

`chart-oddities` waits for cna-engine's `probes/chart-oddities.json`. Once
that file exists, record what it shows in the table's notes. A cell that
cannot be rolled needs no ruling. For any gap that can be rolled, open a
proposed ruling (the next `R-nnn`) with the options (the neighbouring row
above, the row below, no loss) and decide it as in Part C.

### Part C: rulings a probe covers (one PR each)

R-011 and R-012 (cna-engine slice 1), R-009 and R-015 (slice 2), R-001
(slice 3), R-018 (slice 4). A ruling is ready once its probe is on
cna-engine `main`:

```bash
gh api -H 'Accept: application/vnd.github.raw' repos/basmith7/cna-engine/contents/probes/R-012.json
```

A 404 means it is not ready. Skip it; that is not a blocker. Once Parts A and
B are done and every remaining Part C ruling is waiting on a probe, end the
run early and say so in the journal.

### Leave alone

- R-020, R-021, R-022. They need the Logistics Game (§47–58) restated first.
- The `copy` group in `decisions.json`. Only Brian's printed copy can answer
  those; they stay as read. Add to it only questions of fact that need his
  copy. Decide everything else yourself.

When Parts A and B are merged and all six Part C rulings are accepted, log
`MISSION 4 COMPLETE` in the journal and `PROGRESS.md` and do nothing further.

### Gates for every PR

All green locally before `gh pr ready`: `pytest`, `check_data.py`,
`check_overlap.py` (with and without arguments), `tools/gen_pages.py` (no
diff left over), `npm run test:site`, `npm run site:build`. Never commit
anything under `build/`.

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
