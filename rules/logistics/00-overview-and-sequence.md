---
title: Logistics Game — overview and sequence of play
status: provisional
---

# Logistics Game: overview and sequence of play

This file switches the game from abstract supply to **full logistics**. It
says what the Logistics Game tracks, which parts of the
[abstract rules](../95-abstract-logistics-and-air.md) it throws out and
which it keeps, and the turn order once it is in play. The procedures
themselves (fuel, ammunition, stores, water, trucks, dumps, ports, convoys)
live in the other files of this folder; this one only fixes *when* they
happen.

::: spi 48.0

## What the Logistics Game tracks

Supply comes in four kinds: **fuel**, **ammunition**, **stores** and
**water**. With the Logistics Game in play, every unit holds and uses up a
counted quantity of each, in points. Supply reaches the front in two ways:
the Axis ships it across the Mediterranean in **naval convoys**, and both
sides carry it overland in **trucks**, stocking it in **supply dumps** along
the way.

Designer's advice, restated: logistics decides this game. Trucks matter more
than any combat unit, and a stage in which nothing moves forward is three
game-days lost. The Axis, fighting far from its ports, feels this most.
Each side should give one player the logistics job and nothing else.

The Air Game is optional. The Logistics Game may be played with the Land
Game alone; then every step marked *Air Game only* below is skipped and the
*abstract air rules* (SPI §58) stand in for it.

## One switch: abstract or full logistics {#switch}

An engine chooses one mode per game. In **full logistics** mode the
following parts of [Abstract logistics and air](../95-abstract-logistics-and-air.md)
(SPI §32) no longer apply:

| Abstract rule (§32) | Replaced by |
|---|---|
| Supply units — load, draw range, capture, stacking (32.1) | Supply points of the four kinds held by units and dumps (*Trucks and dumps*) |
| Supply expenditure — per-assault ammunition, per-stage fuel (32.2) | *Fuel*, *Ammunition and stores*, *Water* |
| Moving supply units — rail, sea and air lift (32.3) | *Trucks and dumps*, *Ports and shipping* |
| Receiving supply units (32.4) | Convoy arrival and Commonwealth supply in *Ports and shipping* |
| Motorisation points (32.5) | Truck points, attached or in convoy (*Trucks and dumps*) |
| Simplified Axis convoys (32.6) | The tonnage convoy system (*Ports and shipping*) |

These parts **stay**:

- **Limited intelligence** (SPI 3.6) — it was only housed in §32; it
  applies in every mode.
