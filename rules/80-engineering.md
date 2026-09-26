---
title: Engineering
status: provisional
---

# Engineering

This file defines the work that changes the map and puts vehicles back into
service: repair of broken-down vehicles and destroyed tanks, what engineer
units can do, construction of every kind (minefields, fortifications, roads,
railways, air facilities, repair facilities, supply dumps), and the effects
of fortifications and minefields once they exist. Breakdown itself (SPI §21)
is in [Special](90-special.md); terrain costs on the Terrain Effects Chart
(SPI 8.37) are cited from [Movement](40-movement.md#terrain).

::: spi-omit 22.1 22.2 22.3 22.6 22.7 23.1 23.2 24.1 24.2 24.3 24.4 24.5 24.7 24.8 25.1 25.2 26.1 26.2 — section headings and design commentary; the rules under them are restated below

## Repair

::: spi 22.0 22.11 22.12 22.13 22.14

Broken-down vehicles and destroyed tanks are repaired during each stage's
**repair phase**, by the phasing player only, either **in the field**
or at a **temporary** or **major repair facility**. A player may repair any
vehicle he controls, whatever its nationality; the Commonwealth repairs
everything together, the Axis rolls German and Italian vehicles separately,
and captured vehicles are always a separate batch. For each vehicle type the
player rolls one die on the relevant schedule: field repair yields a number
or percentage of TOE points fixed, facility repair a percentage. Supplies
are spent whether or not the attempt succeeds, and repaired vehicles return
as truck points or as replacement points ([Organisation](70-organisation.md#replacement-points)).

No repair is possible when:

- the vehicles are in an **enemy-controlled** hex, friendly units present or
  not — unless they sit in a major repair facility, which ignores enemy ZOC;
- there are **no supplies** for it;
- the vehicles were **towed** this repair phase;
- the hex is under **rainstorm or sandstorm** (major facilities excepted).

::: spi 22.8 22.44

Both repair tables are data. `data/tables/vehicle-repair.json` (SPI 22.8):
in the field a 0 or 1 returns two truck points, one armoured-car point or a
quarter of a tank type, a 2 one truck point and a tenth of the tanks, and
from 5 up nothing; facilities do better, a major one returning three-quarters
on a 0–1 and still a tenth on an 8. The chart's own sentence about die
additions is void (E-017): the modifiers are those of 22.34 above.
`data/tables/destroyed-tank-repair.json` (SPI 22.44): a 1 repairs anywhere;
a 2 repairs at any facility; German tanks at an Axis facility repair on a 3
as well; Italian tanks are junked on a 5; a 6 or 7 junks at every facility;
the field column is only for the delivery and recovery squadrons.

::: errata E-017 — 22.8: the table's last two sentences on die-roll additions are wrong; use 22.34

### Field repairs

::: spi 22.21 22.22 22.23 22.24 22.25 22.26 22.27 22.28

Any broken-down vehicle that shares a hex with some friendly unit — even a
squadron ground support unit — may be tried in the field, subject to the
bars above and provided it was not towed this phase. Destroyed tanks are
never repaired in the field except by the delivery squadrons
([below](#tank-delivery)). Field repair is a gamble:

| Vehicles | Roll | Result | Supplies |
|---|---|---|---|
| trucks (one roll per hex) | 1 | two light or medium points in any mix, or one heavy | none |
| | 2 | one light or medium point | none |
| armoured cars and recce (one roll per hex) | 1 | one TOE point | none |
| tanks and self-propelled guns (one roll per *type* per hex) | table, field column | percentage of that type in the hex, fractions up | 1 fuel per point attempted, paid first |

A single tank point under repair ignores a 10 % result. Only points whose
fuel has been paid may be attempted.

### Facility repairs

::: spi 22.31 22.32 22.33 22.34 22.35 22.36 22.37 22.38

**Temporary facilities** are built by the players ([below](#repair-facilities))
or placed by the scenario; **major facilities** exist at Tripoli (the box),
Tobruk (for its controller), and every hex of Alexandria and Cairo. A vehicle
that begins the maintenance segment in a facility hex, not having been towed
this stage, may be repaired there. Roll once per vehicle type — trucks,
recce/AC, broken-down tanks and guns by type, destroyed tanks by type — on
the repair table's temporary or major column for the percentage repaired
(as for field repair). Each truck, gun or tank point attempted costs **1
store and 1 fuel**, paid before rolling.

Bombing and barrage degrade facilities through the fortification level of
the hex:

- In a **major city**, one level lost adds **+1** to the repair roll; two or
  three levels lost add **+2**.
- Elsewhere, bombs or barrage sufficient (on the Air Bombardment Table) to
  drop a fortification one level **neutralise** the facility for the stage.

Temporary facilities stop in rainstorm or sandstorm and in enemy ZOC (unless
in a major city); major facilities work through both.

::: errata E-018 — 22.34: the reference to 22.35 is void

### Destroyed tanks

::: spi 22.4 22.41 22.42 22.43

Destroyed tanks — anyone's, once brought to a facility ([capture](60-combat.md#capturing-destroyed-tanks))
— are repaired only in facilities. Decide first how many points to attempt and
**pre-pay 2 stores and 2 fuel** for each (Logistics Game); then roll one die
per point on the Destroyed Tank Repair Table: repaired, **junked** for good,
or no result and another try later.

### Repaired vehicles

::: spi 22.5

A repaired vehicle is a replacement point of its type, with every replacement
rule except training, and needs fuel before it moves.

### Tank delivery squadrons {#tank-delivery}

::: spi 22.61 22.62 22.63 22.64 22.65 22.66 22.7

::: ruling R-016 — a tank delivery squadron moves only in the truck convoy phase

::: ruling R-017 — a tank delivery squadron reacts or retreats only with a friendly combat unit

The Commonwealth receives three **Tank Delivery Squadrons** (TDS) over the
game — the Desert Tank Delivery Organisation is a name, not an HQ. A TDS is a
mobile advanced workshop:

- Broken-down tanks in its hex get **−1** on the field repair roll; destroyed
  *Commonwealth* tanks repair on a **1**, never junk. It cannot repair enemy
  tanks.
- No combat ratings, **0 SP**, CPA **25** as a vehicle, never voluntarily
  over its CPA and never into enemy ZOC. It moves only in the truck convoy
  phase (H), whether towing or not ([R-016](../rulings/R-016.md)). Alone in a hex and placed in an
  enemy ZOC, it is eliminated; it returns eight turns later.
  Only when stacked with a friendly combat unit may it react, retreat
  before assault, or retreat with the stack after combat
  ([R-017](../rulings/R-017.md)).
- Holds up to **3** tank points as reserves (treated as tank replacement
  points), still at 0 SP.
- Tows up to **3** tank points (besides its reserves) at **20 CP** rather than
  the usual 10, still at 0 SP; but it cannot field-repair in a stage it tows,
  nor in the stage after one in which it overspent its CPA (it may still
  tow).

The one **German Mobile Tank Repair Squad** works identically but repairs
German tanks only — not Italian, not captured.

## Engineers

::: spi 23.0 23.12 23.13 23.14 23.15

Engineers come as battalions, companies, and HQs marked **E** beside their
stacking value (otherwise ordinary HQs). Eliminated engineer units can be
rebuilt at the replacement rate (SPI 20.3). Special cases: the two New
Zealand railway construction units work only on railways, the 1st SA Road
Construction unit only on roads, and the two Commonwealth tank battalions
re-equipped with **Scorpion** flail tanks count as engineers for
minefields alone, while they hold at least six Scorpion points — points
that never transfer elsewhere (§32 addition).

::: errata E-019 — 23.11 (not in the transcription): engineers use parenthesised strengths only when not stacked with a friendly combat unit, and may always enter a friendly-occupied enemy-controlled hex

::: spi 23.21 23.22 23.23 23.24 23.25 23.26

What engineers (and E-marked HQs) do, mostly detailed elsewhere in this
file:

- A unit stacked with them enters an enemy minefield for **6 CP** motorised
  or **3 CP** on foot ([minefields](#minefields) gives the fuller rule).
- One that spends a whole stage in an enemy minefield without spending CP
  clears it at the end of the stage.
- They build and rebuild fortifications, bombed roads, temporary repair
  facilities, railways and air facilities.
- An **unpinned engineer battalion** or E-HQ attached to units close
  assaulting a fortified hex (not a major city) gives **one column** to the
  attacker ([combat](60-combat.md#terrain-and-close-assault)).
- They can never build or blow river or wadi crossings, nor touch
  escarpments.

## Construction

::: spi 24.0 24.11 24.12 24.13 24.14 24.15 24.16

All construction starts in the **construction segment** of the organisation
phase and completes at the start of the construction segment of a later
stage, after the number of stages on the Construction Chart (the starting
stage counts). A unit building may spend **no CP** that stage or the stage is
lost; a unit may run only one project at a time, obeys stacking (but not
road stacking limits), and may abandon a project freely. Supplies for a
project must begin the segment in the hex and are spent then, even if the
builders are later driven off; normal upkeep is paid as well. Weather and
fire interfere:

::: spi 24.21 24.22 24.23 24.24

- **Hot weather**: each site pays **10 water** extra.
- **Sandstorm or rainstorm**: the stage does not count; if a builder leaves
  the hex during one, the project is lost and starts again.
- **Pinned** builders lose the stage in the same way.
- Other friendly units in the hex are irrelevant (stacking aside).

::: spi 24.17 24.18

The Construction Chart and Demolition Chart are data:
`data/tables/construction.json` and `data/tables/demolition.json` — per
item, who may do the work, what it costs and how long it takes. The chart
figures are what the sections below use, with two exceptions where the
chart and the rules text disagree: a temporary repair facility is **50 fuel
+ 250 stores in one stage** on the chart but 150 fuel + 250 stores over
three stages in the text, and rebuilding a facility level is **10 fuel + 50
stores** on the chart but 30 fuel + 50 stores in the text (the prose below
keeps the text; for supply dumps the chart governs, per
[R-018](../rulings/R-018.md)). The
Demolition Chart adds what the text scatters: roads and fortifications fall
only to bombing and barrage; an airfield is *reduced* but never destroyed
by a raid; unblocking a port costs **50 ammunition + 25 stores** per level
(Tobruk 25 + 10; Benghazi 100 + 50 and two engineer units).

::: errata E-020 — 24.15: builders do not count against road stacking (24.12) despite "subject to all stacking rules"

### Minefields {#laying-minefields}

::: spi 24.31 24.32 24.33 24.34 24.35 24.36 24.37 24.38

Any engineer unit (or Commonwealth E-HQ) lays one **real** or **dummy**
minefield per project — the counter's back tells which — taking exactly one
stage, marked *under construction* and done at the next construction
segment. A real field costs **15 stores + 15 ammunition** up front; a dummy
**3 stores**. Sites: clear, sand/gravel or rough, one field per hex, never
in a major city or an enemy-controlled hex. Effects are in
[minefields](#minefields); removal is as under [engineers](#engineers).

### Fortifications {#building-fortifications}

::: spi 24.41 24.42 24.43 24.44 24.45 24.46 24.47 24.48

One **level** of fortification takes one engineer-capable unit of any size
plus an infantry battalion of **3+ TOE points**, **30 stores** paid at the
start, and three full construction segments without CP spent; the counter
goes down at the fourth. Build one level at a time, to level 2 at most (a
city's own levels only back to their original 2, or 3 for Cairo and
Alexandria). New fortifications go in any hex that is not mountain, salt marsh,
desert, delta or a major city, and never start in an enemy ZOC;
*rebuilding* a level lost to bombing or barrage follows the same recipe but
may happen in enemy ZOC. Nothing else may be built in a hex while a
fortification is going up. Once built a fortification cannot be removed;
only bombing and barrage reduce it.

### Roads

::: spi 24.51 24.52 24.53 24.54 24.55 24.56

Only hexes printed as **unfinished road** may be built, and destroyed road
hexes rebuilt; both count as track until done. Per construction segment, at
**2 stores per hex** from the builders' hex and never in an enemy-controlled
hex:

| Builder | Road hexes |
|---|---|
| infantry battalion of 3+ points | 1 |
| engineer company or E-HQ | 1 |
| engineer battalion, or engineer company/E-HQ with a 3-point infantry unit | 3 (own hex plus two adjacent road hexes) |

Use the End of Road marker for progress and note when a stretch is complete.

### Railways

::: spi 24.6 24.61 24.62 24.63 24.64 24.65 24.66 24.67

Only the two NZ railway construction companies (10th and 13th — engineer
companies for railway work only) lay **new** track: one company needs two
stages per hex, two together one stage. Any engineer unit, NZRRC included,
and Commonwealth E-HQs may **rebuild** destroyed track, three hexes per
segment (own plus two adjacent). Each hex built or rebuilt costs **1 store**
present with the unit. No enemy-controlled or enemy-occupied hex may be
worked. Track is destroyed by bombing, barrage, or any engineer, E-HQ or
3-point infantry unit that spends a full stage in the hex without spending
CP; mark it destroyed. The Alexandria–Mersa Matruh–Tobruk line grows only
westward from the last built hex beyond Mersa Matruh, hex by hex behind the
Railhead marker; unbuilt hexes do not exist. The Benghazi–Barce line is
decoration and may never be used.

### Air facilities

::: spi 24.71 24.72 24.73 24.74 24.75 24.76 24.77 24.78 24.79

(Air Game only.) Airfields and flying-boat basins take **three** segments
and may be built by engineer battalions, Commonwealth SGSUs and E-HQs;
landing strips and alighting areas take **one** and may also be built by
engineer companies or squadron ground support units. Strips and airfields go
in clear, rough, major city, desert or sand/gravel hexes; flying-boat
facilities in any coastal hex; none in an enemy-controlled hex. Supplies are
on the Construction Chart. At most one flying-boat and one land facility per
hex; a strip or alighting area may be upgraded to airfield or basin at full
cost, unusable meanwhile (§32 addition). Bombing reduces capacity or
destroys: strips and flying-boat facilities are rebuilt from scratch,
airfields one capacity level at a time at the cost of a strip. Facilities are
lettered counters placed when built, except the printed ones — every Cairo
hex is an airfield, and Malta, the Tripoli–Tunis boxes, the Commonwealth
off-map bases, Crete, Italy and Sicily have theirs (Air Rules).

::: errata E-021 — 24.72 addition: Commonwealth SGSUs and E-HQs may build airfields and basins

### Repair facilities {#repair-facilities}

::: spi 24.81 24.82 24.83 24.84 24.85 24.86 24.87 24.88

Only **temporary** repair facilities are built; major ones exist already and
cannot be destroyed by enemy presence, though both kinds can be reduced or
neutralised by bombing and barrage. Any engineer unit, HQs included, may
build, rebuild or dismantle a temporary facility or rebuild a major one.

- **Build**: an engineer unit of any size, three segments, **250 stores
  + 150 fuel** paid at the start; in a major city or village hex only; never
  in an enemy-controlled hex; at most **two** temporary facilities per
  player at once.
- **Rebuild a city facility** whose city level was bombed down: first
  restore the city level, then one engineer unit for one segment with **50
  stores + 30 fuel**. Rebuilding and dismantling are allowed in enemy ZOC.
- **Dismantle**: one engineer-capable unit, one segment, yielding **120
  stores + 25 fuel** in the hex; the facility is gone and may not be used
  while being taken down.

### Supply dumps

::: spi 24.9

::: ruling R-018 — dump costs follow the charts: real 3 CP + 10 stores, dummy 2 CP

Any one TOE point of any type creates a **supply dump** by spending **3 CP**
and, in the Logistics Game, **10 stores**; a **dummy dump** costs **2 CP**
only. These are the Construction Chart's and CP summary's figures, which
govern over the 24.9 text (ruling [R-018](../rulings/R-018.md)). Supplies may lie in a hex without a dump, tracked by the owner and
capped by the Logistics Game, but convoy trucks cannot load from such a hex.

## Fortifications {#fortifications}

::: spi 25.0 25.11 25.12 25.13 25.14 25.15 25.16

Every major city is a fortification: level **2**, or level **3** for Cairo
and Alexandria; villages are not. Built fortifications are level 1 or 2 and
never higher except in those two cities. Each level gives a larger defensive
benefit on the Terrain Effects Chart. Only bombing and barrage reduce a
level, and a reduced level may be rebuilt. Level 0 means nothing in the Land
Game except that rebuilding is easier (and see the Strafing Table, SPI
40.8); reduced levels do affect repair rolls ([above](#facility-repairs)).

::: errata E-022 — 25.15: the reference should be 22.34

::: spi 25.21 25.22 25.23 25.24

Fortifications never alter movement or breakdown. Their combat effects
are on the Terrain Effects Chart. Bombing and strafing of anything in a
fortified hex — units, trucks, flak, dumps — takes the same column shifts as
barrage, except that nothing in a level-3 city is affected by bombing until
the city is down to level 2. Units in a level-3 city ignore every **pinned**
result from any source.

## Minefields {#minefields}

::: spi 26.0 26.11 26.12 26.13 26.14 26.15

Minefields are **obstacles**, rarely killers. A counter is real or dummy on
its back, and a friendly field is flipped face-up the moment an enemy enters
it. Real fields are cleared by an engineer (or E-HQ) that starts the stage in
the hex, spends no CP on movement, and is still there at the end — friendly
or enemy field alike. A dummy field is removed at the end of the movement
phase in which an enemy paid to enter it.

::: spi 26.21 26.22 26.23 26.24 26.25 26.26

- Entry costs are on the Terrain Effects Chart, on top of the hex's own
  cost; for motorised units the enemy-minefield cost scales with CPA (an
  artillery unit pays 15), so units without engineers will blow far past
  their CPA. Friendly minefields are cheaper because the lanes are known.
- A dummy field costs the same to enter as a real one, and everyone entering
  during the same movement phase still pays, even after it is revealed.
- Engineers themselves, and any combat unit sharing a hex with an engineer
  **battalion** or a Commonwealth E-HQ, pay only **+4 CP** to enter an enemy field and nothing
  extra for a friendly one.
- Vehicles entering an enemy field without such an escort risk the mines:
  roll one die per battalion-sized (or smaller) combat unit and one for all
  second- and third-line trucks together; on **5 or 6** one TOE point of
  tanks or motorised infantry, or one unattached truck point, is destroyed.
- Anti-armour or close assault by attackers standing in an enemy minefield,
  or a close assault against a defender in his own enemy-to-you minefield,
  shifts every column **one for the defender**. Barrage is unaffected.

---

*Drawn on: SPI §22, §23, §24, §25, §26, the §32 additions 23.15 and 24.79, and the September 1979 errata (E-017–E-022).*
