# Logistics Game Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restate SPI §48–58 (the Logistics Game) in `rules/logistics/`, with
its charts as data, NJHarman's logistics items seeded, and every logistics
ruling decided.

**Architecture:** This is the same pipeline the Land Game used (Missions 1–2):
source text, our prose with `::: spi` badges, the overlap gate, the coverage
report, `EXTRACTION.md`, and charts transcribed as JSON with a schema and a
test. The one structural change: rules files may now live in a subfolder.

**Tech Stack:** Python 3.12 tools (`tools/`), pytest, VitePress site,
JSON Schema.

**Spec:** `docs/designs/2026-09-27-logistics-game-design.md`. Read the
living-rules design (`docs/designs/2026-09-18-cna-living-rules-design.md`)
for writing rules and for the review criteria.

## Global Constraints

- No SPI text in the repo or on the site. Paraphrase, and cite case numbers.
- Every rules PR passes: `pytest`, `check_data.py`,
  `check_overlap.py` (with and without arguments),
  `check_coverage.py --sections <the sections drawn on>` (clean for them),
  `tools/gen_pages.py` (no diff left over), `npm run test:site` and
  `npm run site:build`.
- Examples are our own situations, never SPI's with new numbers.
- Tables are recorded **as printed**. Corrections go in `data/errata/` overlays
  (SPI errata) or in rulings (ours).
- Rulings follow `rulings/README.md`; NJHarman quotes follow its *Quoting a
  third-party source* section and are listed in `ATTRIBUTION.md`.
- One PR per rules file. Chart transcription may go in a PR of its own just
  before the file that needs it.

## Review Focus

1. **The Land Game must still read correctly on its own.** A `::: note`
   pointer to the Logistics Game must never change a Land Game rule body.
   Check: `git diff main -- rules/*.md` shows only added `::: note` blocks.
2. **Links into the subfolder.** A generated page (`changes.md`,
   `coverage.md`) must link `logistics/10-fuel.md` correctly, not
   `10-fuel.md`. Tested in Task 1.
3. **Table cells that the second scan cannot confirm** must be listed in the
   table's `notes`, never silently taken from one source. The cross-check
   count goes in `EXTRACTION.md`.
4. **Per-unit values that live on OA sheets or counters** must be named as
   variables in the prose and recorded in `data/README.md` as expected from
   the OA sub-project. Never invent them.
5. **§47 is out of scope.** Its cases stay uncovered in the report; do not
   `spi-omit` them.

---

### Task 1: Rules subfolders in the tooling; sidebar group

**Files:**
- Modify: `tools/gen_pages.py` (`_rules_files`, `collect_annotations`, `render_coverage`)
- Modify: `tests/test_gen_pages.py`
- Modify: `site/.vitepress/config.mts` (sidebar)
- Modify: `.github/workflows/*.yml` (coverage report `--sections 1-32,48-58`)

