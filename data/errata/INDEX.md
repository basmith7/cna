# Errata index

Every SPI September 1979 errata item we have applied gets an `E-nnn` id,
sequential, never reused. Items that change a **table value** also get an
overlay file `E-nnn.json` in this directory; items that only change **prose**
are annotated in the rules file with `::: errata E-nnn — paraphrase` and
listed here alone.

| Id | SPI item | Kind | Where applied | Paraphrase |
|---|---|---|---|---|
| E-001 | 11.32 | correction | rules/60-combat.md | the formula multiplies rating by TOE strength ("+" was a misprint for "×") |
| E-002 | 12.44 | clarification | rules/60-combat.md | a barrage pin applies to the target battalion-equivalent only, never to the whole hex or division |
| E-003 | 14.47 | correction | rules/60-combat.md | self-propelled guns absorb anti-armour damage by armour protection alone; an SP gun barraging *back* neither absorbs nor suffers anti-armour fire |
| E-004 | 14.48 | addition | rules/60-combat.md | at most two halftrack-motorised TOE points are lost to anti-armour fire in one segment |
| E-005 | 15.4 | correction | rules/60-combat.md | the worked figure for four unsupported tank points is a reduction to one, not two |
| E-006 | 15.53 | correction | data/tables/assault-size-shifts.json | "Brigade" belongs in the smaller-side column (3-point and 2-point brigades), not under adjustment |
| E-007 | 15.56 | addition | rules/60-combat.md | a hex whose defenders are all pinned defends at 0 with two columns shifted to the attacker |
| E-008 | 15.79 | correction | data/errata/E-008.json → data/tables/close-assault-results.json; rules/60-combat.md | defender losses, +4 column, 10 % row: dice range 34–45 (printed 24–45 overlapped the 15 % row) |
| E-009 | 15.88 | clarification | rules/60-combat.md | −17 cohesion surrenders when assaulted; −26 surrenders when an enemy merely moves adjacent (SPI 6.26) |
| E-010 | 16.11 | addition | rules/60-combat.md | Italian L/6, Commonwealth Stuarts and all mechanised infantry (incl. Panzergrenadiers) may supply patrol points |
| E-011 | 19.14 | clarification | rules/70-organisation.md | example corrected: attached to the NZ division, assigned to 7th Armoured |
| E-012 | 20.3 | correction | data/errata/E-012.json → data/tables/replacement-conversion.json; rules/70-organisation.md | ignore the chart's SGSU line; SGSUs need no replacement points (34.82) |
| E-013 | 20.62 | correction | rules/70-organisation.md | the example needs 300 tons, not 350 |
| E-014 | 20.66 | correction | (pending) data/tables/axis-replacement-pool.json | explanatory note refers to the M 11/39, not 13/39 |
| E-015 | 20.72 | correction | rules/70-organisation.md | Commonwealth plans one month ahead (not two) and reads the production table for the arrival month |
| E-016 | 20.83 | correction | rules/70-organisation.md | the reference to 20.75 is void |
| E-017 | 22.8 | correction | rules/80-engineering.md; noted in data/tables/vehicle-repair.json (no value changes, so no overlay) | the table note's die-roll additions are wrong; 22.34 governs |
| E-018 | 22.34 | correction | rules/80-engineering.md | the reference to 22.35 is void |
| E-019 | 23.11 | correction/clarification | rules/80-engineering.md | engineers use parenthesised strengths only when not stacked with a friendly combat unit; may always enter friendly-occupied enemy-controlled hexes |
| E-020 | 24.15 | clarification | rules/80-engineering.md | 24.12 (no road-stacking effect) is an exception to "subject to all stacking rules" |
| E-021 | 24.72 | addition | rules/80-engineering.md | Commonwealth SGSUs and E-HQs may also build airfields and flying-boat basins |
| E-022 | 25.15 | correction | rules/80-engineering.md | the reference should be 22.34 |
| E-023 | 21.12 | correction | rules/90-special.md, data/tables/breakdown-adjustments.json | Italian M 13/40 BAR is 1R, as on the charts |
| E-024 | 29.1 | clarification | rules/90-special.md, data/tables/seasons.json | the printed Roman numerals are weeks of the month |
| E-025 | 29.61 | correction | data/errata/E-025.json → data/tables/weather.json; rules/90-special.md | the Weather Table's season rows are backwards: each row's game-turn bands belong to the opposite season (turns 1–12 are autumn) |
| E-026 | 27.16 | clarification | rules/90-special.md | re-formed raiders follow 27.13; the example's turns are 55 and 59 |
| E-027 | 27.36 | clarification | rules/90-special.md | raiders may react after any spotting attempt |
| E-028 | 27.88 | correction | rules/90-special.md | the hidden-movement reference is 27.32 |
| E-029 | 28.17 | correction | rules/90-special.md | one guard point per five prisoners on the move |
| E-030 | 30.5, 30.55, 30.57, 30.58, 30.59 | corrections | rules/90-special.md | references to 56.0 / 55.2 / 55.3; barraged units may still transfer; 30.57 replaced by 10 % tonnage loss per SP landed |
| E-031 | 8.37 | correction | data/errata/E-031.json → data/tables/terrain-effects.json; rules/40-movement.md | Terrain Effects Chart: footnote 4 belongs to Major City, not Swamp; a track halves the hex terrain's cost rather than costing 1 CP |
