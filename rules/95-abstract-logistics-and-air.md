---
title: Abstract logistics and air
status: provisional
---

# Abstract logistics and air

This file defines the **Land Game played alone**: SPI §32 replaces the
Logistics and Air Games with supply units, motorisation points, simplified
convoys, a token bombardment of the fleet, and trimmed anti-air. Everything
else in the Land Game applies unchanged. It closes with the
**limited-intelligence** rules (SPI 3.6) that every file leans on.

::: note
SPI's designer warned in the errata that these abstract rules were never
tested and may not work. They are restated faithfully; expect rulings.
:::

::: spi-omit 32.1 32.2 32.3 32.4 32.5 32.6 32.7 32.8 — subsection headings and commentary; the rules under them are restated below

::: spi 32.0

These rules apply when the Land Game is played without the Air and Logistics
Games. Every supply expenditure in the Land and Air rules is ignored and
replaced by the ammunition and fuel costs below; trucks are replaced by
**motorisation points**; supplies come as **supply units** that arrive like
ordinary supplies with the adjustments given here. Game balance shifts
somewhat (SPI §65).

## Supply units

::: spi 32.11 32.12 32.13 32.14 32.15 32.16 32.17 32.18

Ignore all ammunition, fuel, stores and water rules: nothing suffers
attrition for want of them. Instead a **supply unit**, shown by a supply dump
counter, holds at most **40 ammunition and 60 fuel** (its starting load) and
is removed when both reach zero. Units in one hex may rearrange their
contents freely in the organisation phase. A supply unit has no combat value
and **0 SP**; an enemy combat unit entering its hex captures it and may use
it at once. At most **five** may stand in a major city hex, **three** in any
other hex; the Tripoli–Tunisia boxes hold any number.

A combat unit may draw on any friendly supply unit within **half its CPA**
— 5 CP for foot infantry, 10 for a heavy-weapons unit on motorisation
points, 23 for a typical recce unit — the distance traced as a medium truck
would move it (as infantry for foot infantry), never through impassable
terrain or an enemy ZOC without a friendly unit in it.

**Destroying** your own supply unit: before any movement in a sub-segment,
spend half the CPA (rounded up) of every unit in the hex and roll one die
per supply unit; 1–3 destroys it, +1 to the roll if the hex holds 1 SP or
less. One attempt per unit per sub-segment.

**Dummy** supply units: one per three real units received or started with,
moved like real ones (needing fewer motorisation points), removed when
found.

## Supply expenditure

::: spi 32.21 32.22 32.23 32.24 32.25

::: ruling R-013 — pinned units spend no ammunition in a close assault

Keep ammunition and fuel per supply unit on the dump, convoy or TOE log
sheets. The fleet and patrolling points need nothing.

- **Ammunition**, per battalion-equivalent (a 5-SP division pays by its
  component counters), at the instant of combat: a non-phasing
  battalion-equivalent pays **1** to defend in an assault and **2** to
  barrage; a phasing unit pays **double**. Only units committed to the
  assault pay; pinned, retreated-in and withheld units in the hex share the
  losses but spend no ammunition ([R-013](../rulings/R-013.md)).
- **Fuel**, per stage: the first time a fuel-using unit moves by land in a
  stage it pays its fuel from a supply unit and may then move up to its CPA
  in any pattern; exceeding its CPA costs the same again at that instant. A
  tank battalion-equivalent pays **2**, a tank company-equivalent **1**;
  gun-class and recce battalion-equivalents (not camel reconnaissance)
  **1**; motorisation points carrying infantry (not replacements), a gun
  battalion-equivalent or a real supply unit **1**. Company-equivalents and
  motorisation points doing anything else pay none. Rail and sea moves pay
  none. Patrolling pays none.

## Moving supply units

::: spi 32.31 32.32 32.33 32.34 32.35 32.36 32.37

Supply units move by land, rail, sea or air — by land or rail in their
arrival stage too.