- [ ] **Step 1: Write the failing test** (append to `tests/test_gen_pages.py`; follow the file's existing fixture style for building a temporary `rules/` tree)

```python
def test_subfolder_files_are_collected_with_their_path(tmp_path):
    rules = tmp_path / "rules"
    (rules / "logistics").mkdir(parents=True)
    (rules / "10-alpha.md").write_text("---\ntitle: Alpha\n---\n::: ruling R-001 — a\n")
    (rules / "logistics" / "10-fuel.md").write_text("---\ntitle: Fuel\n---\n::: ruling R-030 — b\n")
    ann = gp.collect_annotations(rules)
    assert ann["rules/logistics/10-fuel.md"]["rulings"] == [("R-030", "b")]
    assert "rules/10-alpha.md" in ann
```

Use the module alias the file already uses for `tools/gen_pages.py`.

- [ ] **Step 2: Run it.** `.venv/bin/python -m pytest tests/test_gen_pages.py -q`. Expected: FAIL (key missing).

- [ ] **Step 3: Implement.** In `_rules_files`, change `rules_dir.glob("*.md")` to `rules_dir.rglob("*.md")`, still excluding `GENERATED`. Wherever a key or a link is built from `p.name`, use `p.relative_to(rules_dir).as_posix()` instead: the `f"rules/{p.name}"` key in `collect_annotations`, and `badges[...]`/`titles[...]` and the `./{f}` link in `render_coverage`. Then check `render_changes` for the same pattern.

- [ ] **Step 4: Run it**, then `.venv/bin/python tools/gen_pages.py`. Expected: PASS, and no change to the committed pages (there are no subfolder files yet).

- [ ] **Step 5: Sidebar and CI.** In `config.mts`, add a second group after the Land Game group:

```ts
{
  text: 'Logistics Game',
  items: [
    // one entry per file as it lands, e.g.
    // { text: 'Overview & sequence', link: '/rules/logistics/00-overview-and-sequence' },
  ],
},
```

Leave `items` empty in this task; each file's PR adds its own entry, because a link to a page that does not exist fails the build. In the workflow, change the coverage report to `--sections 1-32,48-58` (`parse_sections` already accepts comma lists).

- [ ] **Step 6: Gates and PR.** Run the full gate list, open the PR (`autopilot/l-tooling`), and merge on green CI.

### Task 2: Seed NJHarman's logistics items

**Files:**
- Create: `rulings/R-0nn.md` (numbered on from the highest existing `R-nnn`), `rulings/V-0nn.md`
- Modify: `EXTRACTION.md` (the NJHarman table), `ATTRIBUTION.md` if a new quote source appears, `rulings/register.md` (generated)

The four items Mission 2 set aside "for a later spec" (the `EXTRACTION.md` NJHarman table, rows *Coastal Shipping*, *Unlimited Supplies*, *Leaky Gas Tanks*, *Logistics (Additions section)*):

- *Coastal Shipping* (CORRECTION/CLARIFICATION, shipping phase name): a `proposed` ruling.
- *Unlimited Supplies* (CLARIFICATION, 60.44 vs 57.0, Cairo only): a `proposed` ruling, `affects: [57.0, 60.44]`.
- *Leaky Gas Tanks* (self-tagged as a possible CHANGE: fuel in tanks does not evaporate): a **variant**, because the item itself says it may change the rule.
- *Tobruk port efficiency is 5* (CORRECTION): a `proposed` ruling, `affects` the §55 case that sets Tobruk's efficiency.

- [ ] **Step 1:** Re-read `~/.cache/cna-scans/njharman-clean.txt` for any other item touching §48–58 that the table does not list. Add each one to the table and seed it the same way.
- [ ] **Step 2:** Write each file by the conventions of the existing seeded rulings (`rulings/R-002.md` is a good model): verbatim quote plus footnote in **Problem** and **Options**, his leaning in **Options**, "None yet — proposed." in **Decision**.
- [ ] **Step 3:** Change each table row's last column from "not imported — … later spec" to the new id. Run `tools/gen_pages.py`.
- [ ] **Step 4:** Run the gates, then open and merge the PR (`autopilot/l-seed`). One PR is enough here (four or five items).

### Tasks 3–9: One rules file each

Do this procedure once per file, in this order:

| Task | File | SPI | Charts expected (locate them; the list may be incomplete) |
|---|---|---|---|
| 3 | `rules/logistics/00-overview-and-sequence.md` | 48 | Logistics sequence of play |
| 4 | `rules/logistics/10-fuel.md` | 49 | Fuel consumption rates; evaporation |
| 5 | `rules/logistics/20-ammunition-and-stores.md` | 50, 51 | Ammunition Consumption Rates Chart |
| 6 | `rules/logistics/30-water.md` | 52 | Water Availability Table; Poisoning and Sweetening Wells Table; water usage rates |
| 7 | `rules/logistics/40-trucks-and-dumps.md` | 53, 54 | Truck Characteristics Chart; Equivalent Weights Chart |
| 8 | `rules/logistics/50-ports-and-shipping.md` | 55, 56, 57 | Port Capacity and Efficiency Level Chart; Axis Naval Convoy Level Chart; Axis Convoy Capacity Table |
| 9 | `rules/logistics/60-abstract-air.md` | 58 | any charts in §58 (the Abstract Truck Loss Chart is already `data/tables/motorisation-losses.json`: reuse it, do not duplicate) |

Branch `autopilot/l-<file-slug>`. For the file:

- [ ] **Step 1: Read the source.** `.venv/bin/python tools/fetch.py sections`, then read `~/.cache/cna-scans/source/<commit>/section-NN.adoc` for each SPI section. Note every case id, every mechanic, every chart and every place the text is ambiguous or contradicts itself or the Land Game.

- [ ] **Step 2: Locate each chart.** Search `~/.cache/cna-scans/djvu.xml` (the OCR of the archive.org scan, one `OBJECT` per jp2 page) for the chart's title. Record its jp2 page, fetch it with `.venv/bin/python tools/fetch.py pages <n>`, and view it; rotate it if it is printed sideways. Find the same chart in a second scan: the Discord 300 dpi chart PDFs under `~/.cache/cna-scans/discord/`, or Clay Stone's *Air & Logistics* PDF (add it to `tools/sources.json` with a hash if you fetch it). If a chart is printed only as a table inside the rules text, the transcription in the source `.adoc` counts as the second reading.

- [ ] **Step 3: Transcribe each chart (TDD).** For each chart:
  1. Write `data/schema/<concept>.schema.json`.
  2. Write `tests/test_<concept>.py` first. Assert the shape and at least three cells read by hand from the scan, and any row or column totals the chart has as invariants. Model it on `tests/test_construction.py`.
  3. Run it: expect FAIL.
  4. Write `data/tables/<concept>.json`, with `sources: ["CNA1979:<case>", "scan:p<jp2>"]` and `notes`.
  5. Diff the two readings cell by cell. Resolve each disagreement from the clearer scan, and list anything unresolved in `notes`.
  6. Run the test and `check_data.py`: expect PASS.
  7. Apply any SPI errata item for the chart as an overlay in `data/errata/E-nnn.json` (see `data/errata/INDEX.md`).

- [ ] **Step 4: Write the prose.** Frontmatter `title:` and `status: provisional`. Organise by our model; each block is preceded by `::: spi <cases>` (primary), with `::: spi-ref` for later mentions and `::: spi-omit <case> — <reason>` for pure commentary. Define terms in bold on first use, number the steps, use *may / must / may not*, and link the charts' data files. Apply every errata item for these cases, with `::: errata E-nnn — summary`. End with the provenance line. For the overview (Task 3), also state which parts of `rules/95-abstract-logistics-and-air.md` the Logistics Game replaces and which stay.

- [ ] **Step 5: Land Game pointers.** For each Land Game passage this file replaces, add below it:

```markdown
::: note
In the Logistics Game this is replaced by [<topic>](logistics/<file>.md#<anchor>).
:::
```

Change nothing else in that Land Game file.

- [ ] **Step 6: Rulings.** For every ambiguity noted in Step 1, open `rulings/R-nnn.md` as `proposed`, with at least two options and their consequences, following `rulings/README.md`. Do not decide it here; Task 10 does.

- [ ] **Step 7: Gates.**

```bash
.venv/bin/python -m pytest -q
.venv/bin/python tools/check_data.py
.venv/bin/python tools/check_overlap.py && .venv/bin/python tools/check_overlap.py rules/logistics/<file>.md
.venv/bin/python tools/check_coverage.py --sections <NN[,NN]>      # 0 uncovered for these sections
.venv/bin/python tools/gen_pages.py && git status --short          # commit what it regenerated
npm run test:site && npm run site:build
```

  If the overlap gate fails, rephrase; never widen `tools/overlap-allowlist.txt` for prose.

- [ ] **Step 8: Docs and PR.** Add an `EXTRACTION.md` entry (cases read → mechanic → how we expressed it; charts with their jp2 pages and cross-check counts) and the sidebar entry. Then PR, CI green, merge (`gh pr merge --merge`).

### Task 10: Decide the logistics rulings

- [ ] For each `proposed` ruling whose `affects` falls in §48–58, R-020, R-021 and R-022 included, follow **How to decide a ruling** in `AUTOPILOT.md` (Mission 4 wording, repeated in Mission 5): one PR each, rules prose updated with `::: ruling R-nnn`, register regenerated. Variants stay `recorded`.

### Task 11: Docs

- [ ] `README.md` layout table: add `rules/logistics/`. `rules/00-overview.md`: one paragraph linking the Logistics Game module. The design's **Status** line: "complete, PRs #…". `data/README.md`: the OA-sheet variables the prose names (Review Focus 4). One PR (`autopilot/l-docs`).
