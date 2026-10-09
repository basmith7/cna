---
title: Air Game — the Mediterranean bases and Malta
status: provisional
---

# The Mediterranean bases and Malta

The Axis held the northern shore of the Mediterranean and flew bombers from
Italy, Sicily, Greece and Crete as well as from Africa. The map has boxes
for Italy, Sicily and Crete, with their flight distances. This file covers
those bases (§43) and Malta (§44).

## Axis bomber bases across the Mediterranean

::: spi 43.0 43.1 43.11 43.12 43.13 43.14

The German player must keep part of his bomber force in the Mediterranean
boxes. The types concerned are the **He 111**, the **Ju 88D** (the bomber;
the Ju 88C is a fighter and is not counted) and the **Fw 200** (printed
"FW220").

- **Always:** at least **75 %** of them are in Mediterranean bases.
- **Until Game-Turn 35** (the first week of June 1941): that 75 % must be
  in **Italy or Sicily**.
- **From Game-Turn 35 to the end:** at least **50 %** must be in **Crete**;
  the other 25 % may be in Italy, Sicily or Crete.
- Moving between Italy (or Sicily) and Crete, either way, takes **one
  Operations Stage**.

*Our example.* In August 1941 the Germans have 40 of these bombers. At
least 30 must be in the boxes, and at least 20 of those in Crete; the
remaining 10 may be anywhere, Africa included.

::: spi 43.2 43.21 43.22

