---
title: Units and state
status: provisional
---

# Units and state

This file defines what a **unit** is, the categories an engine must be able
to sort units into, the numbers each unit carries, and the state that changes
during play (strength, cohesion, morale, motorisation). Sequence, movement
and combat procedures that *use* these values live in their own files.

::: spi-omit 3.0 3.2 — section and subsection headings; the rules under them are restated below

::: spi-omit 3.1 — term definitions; restated in [Glossary](glossary.md)

## Unit types

::: spi 3.21 3.23

Every counter has exactly one **type**. Types are fixed for the life of the
counter and decide which procedures apply to it.

| Type | Examples | Combat unit? |
|---|---|---|
| Infantry | foot, motorised, mechanised, motorcycle, heavy-weapons, garrison, airborne | yes |
| Tank | tank battalions and regiments | yes |
| Reconnaissance | armoured-car and recce battalions | yes |
| Anti-tank | towed and self-propelled anti-tank guns | yes |
| Anti-aircraft | flak batteries and regiments | yes |
| Artillery | field, medium and heavy guns; self-propelled; coastal | yes |
| Engineer | engineer companies and battalions | no (see [Engineering](80-engineering.md)) |
| Headquarters | divisional, brigade, regimental HQs | conditional (below) |
| Ground support | squadron ground support units (Air Game) | no |
| Recovery | tank recovery squadrons | no |
| Dummy tank formation | no counter; tracked on a log sheet | no |
| Truck | light and heavy trucks | no |

A **combat unit** is any unit of the six types marked *yes*. A headquarters
with combat units attached is also a combat unit. Some non-combat units count
as combat units for particular checks — zones of control, reconnaissance,
barrage targeting — and each such exception is stated where the check is
defined.

## Target classes

::: spi 3.22

For barrage, strafing and bombardment a unit is one of four **classes**.
Class is derived from type and from whether the unit's strength points carry
an armour protection rating (APR):

| Class | Members |
|---|---|
| Infantry | infantry type; engineers; ground support units; recce without APR; HQs that have a defensive close-assault rating but no APR |
| Armour | tank type; dummy tank formations; recovery squadrons; recce, HQ, artillery and anti-tank units that have an APR |
| Gun | artillery, anti-aircraft and anti-tank strength points without an APR, plus HQs and infantry that have a barrage rating |
| Truck | trucks |

An artillery or anti-tank counter whose strength points are partly armoured
and partly not is treated as **two targets**, one Armour-class and one
Gun-class, each with its own points.

## Headquarters

::: spi 3.3 3.31 3.32 3.33

A **headquarters** (HQ) counter stands in for every unit attached to it —
combat units, trucks and the supplies those trucks carry. On the map only
the HQ counter moves; the attached units are recorded on its log sheet.

- **Strength.** An HQ with combat units attached fights with the sum of
  their values and is a combat unit.
- **Speed.** The capability point allowance of an HQ (or any parent unit)
  is that of the slowest unit attached to it.
- **Stacking.** An HQ's printed stacking value assumes a full
  formation; a formation below full strength uses the equivalent rules in
  [Stacking and ZOC](50-stacking-and-zoc.md). An HQ with **no** combat units
  attached occupies zero stacking points, may use its parenthesised
  ratings, is not a combat unit, and may not attack.

::: spi 3.34

Some HQs (chiefly Italian regimental HQs) have guns of their own. Such an HQ
uses its printed combat values and takes gun losses like any unit; when the
last gun point is gone it is not destroyed but becomes a non-combat HQ.

::: spi 3.35

Armoured division and brigade HQs usually carry a small tank element,
visible in their ratings. Those tanks:

1. may fight only while the HQ has no combat units attached;
2. may never be transferred to another unit;
3. are rebuilt from the first tank replacement points available after loss;
4. exempt the HQ from breakdown.

::: spi 3.36

An HQ with no combat values at all (printed or parenthesised) that is alone
in a hex — no friendly combat unit present — is **captured** the moment an
enemy combat unit's zone of control covers the hex. Capture costs no
capability points and yields one prisoner point.

## Unit characteristics

::: spi 3.5

A counter is a bundle of **TOE strength points**; its abilities are those of
its points. A counter with no strength points has only a capability point
allowance. The characteristics an engine stores per unit:

| Characteristic | Meaning | Used by |
|---|---|---|
| Capability point allowance (CPA) | Budget for movement and combat each stage | [Capability points](30-capability-points.md) |
| Barrage rating | Strength when firing indirectly | [Combat](60-combat.md) |
| Vulnerability | How easily a gun is destroyed or captured in a forward position | [Combat](60-combat.md) |
| Anti-armour strength | Ability to destroy armoured vehicles | [Combat](60-combat.md) |
| Armour protection rating (APR) | Resistance to anti-armour fire | [Combat](60-combat.md) |
| Offensive close-assault rating | Strength when attacking in close assault | [Combat](60-combat.md) |
| Defensive assault rating | Strength when defending against close assault | [Combat](60-combat.md) |
| Anti-aircraft rating | Ability to shoot down aircraft | Air Game (abstracted in [§32](95-abstract-logistics-and-air.md)) |
| Maximum TOE strength | Full-strength point count | [Organisation](70-organisation.md) |
| Basic morale rating | Training and spirit, −3 to +3 | [Combat](60-combat.md) |
| Fuel rate | Fuel consumed per movement | [Movement](40-movement.md) |
| Breakdown adjustment | Mechanical reliability modifier | [Movement](40-movement.md) |

