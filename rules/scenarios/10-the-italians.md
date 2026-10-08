---
title: Group One — the Italians
status: provisional
---

# Group One — the Italians

The first group covers the opening of the desert war, from mid-September
1940 to mid-February 1941: the Italian advance into Egypt and the British
counter-offensive. The quieter months before it are left out.

::: spi 60.0 60.1

## The two scenarios {#scenarios}

::: spi 60.2 60.21 60.22 60.23

Both start in **Game-Turn 1, OpStage 1** from the same set-up and can be
played on their own.

| Scenario | Ends after | Data |
|---|---|---|
| **Graziani's Offensive** | Game-Turn 6, OpStage 3 | `data/scenarios/grazianis-offensive.json` |
| **The Italian Campaign**, which takes in Operation Compass | Game-Turn 20, OpStage 3 | `data/scenarios/italian-campaign.json` (extends the first) |

Graziani's Offensive is the shortest scenario in the game and the one the
engine is built on first.

## Axis forces {#axis}

::: spi 60.3 60.31

Every Italian unit's starting hex, its attachments and its first-line trucks
are in the scenario file (`sides.axis.deployments`). Points worth knowing:

- Several Libyan Tank Command battalions start attached to infantry
  divisions (I(M) to the 1st Blackshirt Division, LXII(L) to Marmarica,
  LXIII(L) to Cirene, IX(L) to the 2nd Libyan Division, II(M) to Maletti);
  their own regiments list them as detached.
- The sheets of the 61st *Sirte*, 62nd *Marmarica* and 63rd *Cirene*
  divisions were left out of the printed OA charts and are taken from SPI's
  errata.
- **Armoured cars.** Two TOE strength points of Autoblinda 40 recce may
  each be attached to a different unit, ignoring composition limits, or
  start in Tobruk as trained, fuelled replacement points.

::: ruling R-094 — Italian artillery printed twice in the Libya list

The Libya list names the 4/1 artillery battalion and the XXI Corps
artillery twice; each is a single counter and is placed once.

::: spi 60.32

**Air.** The Italian planes may start at any Italian air facility in
Libya within its capacity, but none in Italy or Sicily, and Crete is still
British. No Italian plane may be refitted before Game-Turn 1, OpStage 2.
Types, numbers, pilots and SGSUs are in `sides.axis.air`.

::: variant V-007 — some Italian squadrons start in Sicily

::: spi 60.33 60.34 60.35 60.36 60.37

**Trucks, supply and shipping.**

- Second- and third-line trucks start at Tripoli, anywhere in Libya, or on
  air facilities, as `sides.axis.trucks` lists. Italy has a major repair
  facility at Tripoli and temporary ones at Tobruk and Benghazi.

::: ruling R-099 — Tobruk's repair facility, temporary or major

Tobruk's facility is temporary in this scenario, as the set-up says; a
scenario's own list of repair facilities governs it, and 22.31's major
facilities apply wherever a set-up says nothing.

- Dumps start at Tobruk, Bardia, Benghazi, Derna, the Tripoli box and
  C0716. Two more real dumps and two dummies go anywhere in the Libyan part
  of map C that is more than four hexes from every Commonwealth unit. A
  further total is spread over the Italian air facilities.
- All Axis coastal shipping is available and starts at Tripoli.
- Axis strategic attacks on Malta are limited to what Availability Level I
  of the Axis Strategic Commitment Chart allows.
- Before play, the Italian player plans his convoys for the rest of
  September 1940, using lanes 2, 3 and 6 only; reinforcements arrive by the
  track.

::: ruling R-097 — when the first Axis convoy arrives, and whether it can be bombed

The plan covers Game-Turns 1 and 2. The Game-Turn 1 convoy unloads in
OpStage 1; the Commonwealth cannot bomb it, as the turn's bombing phase
comes before the scenario starts.

## Commonwealth forces {#commonwealth}

::: spi 60.4 60.41

The Western Desert Force's starting hexes, attachments and first-line trucks
are in `sides.cw.deployments`. The 6th Australian Division is in training
in Cairo or Helwan, less the brigade and two artillery regiments that
arrive later. Three TOE points of cruiser tanks start broken down in
Alexandria.

::: ruling R-096 — a unit set up before its OA arrival (the French Motor Marines company)

::: spi 60.42 60.43 60.44

**Air, trucks and supply.** Planes, pilots and SGSUs may start at any
Commonwealth air facility in North Africa within its capacity (two French
types may share a squadron). Second- and third-line trucks start in Cairo,
Alexandria, anywhere on the maps or at air facilities. Dumps start at Mersa
Matruh and Sidi Barrani, with one more real dump and one dummy in the
Egyptian part of map C or D, and a total for the air facilities. Cairo and
Alexandria hold unlimited supply under the normal rules. A temporary repair facility stands at Mersa Matruh.

