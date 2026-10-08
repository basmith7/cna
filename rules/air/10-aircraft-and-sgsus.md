---
title: Air Game — aircraft and squadrons
status: provisional
---

# Aircraft and squadrons

Aircraft are individual counters by type; each belongs to a **squadron**,
and each squadron has a ground echelon on the map, its **squadron ground
support unit** (SGSU). This file will restate the aircraft themselves (§34;
their ratings are already data,
[`data/tables/aircraft-characteristics.json`](https://github.com/basmith7/cna/blob/main/data/tables/aircraft-characteristics.json))
and, below, the squadrons and their SGSUs (§35).

## Squadrons and their SGSUs

::: spi 35.0

The squadron is the only level of air organisation the game uses (a German
*Staffel*, an Italian *squadriglia*). Every aircraft is assigned to one, and
the squadron's record sheet lists its aircraft, its pilots and its supplies.
The squadron's SGSU is its ground crew, workshops and transport: it keeps
the squadron's aircraft fuelled, refitted and armed.

### The SGSU counter

::: spi 35.1 35.11 35.12

An SGSU marks where its squadron is based, normally at an air facility. It
is not an air unit and does not carry the aircraft with it. It is a
**vehicle** unit, as medium trucks are, with its CPA printed on the counter,
and it moves in the truck convoy phase. It has **no stacking value** and no
combat strength of any kind. When an enemy combat unit moves next to an SGSU
with no friendly combat unit in its hex, the SGSU may react if it can; if it
cannot, it is eliminated. How many squadrons a facility can actually work is
set by the facility's capacity ([air facilities](20-air-facilities.md)).

::: spi 35.13

SGSUs enter play when their player calls them in, under the air
reinforcement rules (§34, 34.8). Their squadron numbers are historical but
need not be used historically. An eliminated SGSU may come back one
Game-Turn later by the same rules.

::: spi 35.14 35.15

**Its own supply.** For its own upkeep every SGSU needs, each Operations
Stage, **1 fuel and 1 water**, and each Game-Turn **1 stores**. An
SGSU lacking any of these cannot repair its aircraft. Servicing the aircraft
costs fuel and ammunition on top
([maintenance](30-flight-and-maintenance.md#maintenance)). Trucks may be
attached to an SGSU as its first-line transport, to carry what it needs.

::: spi 35.16 35.17

SGSUs may build landing strips and flying-boat alighting areas
([construction](../80-engineering.md#air-facilities)). Only SGSUs refuel
and refit aircraft. Any SGSU may refuel any aircraft; refitting is best done
by the aircraft's own squadron's SGSU, and costs +1 on the refit roll at any
other. Nothing is serviced beyond the facility's capacity.

::: spi 35.18

SGSUs marked USAF (United States Army Air Forces) may not be used before
**1 August 1942**.

### What a squadron may hold

::: spi 35.2 35.21

A squadron holds one class of aircraft: **fighters**, **bombers** or
**transports**. Fighter-bombers may go in a fighter or a bomber squadron,
and reconnaissance aircraft in any. Keeping one aircraft type per squadron
is advised for bookkeeping but is not a rule.

::: spi 35.28

German and Italian aircraft never share a squadron, since they need
separate servicing; but an Italian squadron may consist entirely of German
aircraft (not the reverse).

::: spi 35.23 35.26

**Size.** A squadron has a **ready capacity**, the most aircraft it can keep
ready to fly, and may hold a further **reserve** of a third as many:

| Squadron | Ready | Reserve | Total |
|---|---|---|---|
| Italian squadriglia | 9 | 3 | 12 |
| German Staffel | 12 | 4 | 16 |
| Commonwealth, to June 1941 | 15 | 5 | 20 |
| Commonwealth, from July 1941 | 18 | 6 | 24 |

Reserve aircraft may be readied and armed, but fly only to make up for
ready aircraft that were not readied: never while the full ready capacity is
flying. Reserves may not scramble; they may take emergency flight
([flight](30-flight-and-maintenance.md#emergency-flight)).

::: spi 35.24

**Pilots** of fighters and fighter-bombers belong to the squadron, not to
an aircraft; the squadron sheet lists them, and each mission pairs pilots
with aircraft (§40).

::: spi 35.22 35.25

**Changing squadron.** Aircraft stay in their squadron, with two
exceptions: when their SGSU has been eliminated (they may join any other
squadron or go into reserve), and when a squadron is below half its ready
capacity (aircraft from other squadrons may join it until it is above
half). An aircraft that must fly to its new squadron does so as a transfer
mission in the mission deployment segment; if the new SGSU is in its own
hex, the change is made in the organisation phase.

::: spi 35.27

**Capture.** When an SGSU is eliminated, aircraft on the ground with it are
captured. Their captor may use them from one Game-Turn later, or destroy
them.

::: spi 35.29

*Colour, not rule:* German SGSU counters carry their unit types (JG
fighters, St.G dive bombers, KG bombers, ZG fighter-bombers, H and F
reconnaissance), unlike the Italian and Commonwealth ones. Players need not
follow them.

## Engine notes

- A squadron needs: nation, class, ready capacity and reserve (by date for
  the Commonwealth), its SGSU (hex, CPA, supplies, attached trucks), its
  aircraft (each with type, readied, refitted, fuelled, armed) and pilots.
- An SGSU is a vehicle for movement, breakdown and supply, with zero
  stacking and no combat values.
