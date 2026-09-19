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
