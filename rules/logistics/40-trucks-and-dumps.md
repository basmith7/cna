---
title: Trucks and dumps
status: provisional
---

# Trucks and dumps

Supplies do nothing until they are where a unit can use them. In the
Logistics Game that means **trucks** hauling ammunition, fuel, stores, water
and men between ports, **supply dumps** and the front, plus the
Commonwealth railway (and, with effort, an Axis one). This file covers how
trucks are organised and restricted, what happens to vehicles stranded in a
salt marsh, what a dump may hold and how to blow one up, rail haulage of
supplies, and the weights used to convert supplies into tons. It replaces
the supply units and motorisation points of the Land Game played alone
([Abstract logistics and air](../95-abstract-logistics-and-air.md#moving-supply-units)).

::: spi-omit 53.1 53.2 53.3 54.1 54.3 54.4 — subsection headings; the rules under them are restated below

::: spi-omit 54.0 — designer's commentary on why the section gathers scattered rules

## Truck points

::: spi 53.0

Trucks are counted in **truck points**; one point stands for about ten real
vehicles. There are three classes:

- **heavy** trucks: roughly three tons and up, heavy lorries and half-tracks
  included;
- **medium** trucks: vehicles of about 30 hundredweight;
- **light** trucks: anything smaller than that.

Trucks carry either supplies or men (motorising infantry-type units). Moving
trucks burn fuel and water (see the Fuel and Water files of this module) and
accumulate breakdown ([Breakdown](../90-special.md#breakdown)).

## What one truck point carries

::: spi 54.2

The **Truck Characteristics Chart** gives, for one truck point of each class,
its CPA for each kind of load, its lift, fuel figures and breakdown rating.
Data: [`data/tables/truck-characteristics.json`](../../data/tables/truck-characteristics.json).

| Truck | CPA: infantry | CPA: guns | CPA: supplies | Infantry TOE | Artillery TOE | AA TOE | Ammo | Fuel | Stores | Water | Fuel capacity | Fuel use | BAR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Light | 25 | not allowed | 40 | ½ | not allowed | 1 | 2 | 50 | 6 | 40 | 8 | 1 | 2L |
| Medium | 20 | 15 | 30 | 1 | 1 | 2 | 4 | 120 | 15 | 100 | 6 | 1 | 2L |
| Heavy | 20 | 15 | 30 | 2 | 1 | 4 | 8 | 250 | 30 | 200 | 6 | 1 | 2L |

Reading the chart:

- The supplies CPA applies only to trucks moving as a convoy with supplies
  aboard; the other CPAs are those of a truck point motorising that kind of
  unit.
- A light truck point carries half an infantry TOE point: it takes **two**
  light points to lift one. You may do it, but it is a poor use of them.
- The BAR is the column shift to the left on the breakdown table.
- **Light trucks off the road.** A light truck point that is not moving
  along a road gains **one extra** breakdown point for every hex it enters
  and every hexside it crosses, on top of what the terrain charges.

::: variant V-003 — NJHarman drops the light-truck off-road breakdown note entirely

## First-, second- and third-line trucks

::: spi 53.11 53.12 53.13

Every truck point belongs to one of three **lines**, named for the job it
does:

1. **First-line trucks** belong to a combat unit (battalion, brigade,
   division and so on) and carry that unit's own men and supplies. They have
   no counter: record on the unit's TOE sheet how many points of each class
   it has and what each carries. A unit may detach first-line trucks in the
   Organisation Phase; they then get a counter and stop being first-line.
2. **Second-line trucks** shuttle between forward dumps and the combat
   units. They have counters and are recorded on the truck and Major End
   Items sheets. They may carry anything a truck is not forbidden to carry.
   Belonging to no unit, they move in each stage's Truck Convoy Movement
   Segment.
3. **Third-line trucks** shuttle between the major ports of entry
   (Alexandria, Tripoli, Tobruk, Cairo and the like) and the forward dumps.
   They work exactly like second-line trucks; the name only helps you plan.
   Nothing stops them driving straight to a combat unit.

::: spi 53.14

The lines are a planning aid, not a restriction. The recommended chain,
which neither side is obliged to follow, is: third-line trucks carry from
port to forward dump, second-line trucks from dump to the combat unit, and
there the load passes to the unit's first-line trucks, where the unit can
use it at once.

## Restrictions on trucks

::: spi 53.21 53.22

1. **Convoys move only in the convoy segment.** Any truck counter on the map
   is a **convoy** (trucks that belong to no combat unit or HQ) and moves
   only in the Truck Convoy Movement Segment
   ([Movement](../40-movement.md#trucks)).
2. **Extended CPA.** In that segment convoys use an **extended CPA**:
   **30** for heavy and medium trucks, **40** for light. They may never go
   over it. If something forces them past it, they break down
   ([Breakdown](../90-special.md#breakdown)) the moment they do.
3. **First-line trucks** move with their unit, using the basic truck CPA
   (20 or 25), and like the unit they may go over it
   ([Capability points](../30-capability-points.md)).

::: spi 53.23

4. **Low cohesion.** A combat unit at cohesion **−5 or worse** may not
   detach its first-line trucks by choice. Second- or third-line trucks
   attached to a unit as first-line trucks take on that unit's cohesion.

::: spi 53.24

5. **Loading and unloading cost CP** (2 CP each way at most times, nothing
   in the Organisation Phase; see the
   [CP cost table](../../data/tables/cp-costs.json)). A load must come off
   one truck unit before another truck unit may pick it up, even when both
   serve the same parent or convoy. A second- or third-line truck that has
   used its full extended CPA may not unload for another truck to collect
   if paying the unloading cost would take it past that CPA.
   *Exceptions:* in the Supply Distribution Segment trucks load and unload
   freely; and in a Combat and Movement Segment a unit may spend ammunition
   and fuel straight off trucks in its own hex without unloading them.

::: spi 53.25

6. **No leapfrogging.** A load carries the CP its trucks have spent. When it
   changes trucks, the new truck starts from what the load has already used,
   and over the Operations Stage the load may never travel beyond the CPA of
   the first truck that carried it. *Our example:* a medium convoy hauls
   fuel 24 CP and unloads it; a second convoy that picks it up that stage
   has only 6 CP of the fuel's allowance left, however fresh its own trucks
   are.

## Abandoned vehicles

::: spi 53.31

Trucks, and any other vehicles barred from salt marsh, that stand in a
**salt marsh** hex off a road or track are **abandoned** at once
([Movement — Special terrain](../40-movement.md#special-terrain)). Then:

1. If the vehicles were carrying infantry-type units, or are an artillery
   unit, count three traversable hexes from each enemy combat unit to the
   marsh hex.
2. If an enemy combat unit is within that distance, and at the end of the
   Movement Stage no friendly combat unit is within the same three hexes,
   the infantry **surrenders** and the guns are **captured**.
3. Otherwise the infantry continues on foot from the next Movement Stage and
   the guns are left where they stand.

::: spi 53.32

A unit with engineering capability
([Engineering](../80-engineering.md#engineers)) in a hex next to the
abandoned vehicles or guns, and not itself in salt marsh, may **recover**
them. Both the recovering unit and the abandoned vehicles pay **10 CP**
(the abandoned vehicles count as having their whole CPA). Recovery may not
be attempted if either is next to an enemy combat unit. Recovered vehicles
join the recovering unit as attached.

## Supply dumps

::: spi 54.11 54.15 54.16

A **supply dump** stores ammunition, fuel, stores and water where combat
units can reach them. Any hex may hold a dump, and every major city counts
as one already. Either player may draw on any dump in a hex he can use,
including one he has just captured. Dump counters carry ID numbers so each
player can keep his dump records (and his dummies) straight.

Plan dumps so that each lies within one Operations Stage's truck run of the
next, loading and unloading included; a chain with gaps in it stalls.

::: spi-ref 24.9

::: ruling R-018 — dump costs follow the charts: real 3 CP + 10 stores, dummy 2 CP

Building a dump costs **3 CP and 10 stores**; a dummy costs **2 CP**
([Engineering — Supply dumps](../80-engineering.md#supply-dumps)).

::: spi 54.12

A **dummy dump** is a dump counter with nothing in it. It stays hidden until
an enemy unit enters its hex, or bombs or strafes it; it is then revealed and
taken off the map.

::: variant V-005 — NJHarman: bombing and strafing do not reveal a dummy dump

### Dump capacity

::: spi 54.13

A dump may hold only so much of each supply type, by where it stands; a hex
with no dump may hold only a little. Data:
[`data/tables/supply-dump-capacity.json`](../../data/tables/supply-dump-capacity.json)
(the chart sheet numbers it 54.12).

| Location | Ammo | Fuel | Stores | Water |
|---|---|---|---|---|
| Tunis/Tripoli box (each of the four) | unlimited | unlimited | unlimited | unlimited |
| Major city | unlimited | unlimited | unlimited | unlimited |
| Village | 2,500 | 8,000 | 3,000 | 1,000 |
| Other terrain | 1,500 | 5,000 | 1,000 | 1,000 |
| No dump in the hex | 50 | 0 | 50 | 0 |

Water may be drawn from, as well as stored in, a village, a major city or a
Tunis/Tripoli box. The In Transit box may never serve as a dump.

::: note
Open question, not yet decided: whether the Tunis/Tripoli boxes are dumps or only unlimited storage ([R-073](../../rulings/R-073.md)).
:::

::: variant V-004 — NJHarman lets stores be paid in instalments, easing the stores limits

### Blowing a dump

::: spi 54.14 54.17

You may try to destroy (**blow**) a dump and what it holds, yours or one
you have captured.

1. **Who.** Only a non-gun unit may try, and only one phasing unit per hex
   may try against a given dump in a Player-Turn. It may happen in any
   segment of an Operations Stage.
2. **Cost.** Spend one third of the unit's basic CPA, rounded up. Before
   rolling you may announce an extra third or two extra thirds for **+1**
   each. The unit may never spend more than its basic CPA on the attempt,
   and may not exceed its CPA for it.
3. **Roll** one die, apply the modifiers below, and read the percentage
   under the result on the **Supply Dump Demolition Table**. That share of
   **each** supply type in the dump is destroyed.

Modifiers (add every group that applies; within a group, at most one):

- **+1** for each extra third of basic CPA spent;
- **+1** if the unit is a full (not shell) division, *or* **−1** if the
  units trying total 1 stacking point or less;
- **−2** in a major city hex; anywhere else, **+1** if the dump holds 500
  points or fewer in all, *or* **−1** if it holds 4,000 or more;
- **+1** if the units trying have just captured the dump, *or* **−1** if it
  was not just captured and the nearest enemy unit is at least 20 CP away
  by medium truck.

| Modified die | % of each type destroyed |
|---|---|
| −1 or less | 0 |
| 0 | 0 |
| 1 | 10 |
| 2 | 20 |
| 3 | 33 |
| 4 | 50 |
| 5 | 75 |
| 6 or more | 100 |

::: errata E-032 — the −1 and 7 columns read 0 % and 100 %; the chart printed 33 % in both

Data: [`data/tables/supply-dump-demolition.json`](../../data/tables/supply-dump-demolition.json)
(as printed; the errata is applied by `data/errata/E-032.json`).

A unit in a dump's hex may also try to blow it as part of a
[retreat before assault](../60-combat.md#retreat-before-assault). It may
spend only the basic one third of its CPA, and it must leave the hex
whatever the result.

*Our example:* a 1-SP company in open desert, next to the enemy, tries to
blow a dump of 600 points it has held for days. It spends two thirds of its
CPA (+1). Modifiers: +1 extra third, −1 for its size, nothing for the dump
total (600 is neither 500 or less nor 4,000 or more), nothing for capture.
A roll of 4 stays 4: half of each supply type is destroyed.

## The Commonwealth railway

::: spi 54.31 54.32 54.33

The Commonwealth railway moves supplies as well as men
([Movement — Rail movement](../40-movement.md#rail-movement)).

::: ruling R-005 — one rail stack each way may mix units and supplies and change its load en route, within both limits

- It lifts up to **1,500 tons** of supplies each Operations Stage in each
  direction. Convert Supply Points to tons with the Equivalent Weights Chart
  [below](#equivalent-weights).
- A supply run carries a **single type** of supply: fuel, ammunition or
  stores, never two of them together.
- Water is never carried: the railway hexes act as a water pipeline.
- As printed, a run carries supplies or men, not both, though men may go
  one way while supplies go the other.

::: note
Open question, not yet decided: whether that last limit or the Land Game's ruling R-005 (units and supplies may share a run) governs in the Logistics Game ([R-071](../../rulings/R-071.md)).
:::

::: spi 54.34

Once each calendar month the railway is busy hauling its own water for one
whole Operations Stage and may carry nothing. The Commonwealth player
announces each month which stage that will be.

::: spi 54.35

Supplies may be loaded at any point and set down at any other. Once they
reach the hex where they are unloaded they may not move again that
Operations Stage.

## Axis use of the railway

::: spi 54.4 54.41 54.42

::: errata E-033 — the Axis may use the rail lines under these cases, despite the Land Game's Commonwealth-only wording

The Axis may run trains on the coastal line from Egypt into Libya once he
holds it and has shipped in rolling stock. The Barce line east of Benghazi
is never usable.

1. **Control.** The Axis controls a rail hex if an Axis land combat unit of
   any kind was the last to pass through it. With **five or more
   contiguous** controlled rail hexes he may use them.
2. **Repair, not building.** The Axis may repair controlled rail hexes at
   the Commonwealth's rate, but may never lay new track.

::: spi 54.43 54.44 54.45

3. **Rolling stock.** For every **250 stores and 100 fuel** delivered from
   Europe to any controlled, working rail hex, the Axis may activate his
   contiguous controlled rail hexes to haul **300 tons** of supplies in one
   direction per Operations Stage. Moving **one stacking point** of units
   needs active stock worth **900 tons**.
4. The stores and fuel spent on rolling stock are gone for good. If the
   Axis ever holds fewer than five contiguous rail hexes, all his rolling
   stock is destroyed. Neither side may use the other's rolling stock.

::: note
Open question, not yet decided: whether rolling-stock lots add up, whether capacity is per direction, and when Axis trains move ([R-072](../../rulings/R-072.md)).
:::

::: spi 54.46

Otherwise every Commonwealth rule for moving men and supplies by rail
applies to the Axis too.

## Equivalent weights {#equivalent-weights}

::: spi 54.5

The **Equivalent Weights Chart** converts points into tons (for naval
convoys, interport transfer, rail and air) and into stacking points (for
rail and interport moves). Data:
[`data/tables/equivalent-weights.json`](../../data/tables/equivalent-weights.json).

| One point of | Tons |
|---|---|
| Ammunition | 4 |
| Fuel | 1/8 |
| Stores | 1 |
| Water | 1/6 |

| Moved by | Replacement point | Truck (motorisation) point |
|---|---|---|
| Axis naval convoy | see the Axis Replacement Pool | see the Axis Replacement Pool |
| Interport | counted in stacking points | 50 tons † |
| Railroad | counted in stacking points | counted in stacking points |
| Air | 2 tons (infantry-class only) | not allowed |

::: ruling R-070 — the "unit of stacking points" row reads as 1: a unit counts its own printed stacking points

| By rail or interport, one | Counts as stacking points |
|---|---|
| Truck point ‡ | 1/10 |
| Replacement point | 1/5 |
| Squadron ground support unit | 1/2 |
| "Unit of stacking points" (as printed) | 1/2 |

†, ‡: only for truck points that are unattached, or attached beyond the
total TOE Strength Points of the parent they belong to; trucks within that
total travel with their unit.

The last row's 1/2 is treated as a slip: any other unit moved by rail or
interport counts exactly its printed stacking points.


*Our example:* the Commonwealth railway's 1,500 tons move 375 ammunition
points, or 1,500 stores, or 12,000 fuel points in one run.

---

*Drawn on: SPI §53.0–53.32 and §54.0–54.5, the chart sheet (jp2 108–109), and the September 1979 errata to 8.71 and 54.17.*
