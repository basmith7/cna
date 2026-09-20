---
title: Special rules
status: provisional
---

# Special rules

This file collects the Land Game systems that sit outside the main
move–fight loop: vehicle **breakdown** and towing, **desert raiders and
commandos**, **prisoners**, **weather**, the Commonwealth **Mediterranean
Fleet**, and **Rommel**. Repair of what breaks down is in
[Engineering](80-engineering.md#repair); the Terrain Effects Chart values
that breakdown and weather modify are cited from [Movement](40-movement.md#terrain).

::: spi-omit 21.1 21.2 21.3 21.4 21.5 21.6 27.0 27.1 27.3 27.4 27.5 27.6 27.9 28.1 28.2 29.2 30.1 30.2 30.3 — section and subsection headings and design commentary; the rules under them are restated below

## Breakdown

::: spi 21.0 21.11 21.12 21.13 21.14 21.15

Every **truck point** and every **tank, armoured-car/recce and
self-propelled-gun TOE point** — in a unit or as a replacement — can break
down; motorcycles, the notional transport of gun units, and the points of an
HQ counter (§32 addition) cannot. Each vehicle type has a **breakdown
adjustment rating** (BAR) that shifts the column on the Breakdown Table;
the summary is `data/tables/breakdown-adjustments.json`:

| Points | BAR |
|---|---|
| trucks | 2 left |
| armoured cars | 1 left |
| armoured recce | none |
| SP guns, tanks | from 1 left to 2 right, per model on the Tank & Gun Characteristics Charts |

Nothing checks for breakdown moving to, from or between the Tripoli–Tunisia
boxes.

::: errata E-023 — 21.12: the Italian M 13/40's BAR is 1R, as the charts say

::: spi 21.38

The Breakdown Table is data: `data/tables/breakdown.json` gives, for each
band of accumulated breakdown points (0–3, 4–10, then tens up to 71+), the
dice ranges for losing 0, 10, 25, 33, 50 or 75 % of a vehicle type. Under
four points nothing ever breaks; at 4–10 a 65 or 66 already costs a quarter
or a third; from 61 points up no roll escapes, and at 71+ a 64 or better
strands three-quarters of the type. The BAR and weather shifts move the
column before the roll.

### Accumulating breakdown points

::: spi 21.21 21.22 21.23 21.24 21.25 21.26 21.27 21.28 21.29

Each hex's terrain, and some hexsides (wadis), carry a **breakdown point**
value on the Terrain Effects Chart, modified by weather. Every vehicle or
motorised unit collects that value for each hex entered or hexside crossed,
in any kind of movement — retreat and reaction included; combat itself adds
nothing. A whole stack or formation moving together collects the same
points.

*Our example:* a tank battalion using a road for two hexes (½ each), then
entering rough (8), crossing a ridge (2) and finishing in clear (4) has 15
points.

A check is made whenever a vehicle unit **stops** — at the end of its
movement, or between legs of continual movement — once it holds more than
**3** points. Points are not discharged by a check: they keep accumulating
until the end of the stage, through both players' halves. After a first
check, another is needed only when the running total has climbed into a
**higher column** of the table at the moment the unit next stops: a
battalion at 15 that moves one more hex to 17 is still in the same column
and need not roll; retreating for 10 more to 27 puts it in a new column and
it rolls again. Checks are per type — trucks; tanks and SP guns; armoured
recce and cars — and per BAR within a type, and per unit where units in a
stack hold different totals (a recce unit at 38 and one at 23 roll
separately), each with its own dice.

### Resolving a check

::: spi 21.31 21.32 21.33 21.34 21.35 21.36 21.37

1. Find the column for the points accumulated (fractions round up: 20.5 →
   21).
2. Shift it by the BAR and by weather, cumulatively — 2 left for trucks and
   1 right for heat is a net 1 left. Above 71 points the **71+** column is
   used and counts as one column; a column shifted below **4–10** means no
   breakdown.
3. Roll two dice, read sequentially, in that column; the result gives the
   **percentage of TOE points** (truck points count as TOE points) of that
   group that break down, fractions rounded **up** — except that a group of a
   single point ignores a 10 % result. Spread the losses as evenly as possible
   across vehicle types and across units.

*Our example:* 30 truck points and 20 points of a cruiser tank rated 1R
stop at 35 points in hot weather. Trucks: 31–40 shifted 2 left and 1 right
→ 21–30; a roll giving 10 % breaks 3 trucks. Cruisers: 1R plus 1R → 51–60;
a roll giving 33 % breaks 7 points (6.7 rounded up).

Weather: normal, nothing; **hot**, one column right per check;
**rainstorm**, road breakdown values become track values; **sandstorm**, one
column right if at least half the CP spent in that movement phase (or
retreat, reaction, etc.) was on a map under sandstorm.

### Broken-down vehicles

::: spi 21.41 21.42 21.43 21.44 21.45

Breakdown happens in the hex where the unit stopped — except that a unit
whose move began within two hexes of an enemy combat unit bigger than a
battalion — with no friendly unit, friendly ZOC or impassable terrain in
between — must leave at least **half** of what breaks down in its starting
hex. Place a numbered **broken-down vehicle marker** and record what it
stands for. Broken-down vehicles have no CPA and take no part in combat; they
can be captured or towed. A broken truck keeps its cargo unless empty
trucks can take it over — and a motorised battalion that loses one truck it
cannot replace is no longer motorised. Supplies may be shifted to working
trucks in the hex at the moment of breakdown for **2 CP**; infantry may
dismount (1 CP) and walk, their CP spent while mounted counting against the
foot allowance of 10 (or 8) but capped at that figure. Loading onto trucks
that were not attached to the unit costs the usual loading CP.

### Capturing broken-down vehicles

::: spi 21.51 21.52 21.53 21.54 21.55

Any friendly **combat unit of at least battalion size** moving next to a
broken-down vehicle marker captures it at once — unless the marker is
stacked with enemy combat units, HQs or engineers, or sits in an
enemy-controlled hex, and only if the two hexes join through passable
terrain (tanks below an escarpment cannot take vehicles above it). Captured
vehicles may be placed up to **three hexes** away immediately, for no CP,
by a path avoiding enemy units, enemy ZOC and impassable terrain; the captor
moves on. This differs from capturing destroyed tanks
([Combat](60-combat.md#capturing-destroyed-tanks)) and abandoned vehicles.

### Towing

::: spi 21.61 21.62 21.63 21.64 21.65 21.66 21.67

Anything awaiting facility repair — broken-down or destroyed, retrieved or
captured — may be towed toward the **nearest** temporary or major repair
facility. There are no tow vehicles (the tank delivery squadrons apart,
[Engineering](80-engineering.md#tank-delivery)): each marker moves itself
as a medium truck at **10 CP** per repair phase, only in the repair phase,
never reacting or retreating, never breaking down, and for no fuel, stores
or water. Part of a hex's vehicles may be towed, leaving a second marker
behind (§32 clarification). No towing out of an enemy-controlled hex except
at the instant of capture; friendly units cancel the ZOC. A vehicle under
field repair this phase, or that failed field repair this phase, may not be
towed. Keep the number of markers on the map down (§32 note).

## Desert raiders

::: spi 27.11 27.12 27.13 27.14 27.15 27.16 27.2

The Commonwealth has two **Long Range Desert Group** counters, the Axis one
**Sonderkommando Almasy** (DSA). A raider unit is made in the organisation
phase, at no CP, by removing one recce or armoured-car TOE point from a unit
that has reached maximum morale through training (DSA: German units only)
and placing the raider counter instead; the point never reverts. Raiders
have CPA **50**, no combat ratings, no stacking points, and cannot fight
normally. An eliminated raider is re-formed the same way four turns later
(eliminated in turn 55, stage 2 → re-formed in the organisation phase of
turn 59, stage 3).

::: errata E-026 — 27.16: re-formed raiders are made as in 27.13; the example's dates are turns 55 and 59

### Hidden movement

::: spi 27.31 27.32 27.33 27.34 27.35 27.36 27.37 27.38

A raider is on the map only when formed, when it raids, and when spotted;
otherwise its owner records its position and moves privately, under the
ordinary movement rules for a recce vehicle. Raiders have no ZOC, need not
stop in enemy ZOC (at the risk of being spotted), and enter an enemy-held
hex only to raid. Once per **game-turn** a raider has to call at a
friendly dump, oasis or well: at a dump it takes and spends 1
ammunition and 2 fuel (it waits if none is there, and cannot travel without
the fuel); water comes from any dump, oasis or well, and a raider that has
not watered by the end of a turn is eliminated. Taking supply in stage 1 of
one turn and stage 3 of the next stretches to five stages. Raiders may react
(including after any spotting attempt), never exceed CPA 50 — forced over it
they are eliminated — use no fuel beyond the weekly draw, and never break
down.

::: errata E-027 — 27.36: reaction is allowed after any spotting attempt

### Spotting

::: spi 27.41 27.42 27.43 27.44

Whenever a raider enters an enemy-controlled hex, or an enemy combat unit
enters a raider's hex, the raider's owner announces it and rolls one die: a
**6** spots and eliminates the raider. The moving enemy must spend **1 CP**
to try, may decline, and may try only once per stage per phasing unit.

### Raids

::: spi 27.51 27.52 27.53 27.54 27.55 27.56 27.57 27.58 27.59

A raid puts the counter on the map, costs **5 CP**, and is made during
movement; the raider may move on afterwards. Targets behind the lines:

- **Water pipeline** (including where it runs along a railway, which is
  unharmed — §32 clarification): in a pipeline hex with no enemy combat
  unit, roll one die; 1–4 blows it. Once per stage.
- **Airfield** (not landing strips, not in a major city, no enemy combat
  units present — SGSUs do not count): 1–2 drops its capacity one level.
  Once per airfield per turn; may be combined with a plane raid.
- **Aircraft on the ground** at an airfield or strip (not flying-boat
  facilities, not in a major city, no combat units): 1–2 destroys at least
  10 % of the planes there, raider's choice; a 6 eliminates the raider.
- **Supply dump** (not in a major city; guarded dumps allowed): unguarded,
  1–2 destroys 10 % of the supplies. Guarded, first roll two dice: a total
  above the guards' raw defensive assault strength lets the raid proceed as
  unguarded but with a 6 eliminating the raider; a total not above it
  eliminates the raider outright. A dummy dump is revealed after the fight
  and nothing burns, though guard and elimination results stand.
- **Truck convoy**, by entering its hex or by **interception** — if a
  convoy passes within 4 CP of a raider in the enemy truck convoy phase the
  raider may stop it (the convoy spends 5 CP, not beyond its CPA; the raider
  5, then up to 5 more to leave). Roll one die: 1–2 destroys one truck point
  (defender picks the truck type, raider the cargo). Trucks carrying
  replacement points add 1 to the roll and a 6 eliminates the raider; if
  every truck carries replacements the raider dies and no truck is lost.

### Raid on Rommel

::: spi 27.61 27.62 27.63 27.64 27.65

An LRDG entering Rommel's hex may try to kill or capture him: **10 CP**
(an LRDG with no CP left is eliminated too), two dice on the Raid on Rommel
Table. At most four attempts in a campaign game, one in a shorter scenario.
Kinship with the right novelists earns +1.

::: spi 27.93

The SAS Raid Table is data: `data/tables/sas-raid.json` — one die, and from
nothing on a 1 to half the aircraft on the ground on a 6 are destroyed.

::: spi-omit 27.91 27.92 — the Desert Raider Raids Table (jp2 102, a per-target list) and the Raid on Rommel Table are still to be captured; to `data/tables/raids.json`

## Commandos

### Layforce

::: spi 27.7 27.71 27.72 27.73 27.74 27.75 27.76 27.77

"A" Battalion, Special Service Brigade is an ordinary infantry battalion
with one power: after a full turn in Alexandria it may be landed, in a stage
it starts there, in any coastal hex, carried by a Commonwealth Fleet ship —
**5 CP** per 50 hexes the ship travels, plus the terrain cost. It needs no
supply for its first three stages ashore, landing stage included; no trucks
may load with it on a raid. While the ship stays in the landing hex Layforce
may retreat into it (satisfying any mandated retreat) or re-embark at will,
whereupon the ship returns to Alexandria at once; if the ship is sunk with
Layforce aboard, Layforce dies with it (§32 addition to 30.36). Losses are
replaced at **three** infantry replacement points per TOE point, trained
twelve stages with the unit in Alexandria.

### Special Air Service

::: spi 27.8 27.81 27.82 27.83 27.84 27.85 27.86 27.87 27.88 27.89

The SAS Brigade is a battalion-sized infantry unit, CPA **15**, motorisable
except when carried by sea or air. It may fight as infantry, or raid Axis
air facilities in any movement/combat segment: it reaches the target by
land (normal rules), by any one Commonwealth ship to a coastal hex (**5
CP** per 50 movement points or part), or by air drop (**5 CP**, SPI 42.4).
Sea- or air-delivered, it is in supply for three stages including the
delivery stage. Guarded facilities may be attacked, but the plane roll needs
the hex clear of Axis combat units — fight or drive them off first. The
raid costs **3 CP** on top of anything else spent, once per month with at
least six stages between raids; roll one die on the SAS Raid Table for the
percentage of every plane type present, regardless of SAS strength. Afterwards
it may move on within continual movement and cohesion; stacked with an LRDG
it becomes hidden like a raider at CPA **30** and stays so until the LRDG
escorts it back onto the map. Replacement is three trained infantry points
per TOE point over twelve stages; an SAS Brigade wholly eliminated is gone.

::: errata E-028 — 27.88: the hidden-movement reference is 27.32

## Prisoners

::: spi 28.0 28.11 28.12 28.13 28.14 28.15 28.16 28.17 28.18

Every surrendering **infantry** TOE point becomes one **prisoner point** —
guns and tanks are captured equipment ([below](#captured-equipment)), and
prisoners are never massacred. At the instant of surrender the captor may
shift them up to **three hexes**, avoiding enemy-controlled or -occupied
hexes and impassable terrain. Prisoner points have CPA **8** for movement
only, move in the captor's convoy phase, never exceed it, cannot fight, and
stand still when their guards retreat. At most **40** points per hex; more
than five standing still may be marked as a detention camp. Every five
points cost the captor **1 store per stage**, drawn from the nearest dump
before any other store is spent. Prisoners leave the game for good on
entering the captor's **departure point** — the Sirte box for the Axis,
Alexandria or Cairo for the Commonwealth. Each camp needs one **guard
point**; on the move, one guard per **five** prisoners. Trucks may carry
prisoners if you can spare them.

::: errata E-029 — 28.17: one guard per five prisoners, not one

::: spi 28.21 28.22 28.23 28.24 28.25 28.26

**Guards** are made by taking one TOE point from any infantry-type unit and
replacing it with a guard counter: a one-point infantry unit rated 0/1, CPA
10 (though it usually walks at its prisoners' 8), able to fight and react —
but prisoners do not follow a guard that reacts or retreats before assault.
Unused guards rejoin their unit. Prisoners left without guards, or beyond
the guard ratio, **escape**: within 8 CP of a friendly unit (enemy ZOC and
units not crossing the path) they join it, leave play, and return a month
later as replacement points for retraining, never to assign or attach;
farther away they walk toward friends in the truck convoy phase needing only
water, losing 10 % (rounded up) per waterless stage, stopping at a friendly
unit or major city or when recaptured by an enemy entering their hex.
Escapees have no combat value and cannot be attacked. (Do not march
prisoners into the deep desert and abandon them; the rule is for flavour.)

### Captured equipment {#captured-equipment}

::: spi 28.3

Captured guns and tanks, once repaired, may be used against their former
owners.

## Weather

::: spi 29.0 29.1

Weather is rolled once per stage by the initiative holder: two dice read
sequentially on the Weather Table, in the row for the **season**
(`data/tables/seasons.json`):

| Season | From | To (inclusive) |
|---|---|---|
| spring | March, week 3 | June, week 2 |
| summer | June, week 3 | September, week 2 |
| autumn | September, week 3 | December, week 2 |
| winter | December, week 3 | March, week 2 |

Four results: **normal**, **hot**, **sandstorm**, **rainstorm**. A storm
result sends the player to the Foul Weather Location Table (one die) for
the map sections affected; the rest have normal weather. Weather never
touches Malta, Italy, Sicily, Crete or the Tripoli–Tunisia boxes; map E's
weather does apply to the Allied off-map airfields.

::: errata E-024 — 29.1: the printed Roman numerals are weeks of the month

::: spi 29.6

The Weather Table is data: `data/tables/weather.json` gives, per season,
the dice range for each of the four weathers. Sandstorms are a summer
affliction (a 56 or better, and rain is impossible); rain belongs to
winter (53 or better, with no hot weather or sandstorm at all); spring
and autumn can produce any of the four. The printed game-turn bands are
attached to the wrong seasons (E-025); the corrected bands put the
campaign's opening turns in autumn.

::: errata E-025 — 29.61: the Weather Table's season rows are backwards; the turn bands are swapped with the opposite season's, per the 29.1 calendar

::: spi 29.7

The Foul Weather Location Table is data too: `data/tables/foul-weather-location.json`
maps the one-die roll to the map sheets a storm covers — two sheets on
most faces, three (B, C, D) on a 6, and never sheet A except with B on a 1.
A sandstorm rolled onto sheet E is normal weather on Delta hexes, and no
sandstorm reaches north of the coastal hexes.

::: spi 29.3 29.31 29.32 29.33 29.34 29.35

**Normal** weather has no effect. **Hot** weather covers every map at once
and: charges construction sites 10 water
([Engineering](80-engineering.md#construction)); shifts breakdown one column
right; evaporates **5 %** of all fuel and water stocks (dumps and trucks,
not wells, oases, or what is in tanks and radiators) during the weather
phase; and doubles every unit's water need.

::: spi 29.4 29.41 29.42 29.43 29.44 29.45 29.46 29.47

**Sandstorms** strike only the map sections rolled, never delta hexes, and
stop at the coast. Where they blow: no construction, no aircraft in or out,
**double** movement costs, one column right on breakdown for a unit that
spent half or more of its movement CP in storm hexes, and grounded aircraft
may be damaged (SPI 38.5).

::: spi 29.5 29.51 29.52 29.53 29.54 29.55 29.56 29.57 29.58

**Rainstorms** strike the sections rolled and extend out to sea. Where they
fall: no aircraft in or out; no construction; depleted wells refill; wadi
hexsides cannot be crossed except by road, nor drawn from for water; roads
cost and break down as tracks (tracks unchanged); river hexsides without
road or railway are impassable; and no vehicle or motorised unit enters a
delta hex except on road or rail — those already in one stay put for the
stage unless on road or rail.

## The Mediterranean Fleet

::: spi 30.0 30.11 30.12 30.13 30.14 30.15 30.16 30.17 30.18

Commonwealth **naval counters** are abstract battleships, cruisers and
destroyers with real names but no fixed identity; there is no naval combat.
Each has a **gun rating** — its actual barrage points, and also its hit
points — and an **AA rating** in actual AA points, reduced in proportion as
gun points are lost; a battleship might start at 6 guns and 12 AA. Ships have
no stacking value, stack freely in any coastal or sea hex, and never affect
land, air or other naval movement. They do not move: each stage a ship is
placed anywhere within **100 sea hexes** of Alexandria (no farther west than
hex row xx29 on map B). They need no supply, but must spend **two stages in
port for each stage at sea** and never more than three consecutive stages
out. Ships may shuttle to Valletta (Malta, five at a time), a recovery port
from which they return only to Alexandria; the one-stage passage is not
"at sea". The Italians' one ship, the *San Giorgio*, lies half-sunk blocking
Tobruk harbour: it acts as an immobile artillery unit until removed or sunk
by enemy engineers, firing into adjacent hexes and at Commonwealth ships
across sea hexsides.

::: variant V-001 — the San Giorgio as a live gun battery: torpedo-immune, own AA, may sortie, no port-efficiency penalty (NJHarman)

### Off-shore bombardment

::: spi 30.21 30.22 30.23 30.24 30.25

A ship may bombard the coastal hex it sits in; battleships and heavy
cruisers (4-point ships) may also bombard any adjacent hex, at **half**
strength. Gun ratings are used as actual artillery points needing no
ammunition, under the [barrage rules](60-combat.md#barrage) (facilities
included). Place the ships in the fleet assignment segment; each ship fires
**once** per stage, in whichever barrage step its owner chooses, and must
then spend the next **two stages in Alexandria** (firing AA does not trigger
this).

### Damage and repair

::: spi 30.31 30.32 30.33 30.34 30.35 30.36 30.37 30.38 30.39

Ships are damaged by air bombardment, by coastal guns, or by the chariot
raid. Bombing a ship is a mission flown by bombers, fighter-bombers or
torpedo planes assigned to it in the ship's hex (SPI 41.3, 41.7); the Air
Bombardment Table gives damage in gun points, and the ship fires thereafter
at its reduced ratings (a 4 taking 2 damage has 2 guns and half its AA).
Artillery with vulnerability **6 or more**, and emplaced guns, may fire at
ships in their own hex instead of at land units that stage: **half** the raw
barrage points (emplaced guns, CPA 0, are not halved) enter the Air
Bombardment Table as bomb points. The *San Giorgio* fires at ships the same
way. A ship below **50 %** of its printed guns may not leave port until
repaired above it; at zero it is sunk. Repair is one gun point per **six
consecutive stages** in Alexandria, no engineers or supplies, restarting if
the ship moves. Ships always fire AA, wherever they are and whatever they
are doing. A ship sunk while carrying commandos takes them down with it
(§32 addition).

### Chariot raid

::: spi 30.4 30.41 30.42 30.43 30.44 30.45

From **July 1941**, once per campaign game (never in a shorter scenario),
the Axis player may send the 10th Light Flotilla's human torpedoes against
Alexandria: note the plan secretly, execute it in the **seventh** stage
after, during the land support air phase's mission-completion segment
(once ships have been assigned), roll one die on the Chariot Table. No
supplies are involved.

::: spi-omit 30.46 — the Chariot Table is on the chart sheet; to `data/tables/chariot.json` when captured

### Naval transport of troops

::: spi 30.5 30.51 30.52 30.53 30.54 30.55 30.57 30.58

Only the Commonwealth moves troops by sea, port to port, **once per stage
per port** in either direction, in the truck convoy phase. The load is
limited by the smaller **port personnel capacity** (stacking points per
stage) of the two ports. The units must start the stage in the port of
departure and spend no CP before the convoy phase — units that were
barraged or bombed may still go — and land at the destination for their
full CPA. Ports must both be friendly-controlled (last occupied) and not
knocked out by bombing; a port mined or blocked below **two-thirds**
capacity (rounded up) can neither send nor receive troops. Landing troops
cuts the port's supply tonnage for the stage: **10 % per stacking point**
landed (points shipped out cost nothing); for ports whose incoming capacity
is above one SP, bringing in at least half the tonnage maximum cuts the SP
level by at least a third; one-SP ports lose nothing.

::: errata E-030 — 30.5: the supply-by-sea reference is 56.0; 30.55 also admits barraged/bombed units; 30.57 is replaced by the 10 %-per-SP rule; 30.58's reference is 55.2

::: spi-omit 30.59 — there is no 30.59 chart (errata): the Port Capacity Chart is SPI 55.3 and the Commonwealth Fleet Reinforcement Schedule is on the chart sheet; both to `data/` when captured

## Rommel

::: spi 31.0

The Axis has a **Rommel** counter: a vehicle (a medium truck for movement
and breakdown), CPA **60**, no combat ratings. He may react and retreat
before assault when any unit but an LRDG approaches, and may retreat
through enemy ZOC freely. A stack fighting with Rommel in its hex gets
**+1 morale**; a unit he stays with for a whole stage, from its start, gets
**+5 CPA**. At the start of each turn he is present the Axis rolls two dice:
a **12** sends him to Germany for the turn and drops Axis initiative to 3;
he is back the next turn unless another 12 is rolled. The LRDG may try to
remove him ([raid on Rommel](#raid-on-rommel)).

---

*Drawn on: SPI §21, §27, §28, §29, §30, §31, the §32 addenda to 21.11, 21.63, 21.67, 27.32 and 30.36, and the September 1979 errata (E-023–E-030).*
