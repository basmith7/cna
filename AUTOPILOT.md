# AUTOPILOT.md — standing orders for unattended runs

Read by `~/Scripts/claude-autopilot.sh`, which cron launches every few hours
when the Claude plan has headroom. Each run is a fresh session with no memory
of the last one; this file plus the journal is the only continuity.

## The goal

This repo and `basmith7/cna-engine` share one goal, and every mission in
either repo serves it:

> **An open-source, self-hostable digital *Campaign for North Africa*.**
> Two players play a scenario, and in the end the full campaign, in a
> browser, against each other, with the engine enforcing every rule. Each
> ruling is a switch, so a group picks its ruleset.

The two repos split the work:

- **cna (this repo)** is the rulebook: every SPI rule restated in our own
  words, every chart, map hex, scenario and OA sheet as data, and every
  ambiguity decided as a ruling. It is done when an engine can build the
  whole game from it without opening the SPI books. No engine code here.
- **cna-engine** builds the game from this repo: rules core, game state,
  turn sequence, then a server and browser client. It reads this repo as a
  submodule and never copies its prose.

The engine is the critical path. Order work here by what it needs next.

## Mission

The autopilot works through a **queue** of missions (issued 2026-10-06).
Each of Missions 1–5 took a run or two and then left the autopilot idle for
days, so finishing a mission now means starting the next one in the same
run. A `COMPLETE` entry in the journal or `PROGRESS.md` is never a reason
to idle.

The delegation of 2026-09-26 still stands: decide anything cheap to reverse
yourself. Anything Brian writes in **Feedback** wins. Bring him only
questions of fact that need his printed copy: add them to the `copy` group
of `docs/autopilot/decisions.json` and to **Next steps**, and leave the data
as read.

### Requests from cna-engine come first

Every run, after **Feedback** and before the queue, read the **Requests for
cna** section of cna-engine's `docs/autopilot/PROGRESS.md`
(`gh api repos/basmith7/cna-engine/contents/docs/autopilot/PROGRESS.md --jq .content | base64 -d`).
Each request is a gap the engine hit: a missing table, a ruling it cannot
model, data in the wrong shape. Handle each as one PR, branch
`autopilot/req-slug`, and note the PR number in this repo's `PROGRESS.md`
under **Addressed**; the engine's autopilot clears its own list. A request
that is really a whole mission goes into the queue instead.

### Queue

| # | Mission | SPI | Cases | State |
|---|---|---|---|---|
| 1–5 | Land Game, rulings, map, decision board, Logistics Game | §1–32, §48–58 | | done |
| 6 | **Scenarios and OA sheets** | §59–65 | about 170 | done |
| 7 | **The Air Game** | §33–47 | about 430 | done |

Scenarios come before the Air Game because the engine cannot set up a game
without them, while the Air Game is an optional module (§32 and §58 already
abstract it). The current mission is the first row not marked `done`. When
its last part merges: log `MISSION n COMPLETE` in the journal and
`PROGRESS.md`, set its row to `done` and the next row to `next` (in its
docs PR), and go straight on to the next mission's Part 0. Case counts come
from `rules/coverage.md`.

### Every mission's parts

Missions 1–5 came with a spec and plan written with Brian. Queued missions
don't: the autopilot writes its own as Part 0. Then the parts follow the
Mission 5 shape unless the mission's spec says otherwise.

0. **Spec and plan**, one PR, branch `autopilot/m6-spec` (and so on). Write
   `docs/designs/YYYY-MM-DD-slug-design.md` and `docs/plans/YYYY-MM-DD-slug.md`
   in the shape and depth of the Logistics Game pair
   (`docs/designs/2026-09-27-logistics-game-design.md`,
   `docs/plans/2026-09-27-logistics-game.md`): goal, scope with cases per SPI
   section, in and out, a decisions table, merge criteria, order; plan tasks
   one PR each. The goal section says how the mission serves **The goal**
   above. Every decision is yours under the delegation and must be
   reversible with one PR; say so in the spec's header, as Mission 5's does.
   Merge it once the gates pass, then follow the plan task by task. Where a
   plan and its spec disagree, follow the spec and say so in the journal.
1. **Tooling**, if the plan needs any.
2. **Seed NJHarman's items** on the mission's topic as rulings and variants.
3. **Rules files**, one PR per file, charts as `data/tables/*.json`.
4. **Decide every new ruling**, one PR each, by the procedure below.
5. **Docs**: README, overview links, design Status, this queue.

Mission notes, for the spec to take up:

- **6, scenarios and OA sheets.** §59–65 as rules prose, plus scenario
  set-ups, OA sheets and reinforcement schedules as `data/` JSON where the
  scans support it, and the per-unit figures `data/README.md` lists as
  expected from the OA sub-project. Shape the data for an engine that loads
  a scenario and places every unit: check the schema against what
  cna-engine's `cna-data` crate already reads. Values read from scans get
  the same cross-checks as the map and charts; what the scans cannot settle
  goes to the `copy` group for Brian, and the data stays as read. **Part 1
  of the plan is one small Land Game scenario, complete** (set-up, OA,
  victory conditions), merged before anything else in the mission: it is
  step 1 of the *Path to a playable game* Brian agreed on 2026-10-07, and
  cna-engine's Mission 2 is built on it. Pick the smallest scenario that
  needs neither the Air Game nor the Logistics Game, and say why in the
  spec. The rest of the scenarios and the OA sheets follow.
- **7, the Air Game.** §47 (the Air Game's own logistics) belongs here;
  Mission 5 left it out on purpose. Use a `rules/air/` folder and sidebar
  group, as `rules/logistics/` did. State exactly which parts of §32
  (`rules/95-abstract-logistics-and-air.md`) and §58
  (`rules/logistics/60-abstract-air.md`) the Air Game replaces, so an engine
  has one switch. At about 430 cases this is over twice Mission 5: plan for
  several runs, and keep each rules file under about 70 cases.

### After the queue: the finish line

When Mission 7 is complete, every SPI section is covered and the rulebook
is done. From then on this repo works only on **Requests from cna-engine**
(above) and Brian's **Feedback**. Do not start missions of your own: no
polish passes, no site features nobody asked for. With nothing requested,
say so in **Next steps** and stop; idle runs cost almost nothing, and the
quota is better spent by cna-engine.

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
