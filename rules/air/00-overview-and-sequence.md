---
title: Air Game — overview and sequence of play
status: provisional
---

# Air Game: overview and sequence of play

This file switches the game from abstract air power to the **full Air
Game**. It says what the Air Game adds, which parts of the abstract rules it
replaces, and where its steps fall in the turn. The procedures themselves
(aircraft, air facilities, flight, maintenance, missions, combat, flak,
Malta) live in the other files of this folder, added one at a time.

::: spi 33.0

## What the Air Game adds

Every aircraft is a counter of its own type, and fighters carry named
pilots. Each type has its own ratings and mission abilities, listed on its
nation's aircraft characteristics chart. Combat between aircraft is
resolved operationally, not dogfight by dogfight: a mission meets
opposition, the opposition is resolved as a whole, and what is left goes on
to bomb, strafe, scout, carry or drop.

The Air Game can be played with the Land Game alone or with the Land and
Logistics Games together. Played without the Logistics Game, it keeps
abstract supply, in the Air Game's own version of it
([§47](90-abstract-logistics.md)).

## One switch: abstract or full air {#switch}

With the Air Game in play, the abstract air rules go. Each passage below
carries a note pointing to its replacement.

From [Abstract logistics and air](../95-abstract-logistics-and-air.md) (§32):

- the abstract **motorisation point losses** (32.57, 32.59): motorisation
  points are strafed and bombed as trucks instead (47.5);
- the **simplified Axis convoys** (32.6), replaced by the Air Game's own
  abstract convoys (47.6), bombed under the Air Game's convoy rules (41.6);
- the abstract **bombardment of the fleet** (32.7), which bombing missions
  replace (47.7);
- the **anti-air modifications** (32.8), which strip AA units and points
  only because nothing flies: with the Air Game every AA unit and point
  stays (R-114).

From the Logistics Game, all of
[Abstract air](../logistics/60-abstract-air.md) (§58).

The rest of §32 depends on the other switch. With the Logistics Game, its
supply rules are already replaced and the Air Game uses full logistics.
Without it, §32 stays, changed and extended (depots, aircraft supply, air
transport of supply units) by
[the Air Game's abstract logistics](90-abstract-logistics.md) (§47).

## Turn outline {#turn-outline}

The Game-Turn with the Air Game is the Logistics Game's turn
([outline](../logistics/00-overview-and-sequence.md#turn-outline)), which
already lists every air step, and the full table is data:
[`data/tables/logistics-sequence.json`](https://github.com/basmith7/cna/blob/main/data/tables/logistics-sequence.json),
where `air_game_only` marks the air steps. Played without the Logistics
Game, drop the steps marked `logistics_game_only` (stores expenditure, water
distribution and attrition); what remains is the Land-and-Air turn, in the
same order.

The air steps, in brief:

1. **Strategic air planning**, once a turn after initiative: each side
   designates its aircraft for land support or strategic missions; the Axis
   learns how much of the off-map air force will help against Malta;
   strategic missions are assigned (Axis: raids on Malta or convoy cover;
   Commonwealth: naval reconnaissance or a bombing reserve); then the Axis
   raids on Malta are flown, flak suppression, flak and bombs in that order.
   Warships at Valletta can only be hit by land support missions.
2. **Convoy stage**: after the Axis plans its convoys, the Commonwealth
   resolves its convoy reconnaissance, both sides commit aircraft to
   particular convoy lanes (Axis cover; Commonwealth cover, flak suppression
   or bombing), and every lane's air fighting, flak and bombing is resolved.
3. **Land support air phase**, in every Operations Stage after the fleet
   phase and before reserves are designated, by both sides together:
   assign missions to fuelled aircraft, place them, resolve air combat
   (scrambles and interceptions included; aborts may come first), then flak,
   then complete the missions, return the survivors to base, and try to
   ready aircraft for the next stage.
4. **Strategic air recovery**, at the end of the turn: aircraft that flew
   the strategic missions of step 1 return to base, and both sides try to
   ready them again.

Air reinforcements arrive with the land ones in each naval convoy arrival
phase.

## Engine notes

- Two independent switches select the rules: Air Game on or off, Logistics
  Game on or off. The sequence table serves all four combinations through
  its `air_game_only` and `logistics_game_only` flags.
- The replacement list above is final: any §32 rule not named there is
  still in force with the Air Game and abstract logistics, as §47 changes
  it; §58 never applies with the Air Game.