One strength point stands for roughly 100–200 men, a platoon of 5–8 armoured
vehicles, or a battery of four guns. Some Commonwealth units reach their
printed basic morale only after training ([Organisation](70-organisation.md)).

### Parenthesised ratings

::: spi 3.4

A rating printed in parentheses is a **fallback** value: it may be used only
when the unit is attacked while no friendly combat unit with an ordinary
(unparenthesised) rating of that kind shares its hex.

### Type notes with rule effect

The type descriptions in the original are mostly colour. These are the
statements in them that change play:

- **Motorised infantry** moves at truck speed only while it actually has
  trucks; otherwise it is foot infantry.
- **Motorcycle units** may not enter hexes closed to light trucks; they use
  no fuel and never break down.
- **Garrison units** (marked *G*) occupy zero stacking points in the town
  they were raised to garrison.
- **Artillery** has built-in transport that may not be stripped, uses fuel
  and water when moving, and does not break down. Guns of several calibres
  on one counter are one unit.
- **Self-propelled artillery** fires as a gun, has a vulnerability rating,
  can be killed by anti-tank fire, uses fuel and water, and does break down.
- **Coastal guns** have a CPA of 10 for combat (or their printed CPA if
  higher), move only with trucks assigned for the purpose, and if printed
  CPA is `0` are emplaced: no vulnerability rating; only barrage, capture
  or air bombardment can remove them. Motorised coastal guns break down.
- **Anti-tank units** are unarmoured unless self-propelled. Some non-AT
  points (British 25-pdr, German 88 mm, Italian 75/90 mm AA) also have
  anti-armour strength as printed.

## Cohesion

::: spi 6.2

**Cohesion** is the running measure of a unit's condition. It is a single
signed integer, the **cohesion level**, kept per unit:

- a level of **0** is the unit's normal state;
- a **negative** level means the unit is worn down and coming apart
  (disorganised) by over-exertion or heavy losses;
- a **positive** level means the unit is buoyed by recent success.

