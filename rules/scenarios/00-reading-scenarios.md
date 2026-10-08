---
title: Reading a scenario
status: provisional
---

# Reading a scenario

A scenario is a starting position, a length and a way to judge the result.
The game has five groups of them: four cover a single offensive each, and the
fifth is the whole campaign. This page explains how a scenario's set-up is
read; each group has its own page with its special rules, and its set-up is
data in `data/scenarios/`, one file per scenario.

::: spi-omit 59.0 — the designer's commentary on the scenarios (which to try first, how long set-up takes, how to read victory); advice only

## What a scenario gives {#contents}

::: spi 59.1 59.11 59.12

Groups one to four each state, for every scenario in the group:

1. how long it lasts, in Game-Turns and Operations Stages;
2. its victory conditions;
3. where every land and air unit starts, and at what strength;
4. where every supply dump starts, and what it holds;
5. where every truck starts;
6. what each side has off the main map: Malta for the Commonwealth, and
   Italy, Sicily and Crete for the Axis;
7. how to play it without the Air Game, the Logistics Game or both;
8. any rules special to it.

The fifth group, the campaign game, is built the same way but uses the
whole schedule of arrivals.

In the data, items 3 to 6 are the `sides` blocks of each scenario file
(`deployments`, `air`, `supply`, `trucks`, `fleet`), item 7 is the
`abstractions` block, and item 8 is each side's `special` list.

## Reading the set-up {#set-up}

::: spi 59.2

Units are listed by the hex they start in. A listed unit means **that unit
and everything assigned to it on its OA sheet** (`data/oa/`). Where the
scenario's unit differs from its sheet, it says how:

| In the set-up | In the data | Meaning |
|---|---|---|
| *Less* | `less` | units on the sheet that this unit does not have |
| *Assg* | `assigned` | extra units assigned to it (they may later be detached) |
| *Det* | `detached` | units of its sheet that start elsewhere; each is listed again where it starts |
| *Att* | `attached` | units attached to it but not assigned |
| *Consists of* | `consists_of` | a roster that replaces the sheet's entirely |
| *HQ:* | `alone` | the headquarters counter only, without its subordinates |

A garrison sheet with no single headquarters is placed whole: the data names
the formation (`formation`) instead of a unit.

- **More than one hex.** When a group is listed for several hexes, its
  owner divides it among them as he likes, within stacking limits.
- **Free organisation.** Units starting together in one hex may be
  attached to and detached from one another before play in any way the
  [organisation rules](../70-organisation.md) allow.
- **Over the limits.** A unit that starts larger than its formation limits
  allow may operate as it is. It may not take on any new unit, and once a
  unit leaves it, it may not take on another that would break the limits.
- **First-line trucks.** Trucks listed with a group are first-line trucks
  and must be given to the units of that hex, in any split.
- The set-up marks a unit's type in parentheses where its name does not
  show it (infantry, recce, tank, artillery, anti-tank, anti-aircraft,
  headquarters), and names a parent formation the way its counter does. The
  data drops both: the OA sheet already says them.

## Air forces {#air}

::: spi 59.3 59.31 59.32 59.33 59.34 59.35 59.36

Each scenario lists, per side, the planes by type with how many of them are
ready, the pilots, the air facilities and the squadron ground support units
(SGSUs), split between North Africa and Malta (Commonwealth) or North
Africa and Italy, Sicily and Crete (Axis).

- Every plane starts **fuelled and armed**, ready or not, at no cost in
  supply.
- Planes are shared out among the SGSUs as their owner likes, within the
  squadron composition rules; pilots likewise.
- An SGSU may start at any air facility its side owns, up to the number
  that facility can ready.
- **No maintenance** is carried out on any plane in a scenario's first
  Operations Stage.

::: variant V-006 — maintenance allowed in the first Operations Stage

The air set-ups are kept as data (`air`) now; the rules that use them are
the Air Game's.

## Trucks {#trucks}