::: ruling R-098 — whether every hex of Cairo and Alexandria is a major repair facility

The Commonwealth's major repair facilities are every hex of Cairo and
both hexes of Alexandria.

::: spi 60.45 60.46 60.47

**Fleet, Malta and reinforcements.**

- The fleet starts in port at Alexandria and Valletta, armed and undamaged,
  and may not sail before the start of Game-Turn 2 (`sides.cw.fleet`).
- Malta has its own planes, pilots, SGSUs and 17 anti-aircraft points to
  spread over its facilities, which can ready five SGSUs between them. Work
  to enlarge them may start in October 1940.
- Reinforcements arrive by the track
  ([schedule](../70-organisation.md#reinforcements),
  `data/tables/reinforcement-schedule.json`); some must train first, and
  others must be found to train them. No replacement points arrive before
  November 1940.

::: ruling R-095 — the printed fleet total disagrees with the lists

The fleet is the ships the lists name, in the ports they give: the
printed total that disagrees with them is set aside.

## Air facilities {#air-facilities}

::: spi 60.5

Every air facility on the map exists at the start, and whoever controls one
may use it. Egypt's belong to the Commonwealth and Libya's to the Italians,
along with the four off-map Tripoli and Tunisia boxes. There are more
landing strips than counters; use blanks.

## Initiative {#initiative}

::: spi 60.6

The Italian player holds the Initiative for all of Game-Turn 1. From
Game-Turn 2 it is determined as usual.

## Construction at the start {#construction}

::: spi 60.7

No minefields or fortifications; no pipeline beyond the railway, which ends
at Mersa Matruh (D3714). Every port is at its listed efficiency except
Tobruk, partly blocked by the wreck of the *San Giorgio*.

::: ruling R-027 — Tobruk's efficiency level

Tobruk starts at efficiency level **2**: its full level of 5 less the
wreck's three. (The scenario prints 7.)

## Victory {#victory}

::: spi 60.8 60.81

**Graziani's Offensive** is judged by places held at the end, each by a
unit that meets the supply condition (in the data, `victory.levels`). The
highest level a side reaches counts.

| Level | Italian player holds | Commonwealth player holds |
|---|---|---|
| Tactical | Sidi Barrani, while keeping Sollum, Fort Maddalena and Giarabub | Sollum, Halfaya Pass (C3922) and Siwa |
| Decisive | Mersa Matruh and Siwa | Sollum, Siwa, Bardia, Sidi Omar and Fort Maddalena |
| Strategic | any hex of Alexandria or Cairo | Tobruk |

Italian units must be suppliable by convoy: from Tobruk for the tactical and
decisive levels, from map D for the strategic one. Commonwealth units must
have a truck-convoy supply route to Cairo or Alexandria.

::: ruling R-110 — what the supply condition means when only the Land Game is played

With the Land Game alone (60.92) there are no convoys to trace, so the test
is a route: from each holding unit's hex to the source (any hex of Tobruk,
any hex of map D, or any hex of Cairo or Alexandria), any length, that a
medium truck could follow without entering a hex holding an enemy unit or an
enemy ZOC hex with no friendly unit in it. The source hex must be free of
enemy units. No supply unit is needed (`victory.levels[].supply_trace`).

::: variant V-008 — Mussolini's requirements on the Italian advance

::: spi 60.82

**The Italian Campaign** is scored in points for places held at the end by
combat units (units whose close assault rating is not in parentheses) able
to trace supply, no more than a Game-Turn long, to a dump or city linked
back to Cairo or Tripoli. Each place scores for whichever side holds it
(`victory.points`); most points wins. If no Italian combat unit on the map
can trace a supply line, the Commonwealth wins outright.

## Without the Air or Logistics Game {#abstractions}

::: spi 60.9 60.91 60.92 60.93

These change the full set-up on top of [the general rules](00-reading-scenarios.md#abstractions):

- **Air Game left out:** nothing more.
- **Land Game only:** each side may bring in motorisation points as it
  could bring in medium trucks, one for one. Both sides' dumps are replaced
  by regular supply units in the same places (the Italian Dump 1 and Dump 2
  groups placed whole in one hex each, the Commonwealth's Dump I group on
  map D west of Mersa Matruh), with groups of three dummies placed the same
  way. Alexandria and Cairo each also hold three regular supply units.
  (`abstractions.air_and_logistics`)
- **Logistics Game left out, Air Game played:** motorisation points come
  in as medium plus heavy trucks would; the supply units are as for the
  Land Game only, plus a few regular units to share among each side's air
  facilities. (`abstractions.logistics`)

The printed text points the last case at 60.82 for its supply units; the
supply units it means are those of 60.92.