Cohesion has no direct effect by itself; it feeds [Morale](#morale) at the
instant of a close assault, and at its extremes it can immobilise or surrender
a unit. Two kinds of counter move the level: **disorganisation points (DP)**
lower it, **reorganisation points (RP)** raise it. Both are applied the moment
they are earned — not banked to the end of a stage — and both change the same
cohesion level rather than being stored separately.

### Earning disorganisation points

::: spi 6.21

A unit earns one DP for each capability point it spends over its CPA within an
Operations Stage. A unit is also disorganised by a costly assault: if a unit —
and, for a parent formation, the formation and every unit in it — loses 30% or
more of its strength in a single close assault, it earns three DP (see also
[Combat](60-combat.md), SPI 15.29).

### DP and RP applied to the level

::: spi 6.22 6.23

Each DP lowers the cohesion level by one; the effect is immediate and carries
from segment to segment until offset. A cohesion level is raised only by RP,
which are likewise applied at once. **No cohesion level may exceed +10**,
however many RP are earned.

::: spi 6.24

RP are earned two ways:

1. **Rest.** A unit that spends no capability points at all for an entire
   Operations Stage earns five RP — but this method alone may never raise a
   unit above cohesion 0 (a unit at −1 that rests reaches 0, not +4). A unit
   undergoing or conducting [training](#training) does not count as resting.
2. **Victory.** A unit that takes part in a close assault from which the
   defender wholly vacates its hex as a direct result — not through reaction
   or retreat before assault — earns three RP.

### Effects of the cohesion level

::: spi 6.25 6.26

::: ruling R-001 — the −26 disorganisation threshold is a cohesion level, not a count of disorganisation points

A positive level can raise, and a negative level can lower, a unit's basic
morale for a given close assault; the amount is looked up at combat time
([Morale](#morale)). A unit whose level reaches **−26 or worse** is barred from
moving, attacking or defending; should a hostile combat piece come alongside,
it surrenders whatever the size of that enemy (the threshold is the cohesion
level, not a disorganisation-point tally — see ruling
[R-001](../rulings/R-001.md)). Such a unit may still refuel, and it continues
to consume stores and water. A single action may drive a level past −26 in one
step.

### Which level applies when units are mixed

::: spi 6.27 6.28 6.29

Cohesion is tracked per unit, but a close assault uses one level for each side.
When a side's participating units differ, the level of the **largest** unit
(by stacking points) prevails. If several units tie for largest, average their
levels — sum them and divide by the number of contributing counters, rounding
to the nearest whole number. Within a parent formation the same rule applies,
resolved from the innermost formation outward.

## Morale

::: spi 17.0 17.1

Every combat unit has a **basic morale rating** printed on its OA sheet, a
fixed integer from **−3 to +3** (the sole exception is a unit still in
[training](#training)). A battalion or brigade uses the basic morale of its
assigned parent formation unless it has been attached elsewhere or is operating
on its own. Basic morale is the unit's baseline willingness and ability to
fight; cohesion adjusts it for a single close assault, as follows.

### Adjusting morale for an assault

::: spi-omit 17.2 — subsection heading

::: spi 17.21 17.22 17.23 17.24

Each time a unit joins a close assault (or a probe), its cohesion level at that
moment may shift its basic morale. The shift is read from the
**Morale Modification Table** — a table this file does not own; it is a
combat-resolution table transcribed alongside [Combat](60-combat.md). The
lookup uses a sequential two-dice roll (11–66): the unit's cohesion level
selects the row, the roll selects the column, and the column gives the
modifier, which is added to basic morale to give the **adjusted morale rating**
for that assault. The adjusted rating is capped to the −3…+3 range (exception:
Rommel, below). Cohesion of −17 or worse reads on the "−17 et seq" row; +8 or
higher reads on the "+8" row.

::: spi 17.25 17.26

The table's rightmost column is **Surrender**: a unit whose row-and-roll lands
there surrenders immediately and becomes [prisoners](95-abstract-logistics-and-air.md).
If both sides roll Surrender the two cancel: the fight is called off, leaving
both Engaged. A unit or formation whose (individual or combined) basic
morale is **+1 or better** ignores a Surrender result, treating it as a −4
modifier instead, *unless* its cohesion is −11 or worse, or the enemy brings at
least three times its strength (enemy raw offensive-assault strength against
friendly raw defensive strength).

::: spi 17.27 17.28

When a side's units hold different cohesion levels, the level that feeds the
table is chosen by the largest-unit rule ([above](#which-level-applies-when-units-are-mixed)).
Axis units that share **General Rommel**'s hex when an assault is joined add +1
to their adjusted morale, and this bonus may carry the rating above +3.

::: spi 17.6

The Training Chart is data: `data/tables/training.json` — one stage for
guns, three for infantry, six for tanks and recce, twelve for commandos,
and six to lift an untrained Commonwealth unit's morale a point.

::: spi 17.4

The Morale Modifier Table is data: `data/tables/morale-modifier.json` —
twenty-six cohesion rows from +8-and-better to −17-and-worse, each giving
the dice range for every modifier from +4 to −4 and for surrender. At +8
nothing worse than +1 is possible; at 0 the roll is almost always "no
change"; from −7 down a high roll surrenders the force, and at −17 every
roll does. One printed gap (level −4, reading 56) is declared in the file
and awaits a ruling.

## Training

::: spi 17.3 17.31

Some Commonwealth units arrive below their assigned basic morale and must be
**trained** up to it; German and Italian units never train. A unit that must
train shows two morale ratings on its OA sheet: the value in parentheses is its
starting (untrained) rating, the other is the ceiling it may reach.

::: spi 17.32 17.33 17.34

Training happens only in designated areas — Cairo (any city hex), Helwan
(1430), Alexandria (any city hex), Amiriya, Abougir or Deghelia. To train
during an Operations Stage a unit must spend **no** capability points; any
expenditure interrupts that stage's training. Every six Operations Stages of
training raise the unit's current rating by one point, never past its assigned
basic morale.

::: spi 17.35 17.36 17.37

A qualified **instruction battalion** must share the hex each stage: a combat
battalion already at its assigned basic morale, of a matching arm — an
infantry-type battalion for infantry divisions or brigades, a tank battalion
for any unit that includes tanks. An instruction battalion must be at least one
quarter of its assigned TOE strength, does not count against stacking, and may
train as many units as can stack in the hex. Training is optional: a unit may
fight at its lower rating and be withdrawn to train later, but only training
ever raises basic morale permanently. Training areas (Commonwealth and Axis)
are marked on the maps.

## Voluntary surrender

::: spi 17.5 17.51 17.52 17.53

Besides being captured through combat, ammunition failure or collapse of
cohesion, a player may **voluntarily surrender** units. Surrendered units are
treated exactly as captured ones: infantry become prisoners, while tanks, guns
and aircraft become replacement points. To surrender voluntarily:

- it may not be during steps *b* through *f* of a Combat Segment;
- **every** unit, replacement point and item in the hex must be surrendered
  together;
- the units giving up must sit next to a hostile combat piece, with a clear
  move straight into its hex.

The enemy combat unit may be of any size or status, but it must **accept**,
spending two capability points to do so; if it cannot spend them the surrender
cannot happen.

::: spi 17.54 17.55 17.56

Before handing units over — and only after declaring the surrender — the owner
may try to destroy his own material, except anything that can move only in the
phasing truck convoy or repair phase. Roll one die per category: for tanks and
guns, subtract one from the roll and multiply by 10%; for trucks and
motorisation points, subtract one and multiply by 20%. The result is the
fraction of that category's TOE strength destroyed, rounding down.

::: spi-ref 3.61 3.62

The limited-intelligence (hidden-information) rules are restated in
[Abstract logistics and air](95-abstract-logistics-and-air.md#limited-intelligence).

---

*Drawn on: SPI §3, §6.2, §17.*
