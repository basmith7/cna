---
title: Group Three — Operation Crusader
status: provisional
---

# Group Three — Operation Crusader

Winter 1941–42: the Commonwealth's Eighth Army moves to relieve besieged
Tobruk just as Rommel prepares his own blow east, and the two collide in the
desert between Sollum and Tobruk.

::: spi 62.0 62.1

## Length {#length}

::: spi 62.2

**Operation Crusader** starts in Game-Turn 57, OpStage 3, and ends after
Game-Turn 65, OpStage 1 (`data/scenarios/operation-crusader.json`).

## Commonwealth forces {#commonwealth}

::: spi 62.3 62.31 62.32

Starting hexes, attachments and first-line trucks are in
`sides.cw.deployments`: XIII and XXX Corps on the frontier, the Tobruk
garrison inside the fortress, and the rear in Egypt. The tank battalions'
actual strengths, which differ from their sheets, are in the `special`
list, as are the tanks broken down in the Alexandria shops, which may not be
repaired before the second Operations Stage. 42 RTR receives more Matildas
early in Game-Turn 58, sooner if it does not move in the opening stage.

::: ruling R-105 — a counter the set-up places twice (the 7th South African armoured cars)

::: spi 62.33 62.34 62.35 62.36 62.37 62.38

**Air, trucks, supply, Malta, fleet and reinforcements** are in the
scenario file. Reinforcements and replacements arrive in the normal way.

::: ruling R-107 — what an inactive dump is

Of six Commonwealth forward dump sites, four are real, sharing the
supplies with each holding at least a fifth of every item; the two
inactive ones are dummy dumps. The Axis sites are read the same way.

## Axis forces {#axis}

::: spi 62.4 62.41 62.42

Axis starting hexes and attachments are in `sides.axis.deployments`, the
German and Italian tank battalions' strengths in `special`. The 21st Panzer
Division's headquarters is placed although its sheet gives it a later
arrival (see R-096).

::: ruling R-106 — tank strengths for two battalions the set-up never places

The I(L) and II(L) light tank battalions start attached to the Ariete
division, at the strengths the scenario gives them.

::: spi 62.43 62.44 62.45 62.46 62.47

**Air, trucks and supply** are in the scenario file. Every Axis coastal ship
is available. The Axis player plans his replacements for every November
1941 Operations Stage before play, and normally from then on.

## Construction at the start {#construction}

::: spi 62.5

- No minefields; every port at its listed efficiency.
- Every hex next to Bardia holds a level 1 fortification, every hex next
  to Tobruk a level 2 one.
- The railway runs on past Mersa Matruh to C3430, and a pipeline continues
  straight from there to Bir Khamsa (C3029).
- Every unfinished road is built, except that the Siwa track is finished
  only as far as D2001.

## Without the Air or Logistics Game {#abstractions}

::: spi 62.6 62.61 62.62 62.63

On top of [the general rules](00-reading-scenarios.md#abstractions):

- **Air Game left out:** nothing more.
- **Land Game only:** motorisation points come in as medium trucks would,
  one for one, and both sides' dumps become supply units
  (`abstractions.air_and_logistics`).
- **Logistics Game left out, Air Game played:** motorisation points come
  in as medium plus heavy trucks would; the same supply units, plus one at
  each on-map airfield.

## Initiative {#initiative}

::: spi 62.7

The Commonwealth player holds the Initiative in the first Operations Stage,
as it did historically; players may instead roll for it as usual. From the
second stage on it is rolled for.

## Victory {#victory}

::: spi 62.8

Each side scores the places it holds at the end (`victory.points`): Tobruk,
Bardia, Sollum, Halfaya Pass, Fort Maddalena, Sidi Barrani, Giarabub, Siwa
and Fort Capuzzo, at values that differ by side. A place counts only if a
friendly combat unit holds it with enough supply to last a month and
ammunition for a week. The side with more points subtracts the other's
total; the margin gives the result (`victory.margins`): 10 or more a
strategic victory, 6 to 9 decisive, 1 to 5 tactical, 0 a draw.
