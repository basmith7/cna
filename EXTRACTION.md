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