- **Road and track stacking** (32.9) is ignored in both modes.
- **Bombardment of the fleet** (32.7), and the §32 procedure for attacking
  Axis convoys (32.6's bombing step only), stay whenever the Air Game is
  *not* played: §58 reuses them against the fuller convoy cargoes.
- **Anti-air modifications** (32.8) stay whenever the Air Game is not
  played; with the Air Game, its own rules take over.
- Everything else in the Land Game files.

Land Game passages that assume supply units or motorisation points carry a
note pointing to their replacement here.

## Turn outline {#turn-outline}

::: spi-ref 48.0

The data form of this outline is
[`data/tables/logistics-sequence.json`](https://github.com/basmith7/cna/blob/main/data/tables/logistics-sequence.json):
one row per stage, phase and segment, in order, each tagged with the
[Land Game phase](../20-sequence-of-play.md#turn-outline) it corresponds to
and flagged when it is new to the Logistics Game or needs the Air Game.

The Land Game outline gains three once-a-turn stages (strategic air
planning, stores expenditure, strategic air recovery), a convoy resolution
phase, three organisation segments (water, attrition, supply
distribution) and a land-support air phase. The one-turn Land Game stage
numbering therefore shifts: the operations stages are **V, VI and VII**
here, not III–V.

### I. Initiative determination

Both players roll for initiative exactly as in the
[Land Game](../20-sequence-of-play.md#initiative).

### II. Strategic air planning *(Air Game only)*

- **A. Designation** — each player splits their aircraft between land
  support and strategic missions.
- **B. Malta availability** — the Axis player finds how much of the
  off-map North African air force supports raids on Malta.
- **C. Strategic assignment** — strategic aircraft get their tasks: Axis to
  Malta raids or convoy cover; Commonwealth to naval missions or the bombing
  reserve.
- **D. Malta raid** — the Axis resolves flak suppression, anti-aircraft fire
  and bombing against Malta's air facilities. Commonwealth warships at
  Valletta can be hit only by land-support missions.

### III. Naval convoy

- **A. Convoy schedule** — the Axis player reads the convoy level chart,
  rolls one die on the convoy capacity table for the tonnage available
  **next** turn, then plans cargoes and routes.
- **B. Convoy resolution**, in three segments:
  1. *Reconnaissance* (Air Game only) — the Commonwealth flies strategic
     convoy reconnaissance.
  2. *Lane assignment* (Air Game only) — Axis cover aircraft take combat air
     patrol over chosen convoy lanes; Commonwealth bombing-reserve aircraft
     take patrol, flak suppression or bombing over chosen lanes.
  3. *Bombing* — air combat, flak suppression, anti-aircraft fire and convoy
     bombing are resolved. Without the Air Game, see
     [R-032](../../rulings/R-032.md).

Unlike the Land Game, tactical shipping is not planned here; it moves to
the organisation phase of every operations stage.

### IV. Stores expenditure

Once per turn, both players hand out stores to the units that need them and
note every unit left short (*Ammunition and stores*).
Both then reduce stocks of fuel and water for spillage and evaporation.

### V. First operations stage

Phases A–E are joint. The Land Game's phases then run for Player A, and
again for Player B with the labels swapped (see
[R-031](../../rulings/R-031.md) for where phase F falls).

- **A. Initiative declaration** — as in the Land Game.
- **B. Weather** — as in the Land Game; hot weather also costs the extra
  fuel and water evaporation now.
- **C. Organisation** — seven segments, in any order the players choose
  (see [R-030](../../rulings/R-030.md)):
  1. *Water distribution* — water goes to the units that need it
     (*Water*). **New.**
  2. *Reorganisation* — as in the Land Game; unassigned trucks may be
     attached too.
  3. *Attrition* — units that went short of water or stores are reduced.
     **New.**
  4. *Construction* — as in the Land Game.
  5. *Training* — as in the Land Game.
  6. *Supply distribution* — supplies in a hex with land units may be
     shared out among them, up to each unit's and the hex's capacity;
     trucks load and unload. **New.**
  7. *Tactical shipping* — both players carry cargo between African ports
     (*Ports and shipping*). Axis coastal ships
     are counters; Commonwealth coastal shipping has none and is limited
     only by port capacity. (Moved here from the Land Game's stage II.)
- **D. Convoy arrival** — reinforcements, replacement points and supplies
  due now, and actually arriving, are placed at their ports or entry hexes.
  The Axis plans future replacements from its pool. In the first arrival
  phase of each month the Commonwealth reads its production table for the
  points arriving two months later and plans their arrival.
- **E. Commonwealth fleet** — assign ships to sea or coastal hexes for
  bombardment, then repair ships.
- **F. Land-support air** *(Air Game only)* — only aircraft designated for
  land support in stage II fly. Seven segments: assign missions to fuelled
  aircraft; place mission counters; resolve air-to-air combat (including
  scramble and interception, with aborts allowed first); flak; complete
  missions (aborts allowed here too); return to base; then both players may
  try to ready land-support aircraft (tactical maintenance).
- **G. Reserve designation** — Land Game phase F.
- **H. Movement and combat** — Land Game phase G, unchanged, including the
  four-segment cycle and the six combat steps.
- **I. Truck convoy movement** — Land Game phase H: Player A moves
  unattached second- and third-line trucks, and prisoners with their guards.
- **J. Rail movement** — as in the Land Game; Commonwealth only, for units
  or supplies.
- **K. Repair** — tow, then attempt repair, as in the Land Game.
- **L. Patrol** — as in the Land Game.

### VI–VII. Second and third operations stages

Repeat stage V in full.

### VIII. Strategic air recovery *(Air Game only)*

- **A. Return to base** — surviving aircraft from stage II missions go home
  where they can.
- **B. Maintenance** — both players try to ready the aircraft that flew
  strategic missions.

### IX. End of turn

The turn is over; begin the next at stage I.

## Engine notes

- The Logistics outline uses every letter A–L in an operations stage,
  including **I**, where the Land Game skips it. A Logistics phase letter
  from G onward is one later than the Land Game letter for the same phase;
  use `attaches_to` in the data file to map between them.
- Stores are spent once per turn (stage IV); water is handed out every
  stage (phase C).
- Stage VIII picks up missions from stage II only; land-support aircraft
  recover within phase F of each stage.
- In the SPI movement segment the reacting player is called "Player A"; it
  is plainly Player B (the non-phasing player), as in the Land Game.

---

*Drawn on: SPI §48.0 (the Logistics Game introduction and its sequence of
play), with §58 and §32 read for what the abstract rules keep.*