- **Land**: a real unit needs **30** motorisation points attached, a dummy
  **6**, attached or detached only in the organisation phase; without them
  it cannot move. It moves in the movement/combat phase *or* the truck convoy
  phase, not both, and in the movement/combat phase only if it starts and
  stays stacked with a friendly combat unit (non-phasing movement is
  unaffected).
- **Rail** (Commonwealth): two units, real or dummy, one direction, per
  stage, under the rail rules.
- **Sea**: the Axis ships a unit for **2,000 tons** of coastal shipping (two
  ships may share); the Commonwealth moves **one unit per stage** between
  Alexandria, Benghazi and Tobruk in the naval convoy arrival phase, the
  destination port at **50 %** efficiency or better, and in place of any
  troop transport at either port.
- **Air**: one supply unit per player per **turn**, in the organisation
  phase, lifted between hexes that are major cities, villages or Tripoli–Tunisia boxes
  (motorisation points may be detached to allow it), for **12 fuel** from
  any supply unit in the origin hex. Not from a hex with enemy combat units
  within five hexes; not east (Axis) or west (Commonwealth) of the farthest
  hex row held by a friendly division, shell or full; only to a hex holding
  a friendly division or brigade HQ (not a battle group). The unit stays put
  that stage but may be drawn upon.

## Receiving supply units

::: spi 32.41 32.42 32.43 32.44 32.45