**No SGSUs needed.** German bombers in the Italy, Sicily and Crete boxes
need no SGSU: the box supplies everything, fuel and ammunition included,
at no cost to the Axis player. They must still be refitted
([maintenance](30-flight-and-maintenance.md#maintenance)); for the refit
roll by squadron, divide the bombers in each box into groups of 6 to 12 and
treat each group as a squadron.

::: spi 43.23 43.24 43.25

**Crete.** Each month, bombers based in Crete are taken up for four
Operations Stages by raids on the Suez Canal area, off the map: in those
four stages they fly no other missions. The raids are abstract: no effect
on the game and no losses. Bombers flying from Crete never get escort or
combat air patrol from aircraft in Africa; they fly unprotected.

**Italy and Sicily.** Bombers there may be covered by fighters based in
Africa, and may raid Malta (§44).

## Malta {#malta}

::: spi 44.0

Malta sat across the Axis convoy routes, and Commonwealth aircraft based
there struck at convoys and ports. The Axis answers by bombing the island,
in raids whose scale is set by charts standing for decisions taken outside
Africa. Malta cannot be invaded in this game. Aircraft on missions over
Malta are always given a particular hex.

::: spi-omit 44.1 44.2 — subsection headings; the rules under them are restated below

### The Maltese air bases

::: spi 44.11 44.12

The Malta inset on map A is not at the map's scale or in its true place;
its box lists how far it is by air to key places in Africa. Of what it shows,
only the air facilities and the port of Valletta matter. The air facilities
are printed on the map, permanent and fixed: none may be added, and bombing
can reduce them to nothing but never remove them.

::: spi 44.13 44.5

Each scenario gives their starting capacity. Once per Game-Turn, for each
Maltese facility, the Commonwealth may roll on the Maltese Air Facility
Construction Table for the number of levels repaired or built, up to the
facility's standard level, at no supply cost. The table is data:
[`data/tables/malta-construction.json`](https://github.com/basmith7/cna/blob/main/data/tables/malta-construction.json)
(1: none; 2–5: one level; 6: two).

::: spi 44.14 44.15

Malta needs no SGSUs. Each level of facility serves up to **18 aircraft**
of any type, so a six-level airfield takes 108; group them as squadrons for
convenience all the same. At the start of an Operations Stage, before any
mission, the Commonwealth may shift aircraft between Maltese facilities
without flying them, noting it on his sheets and telling the Axis nothing.

::: spi 44.16 44.17

Aircraft on Malta are fuelled and armed free every stage, but must be
refitted as usual. Commonwealth aircraft may transfer between Malta and
Africa if they have the range.

::: spi 44.18

**Malta's flak.** The Commonwealth may send AA replacement points to Malta,
at most **one a month**: a light AA point gives Malta **1** AA point, a
heavy one **4**, up to **48** AA points on the island. They are written on
the record by facility, not shown by counters; bombing losses are noted as
they happen. AA points move between Maltese facilities as aircraft do, but
never between Malta and the mainland.

### Axis raids on Malta

::: spi 44.21 44.22 44.23

Axis bombers in Italy and Sicily, and any Axis aircraft in Africa that can
reach, may raid Malta's air facilities to cut their ability to refit
aircraft. Besides, the Axis may call on Italian and German aircraft kept in
Italy and Sicily and otherwise outside the game, through four **Malta
availability levels**. Each level may be used for a set number of
Game-Turns in each scenario, never more; the Axis plans his raids around
them.

::: spi 44.24 44.25 44.26 44.27

Raids on Malta are flown in the strategic air planning stage, so once a
Game-Turn. The Axis picks a level, rolls two dice on the Axis Malta
Availability Table in that column and reads two percentages:

- **left of the stroke**: the share of each type of his in-play aircraft
  in Italy and Sicily that may fly the raid;
- **right of the stroke**: extra aircraft of each type from outside the
  game, as a percentage of that type's count in Italy and Sicily, fractions
  dropped.

Only then may he add aircraft from Africa: of each type, no more than the
tables gave him, and none of a type the tables gave none of. Each squadron
is sent against one Maltese airfield and the raid is fought normally, air
combat and flak included. Not raiding counts as using level I, which is
unlimited.

*Our example.* At level II the Axis rolls a 7: 25/50. With 8 Ju 87s and 16
CR 42s in play in Sicily, 2 Stukas and 4 Falcos may go, plus 4 and 8 from
outside the game: 6 Ju 87s and 12 CR 42s. From Africa he may add at most 6
more Ju 87s and 12 more CR 42s, and no other types.

::: spi 44.28

**Losses.** Aircraft from outside the game are never lost. Work out the
share of the raid that is *in play* (from Africa, plus the in-play share
from Italy and Sicily) and apply that share to the raid's total losses,
rounding up; the result is taken from the in-play aircraft. Aborts are
noted but are not losses. Of a raid of 36 bombers, 12 in play, that loses
9, the in-play aircraft lose 3.

::: spi 44.29

The Axis may call off the raid after rolling, but the level counts as used
for that Game-Turn, and no map-based aircraft fly against Malta.

::: spi 44.3

**No invasion.** Germany planned to take Malta and even set a date, but the
air units meant for it went to Rommel's drive on Tobruk and never came back;
after Crete's losses, and with little airborne help to expect from Italy,
the attempt would probably never have been made. The Axis may not invade
Malta.

### The Malta charts

::: spi 44.4 44.41 44.42

Both charts are data.
[`data/tables/axis-malta-commitment.json`](https://github.com/basmith7/cna/blob/main/data/tables/axis-malta-commitment.json)
(44.41) gives each scenario's limits per level: in the campaign games, level
I unlimited, II for 25 Game-Turns, III and IV for 12 each; no raids at all
in Graziani's Offensive beyond level I, and none in The Last Chance, which
has no Malta.
[`data/tables/axis-malta-availability.json`](https://github.com/basmith7/cna/blob/main/data/tables/axis-malta-availability.json)
(44.42) gives the two percentages for each roll and level, or none.

## Engine notes

- The base percentages count aircraft of the three types across all German
  bombers, checked whenever bombers are based or transferred; the 50 % in
  Crete is part of the 75 %.
- Mediterranean boxes are off-map air facilities that cannot be bombed
  ([air facilities](20-air-facilities.md)).
- A Malta raid: roll `axis-malta-availability.json` for the chosen level;
  count uses per level against `axis-malta-commitment.json` for the
  scenario (a cancelled raid still counts).
