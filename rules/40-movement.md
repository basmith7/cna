---
title: Movement
status: draft
---

# Movement

<!-- DRAFT SKELETON — not yet restated. Section map to SPI §8 for the next run:
  How units move ........... 8.1  (8.11–8.1x: voluntary vs involuntary, no skipping, ZOC stop/exit)
  Continual movement ....... 8.2  (repeatable G cycle, 2-hex / reserve re-move restriction)
  Terrain effects .......... 8.3  (8.37 Terrain Effects Chart → data/tables/terrain-effects.json;
                                   extend common.schema terrain enum; 8.34 road/track column)
  Special terrain .......... 8.4
  Reaction ................. 8.5  (non-phasing movement; cross-ref 50-stacking-and-zoc)
  Breaking off ............. 8.6  (break contact 2 CP / disengage 4 CP — costs in 30-capability-points)
  Rail movement ............ 8.7  (Commonwealth only, phase J)
  Tripoli and Tunisia ...... 8.8
  Motorised units / trucks . 8.9  (motorisation CPA rule is in 30-capability-points#motorisation;
                                   loading/capacity/fuel/breakdown pointers here; anchor #trucks)
  Breakdown itself is §21 — cross-reference, not restated here.
-->

This file defines how land units move: when movement is allowed, what it
costs, how the repeatable move–fight cycle works, terrain, reaction, breaking
off, rail and trucks. The CP budget itself is in
[Capability points](30-capability-points.md); zones of control and stacking
in [Stacking & ZOC](50-stacking-and-zoc.md); breakdown in [Special](90-special.md).

::: spi-omit 8.0 8.1 8.2 — section headings and design commentary; the rules under them are restated below

## When a unit may move

::: spi 8.11 8.12 8.13 8.14 8.15 8.16 8.17 8.18 8.19

**Voluntary** movement happens only in a movement segment of the phasing
player's own half of the stage, or in the retreat-before-assault step of the
enemy's. Nothing moves outside the sequence of play. The non-phasing player
still gets to move during the enemy's segments — by reacting and by retreating
before assault — but that is not voluntary movement for the purposes of the
limits below.

**Involuntary** movement — a retreat forced by combat — follows the same
rules: it costs CP and, for vehicles, triggers a breakdown check.

Every move costs CP ([cost table](30-capability-points.md#cost-table)) and
every vehicle move (armour, self-propelled guns, trucks) is checked for
breakdown. A unit passes freely through friendly units, except on roads and
tracks (see *Terrain*).

Movement is hex to hex, adjacent hexes only; a unit never enters a hex
holding an enemy unit (the capture case in [Combat](60-combat.md) is the one
exception). Entering an enemy zone of control ends the unit's movement for
that segment; it will usually have to attack the unit projecting the ZOC.

A unit that *starts* a movement segment in an enemy ZOC may leave it and keep
moving if:

1. it does not step directly into another enemy ZOC (ZOC-to-ZOC movement is
   defined in [Stacking & ZOC](50-stacking-and-zoc.md)); and
2. it pays 2 CP to **break contact**, or 4 CP to **disengage** if the
   position came from an *engaged* combat result.

Units may keep moving and fighting as long as their owner wishes, subject to
the continual-movement limits below. Exceeding the CPA is allowed and costs
cohesion. Two hard limits:

- A **non-motorised** unit (CPA 10 or less) may never *voluntarily* spend more
  than 150 % of its base CPA in its own half of the stage: 8 → 12, 10 → 15.
  Reaction and retreat before assault happen in the enemy half and do not
  count.
- A unit at cohesion level **−26 or worse** cannot move at all
  ([Units and state](10-units-and-state.md#effects-of-the-cohesion-level)).

Truck convoys (second- and third-line trucks) have their own phase (H) and
never move in a movement segment. A truck moves in a movement segment only
while it is attached to, and forms part of, a combat unit or HQ; attaching and detaching
happens in the organisation segment.

**Commonwealth boundary.** No Commonwealth land unit may ever be west of
Marble Arch (hex A2109), for any reason.

## Continual movement

::: spi 8.21 8.22 8.23 8.24 8.25

There is no fixed movement allowance. A unit may move and fight, move again
and fight again, any number of times in a stage, paying CP for everything;
the only limits are the CPA overspend rule, the non-motorised cap and the
two-hex rule below.

The phase is a **cycle**: move everything you intend to move, *then* resolve
all combat, then move again, then fight again — repeat until you stop.
No combat is resolved while any movement in that cycle is still going on
(order of segments: [Sequence of play](20-sequence-of-play.md)).

**Two-hex rule.** After a movement segment, only phasing units that ended it
within two hexes of an enemy combat unit may move in a later segment of the
same phase. A unit that stops further away is done for the phase, however many
CP it has left — unless it is in reserve status, which is the one exception
([Stacking & ZOC](50-stacking-and-zoc.md#reserve)).

A phasing unit that *begins* the phase in an enemy ZOC pays 2 CP to break
contact before moving, or 4 CP if it is there because of an *engaged* result
(in which case whether an enemy ZOC is present is irrelevant).

A unit may attack the same enemy repeatedly in one stage without either side
moving; each attack is resolved after all other movement in that cycle has
stopped. With no movement at all, cycles of combat alone may continue as long
as the phasing player has the ammunition and is willing to pay the CP.

## Terrain

::: spi 8.31 8.32 8.33 8.34 8.35 8.36

Each hex entered, and some hexsides crossed, costs CP that depend on the
terrain and on the unit type. Costs run from ½ CP (a motorised unit on a
road) up to +8 (a vehicle descending an escarpment by track, or a foot unit
crossing the Nile with no bridge). Some terrain is **prohibited** to some
unit types — vehicles may not enter salt marsh, for instance, unless on a
road or track. All of this, and every combat effect of terrain, is on the
Terrain Effects Chart, transcribed as `data/tables/terrain-effects.json`.

::: spi-omit 8.37 — the Terrain Effects Chart is a lookup table on the chart sheet; transcribed to `data/tables/terrain-effects.json` (pending capture of the sheet), not restated as prose

**Roads and tracks.** A unit gets the road or track rate only when it moves
between two adjacent road/track hexes that are joined across a road/track
hexside. While doing so it ignores every other terrain
feature of the hex and hexside — except that vehicles still pay to cross an
escarpment (see *Special terrain*). A unit with any vehicles in it, moving by road or track, is restricted
when it comes to friendly units sitting on that road ([Stacking & ZOC](50-stacking-and-zoc.md#roads)); it may always
leave the road, go round them through the hex's own terrain, and rejoin the
road in the next hex.

**Slopes, ridges, escarpments.** Slopes and escarpments each have an *up* and a *down* side (the map's splash contours mark the
down side),
so crossing one of these hexsides is always either climbing or descending.
Ridges have no direction: a ridge is a two-sided slope and costs the same
from either side.

## Special terrain

::: spi 8.41 8.42 8.43 8.44 8.45 8.46 8.47 8.48 8.49

::: spi-omit 8.4 — subsection heading and historical commentary

**Wadis** are hexside features (the one exception, Wadi Natrun west of the
Delta, is treated as salt marsh). Crossing a wadi hexside costs CP for every
unit and gives vehicles a breakdown factor of 8. A road cancels the wadi;
a track halves the crossing cost. On a road a vehicle pays the
road breakdown rate (2 BP); on a track, 4 BP rather than 8. In a **rainstorm**
stage, wadis in the affected map sections are impassable except by road;
crossing a flooded wadi by road costs +2 CP with no extra breakdown (still
½ BP).

**Escarpments.** Crossing costs are on the chart; on top of those, no vehicle
may ever cross an escarpment hexside *upward*. Where a track crosses one,
vehicles may use it to go down — never up — at +8 CP and 6 BP.

**Slopes and ridges** may be crossed by every unit at the chart's CP and
breakdown costs.

**Salt marsh.** A vehicle needs a road or track to get into or out of salt
marsh, except light trucks, motorcycle infantry and recce-type units. Any
prohibited vehicle that ends up in salt marsh off the track — for whatever
reason — is abandoned ([§32](95-abstract-logistics-and-air.md) for the
logistics form). Because of this, no motorised unit or AFV may ever assault a
defender in a salt-marsh hex. The Meharisti camel unit moves as infantry in
salt-marsh hexes without a track.

**Desert** (the Libyan Sand Desert) is soft sand. Light trucks, motorcycle
infantry and motorcycle recce may never enter a desert hex, track or no track.

**Tracks** cost 1 CP per hex, halve most hexside crossing costs and halve the
breakdown cost for the hex.

**Railways and roads not yet built** in a scenario's start date are listed by
the scenario. An unbuilt railway hex is ignored entirely; an unbuilt road is
a track.

**Oases** have no movement effect; they are non-diminishing supply dumps for
water and stores.

Terrain's combat effects are stated in [Combat](60-combat.md), which also
carries the chart's combat columns.

## Reaction

::: spi 8.51 8.52 8.53 8.54 8.55 8.56

::: spi-omit 8.5 — subsection heading and design commentary

**Reaction** is movement by a non-phasing combat unit, during the enemy's
movement/combat phase, when an enemy combat unit moves next to it. It follows the normal movement rules except as below, costs CP, and
never costs the break-contact or disengage fee. A unit may react any number
of times in a stage. There is no distance limit, but a reacting unit may
**never enter an enemy ZOC**.

A unit may *not* react when:

- it is non-motorised, a squadron ground-support unit, or a truck convoy not
  stacked with a friendly combat unit;
- the adjacent enemy unit's CPA exceeds its own by **6 or more** *and* the
  phasing player declares a close assault against it (it may still retreat
  before assault — [Combat](60-combat.md)); each unit in a stack is judged on
  its own CPA;
- it is already in an enemy ZOC — this is how faster units **pin** slower
  ones; or
- it is in combat or *engaged*.

*Example (our own).* An Axis recce battalion (CPA 45) moves adjacent to a
Commonwealth motorised battalion (CPA 20 from its trucks) and declares an
assault: the battalion is pinned, 45 − 20 ≥ 6. A tank battalion at CPA 25
doing the same would not pin it (25 − 20 = 5).

**Size limit on pinning.** Regardless of CPA, no battalion-sized unit can
pin a division and no company-sized unit can pin a brigade or larger. Size
is judged by stacking points and TOE, not by the designation on the counter
([Stacking & ZOC](50-stacking-and-zoc.md)); if it is genuinely unclear, use
common sense.

**Reacting out of a formation.** An attached unit may react by paying the
detachment cost first. A brigade HQ cannot detach from its division unless
everything attached to that brigade HQ detaches too. Detachment may not be
used to dodge the size limit above — a parent may not shed units so that it
becomes a shell and is now "too small to pin", nor shed its slow units so
that the remainder is fast enough to react. Attached trucks may be split
freely between the parent and the units detaching to react.

## Breaking off

::: spi 8.61 8.62 8.63 8.64 8.65 8.66 8.67 8.68

::: spi-omit 8.6 — subsection heading

Two states tie a unit to an enemy combat unit; both are shown with markers:

- **Contact** — the unit is in an enemy ZOC at the start of a movement
  segment.
- **Engaged** — a close-assault result ([Combat](60-combat.md)). An engaged
  unit need not be in an enemy ZOC.

A unit in either state at the start of a movement segment (or of a
retreat-before-assault step) may not move until it pays to **break off**: **2 CP** from
contact, **4 CP** from engaged. Reaction is exempt (see above). First-line
trucks detaching from a contacted or engaged parent pay the normal
detachment cost; second- or third-line trucks attaching as first-line trucks
to such a unit pay nothing extra.

Once every friendly unit that was in contact or engaged with a given enemy
unit has broken off, that enemy unit is no longer in contact or engaged
either.

The markers bind only the combat units that were in the hex when they were
placed. A unit that moves into a marked hex later is not affected by the
marker.

## Rail movement

::: spi 8.71 8.72 8.73 8.74 8.75 8.76 8.77 8.78

::: spi-omit 8.7 — subsection heading

Only one railway matters: **Alexandria–Mersa Matruh**, Commonwealth-only
whatever the strategic situation, extendable by construction
([Engineering](80-engineering.md)). The Soluch–Benghazi–Barce line is
decoration: it has no effect on anything.

Once per stage, in phase J, the Commonwealth player may run **one stack
eastward and one stack westward**, each any distance along finished track;
a stack is units and/or supplies. Limits:

- a rail-moving unit must begin the stage on a rail hex, must have spent
  **no CP** on anything that stage, and must not be in an enemy ZOC;
- it may never enter an enemy ZOC or an enemy-occupied hex on the way;
- at most **2 stacking points** per stack (large brigades split up); supply
  limits are in [§32](95-abstract-logistics-and-air.md);
- rail hexes that are bombed out are unusable until repaired, and unbuilt
  rail hexes until built;
- any rail hex west of an Axis combat unit sitting on the line is off limits.

Units may be picked up and set down anywhere along the line, so long as the
stacking, direction and no-CP-spent conditions all hold.
