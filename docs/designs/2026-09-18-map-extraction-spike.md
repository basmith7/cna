# Map extraction — findings

**Source:** `CNAv2.1.0.vmod` (Mitch Guthrie, 2021; © White Box Games). One
14310×4632 PNG redraw of all five sheets plus Malta, and `buildFile.xml`
with a sideways `HexGrid` (`dx=72.95 dy=85.25`) and `HexGridNumbering`
inside each sheet's `Zone`. **Legend:** the Terrain Key and [8.37] Terrain
Effects Chart printed on Map A, archive.org scan p0187. **Tool:**
`tools/map_extract.py` (numpy + Pillow, ~15 s for all sheets).

## Geometry

Porting VASSAL's `HexGrid`/`HexGridNumbering` arithmetic (swap x/y for
sideways, `vDescend`, Map A's `stagger`, per-sheet `hOff`/`vOff`) enumerates
7,105 hexes: A 1007, B 1959, C 1520, D 1240, E 1308, Malta 71. Every hex in
the printed "Summary of Important Locations" and the scenario-book set-up
references lands on its symbol; `--check` scores 51/54 (misses: Jalo and
Siwa are oasis palms, not dots; Amiriya E2212 has no symbol in the redraw).

## Palette → Terrain Key

| Redraw colour | Class | Terrain Key / [8.37] |
|---|---|---|
| (251,250,239) | clear | Clear |
| (138,181,207) | sea | Sea; also river water |
| (194,185,149) plain tan | rough | Rough |
| (186,175,129) + yellow net | salt_marsh | Salt Marsh |
| (223,207,100) yellow | desert | Desert |
| (164,178,171) | delta | Delta |
| (151,136,66) | mountain | Mountain |
| (203,216,91) | heavy_veg | Heavy Vegetation |
| (91,161,102) dashes | swamp | Swamp |
| (170,157,97) ring outlines | gravel | Rock/Gravel |
| (91,149,185) hatch blocks | major_city | Major City (same blue as the coastline stroke — separated by a 5×5 solidity test) |
| (74,138,179) / (66,70,73) 12 px dot | village | Village/Bir (dark dots on Map E) |
| (94,97,98) band | escarpment | Escarpment; `band_hex` = hex the band is drawn in |
| (160,146,80) band, both sides | ridge | Ridge |
| (160,146,80) band, one side | slope | Slope; `band_hex` = hex the band is drawn in |
| (127,148,142) | wadi | Wadi |
| sea-colour band along a hexside | major_river / minor_river | by width (≥14 px = major) |
| (72,63,34) double line | road / unfinished_road | Unfinished Road is closed dash rectangles; told apart by end-cap pixels on the centre axis |
| (84,88,89) | railroad / track | rail is a 1 px hairline that anti-aliases away; ties give ≥90 px in a 49 px window, dashed track ≤40 |

Terrain is the majority fill in a 16 px disc at the hex centre; a hex whose
centre is water but with ≥30 % land in a 30 px disc, or with a village dot,
is a coastal *land* hex (`cov_sea` records the water share). Hexside
features are sampled on and 9 px either side of the midpoint; crossings
(road, rail) are looked for along the whole hexside and must appear on both
sides. One record per hexside pair in `hexsides.csv`.

Totals: clear 4228, desert 677, rough 650, gravel 464, sea 346, delta 325,
salt marsh 267, mountain 107, swamp 24, major city 11, heavy vegetation 6;
141 villages. Hexsides: wadi 701, track 565, slope 529, road 320,
minor river 221, escarpment 205, railroad 142, ridge 122, unfinished road
97, major river 71.

## Known gaps

- **Up/down for slope and escarpment**: the data records which hex the band
  is drawn in (`band_hex`); which side is "up" is a rules question for the
  movement restatement, not decided here.
- **Oasis, port, airfield, flying-boat symbols** are not detected; oases
  count as villages for [8.37], ports come from the printed locations table,
  airfields from the scenario OBs.
- **Heavy vegetation** looks under-counted (6 hexes); the Jebel Akhdar
  stipple may use a second green. Check against the scan.
- **Crossings near a vertex** can be missed (strip covers ±70 % of the
  hexside); unfinished railroad is not distinguished from railroad.
- Partial hexes on zone edges get out-of-range IDs (e.g. `Malta 12-01`);
  clip to the printed range when the data schema is fixed.
- No hand-checked error rate yet beyond the 54 known places.

## Next

1. Hand-check ~100 hexes per sheet against the scan; record misreads as the
   error budget. Miller's CSV, if it turns up, is a second cross-check.
2. `data/map/` schema in `data/README.md`; commit only the derived CSVs, the
   PNG stays in `~/.cache/cna-vassal/`.