Each scenario grants starting supply units; the rest come from the
Simplified Supply Availability Tables. Axis units arrive by convoy
([below](#simplified-axis-convoys)); Commonwealth units appear in Cairo, or
one in Alexandria per three received in a turn. Planning is done at the
start of each turn: the Axis player looks up the tonnage availability letter
for the month he is *planning in*, rolls one die on the Axis table under that
letter, and receives that many real units by convoy **two turns** later; the
Commonwealth player rolls on his table under the period of *arrival* and
receives them **four turns** later. Except in a scenario's first turn, units
arrive every turn the rolls allow.

::: spi 32.46 32.47

Both Simplified Supply Availability Tables are data:
`data/tables/simplified-supply.json` — the Axis table runs one die against
tonnage letters A–G (from nothing on a 1 under A to six units on a 6 under
G), the Commonwealth table one die against three supply periods (September
1940 to April 1941, May 1941 to May 1942, June 1942 on), one to seven
units.

## Motorisation points

::: spi 32.51 32.52 32.53 32.54 32.55 32.56 32.57 32.58

**Motorisation points** stand in for truck points and are medium trucks in
every respect not changed here. Scenarios give the starting number,
reinforcements add more, and replacements arrive at the medium-truck rate.
They carry units and any gun with CPA 0+; all other units have built-in
transport. Any foot infantry may be motorised, but historically motorised
battalions (CPA 8+ and 10+) must all be served first. They never break down
(other breakdown rules stand), are lost only with their unit (captured with
it, for the enemy's use), and never suffer a barrage truck result.

**Abstract losses**: in each month's first naval convoy stage, read the
Abstract Motorisation Point Loss Chart for the previous month — Commonwealth
percentage left of the stroke, Axis right — of all the player's points on
the map (boxes included), removed from map E (Commonwealth) or map A and the
boxes (Axis).

Points carrying a supply unit have CPA **15**; forced over it they return to
the last hex where they were within it; they pay no CP when stacked with
combat units in combat; and they may react unless the approaching unit has
CPA **35 or more**.

::: spi 32.59

The monthly loss chart is data: `data/tables/motorisation-losses.json` —
October 1940 to January 1943, Commonwealth and Axis percentages (the
Commonwealth figure peaks at 10 % in March 1941, the Axis at 6 % in
November 1942). The chart sheet heads it 58.5.

## Simplified Axis convoys {#simplified-axis-convoys}

::: spi 32.61 32.62 32.63 32.64 32.65

An Axis convoy is the turn's supply units, motorisation points and
replacement points, split among the convoy lanes (SPI 56.0) with no tonnage
limit but at most **three supply units and twenty motorisation points per
lane per convoy stage**, and within the replacement pool's per-turn maxima.
In the naval convoy phase the Axis names the lanes in use and the
Commonwealth attacks each arriving convoy separately, whatever the weather:
read down the lane's column of the Simple Axis Naval Convoy Bombing Chart to
the westernmost qualifying Commonwealth division for the bomb points, then
roll two dice sequentially on the Air Bombardment Table in that column for
the percentage destroyed. A **10 %** result hits only motorisation (fractions
down) and replacement points (fractions up); **20 % or more** hits
everything, fractions down, but always at least one point of each item and
one supply unit. Tank and gun losses are a percentage of each nationality's
total, the Axis choosing the types.

::: spi 32.66

The Simple Axis Naval Convoy Bombing Chart is data:
`data/tables/axis-convoy-bombing.json` — six route columns, ten bomb-point
bands from 21–40 up to 471+, each cell the westernmost map column a full
Commonwealth division must have passed for that band to apply; dashes
where a route can never be hit that hard.

## Bombardment of the fleet

::: spi 32.71 32.72 32.73 32.74 32.75

The Axis gets a few strikes on the fleet in Alexandria harbour: roll one die
secretly at the start of the scenario (+2 in a campaign game) for the number
of attacks. One per stage, plotted secretly in the Commonwealth fleet
assignment segment and executed in the tactical naval movement segment,
never while map E is under rainstorm or sandstorm. Roll one die (+2 in a
campaign game) to pick that many columns in from the left of the Air
Bombardment and Secondary Barrage Targets table, then two dice sequentially
in that column: the result is damage points, as on the Chariot Table,
distributed as the Axis likes among ships in the harbour.

## Anti-air modifications

::: spi 32.81 32.82 32.83 32.84

Anti-air is thinned because there is no Air Game:

- **Commonwealth**: remove every AA unit and every light and heavy AA TOE
  point and replacement point; captured Axis AA points go too.
- **German**: remove AA units coded *z* and *bb*, and all assigned light AA
  points and replacements; heavy AA stays.
- **Italian**: remove AA units (*ss*, *tt*, *uu*); strip AA points from
  emplaced-gun units (*pp*); artillery that may hold AA (*kk*) loses its
  heavy AA points; heavy (75 mm and 90 mm) AA replacements are lost; light AA
  replacements arrive at one per month.

None of this touches non-AA points that merely carry an AA rating.

## Road and track stacking

::: spi 32.9

Ignore the road and track stacking limits of
[Stacking & ZOC](50-stacking-and-zoc.md#roads); all other stacking applies.

## Limited intelligence {#limited-intelligence}

::: spi 3.61 3.62

CNA runs on trust: a player is entitled to nothing about an enemy counter's
status, composition or attributes except what a rule expressly grants. In
land combat only totals are revealed, never the units behind them. What *is*
available:

| Occasion | Revealed |
|---|---|
| map | any stack may be examined; not what the counters contain |
| anti-armour fire | the tank and SP-gun types, and whether armoured recce or halftracks took part in the assault — not numbers, origin hexes, or which points absorbed damage |
| close assault | the unit types that took part (or were overrun) — not numbers or which weapons were lost |
| prisoners | nothing; they cannot be questioned |
| patrol | as in [combat](60-combat.md#what-a-patrol-learns), never supplies or trucks beyond motorised-or-not |
| broken-down, destroyed or abandoned vehicle markers | contents secret |
| POWs, camps, guards | numbers (and Axis nationality) secret |
| construction | the item secret |
| trucks and replacement points | numbers and types secret |
| air reconnaissance | less than a patrol |
| aircraft | makes known in air-to-air combat, pilot ratings secret until it; a land unit without AA points or an SGSU learns only the mission type of planes attacking it |

---

*Drawn on: SPI §32.0–32.9 and §3.6 (3.61–3.62, from the §32 addenda), and the designer's errata note on §32.*
