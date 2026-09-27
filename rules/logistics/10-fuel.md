---
title: Fuel
status: provisional
---

# Fuel

In the Logistics Game every motor vehicle burns **fuel** to move. This file
covers how fuel is counted, how much a unit burns, where it must draw it
from, how it is carried, and how stocks shrink over time. It replaces the
per-stage abstract fuel cost of the Land Game played alone
([Abstract logistics and air](../95-abstract-logistics-and-air.md#supply-expenditure)).

::: spi-omit 49.1 49.2 49.3 — subsection headings; the rules under them are restated below

## Who uses fuel

::: spi 49.0 49.12

Treat a vehicle as a fuel user unless some rule says it is not. Fuel users
include:

- every TOE Strength Point of vehicles (tanks, trucks, armoured cars and the
  like);
- every gun-class unit;
- any HQ whose TOE Strength Points are printed without parentheses.

These do **not** use fuel: motorcycles, and tanks or trucks being towed back
to a repair facility. Desert raiders, patrols and a few other units follow
their own fuel rules ([Special units](../90-special.md)). Fuel is also spent
on some construction; the amounts are on the
[Construction Chart](../80-engineering.md#construction).

Record every change in a fuel stock at once: on the Supply Dump Sheet for a
dump, the TOE sheet for a unit, and the Truck Convoy Sheet for fuel on the
road.

## Fuel Points

::: spi 49.11 49.19

Fuel is counted in **Fuel Points**. One point stands for about an eighth of
a ton of petrol and oils (the weight the Equivalent Weights Chart uses). Aircraft do not use Fuel Points: the Air Game
counts fuel in its own abstract way.

Fuel belongs to nobody. Either side may burn fuel it finds or captures, so a
dump is worth taking.

## Consumption and capacity

::: spi 49.13 49.14

Each TOE Strength Point of vehicles has two values on its side's
organisation sheets: a **fuel consumption rate** and a **fuel capacity
rating**. We do not reproduce those values here; they are per-unit data.

1. **Consumption.** For each block of five Capability Points spent on
   movement, and for any part-block left over, the Strength Point burns
   its consumption rate in Fuel Points. Only CP spent moving from hex to
   hex count; CP spent on combat or anything else burn no fuel.
2. **Capacity.** The capacity rating is what one Strength Point holds in
   its own tanks: its CPA divided by five, times its consumption rate. A
   full tank is meant to last exactly one full CPA of movement.

*Example.* A Strength Point of armoured cars with rate 2 moves and spends
13 CP. That is two full blocks of five and one part-block, so three blocks:
it burns 3 × 2 = **6** Fuel Points.

::: ruling R-041 — part-blocks of five CP are rounded up for each Movement Segment's draw

Part-blocks are counted **per Movement Segment**: the CP a unit will spend
moving in one segment are split into blocks of five and any part-block is
charged in full, when the fuel for that segment is drawn. Nothing carries
over to the next segment; three 3-CP moves in one stage cost three blocks.

::: note
Open question, not yet decided: capacity when the CPA is not a multiple of five ([R-043](../../rulings/R-043.md)).
:::

## Drawing fuel

::: spi 49.15 49.16

Fuel can only be burned where it is: in the same hex as the Strength Point
using it. A unit's own tanks are always with it, so most movement is simply
charged against the fuel in its tanks, and you must track how far each
unit has moved since it last filled up.

At the start of each Movement Segment in which a unit moves:

1. Decide how far it will go this segment and work out the fuel needed.
2. Take that fuel from any source in the hex where the unit starts the
   segment: a dump, first-line trucks, another source there, or its own
   tanks. Fuel on second- or third-line trucks must be unloaded before it
   can be drawn.
3. Move the unit.

Filling up costs no CP. If the unit moves again later in the same
Operations Stage, it draws from whatever is in its new hex, or from its own
tanks.

## Siphoning

::: spi 49.17

When one of two units in a hex holds fuel while the other is dry, and no
other fuel is in the hex, the players may treat it as an emergency (they
decide together what counts as one). The owner may then move some or all of
the first unit's fuel into the second, up to the second unit's capacity.
Both units pay **3 CP**. This may be done in any Movement Segment.

Fuel may be siphoned in the same way from enemy vehicles that are abandoned
or broken down, never from destroyed ones. When asked, the enemy player
states how many Fuel Points such vehicles hold.

## Carrying fuel

::: spi 49.18 49.2

Only trucks, trains and (sometimes) aircraft carry fuel from place to
place. Tanks and other vehicles never do, and neither does infantry on
foot. How much a truck carries is on the Truck Characteristics Chart; how
much an aircraft lifts is on the Aircraft Characteristics Chart.

A truck carrying fuel burns fuel as it moves like any other vehicle, and
may burn its own cargo to do so. A long haul can use up a large share of
the load before it arrives.

## Evaporation and spillage

::: ruling R-040 — the per-turn loss reaches fuel in tanks; the hot-weather loss does not

::: spi 49.3

Fuel stocks shrink wherever they are kept. The rates are in
[`data/tables/fuel-evaporation.json`](../../data/tables/fuel-evaporation.json):

1. **Every game-turn**, in the Stores Expenditure Stage, each player cuts
   every fuel stock on the map by **6 %**, rounding the loss down. This
   includes the fuel in each unit's own tanks. Fuel in convoys at sea is
   exempt.
2. **Hot weather.** When an operations stage is found to have hot weather,
   cut every stock by a further **5 %** at once. This loss spares the fuel
   in units' own tanks (it is the weather rule's loss, SPI 29.34).
3. **Commonwealth containers.** From September 1940 through the last
   game-turn of August 1941, the Commonwealth's per-turn rate is **9 %**
   instead of 6 %. (Their early flimsy cans leaked; the rate falls once
   they adopt copies of the German jerrycan.) The same loss applies to some
   water sources (SPI 52.44).

*Example.* A Commonwealth dump holds 75 Fuel Points in the Stores
Expenditure Stage of a turn in March 1941. 9 % of 75 is 6.75, rounded down
to 6, so 69 remain.

::: variant V-002 — fuel in vehicles' tanks does not evaporate

::: note
Open question, not yet decided: how the 9 %, 6 % and hot-weather rates combine ([R-042](../../rulings/R-042.md)).
:::

---

*Drawn on: SPI §49.0–49.3.*
