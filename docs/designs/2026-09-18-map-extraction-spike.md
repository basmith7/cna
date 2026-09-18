# Map extraction spike — findings

**Source:** `CNAv2.1.0.vmod` (Mitch Guthrie, 2021; © White Box Games). One
14310×4632 PNG redraw of all five sheets plus Malta, and `buildFile.xml`
with a sideways `HexGrid` (`dx=72.95 dy=85.25`) and `HexGridNumbering`
inside each sheet's `Zone`. **Tool:** `tools/map_extract.py`.

## What works

- **Hex ID → pixel is exact.** Porting VASSAL's `HexGrid`/`HexGridNumbering`
  arithmetic (swap x/y for sideways, `vDescend`, Map A's `stagger`, per-sheet
  `hOff`/`vOff`) enumerates 7,105 hexes: A 1007, B 1959, C 1520, D 1240,
  E 1308, Malta 71. Every scenario-book hex checked lands on its town dot:
  Soluch A4130, Derna B5925, Sollum C4021, Fort Capuzzo C4020, Halfaya Pass
  C3922, Bir el Menastir C4419, Mersa Matruh D3714, El Hamman E3007.
- **Hex fill** classifies cleanly by palette colour: clear, sea, sand
  (yellow), rough (plain tan), rough-lined (tan with yellow crack pattern),
  cultivated (delta), dark-olive fill, green. Mixed hexes get coverage
  fractions.
- **Hexside bands** (dark grey escarpment, olive band, teal wadi) detected
  from discs on and beside the hexside midpoint. Solid olive band vs. the
  speckled olive fringe of rough patches separates on fill density.
- **Crossings** (road, rail, river) detected by sampling a strip along the
  full hexside on both sides and requiring the colour on both.
- **Town dots** found as a solid ≥9 px blue disc; same blue in coastline
  strokes, labels and the dotted frontier does not trigger.

## Known gaps

- **Palette → [8.37] terrain names** needs the printed legend (on the
  archive.org scan; the module stripped it). The stippled "dot" fill in south
  Map A/B and the blue dotted frontier are not yet classes.
- **Road vs. track vs. trail**: brown solid double, brown dashed double and
  grey dashed thin lines are three symbols; the classifier currently emits
  `road` for the brown ones and `rail` for grey (rail cross-ties vs. dashed
  track not distinguished).
- **Cities, ports, forts, airfields** are icons, not dots: Tobruk C4807,
  Bardia C4321, Malta's airfields with capacity numbers. Needs template
  matching or a hand list (few dozen).
- **Hexside ownership**: bands are reported from both adjacent hexes;
  de-duplicate to one record per hexside once the hexside convention in
  `data/README.md` is fixed.
- Partial hexes on zone edges get out-of-range IDs (e.g. `Malta 12-01`);
  clip to the sheet's printed range.
- Runtime ~12 min for all sheets in pure Python (town-dot scan dominates);
  fine for a one-off, vectorise if it becomes a CI step.

## Next

1. Legend-driven names and a `terrain` enum in `data/README.md`.
2. Hand-check ~100 hexes per sheet against the scan; record misreads as the
   error budget. Miller's CSV, if it turns up, is a second cross-check.
3. Commit only derived CSVs under `data/map/`; the PNG stays in
   `~/.cache/cna-vassal/`.
