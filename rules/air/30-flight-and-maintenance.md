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
arming, is the [second half](#maintenance) of this file.

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

## Maintenance {#maintenance}

::: spi 38.0 38.1

An aircraft is **ready** when it is refuelled and refitted; arming is
optional, but an unarmed aircraft cannot fight back. All three are done by
SGSUs at an air facility, within the facility's current capacity
([air facilities](20-air-facilities.md)). Any SGSU may refuel or rearm any
squadron's aircraft at no penalty; refitting goes best when a squadron's
own SGSU does it.

Maintenance happens at two points in the turn: in the **tactical
maintenance segment** of each stage's land support air phase, for aircraft
on tactical missions, and in the **aircraft maintenance phase** of the
strategic air recovery stage, for aircraft on strategic missions
([turn outline](00-overview-and-sequence.md#turn-outline)).

### Refuelling

::: spi 38.2 38.21 38.22 38.23 38.24 38.25

Each flight takes the aircraft type's **fuel** rating in fuel points
(`fuel` in `data/tables/aircraft-characteristics.json`), whatever the
distance. The fuel must be in the facility's hex, normally in the
facility's own dump; deduct it and mark the aircraft refuelled on the
squadron record.

An SGSU refuels aircraft of any squadron, but no more in one maintenance
step than its own full complement (ready plus reserve): twelve, for
example, if that is its squadron size. The facility only limits how many
SGSUs may work there.

Refuelling is never compulsory, and a refuelled aircraft need not fly.
Reserves may be refuelled too. Fuel in an aircraft never goes off: it may
sit fuelled for the rest of the game.

::: spi 38.26

**Drop tanks.** Some types can carry extra fuel tanks for longer range at
the cost of manoeuvrability (the `*` range entries on the chart). If such
an aircraft is drawn into air-to-air combat it may jettison them: its
maneuver rating returns to normal, but so does its range, which may leave
it short of home.

### Refitting

::: spi 38.3 38.31 38.32 38.33

Refitting makes good the wear of the last mission. Every aircraft starts a
scenario refitted unless the set-up says otherwise; after any mission but a
transfer it must be refitted before it flies again (a transfer needs only
fuel). An SGSU refits up to its own full complement, from its own squadron
or another; refitting aircraft of another squadron is harder (below).

::: spi 38.34 38.35 38.36

**The refit roll.** Roll one die per squadron refitting, and separately for
any aircraft of other squadrons it works on, and read the percentage of the
aircraft refitted on the Aircraft Refit Table (fractions round up). Add to
the roll:

| Condition | Add |
|---|---|
| The aircraft are not the SGSU's own squadron's | +1 |
| The aircraft are Italian | +2 |
| The aircraft are German | +1 |

The additions are cumulative, whichever player owns the aircraft. (The
table's own key words the national additions by the SGSU's nation instead.)

::: ruling R-112 — whether the refit additions follow the aircraft's nation or the SGSU's

Every
squadron that tries to refit, successful or not, spends **one stores
point**, which must be at hand. Refitting is never compulsory.

*Our example.* A Commonwealth SGSU works on six Hurricanes of its own
squadron and three captured Italian fighters from elsewhere. That is two
rolls: one for the six with no addition, one for the three at +3 (another
squadron's, and Italian). Two stores points are spent.

::: spi 38.37

**Sandstorms.** In a hex under sandstorm, a fifth (rounded up) of the
refitted aircraft on the ground lose their refit and must be refitted
again before flying, spread as evenly as possible over the types present.

::: spi 38.38 38.39

The Aircraft Refit Table is data:
[`data/tables/aircraft-refit.json`](https://github.com/basmith7/cna/blob/main/data/tables/aircraft-refit.json).
By squadron, a 1 refits every aircraft, a 2 four-fifths, and the share
falls to a third on a modified 8 or 9. As an optional, slower method, players may roll for each aircraft on two
dice instead: Commonwealth aircraft are refitted on 2–8, German on 2–7,
Italian on 2–6, with +2 (instead of +1) for another squadron's aircraft.

### Arming

::: spi 38.4 38.41 38.42 38.43 38.44 38.45 38.46 38.47

Arming gives aircraft their guns and bombs. It is not needed to fly, but a
bombing mission needs bombs, and air combat needs ammunition. SGSUs rearm
under the same limits as refuelling, from the facility's dump.

- **Guns:** one ammunition point per squadron lets its aircraft use their
  TacAir rating. Without it every aircraft of the squadron has TacAir 0 and
  cannot fire at enemy aircraft.
- **Bombs:** one ammunition point loads a bomber to its full bomb capacity,
  however large; one point likewise loads mines or torpedoes.
- A bomb load is spent on the mission whether dropped or not, emergency
  flights included: nobody lands with bombs aboard.
- Armament may be recorded on the squadron record.

## Engine notes

- Track per aircraft: base, fuelled, refitted, readied, armed; per mission:
  path of hexes (for interception) and target hex.
- Range is measured along the chosen path; any path will do, so the
  shortest path decides whether a target is in range, but the recorded path
  matters for interception.
