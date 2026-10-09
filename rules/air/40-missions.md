---
title: Air Game — missions
status: provisional
---

# Missions

Every aircraft that flies has a **mission**: a word or two on its squadron
sheet saying why it is in the air and what it is to do. This file gives the
rules every mission shares (§39) and the missions that do not fight: transfer,
reconnaissance, transport, airdrop and convoy reconnaissance (§42). Fighter
missions are in §40, bombing in §41.

## Missions in general

::: spi 39.0

No aircraft flies without a mission, and as a rule an aircraft flies one
mission at a time. Missions depend on the aircraft's class and the target,
and a player often has to send them against a hex without knowing what is in
it, learning only when the aircraft arrive. A mission may be **aborted**,
called off before it is complete.

Every mission except a transfer runs in this order:

1. All aircraft are placed over their target hex.
2. Interception and scrambles are resolved.
3. Fighters fight each other, air to air.
4. Fighters on CAP that survive may, in some cases, attack enemy
   non-fighters.
5. Aircraft still over the hex take flak if enemy AA units are there
   ([anti-aircraft fire](70-air-combat-and-flak.md#flak)).
6. Each mission is carried out, in any order its owner likes; the other
   player applies the damage.
7. Survivors fly back to base.

::: spi-omit 39.1 39.3 39.4 42.0 42.1 42.2 42.3 42.5 — section and subsection headings; the rules under them are restated below

::: spi 39.11 39.12

Only an aircraft with an assigned mission may fly, unless it is making an
emergency flight ([flight](30-flight-and-maintenance.md#emergency-flight)),
and none may take off while an enemy land combat unit is adjacent. The
mission is written next to the aircraft on its squadron sheet, in any
shorthand, for the Operations Stage or strategic air phase.

::: spi 39.13 39.14

Missions are **strategic** or **land support**. Strategic missions are the
Commonwealth's against Axis naval convoys and the Axis's against Malta; they
are flown once a Game-Turn, in the strategic air steps of the turn
([turn outline](00-overview-and-sequence.md#turn-outline)). Land support
missions touch the movement and use of land and naval units and are flown in
the land support air phase of each Operations Stage, so up to three times a
Game-Turn.

::: spi 39.15 39.16 39.17

Any number of aircraft may fly a mission to one hex, but only aircraft with
the **capability** for that mission
([ratings](10-aircraft-and-sgsus.md#ratings)). Aircraft of several squadrons
may share a mission or a target, and one squadron's aircraft may fly
different missions, but a squadron's aircraft are never split between
strategic and land support missions. Any number of different missions may be
flown over one hex; keep each mission's aircraft apart.

::: spi 39.18 39.19

The mission families are fighter, bomber, transport, reconnaissance and
transfer; **transfer** is the only one any aircraft may fly. An aircraft
flies at most one mission in any one Operations Stage or strategic phase (combined
missions, below, excepted), and flying in an Operations Stage rules an
aircraft out of that Game-Turn's strategic phase, and the reverse.

### Combined missions

::: spi 39.2

Some fighters could carry a few bombs and drop them while strafing, and dive
bombers could strafe though never fight as fighters. An aircraft whose
mission capability includes **D** may therefore **strafe and bomb the same
target** as one combined mission.

### Aborting a mission

::: spi 39.31 39.32 39.33 39.34

A mission may be aborted only before anything has been done on it: once any
bombing, strafing or air-to-air combat has taken place, it can no longer be
called off. The player announces the abort and sends the aircraft home, if
they qualify (below). An aborted mission still burns its fuel, and bombers
drop their load unused. A player may abort part of a mission and carry on
with the rest.

::: spi 39.35

A **fighter** (anything with a pilot, fighter-bombers included) may abort if
its maneuver rating is no more than **10 below** the best maneuver rating
among the enemy fighters on CAP over the hex: subtract the best enemy rating
from its own; −10 or higher, it may abort. With no enemy CAP it may always
abort, except as 40.26 says.

::: spi 39.36 39.37

A **non-fighter** may abort if it has a sufficient **screen**: friendly
fighters on CAP over the hex numbering at least **a quarter** of the enemy
fighters on CAP there (aircraft counted, not rated). Twenty escorts let
bombers abort against up to 80 enemy fighters, not against 81. Without a
screen it may abort only if its maneuver rating beats the best enemy
fighter's. Fighters screening may not themselves abort, and fighters never
screen other fighters.

::: spi 39.38

Aircraft may also be forced to abort, by flak among other things (46.3,
45.14).

### Night missions

::: spi 39.41 39.42 39.43

Night missions are a phase of their own inside the land support air phase:
night scrambles, air-to-air combat, flak and land support bombing at night
are all resolved apart from the day's missions. Some missions cannot be
flown at night at all, and none by an aircraft without night capability. Apart from
offensive CAP and scramble, an aircraft flies at night only if it was given
a night mission; otherwise it flies by day even if it could fly by night.

::: spi 39.44

At night, aircraft are hard to find: they cannot be intercepted, they may
not fight air-to-air, and flak against them is weaker. Non-fighters on a
night mission get no formation-flying bonus.

### Mission summary

::: spi 39.5

The Aircraft Mission Summary is data:
[`data/tables/air-missions.json`](https://github.com/basmith7/cna/blob/main/data/tables/air-missions.json),
one row per mission with its kind (strategic or land support), side, role
(fighter, bombing, non-combat), whether it may be flown at night, and the
cases that govern it. In brief:

| Kind | Side | Missions |
|---|---|---|
| Strategic | Commonwealth | convoy reconnaissance; convoy bombing; defensive CAP and flak suppression over a convoy; CAP over Malta |
| Strategic | Axis | bombing Malta's air facilities; CAP over Malta; flak suppression over Malta; offensive CAP over a convoy |
| Land support | both | **fighter**: scramble\*, CAP\* (offensive or defensive), strafing (first-line trucks, flak, grounded aircraft, infantry, ports, tanks, trucks in convoy, the water pipeline); **bombing**: air facilities, fortifications and major cities\*, flak, mining harbours, personnel, ports\*, rail and road\*, Commonwealth ships, supply dumps; **non-combat**: airdrop, land reconnaissance, transfer, transport |

\* may be flown at night. Strafing ports is resolved on the Air Bombardment
Table; only Commonwealth-owned Hurricane IIDs strafe tanks.

## Transfer

::: spi 42.11 42.12 42.13

A **transfer** moves an aircraft from one air facility to another, one way:
it does not return to where it started, and it may fly **twice** its range.
Fly transfers before other missions so none is forgotten; they meet trouble
only from enemy CAP (40.27).

::: spi 42.14 42.15

A transfer needs no refit beforehand, but the aircraft must be refitted
after it before it flies again the next stage or turn. It burns fuel; the
owner chooses whether it goes armed. Write "transfer to" and the destination
hex on the squadron sheet; the aircraft is moved there. Transfers fly only in
the land support air phase of an Operations Stage.

## Reconnaissance of land units

::: spi 42.21 42.22 42.25

Aircraft with **R** capability may scout a hex holding an enemy unit, to
learn in general terms what is there. Any hex may be scouted except a major
city, and never a hex being bombed in the same phase.

::: spi 42.23 42.27

After air-to-air combat and flak, count the aircraft still on
reconnaissance over the hex and roll one die on the Air Reconnaissance of
Land Units Table, adding **one for every four** of them (fractions dropped).
The result is how many battalion-equivalents the owner must reveal, or all
units in the hex on 13 or more. The table is data:
[`data/tables/air-reconnaissance.json`](https://github.com/basmith7/cna/blob/main/data/tables/air-reconnaissance.json).

::: spi 42.24

For each battalion-sized unit revealed, the owner names its type and its TOE
strength. Tanks are revealed first (a dummy tank unit counts as TOE 3), then
infantry, then artillery. The strength he gives may be off by up to **2**
either way: a unit of TOE 4 may be called anything from 2 to 6.

::: spi 42.26

Land reconnaissance is flown in the land support air phase and needs a
refit afterwards. Reconnaissance of convoys is strategic (below).

## Transport

::: spi 42.31 42.32 42.33

Aircraft with transport capability carry personnel or supplies up to the
capacity on their characteristics row. The cargo must begin the Operations
Stage in the transport's hex. The transport then either flies to the target
hex, unloads and returns, or flies there and stays, which lets it
use its transfer range. Since transports land, the target must be a friendly
air facility; dropping without landing is an airdrop (below).

::: spi 42.34

Units flown in have spent their CPA for that Operations Stage and may not
move voluntarily. They may be landed in an enemy ZOC but may not attack:
they defend only, and they may not go past their basic CPA by reacting or
retreating before assault.

::: spi 42.35 42.36

Supplies flown in are of no use straight off the aircraft: they must be
assigned to a dump or to units in the organisation phase first. Transport
missions fly only in Operations Stages, and the aircraft need a refit
afterwards.

::: spi 42.37

Only infantry without trucks, motorcycle infantry and recce, and airborne
units may be flown. (SPI adds, deadpan, that dead camels may be flown and
live ones may not.)

## Airdrops

::: spi 42.4 42.41

No large airborne operation was mounted in the desert, though both sides had
airborne troops (the Ramcke Brigade, the Folgore Division); these rules are
hypothetical. Units the OA sheets mark as airborne may be dropped by
transports in a land support air phase.

::: spi 42.42 42.43 42.44

An airdrop is a transport mission of the first kind (fly out, unload, fly
home) except that the units are dropped, so no air facility is needed at the
target; the transports must still take off from a friendly one. The drop
hex must be clear, gravel or desert terrain; not a major city, not occupied
by the enemy, not in an enemy ZOC; it may hold friendly units, within
stacking. It must lie within **two hexes** of a recognisable feature: a
major city, a road (unfinished or destroyed roads count) or railway hex, a
village, an air facility or an oasis.

::: spi 42.45 42.47 42.48

No drops in a sandstorm or rainstorm. There is no drift and no loss: units
land in the target hex. Dropped units move and fight normally but may not
voluntarily go past their CPA in the stage they land. Any number of TOE
strength points may be dropped, as transports allow, but no unit may be
dropped more than once a month (twelve Operations Stages).

::: spi 42.46

Dropped units need supplies like any others. Of supplies, only ammunition
and stores may be dropped, under the same rules; but supplies may be dropped
to a friendly-occupied hex even in an enemy ZOC, and then the recognisable
feature rule does not apply. Dropped supplies may be used at once.

## Convoy reconnaissance

::: spi 42.51 42.52

The Commonwealth may scout the convoy lanes to learn whether an Axis convoy
is using a lane and how big it is. Each scouting aircraft must have **R**
capability and is assigned to one lane within its range. The distances are
on the Axis Naval Convoy Air Distance Chart (56.1); from North Africa, an
aircraft's range must cover the distance from its facility to one of the
chart's key cities plus that city's distance to the lane.

::: spi 42.53 42.54

Convoy reconnaissance is resolved on the convoy reconnaissance table,
[`data/tables/convoy-reconnaissance.json`](https://github.com/basmith7/cna/blob/main/data/tables/convoy-reconnaissance.json):
two dice in order, at or under a number set by how many aircraft scout the
lane (12 for one aircraft, rising to 66 for eight or more). If it succeeds,
the Axis player must say whether the lane holds a convoy this turn and, if
it does, whether it is small (up to 5,000 tons), medium (3,000 to 10,000)
or large (7,000 or more); the bands overlap as printed, so he may choose.
Aircraft on convoy
reconnaissance cannot be attacked, in the air or by flak.

::: spi 42.55 42.56

Convoy reconnaissance is a strategic mission. It is assigned in the
strategic mission assignment step of strategic air planning, any number of
aircraft per lane, and resolved in the convoy reconnaissance segment of the
convoy stage.

## Engine notes

- A mission is a row id of `air-missions.json`; an aircraft may fly it only
  if its characteristics row carries the matching capability letter.
