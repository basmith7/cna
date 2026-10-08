---
title: Air Game — air facilities
status: provisional
---

# Air facilities

::: spi 36.0

Aircraft fly from, land at and are serviced at **air facilities**. There are
four kinds: airfields and air landing strips for land planes, flying-boat
basins and alighting areas for flying boats. What sets them apart is
**capacity**: how many squadrons a facility can land and service in an
Operations Stage. Facilities are built by engineers
([construction](../80-engineering.md#air-facilities), SPI 24.7), lose
capacity to bombing and barrage, and are counters on the map; the ones that
exist when a scenario starts are listed in its set-up (`data/scenarios/`).
The squadron ground support units (SGSUs) that do the servicing are a
separate counter (§35, to come in this folder).

## Capacity at a glance

| Facility | Maximum capacity (squadrons) | Takes | Destroyed at capacity 0 |
|---|---|---|---|
| Airfield | 6 | land planes | yes, rebuilt level by level |
| Air landing strip | 1 | land planes | yes, removed from the map |
| Flying-boat basin | 3 | flying boats only | yes |
| Flying-boat alighting area | 1 | flying boats only | yes |
| Off-map facility | as marked on the facility | as marked | never by bombing |

## Airfields

::: spi 36.1 36.11 36.12 36.13

An **airfield** is a full air base: runways, workshops and complete
maintenance. A counter marks each one built. Its capacity is at most
**six**: in one Operations Stage it can land at most six squadrons' worth
of aircraft, whatever the squadrons' size, and ready at most six squadrons'
worth (aircraft maintenance, §38). Once six squadrons have landed there in a
stage, further aircraft must go elsewhere, even in an emergency. No more than
six SGSUs may be in an airfield hex (off-map facilities excepted, below).

*Our example.* Two Commonwealth squadrons of Hurricanes and four of
Blenheims are back from a morning mission at a full-capacity airfield. A
seventh squadron, damaged and short of fuel, arrives later in the same
stage: it may not land there and must reach another facility or follow the
emergency flight rules.

::: spi 36.14 36.15

**Damage.** Bombing from the air and artillery barrage
([barrage targets](../60-combat.md), SPI 12.5) lower an airfield's capacity
one level at a time; players keep a running record. A field bombed from six
down to three serves three squadrons until it is rebuilt. It keeps all six
of its SGSUs meanwhile, though only as many can work as the capacity
allows. At capacity **zero** the airfield is destroyed for every purpose.

Desert raiders can damage airfields too. Other land units never do, except
by barrage; but a land combat unit that occupies an airfield's hex captures
it or destroys it outright, as that unit's player chooses. An airfield belongs to no
one: whoever holds it may use it.

::: spi 36.16 36.17 36.18

**Servicing and supply.** The airfield provides the capacity; the SGSUs on
it do the work. An airfield is also a supply dump for its SGSUs: fuel,
ammunition, stores and the rest may be stockpiled there and drawn by any
SGSU on the field to service and ready aircraft. Land units may draw on it
only in an emergency, and the player decides what counts as one.

**Built-in flak.** Every airfield has one anti-aircraft strength point of
its own, on top of any AA units present. It fires only at aircraft that
strafe or dive-bomb the field.

## Air landing strips

::: spi 36.2

A **landing strip** is a levelled patch of desert with minimal servicing.
It follows every airfield rule above except that its capacity is **one**
squadron. When that one level is destroyed, the strip is gone: remove the
counter.

## Flying-boat basins

::: spi 36.3

A **flying-boat basin** is an airfield for flying boats, and flying boats
can use nothing else (a basin or an alighting area); land planes may not use
basins. It has every feature of an airfield, including the built-in AA
point, but a capacity of **three** squadrons. Basins go in any coastal hex.
Trucks bring supplies straight into the hex; no other transport is needed.

## Flying-boat alighting areas

::: spi 36.4

An **alighting area** is a basin with a capacity of **one** squadron that
cannot be hit by artillery barrage. Air bombardment still reduces it
(air bombardment, §41).

## Off-map air facilities

::: spi 36.5

Some facilities lie off the map or in boxes: the Tunisia boxes, the
Commonwealth bases such as Deversoir beyond map E, and others. They work like
on-map facilities except that:

1. supplies for servicing and repairing aircraft there are **unlimited**;
2. they may hold more SGSUs than the usual limit, up to the figure printed
   on the facility;
3. bombing can reduce them to zero but never destroys them. The
   Commonwealth rebuilds all of its off-map facilities together with one
   roll per Game-Turn on the Malta Air Facility Construction Table, the
   result being the total levels restored.

The Axis bases across the Mediterranean, in Italy and the Aegean, cannot be
bombed at all (§43).

## Engine notes

- A facility needs: kind, hex (or box), owner by occupation, current
  capacity, maximum capacity, the SGSUs on it, its supply stock, and per
  Operations Stage the squadrons landed and readied.
- Capacity counts **squadrons**, never aircraft: a squadron of any size
  uses one level.
- References to §35, §38, §41 and §43 become links as those files land.
