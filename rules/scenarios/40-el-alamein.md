---
title: Group Four — El Alamein
status: provisional
---

# Group Four — El Alamein

Autumn 1942: the Axis army stands at the end of its supply line in front of
El Alamein. Two scenarios start from the same position. **The Last Chance**
gives the Axis one week to break through to Alexandria; **The Long Retreat**
asks how well it can delay the Commonwealth on the long road west. SPI calls
both historically interesting rather than balanced.

::: spi 63.0 63.1

## Length {#length}

::: spi 63.2

Both start in the first Operations Stage of Game-Turn 102. The Last Chance
lasts that one Game-Turn (`data/scenarios/the-last-chance.json`); The Long
Retreat runs to the end of the last Game-Turn of December 1942
(`the-long-retreat.json`, extending the first).

::: ruling R-108 — the printed start and end Game-Turns

The printed turn numbers are garbled. The Last Chance is Game-Turn 102
only; The Long Retreat ends after Game-Turn 110, the last week of December
1942.

## Commonwealth forces {#commonwealth}

::: spi 63.3 63.31 63.32 63.33 63.34 63.35 63.36 63.37 63.38

The Eighth Army's starting hexes, attachments, first-line trucks and tank
compositions are in `sides.cw`, with its air force, second- and third-line
trucks, supply, fleet, Malta, and its reinforcements and replacements.

## Axis forces {#axis}

::: spi 63.4 63.41 63.42 63.43 63.44 63.45 63.46 63.47 63.48

The Panzerarmee's starting hexes, attachments, trucks, tank compositions,
air force (in Africa and across the Mediterranean), supply, reinforcements
and replacements are in `sides.axis`, together with the equipment upgrades
63.48 allows.

## Special rules {#special}

::: spi 63.5

Two optional rules are not used: the Italian 10th Light Flotilla and the
raid on Rommel.

## Initiative {#initiative}

::: spi 63.6

The Axis player holds the Initiative in the first Operations Stage, as it
did historically; players may instead roll for it as usual.

## Construction at the start {#construction}

::: spi 63.7 63.71 63.72 63.73 63.74 63.75 63.76 63.77

- Every unfinished road and the whole unfinished railway are built, but
  the railway is cut in the three hexes just west of El Alamein.
- Pipelines exist only along the railway: the Axis draws water through it
  from Tobruk, the Commonwealth from Alexandria.
- Ports are at their listed efficiency except Benghazi (1) and Tobruk (5).
- Level 1 fortifications stand in the four hexes next to Tobruk, and the
  Axis player may add three more among the four next to Bardia.
- **Minefields**, all starting face up (status unknown), at the hexes the
  data lists (`construction.minefields`): fifteen Commonwealth sites of
  which ten are real, the owner choosing which; fourteen Axis sites of
  which eleven are real; and the Axis may also lay up to five real and two
  dummy fields near Tobruk and two real and two dummy elsewhere on maps A
  to C, more than five hexes from Tobruk.

## Without the Air or Logistics Game {#abstractions}

::: spi 63.8 63.81 63.82 63.83

On top of [the general rules](00-reading-scenarios.md#abstractions), the
data's `abstractions` block gives each side's changes: fewer second- and
third-line trucks without the Air Game, and supply units in place of dumps
without the Logistics Game.

## Victory {#victory}

::: spi 63.9 63.91

**The Last Chance.** The Axis wins strategically by occupying any hex of
Alexandria with at least a brigade's worth of units, whatever its supply.
Otherwise each side counts its TOE strength points on the enemy's map (the
Axis on map E; the Commonwealth on map D, not counting Layforce and SAS);
the larger total wins a tactical victory.

::: spi 63.92

**The Long Retreat.** The Axis scores points for each place it occupies at
the end (`victory.points`), but only where every combat unit there has a
Game-Turn's stores, ammunition to fire every weapon twice, and fuel to move
20 CP. Ten or more points is an Axis strategic victory, 4 to 9 a
substantive one, 1 to 3 a marginal one; none at all is a Commonwealth
victory.
