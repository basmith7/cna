---
title: Group Two — the Desert Fox
status: provisional
---

# Group Two — the Desert Fox

The second group opens in March 1941 with Rommel and the first German units
landed in Tripolitania, the Italians rebuilt behind El Agheila, and a thin,
worn Commonwealth line holding Cyrenaica while its best formations refit in
Egypt or leave for Greece. Its first scenario is the race for Tobruk; the
same set-up is also offered as the start of a longer campaign.

::: spi 61.0 61.1

## Length {#length}

::: spi 61.2

**Rommel's Arrival** (the race for Tobruk) starts in Game-Turn 26,
OpStage 3, and ends after Game-Turn 38, OpStage 3
(`data/scenarios/rommels-arrival.json`). The campaign from the same set-up
is `desert-fox-campaign.json`; SPI gives it no length or victory conditions
of its own.

::: ruling R-104 — what the Desert Fox campaign scenario consists of

## Commonwealth forces {#commonwealth}

::: spi 61.3 61.31 61.32

Starting hexes, attachments and first-line trucks are in
`sides.cw.deployments`: the 2nd Armoured Division's fragments near Mersa
Brega, the 9th Australian Division between Benghazi and Tobruk, the 3rd
Indian Motor Brigade at El Adem, and in Egypt the 7th Armoured Division,
22nd Guards Brigade, Layforce and the rest. Neither Layforce nor the Long
Range Desert Group unit placed at Jalo has a counter on the OA sheets; both
are noted in the data. The 3rd Armoured Brigade's tank battalions start
with fewer tanks than their sheets give, some of them captured Italian
M13/40s (the data's `special` list gives the figures).

::: ruling R-103 — 5 RTR's tanks with no 5 RTR in the set-up

::: spi 61.33 61.34

**Air.** Squadrons start, all refitted, at the airfields and strips the
scenario lists (`sides.cw.air`), and the Commonwealth player may add three
landing strips anywhere. Malta has a facility capacity of 8 and 26
anti-aircraft points to share out; work on its facilities may not start
before the scenario's second Game-Turn.

::: spi 61.35 61.36 61.37

**Trucks, supply and fleet.**

- Second- and third-line trucks go anywhere on maps A to D (not E), with a
  further pool in Alexandria or Cairo.
- Nine real dumps and three dummies go on the places 61.36 lists, all of
  them used; Benghazi and Tobruk are dumps already. The pool of fuel,
  ammunition and stores is shared out with **no dump holding more than a
  quarter** of any one kind and **every real dump at least 50 points** of
  each. Benghazi also holds Italian prisoners, a camp and one guard.
- Unlisted first-line trucks may start loaded, on top of the listed supply.
- Repair: temporary facilities at Tobruk and Mersa Matruh, major ones at
  Alexandria and Cairo.
- The whole fleet starts at Alexandria, armed and undamaged, and may not
  sail before Game-Turn 27.

::: spi 61.38

**Reinforcements and the release rule.** Reinforcements arrive by the
schedule. Replacement points may not be planned ahead, and none come in
March 1941.

1. Nothing in Cairo or Alexandria moves in the first Operations Stage.
   After that, **one battalion a stage** is released from there (for this count
   the whole 22nd Guards Brigade is a single battalion); a brigade leaves a battalion at
   a time.
2. The 7th Armoured Division starts with **every tank broken down**. A tank
   battalion is released only once at least three quarters repaired, one
   a stage; one other battalion may go west each stage as well. Both begin
   in the first Operations Stage of April 1941. Its headquarters may go at
   any time.
3. The 18th Australian Brigade lands at Alexandria in the first stage of
   April 1941 and may move from the next stage, outside the limit.

## Axis forces {#axis}

::: spi 61.4 61.41

- **Germans:** every German counter the schedule brings before Game-Turn 26,
  OpStage 3 starts within one hex of El Agheila (A1816), not east of it, in
  any organisation, battle groups included. Two oasis companies start at
  Maaten Groter (A1318) and Magadah (A0817).
- **Italians:** Ariete within two hexes of El Agheila, not east of it;
  Pavia, Bologna, Brescia and Savona between Ras el Ali (A2010) and Nofilia
  (A2703), each at least two hexes from the next; Trento, Sabratha and corps
  artillery in Tripoli. Every Italian unit is as its OA sheet shows, except
  the Sabratha Division, which has lost its six infantry battalions
  (rebuildable from replacements) and has its machinegun battalion and
  artillery cut to one TOE point each.

::: spi 61.42 61.43 61.44 61.45

**Air, trucks and supply.**

- The German planes the air schedule brings before the start, all refitted,
  and the Italian planes 61.42 lists. German pilots come from one roll on
  the March 1941 pilot table. Aircraft may be based in Italy or Sicily
  within the German minimum (43.1); Crete is still British. One airfield and
  one landing strip may be placed west of El Agheila.
- German first-line trucks follow their units as the schedule attaches them;
  the Italian first-line trucks are given out freely. The second- and
  third-line pool is better used for supply than for troops.
- Five dumps, two of them dummies, between El Agheila and Nofilia; the pool
  is split among the three real ones with **no dump holding more than half**
  of any kind. Tripoli holds its own stock, and the Tripoli and Tunisia
  air facilities have unlimited fuel and ammunition.
- No Axis convoy arrives in the first Game-Turn; convoys for the second and
  third are planned before play. All other reinforcements come by the
  schedule.

## Initiative {#initiative}

::: spi 61.5

The Axis player holds the Initiative to the end of Game-Turn 27; from
Game-Turn 28 it is rolled for.

## Construction at the start {#construction}

::: spi 61.6

- The railway ends at Mersa Matruh (D3714); no minefields, and no pipeline
  beyond the railway.
- Ports are at their listed efficiency except Benghazi, at **0**, and
  Tobruk, still blocked by the *San Giorgio*.
- Four level 1 fortifications go to the Commonwealth player, placed no more
  than two hexes from Tobruk.
- The unfinished roads between Sollum and Sidi Barrani and all those around
  Tobruk are built.

::: ruling R-027 — Tobruk's efficiency level

Tobruk starts at efficiency level **2**: its full level of 5 less the
wreck's three. (The scenario prints 7.)

## Without the Air or Logistics Game {#abstractions}

::: spi 61.7 61.71 61.72 61.73

On top of [the general rules](00-reading-scenarios.md#abstractions)
(`abstractions` in the data):

- **Air Game left out:** both sides' second- and third-line trucks are cut
  to the totals 61.71 gives.
- **Land Game only:** motorisation points come in as medium trucks would,
  one for one. The Axis starts with 290 unattached motorisation points and
  the Commonwealth with 150 in Alexandria or Cairo and 90 elsewhere. Supply
  units replace the dumps: the Axis ones on the coast road between El
  Agheila and Nofilia, the Commonwealth ones on the dump sites.
- **Logistics Game left out, Air Game played:** as for the Land Game only,
  plus supply for the air facilities.

The printed text of these cases points at the truck cases (61.43, 61.35)
and at a case 61.62 that does not exist; the supply cases (61.44, 61.36)
and 61.72 are meant.

::: ruling R-102 — motorisation points when only the Logistics Game is left out

## Victory {#victory}

::: spi 61.8

Judged at the end, by places held (`victory.levels`):

| Result | Axis player holds |
|---|---|
| Axis victory | Tobruk |
| Axis decisive victory | Tobruk and Bardia |
| Axis strategic victory | Benghazi, Tobruk, Bardia and any two villages or cities in Egypt |

The Commonwealth wins by holding Tobruk, and wins a smashing victory by
holding Tobruk, Bardia and Benghazi.

::: ruling R-101 — who wins when the Axis player holds Tobruk alone

The levels are a ladder: Tobruk alone is an Axis victory. An Axis player
who does not hold Tobruk at the end has lost, even if no Commonwealth unit
holds it either. No supply condition applies to any holding.
