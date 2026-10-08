---
title: Air Game — flight and maintenance
status: provisional
---

# Flight and maintenance

::: spi 37.0

Flight is handled operationally. A player does not move aircraft hex by
hex: he assigns aircraft to fly from a base to a target hex, checks the
distance against their range, records the path (enemy combat air patrols
can intercept along it) and places the aircraft in the target hex. Ground
units never hinder flight, except by flak. An aircraft needs **fuel** to
fly and, after any mission but a transfer, must be **refitted** before it
flies again. Maintenance, which covers readying, refuelling, refitting and
arming, is the second half of this file (§38, to come).

## How aircraft fly

::: spi 37.1 37.11 37.12 37.13

**Range.** Every aircraft type has a range in hexes (its characteristics,
§34). On a mission it may fly at most that far from its base, by any path
the player likes; a **transfer** mission, one way to a new base, may fly up
to **double** range.

**Deployment.** Count the hexes along the chosen path from the base to the
target hex. If they are within range, place one counter for each class of
aircraft on that mission in the target hex, and keep a record of which
squadrons fly which mission and the path each took. Tactical missions are
placed when missions are deployed in each stage's land support air phase;
strategic ones when the Malta raids and the convoy bombing are resolved
([turn outline](00-overview-and-sequence.md#turn-outline)).

The Air Distance Table (37.4) only saves counting: it lists hex distances
between major places. An engine computes distance from the map
(`data/map/`, with `seams.json` across sheet edges) and needs no table.

::: spi 37.4

::: spi 37.14

**Scramble** is the one exception to planned flight: aircraft on the ground
may take off to meet an air threat close by (fighter combat, §40).

::: spi 37.15 37.16 37.17

**Fuel, refit and ammunition.** No aircraft flies unfuelled, and none but an
aircraft on a transfer mission flies without having been refitted. Any
flight, however short, uses the whole fuel load: the aircraft must be
refuelled before it flies again. Aircraft may fly with no ammunition aboard,
at their own risk.

## Restrictions

::: spi 37.2 37.21 37.22

- Never beyond range, except double range on a transfer.
- No flight into or out of a hex under **sandstorm** or **rainstorm**.

::: spi 37.23

**Return to base.** Aircraft land where they took off. Only if that
facility can no longer take them (its capacity has been cut too far) may
they try another. An aircraft that can land nowhere crash-lands as near to a
facility as it can get; roll one die:

| Roll | Result |
|---|---|
| 1–3 | Aircraft and pilot survive. Both are recovered in the next Operations Stage and may fly (once refitted and readied) in the one after. |
| 4–6 | The aircraft is lost. Roll again: on 1–2 the pilot survives unhurt and returns to play one Game-Turn after the crash; otherwise the pilot is lost too. |

::: spi 37.24

**Capacity limits.** No more aircraft fly from a facility than its current
capacity allows ([air facilities](20-air-facilities.md)), and none beyond
what the SGSUs can ready (§35). *Our example:* an Axis airfield bombed down
to capacity three has four SGSUs on it; only three of them may refit and
ready their squadrons, and the fourth squadron sits out. A squadron also
sends no more aircraft on a mission than its readied strength, whatever
reserves it holds.

## Emergency flight

::: spi 37.3 37.31 37.32 37.33 37.34 37.35

When an enemy land combat unit moves next to a friendly air facility with
readied aircraft on the ground, and those aircraft risk being destroyed or
captured, they may try to escape by an **emergency flight**, a transfer
mission flown at once, out of the normal sequence.

1. Only **fuelled** aircraft may try, reserves included.
2. Assign pilots, then roll one die per aircraft: a fighter or
   fighter-bomber gets away on **1–3**; a bomber, reconnaissance aircraft or
   transport on **1–2**. On any other roll it stays on the ground.
3. Aircraft that get away follow the normal flight rules, at up to double
   range.
4. The choice must be made **immediately**: once another enemy unit moves,
   the chance is gone and every aircraft there stays on the ground.

## Engine notes

- Track per aircraft: base, fuelled, refitted, readied, armed; per mission:
  path of hexes (for interception) and target hex.
- Range is measured along the chosen path; any path will do, so the
  shortest path decides whether a target is in range, but the recorded path
  matters for interception.
