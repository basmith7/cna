---
title: Sequence of play
status: provisional
---

# Sequence of play

This file defines the clock: how a game turn is divided, who acts when, and
the fixed order of phases each player works through. Procedures invoked by a
phase (movement, combat, construction, convoys) live in their own files; this
file only fixes *when* they happen.

::: spi-omit 5.0 7.0 7.1 — section headings and design commentary; the rules under them are restated below

## Time

::: spi 5.1

A **game turn** is roughly one week. It contains three **operations
stages**, each roughly two to three days. The stage is the basic unit of
time: nearly everything a unit does — moving, fighting, building, training —
happens inside a stage. A few housekeeping steps run only once per turn,
before the first stage.

## Initiative

::: spi 7.11 7.12 7.13 7.14 7.15 7.16

Each side has an **initiative rating** that depends on the calendar date of
the game turn. The rating table is on
SPI's separate chart sheet, not in the rules text; it is transcribed to `data/`
once that sheet is captured.

At the start of every game turn, before any stage, each player rolls one die
and adds their initiative rating. The higher total **holds initiative** for
the whole turn; on a tie both roll again. Scenarios normally fix who holds
initiative on the first turn — check the scenario before rolling.

Holding initiative means: at the start of each of the three stages, the
holder chooses whether to act first or last in that stage. The choice is made
stage by stage, so the holder may go first, then last, then first again,
which gives them two consecutive half-stages across the second and third
stages.

Within a stage the player who acts first is **Player A**; the other is
**Player B**. These labels can swap from stage to stage; they are positions,
not sides.

*Example (our own).* On a turn where the Commonwealth rating is 3 and the
Axis rating is 1, Commonwealth rolls 2 (total 5) and Axis rolls 5 (total 6):
Axis holds initiative for all three stages of that turn.

::: spi-omit 7.2 — the Initiative Ratings Chart is a lookup table on a separate sheet, not rules text; transcribed to `data/` when captured

## Turn outline

::: spi 5.2

This is the Land Game order when the Air and Logistics Games are not in play.
Stages I–II run once per turn; stage III is the first operations stage and is
repeated as stages IV and V; VI ends the turn.

### I. Initiative determination

Resolve initiative as above.

### II. Naval convoy

1. **Convoy schedule** — the Axis player plans ship cargoes and routes and
   schedules future replacements from the Axis pool. The Commonwealth player
   reads the production table for the replacement points arriving two turns
   from now and plans their arrival. (See [§32](95-abstract-logistics-and-air.md)
   for the abstracted form.)
2. **Tactical shipping** — both players plan cargo moves between African
   ports. Axis coastal ships are counters; Commonwealth coastal shipping is
   uncounted and limited only by port capacity.

### III. First operations stage

Phases A–E are joint; F–L are then done by Player A, then again by Player B
with the labels swapped.

- **A. Initiative declaration** — the initiative holder states whether they
  are Player A or Player B for this stage.
- **B. Weather** — the initiative holder rolls for weather
  ([Special](90-special.md)).
- **C. Organisation** — three segments, in any order the players wish:
  - *Reorganisation*: attach, assign or detach units, including reinforcements,
    replacements and unassigned trucks ([Organisation](70-organisation.md)).
  - *Construction*: first complete any scheduled work (remove/add markers;
    finished units are free to move), then note units beginning or continuing
    work — those may not move voluntarily for the rest of the stage, except to
    react ([Engineering](80-engineering.md)).
  - *Training*: first note units and replacement points completing a level and
    apply the morale effect, then note units beginning or continuing training —
    same movement restriction as construction
    ([Units and state](10-units-and-state.md#training)).
- **D. Convoy arrival** — reinforcements, replacement points and ammunition
  points due this stage appear at their designated port or entry hex.
- **E. Commonwealth fleet** — the Commonwealth player assigns ships to sea or
  coastal hexes, then performs any ship repair.

Then, for Player A and afterwards for Player B:

- **F. Reserve designation** — mark the units held in reserve
  ([Stacking & ZOC](50-stacking-and-zoc.md)).
- **G. Movement and combat** — four segments run as one cycle. The phasing
  player may repeat the whole cycle as often as continual movement allows
  ([Movement](40-movement.md)); every repetition includes all four segments.
  1. *Movement*: every phasing unit that is not in reserve and is able to move
     may move, except unattached trucks and tank recovery squadrons. The
     non-phasing player may react where permitted.
  2. *Breakdown*: both sides check every vehicle and motorised unit for
     breakdown; mark broken-down vehicles.
  3. *Combat* ([Combat](60-combat.md)), in this step order:
     1. position determination for all gun- and armour-class units, both sides;
     2. barrage — both sides plot secretly, then execute;
     3. retreat before assault — Player B only, units permitted to;
     4. force assignment — both sides secretly split TOE strength points between
        anti-armour and close assault; Player A privately decides which
        assaults are probes and which points are withheld;
     5. anti-armour fire — simultaneous; remove casualties, place destroyed-tank
        markers;
     6. close assault — resolved in any order Player A chooses, revealing after
        each one whether it was a probe.
  4. *Reserve release*: the phasing player may release any of their reserves.
- **H. Truck convoy movement** — the phasing player moves unattached second-
  and third-line trucks, and any prisoners with their guards.
- **J. Rail movement** — Commonwealth only, when phasing: rail movement of
  units and supplies ([Movement](40-movement.md)). (There is no phase I.)
- **K. Repair** — the phasing player first tows broken-down and recovered
  vehicles, then may attempt repair of broken-down or destroyed vehicles that
  were not towed this phase.
- **L. Patrol** — if the phasing player made no assault this stage, they may
  patrol for reconnaissance.

### IV–V. Second and third operations stages

Repeat stage III in full, including the initiative declaration in phase A.

### VI. End of turn

The turn is over; begin the next turn at stage I.

## Engine notes

- Phase labels skip **I**; the SPI list runs A–H, J–L. Keep the letters as
  written so citations line up.
- "Phasing player" in any file means the player currently working through
  F–L, even in segments where both sides act (breakdown checks, combat).
  Joint phases A–E have no phasing player.
- Initiative is determined once per turn but *declared* once per stage.
