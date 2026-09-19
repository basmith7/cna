# Extraction log

Evidence of the idea/expression split. One entry per rules file, appended in
the PR that adds or substantially rewrites the file.

## Format

```
## rules/<file>.md — <date>
- Source cases read: <SPI case ranges>
- Mechanics identified: <bullet list of the game-mechanical facts extracted>
- How we expressed it: <structure chosen, terms renamed, what was merged/split, what was omitted and why>
- Errata applied: <E-ids or "none">
- Rulings raised: <R-ids or "none">
```

## Entries

## rules/00-overview.md — 2026-09-18
- Source cases read: 1.0, 2.0, 3.21–3.22, 5.1–5.2, 6.11–6.17, 6.21–6.26, 7.11–7.16, 8.2, 8.23, 8.37, 10.0, 11.31–11.35, 15.5, 15.73, 18.0, 21.0, 32.11–32.16
- Mechanics identified: three nested games with §32 abstraction; turn = 3 stages, stage = A/B halves; phase order A–L (no I) with F–L per player; G as a repeatable 4-segment cycle with the 2-hex / reserve re-move restriction; combat step order; CPA covering both halves, overspend → DP → cohesion; TOE points and ratings; type vs class; terrain costs, breakdown, ZOC, reaction; raw÷10 rounding and the <5 raw rule; two-dice two-readings; differential CRT with column shifts.
- How we expressed it: a system-model summary (time → stage shape → currency → units → movement → combat → loops → roles), tables for the phase list and file map, no procedures — every mechanic here is restated in full in its system file; SPI's team roles reduced to advisory; all citations as `spi-ref`.
- Errata applied: none (no values stated).
- Rulings raised: none.

## rules/glossary.md — 2026-09-18
- Source cases read: 2.0 (term list), 3.21, 3.22, 3.3, 5.1, 5.2, 6.11–6.26, 7.1, 8.0, 8.2, 8.37, 9.0, 10.0, 11.0, 11.3, 12.0, 12.6, 13.0, 14.0, 15.0, 15.5, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 29.0, 32.1
- Mechanics identified: the vocabulary an engine needs as state and enums — CP/CPA, cohesion (DP/RP), TOE points, raw/actual conversion, unit type vs class, reserve/reaction/continual movement, the combat step names, initiative, weather, ZOC, stacking, supply unit.
- How we expressed it: one table, our short definitions, each pointing to the system file that owns the full rule; SPI's glossary prose was not reused, and SPI's role definitions were reduced to the Overview's one paragraph.
- Errata applied: none.
- Rulings raised: none.

## rules/10-units-and-state.md — 2026-09-18
- Source cases read: 3.0–3.5, 3.21–3.23, 3.31–3.36, 3.61–3.62, 6.2, 6.21–6.29, 17.0–17.6, 17.21–17.28, 17.31–17.37, 17.51–17.56
- Mechanics identified: unit type enum and the combat-unit set; the four target classes and the split-target rule for part-armoured guns; HQ as an aggregate (strength, slowest-unit CPA, stacking, capture, gun-HQs, armour-HQ tank element); the per-unit characteristic list; parenthesised fallback ratings; type notes that carry rule effect. Cohesion as one signed level driven by DP (CP overspend; ≥30% assault loss) and RP (rest to ≤0; three per assault-eviction), applied immediately, capped +10, with the −26 immobilise/surrender floor and the largest-unit / averaging rule for mixed levels. Morale: fixed basic rating −3…+3, parent-formation inheritance, cohesion→modifier via the Morale Modification Table (sequential 11–66), ±3 cap, −17/+8 clamp rows, the Surrender column and the +1-morale ignore rule, Rommel +1. Training (Commonwealth-only, six-stage +1, zero-CP requirement, instruction-battalion and area conditions). Voluntary surrender procedure and self-destruction die rolls.
- How we expressed it: split §6.2 and §17 into topic sections (Cohesion, Morale, Training, Voluntary surrender) under the same file, since all describe unit state; DP/RP presented as two operators on one level rather than SPI's separate-counter framing; cross-referenced the Morale Modification and Training charts out to the files that own those tables (spi-omit, not transcribed here — chart values are not in the rules text); §3.1 term list deferred to the glossary; §3.61–3.62 hidden-information rules deferred to the §32 file; §3.0/§3.2 headers omitted. Examples from SPI reproduced only as mechanics, not verbatim.
- Errata applied: none identified (Sept 1979 errata not yet transcribed into the repo; no data values are asserted in this file).
- Rulings raised: R-001 (the −26 disorganisation threshold — cohesion level vs disorganisation-point count).

## rules/20-sequence-of-play.md — 2026-09-19
- Source cases read: 5.0–5.2, 7.0–7.2, 7.11–7.16
- Mechanics identified: turn = 3 operations stages (≈ 2–3 days each), stage as the basic time unit; initiative determined once per turn (die + date-dependent rating, higher wins, ties reroll, scenario fixes turn 1) but declared once per stage, so the holder can take consecutive half-stages; Player A/B as per-stage positions; the joint phases A–E (declaration, weather, organisation with its three any-order segments and their completion-before-initiation ordering, convoy arrival, Commonwealth fleet); the per-player phases F–L (reserve, the repeatable four-segment movement/breakdown/combat/release cycle with the six-step combat order, truck convoys, Commonwealth rail, tow-then-repair, patrol only if no assault); stages IV–V as repeats; no phase I.
- How we expressed it: initiative pulled ahead of the turn outline since the outline depends on it; the outline as a nested list with each phase pointing at the file that owns its procedure; the "repeat with A/B swapped" instruction stated once as a rule of the outline; an engine-notes section for the letter skip and the meaning of "phasing player"; our own initiative example. Naval convoy stage kept in Land Game terms and pointed at §32 for the abstraction.
- Errata applied: none identified (no numeric values asserted).
- Rulings raised: none. The Initiative Ratings Chart (7.2) is on a separate sheet not yet captured — spi-omit, to be transcribed to `data/` when available.

## rules/30-capability-points.md — 2026-09-19
- Source cases read: 6.0, 6.11–6.17, 6.3 (6.2x are in rules/10-units-and-state.md)
- Mechanics identified: CPA as the per-stage action budget; printed CPA 0 → 10 for all but movement; the allowance spans both halves of the stage (defensive spending counts); parent formations move at the lowest component CPA; no carry-over, no transfer; motorisation substitutes the truck CPA for infantry (basic CPA ≤ 10) and the "0+" anti-aircraft rule; the §6.3 cost list including the −4-differential 2 CP defender refund and the "free but restricting" note.
- How we expressed it: one short section per rule with our own retreat example; the cost table transcribed to `data/tables/cp-costs.json` (new `cp-costs` schema: fixed cost + `plus` tec/cpa + `cpa_fraction` + `alt_cost` + defender refund flag) and reproduced as a readable markdown table in the file; engine notes for the reset point and the two effective-CPA exceptions; 6.15's "(without trucks)" aside expressed as "use effective CPA".
- Errata applied: none identified.
- Rulings raised: none.
