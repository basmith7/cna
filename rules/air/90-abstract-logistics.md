---
title: Air Game — abstract logistics with the Air Game
status: provisional
---

# Abstract logistics with the Air Game

::: spi 47.0

When the Air Game is played **without** the Logistics Game, supply stays
abstract: the rules of [Abstract logistics and air](../95-abstract-logistics-and-air.md)
(§32) apply, changed only as this page says. Everything not mentioned here
is §32 as written.

## Supply for aircraft

::: spi 47.1 47.11 47.12 47.13

- Every **off-map** air facility, in North Africa or across the
  Mediterranean, has unlimited supplies for servicing aircraft.
- **Cairo and Alexandria** have unlimited supplies for servicing
  Commonwealth aircraft, for any SGSU in one of their hexes or within reach
  of them (next item).
- An SGSU draws supplies from any friendly supply unit, or from Cairo or
  Alexandria, within **15 CP**, traced as §32 traces a combat unit's supply.

::: spi 47.14

**Depots.** Besides §32's regular supply units, each side receives **depot**
supply units. A depot starts with **180 fuel and 40 ammunition**. It stays a
depot until it holds 60 fuel or less, and from then on is a regular supply
unit. A depot never takes in fuel or ammunition, and its contents go only
to SGSUs and to the motorisation points moving that depot: never to other
supply units, combat units or other motorisation points.

## What the Air Game costs

::: spi 47.2 47.21 47.22 47.23

| Activity | Cost |
|---|---|
| A gun-class unit fires flak at one target group | 1 ammunition |
| Other units firing flak | nothing |
| Arming a fighter or fighter-bomber squadron (TacAir and bombs) | nothing |
| Arming a whole non-fighter squadron | 1 ammunition |
| Refuelling a whole fighter or fighter-bomber squadron | 1 fuel |
| Refuelling a whole Axis non-fighter squadron | 2 fuel |
| Refuelling a whole Commonwealth non-fighter squadron | 3 fuel |

These replace the per-aircraft costs of the full Air Game
([maintenance](30-flight-and-maintenance.md#maintenance)).

### Upkeep, refits and repairs {#upkeep-refits-and-repairs}

::: ruling R-173 — SGSU upkeep with the Air Game and abstract logistics

::: ruling R-174 — refit and repair costs with the Air Game and abstract logistics

Nothing else in the Air Game spends supplies here (§32 ignores every other
supply cost, 32.11):

| Full Air Game cost | With abstract logistics |
|---|---|
| SGSU upkeep, 1 fuel and 1 water a stage and 1 stores a turn (35.14) | nothing ([R-173](../../rulings/R-173.md)) |
| 1 stores per squadron refit roll (38.36) | nothing ([R-174](../../rulings/R-174.md)) |
| 1 stores and 1 fuel per repaired aircraft (45.62, 45.64) | nothing ([R-174](../../rulings/R-174.md)) |

What these supplies were a condition for still holds: an SGSU may refit
or repair aircraft only while it can draw supplies under 47.11–47.13, at
an off-map air facility, in or within reach of Cairo or Alexandria
(Commonwealth only), or within 15 CP of a friendly supply unit, depots
included. Rolls, limits and delays are as printed.

## Moving supply units

::: spi 47.3 47.31 47.32 47.33 47.34

- A depot needs **50 motorisation points** to move, and moves only in the
  truck convoy phase; it is never attached to a combat unit.
- By rail a depot counts as two supply units. The Commonwealth may not move
  a depot by sea; the Axis may, by coastal shipping, at **3,000 tons** per
  depot.

::: spi 47.35

**By air**, regular supply units (not depots) may be flown, the counter
moving from one place to the other, by aircraft able to carry transport:

| Side | Aircraft | Supply unit carried |
|---|---|---|
| Axis | any 30 | up to 8 ammunition and 20 fuel |
| Axis | any 60 | any contents |
| Commonwealth | any 20 | up to 10 ammunition and 25 fuel |
| Commonwealth | any 50 | any contents |
| Either | any 10 | a dummy supply unit |

## Receiving depots

::: spi 47.4 47.41 47.42

Depots come on top of the regular supply units of the Simplified Supply
Availability Tables (`data/tables/simplified-supply.json`):

- **Axis:** one depot for each regular supply unit the table gives.
- **Commonwealth:** per Game-Turn, one depot in the table's first supply
  period (to April 1941), two in the second (May 1941 to May 1942), three
  in the third (June 1942 on).

## Motorisation points {#motorisation-points}

::: spi 47.5 47.51

§32's abstract truck losses go: ignore 32.57 and 32.59. Instead, under
32.56, motorisation points can be destroyed as trucks are, by strafing and
by land support bombing in the Air Game.

::: spi 47.52 47.53

Initial motorisation points are counted as in §32, but **including** the
second- and third-line trucks the scenario lists at air facilities. During
play, motorisation points arrive as truck replacements do: one point for
each medium or heavy truck point the side could bring in, from the Axis
truck production chart of the replacement pool or the Commonwealth truck
production table.

## Axis convoys {#axis-convoys}

::: spi 47.6 47.61 47.62 47.63

This replaces [§32's simplified convoys](../95-abstract-logistics-and-air.md#simplified-axis-convoys).
A convoy is the turn's supply units, motorisation points and replacement
points, spread over the available lanes with no tonnage limit, but at most
**three regular supply units, three depots and 25 motorisation points per
lane** per convoy stage, and replacement points within the replacement
pool's limits. A successful Commonwealth convoy reconnaissance learns the
convoy's totals: regular units, depots, motorisation points, and tank,
infantry, gun and armoured-car replacement points.

::: spi 47.64 47.65

::: ruling R-127 — a 5 % convoy result is applied like 10 %

Convoys are attacked under the Air Game's convoy bombing rules (41.6), not
§32's bombing chart. The
result is applied as follows:

| Result | Effect |
|---|---|
| 5 % or 10 % | motorisation points (fractions down) and replacement points (fractions up) only ([R-127](../../rulings/R-127.md)) |
| 20 % | every item except depots, fractions down; whatever the arithmetic, at least one regular supply unit and a single point of every replacement class are lost |
| 30 % or more | as 20 %, and at least one supply unit of either kind, counting all supply units together |

## The fleet {#the-fleet}

::: spi 47.7

§32's abstract bombardment of the Commonwealth fleet is not used: the fleet
is attacked under the Air Game's rules (§41).

## Stacking

::: spi 47.8 47.81 47.82

Road and track stacking limits ([Stacking & ZOC](../50-stacking-and-zoc.md#roads))
are ignored, as in §32. One depot may stack
in a hex on top of §32's limit for regular supply units.

## Anti-air units

§32's anti-air modifications (32.8) do **not** apply with the Air Game:
every AA unit and AA point stays in play and fires flak under §46, paying
for it as above (47.21).

::: ruling R-114 — anti-air units with the Air Game and abstract logistics

## Engine notes

- With the Air Game on and the Logistics Game off, load §32 and then apply
  this page, which replaces 32.57, 32.59, 32.6 and 32.7 outright; [the overview](00-overview-and-sequence.md#switch) lists what
  the Air Game replaces in every combination.
- A depot is a supply unit with a `depot` flag that clears when its fuel
  falls to 60 or less.
