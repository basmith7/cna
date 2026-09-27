---
title: Abstract air
status: provisional
---

# Abstract air

The Logistics Game may be played with the Land Game alone, leaving the Air
Game out. This file says what changes then. Very little does: the missing
air war shows up mainly as trucks the players do not get, or lose, plus a
cut in Axis fuel landed in Africa. Convoy attacks and the strikes on the
Commonwealth fleet borrow the Land Game's abstract procedures from
[Abstract logistics and air](../95-abstract-logistics-and-air.md).

Everything here applies **only when the Air Game is not played**. With the
Air Game, ignore this file.

::: spi-omit 58.0 — commentary introducing the section; its effect is stated above

## Axis convoys {#axis-convoys}

::: spi 58.1

The Commonwealth attacks Axis naval convoys with the Land Game's procedure,
[Simplified Axis convoys](../95-abstract-logistics-and-air.md#simplified-axis-convoys)
(SPI 32.6): the lane's bombing chart column gives the bomb points, and two
dice on the Air Bombardment Table give the percentage destroyed. The only
difference is the cargo: a Logistics Game convoy carries itemised stores,
fuel, water, trucks and replacement points rather than supply units and
motorisation points, so the percentage is applied to those items.

These may **not** be attacked this way:

- Axis coastal shipping;
- either player's tactical shipping.

::: ruling R-032 — the abstract convoy attack is made in the convoy bombing segment

The attack is made in the bombing segment (3) of the convoy resolution phase,
once per turn, the only convoy-resolution segment that still runs without the
Air Game.

::: note Open question
How the 32.6 rounding rules (the 10 % result versus 20 % or more) map onto
itemised cargo is still open.
:::

## Commonwealth fleet bombardment {#fleet-bombardment}

::: spi 58.2

The Axis may strike the Commonwealth fleet exactly as in the Land Game's
[Bombardment of the fleet](../95-abstract-logistics-and-air.md#bombardment-of-the-fleet)
(SPI 32.7): a secret die roll for the number of strikes, at most one per
stage, damage read from the Air Bombardment and Secondary Barrage Targets
table.

::: ruling R-032 — fleet strikes are plotted and resolved in the Commonwealth fleet phase

The Logistics sequence has no tactical naval movement segment, so each strike
is plotted secretly while the Commonwealth assigns its ships (phase E,
segment 1) and resolved at the end of that same fleet phase; still at most
one per operations stage.

## Axis fuel lost on landing {#axis-fuel-loss}

::: spi 58.3

::: ruling R-090 — only convoy fuel from Europe is cut; the loss is rounded up

Supplies are otherwise untouched. One rule applies, to the Axis only:

1. When fuel from a naval convoy is unloaded in a port, the Axis at once
   loses **three-quarters** of the Fuel Points unloaded, rounding the loss
   up (the Axis keeps the rounded-down quarter). Fuel moved between African
   ports by coastal or tactical shipping has already paid, and is not cut
   again. This stands for fuel the Luftwaffe and
   Regia Aeronautica would have burned.
2. Only then is any evaporation loss worked out, on the quarter that is left.

*Example (ours):* 80 Fuel Points are unloaded at Benghazi. 60 are removed at
once; evaporation is later taken on the remaining 20.

*Example (ours):* 30 Fuel Points arrive by convoy at Tripoli; the loss is
22.5, rounded up to 23, and 7 remain.

## Trucks {#trucks}

The air war in Africa ate trucks: they hauled supplies to airfields and were
strafed and bombed on the roads. Without the Air Game, both players' truck
fleets shrink in three ways.

::: spi-omit 58.4 — heading only; the rules under it follow

### Smaller starting truck fleets

::: spi 58.41

::: ruling R-091 — the set-up loses 10 % of its Truck Points, rounded up, in proportion by type

Each player's initial set-up has fewer **Truck Points**: those that were, or
would have been, given the job of supplying air facilities are left out.

SPI prints no figure, so we use the same rate as for arriving trucks: each
player removes **10 %** of the Truck Points in the initial set-up, rounding
fractions up, spread in proportion by truck type (light, medium, heavy) and,
as for abstract losses below, between trucks in convoy and trucks attached.

### Abstract truck losses {#abstract-truck-losses}

::: spi 58.42 58.44

::: ruling R-092 — monthly truck loss at the first naval convoy stage, on-map base, total rounded up and split by largest remainder

On top of what land combat destroys, both players lose trucks each month to
abstract strafing and bombing.

1. Find the percentage the way the Land Game finds motorisation point losses
   ([Motorisation points](../95-abstract-logistics-and-air.md#motorisation-points),
   SPI 32.57): read the month on the **Abstract Truck Loss Chart**,
   Commonwealth figure left of the stroke, Axis right.
2. Apply that percentage to the player's Truck Points instead of
   motorisation points.
3. The owner chooses where the losses come from, but they must be spread
   **in proportion** both by truck type (light, medium, heavy) and between
   trucks in convoy and trucks attached to units.

The chart is the same one the Land Game uses for motorisation points; it is
data, not repeated here: `data/tables/motorisation-losses.json` (October
1940 to January 1943). The chart sheet heads it 58.5; the rules call it
58.44.

*Example (ours):* a player has 200 Truck Points: 20 light and 30 medium in
convoy, and 40 light, 70 medium and 40 heavy attached. A 10 % loss is 20
points, taken as 2 light and 3 medium from the convoys and 4 light, 7 medium
and 4 heavy from the attached trucks.

**When and on what.** As in the Land Game, the loss for the previous month
is taken in the naval convoy stage (III) of the month's first turn. The base
is the player's Truck Points on the map at that moment, the Tripolitania–Tunis
boxes included; trucks still at sea or not yet arrived do not count.

**Rounding.** Work out the total loss first and round it up. Then give each
type-and-location share its whole-number part, and hand the points still
owed one at a time to the shares with the largest fractions left over (ties:
the owner chooses). The shares always add up to the total.

### Trucks withheld on arrival {#arriving-trucks}

::: spi 58.43

Both players also lose **10 %** of every batch of Truck Points that reaches
North Africa, at the moment it arrives, rounding fractions **up**. This
applies to trucks that come:

- from the Commonwealth Truck Production Table; or
- from the Axis Replacement Pool.

Trucks shown on the reinforcement track are **not** reduced.

*Example (ours):* 23 Axis Truck Points arrive from the Replacement Pool;
2.3 rounds up to 3, so 20 enter play.

---

*Drawn on: SPI §58.0–58.44, reading §32.57–32.59, 32.6 and 32.7 for the
procedures it borrows.*