::: spi 59.4 59.41 59.42 59.43 59.44 59.45

Trucks come in three lots: first-line trucks, second- and third-line trucks
for supply, and second- and third-line trucks for air facilities.

1. **First-line** trucks are listed with the units in a hex and are given
   to those units (above).
2. **Air-facility** trucks start on an air facility.
3. **Supply** trucks start in a hex with a friendly combat unit or dump in
   it, or in a city, town or oasis, unless the Axis player
   starts them off the map; they are spread as their owner likes.

Any truck may begin play already loaded, with supplies of any kind or with
troops or anti-aircraft units aboard, free of charge. Supplies loaded this way are
**extra** to those the scenario lists.

## Supply {#supply}

::: spi 59.5 59.51 59.52 59.53 59.54

Each scenario lists where each side's supplies start and how much there is.

- Supplies are listed either at dumps or at air facilities. Every air
  facility counts as a dump. If a dump's supplies are placed where an air
  facility's are, the two become one dump.
- Where a scenario gives a single total for a side's air facilities, it is
  spread among them as their owner likes, but none of it may go to an air
  facility off the map.
- Some scenarios give **dummy** dumps as well as real ones. A dummy dump may
  not share a hex with an air facility.
- Axis coastal shipping always starts **empty**.

## Without the Air Game or the Logistics Game {#abstractions}

::: spi 59.6 59.61 59.62

- **Air Game left out:** ignore every truck and every supply listed at or
  for air facilities; the [abstract air rules](../logistics/60-abstract-air.md)
  govern.
- **Logistics Game left out** (with or without the Air Game): the game uses
  [motorisation points and supply units](../95-abstract-logistics-and-air.md)
  instead of trucks and supply points, set up as below. Each scenario's own
  abstraction block (`abstractions` in the data) says what else changes;
  it **replaces** the matching block of the full set-up unless it says it is
  in addition.

### Motorisation points {#motorisation}

::: spi 59.63 59.64

Initial motorisation points come from the trucks the scenario lists, unless
its own instructions differ: **one point per medium or heavy truck**; light
trucks give none.

1. **Attached** points: count the first-line trucks hex by hex; the points
   start attached to the units in that hex.
2. **Unattached** points: count the second- and third-line trucks the same
   way. Trucks listed for air facilities are left out when the Air Game is.

Example: a division listed with 8 light, 20 medium and 6 heavy trucks starts
with 26 attached motorisation points.

After the start, motorisation points may be attached and detached freely
under the Land Game rules, except for points still carrying the supplies of
59.66 B (below).

### Supply units {#supply-units}

::: spi 59.65

The scenario lists each side's regular supply units (and, with the Air Game
but not the Logistics Game, depot supply units) with where they start and
what each holds. If the set-up forces more supply units into a hex than
stacking allows, they may stay; nothing more may join them until the hex is
back within limits, and from then on the normal limits apply. Supply units
being carried by motorisation points do not count against stacking.

### Extra supplies at the start {#extra-supplies}

::: spi 59.66

These come on top of the supplies the set-up lists.

1. **Attached points.** An attached motorisation point that is not
   transporting troops or guns may begin with **1 ammunition point or 3
   fuel points** aboard. The unit spends this load before it draws on any supply unit, and may
   not hand it to a supply unit. While loaded, the point may be detached
   only to a combat unit under the same parent.
2. **Unattached points.** In each hex, every full **30** unattached points
   may start carrying one regular supply unit. Points listed at air
   facilities (Air Game only) may instead carry one **depot** supply unit
   per full **50** points, or one regular supply unit per full 30. Points
   that do not make a full group carry nothing. The Tripoli and Tunisia
   boxes count as hexes for this.

Groups may be mixed. Example: a hex holds 70 air-facility points and 65
others. The air-facility points may carry either one depot unit (using 50,
the other 20 too few for anything) or two regular units (using 60); the
others carry two regular units.
