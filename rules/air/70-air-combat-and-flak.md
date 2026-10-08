---
title: Air Game — air combat and flak
status: provisional
---

# Air combat and flak

Aircraft on a mission meet two kinds of opposition in the target hex:
enemy aircraft (air-to-air combat, §45, to come in this file) and then
fire from the ground (anti-aircraft fire, or flak, below).

## Anti-aircraft fire {#flak}

::: spi 46.0

Every aircraft flying a mission in a hex is fired on by the enemy's
anti-aircraft strength in that hex, and its losses are taken before the
mission has any effect. Flak comes in **AA points**: a unit's AA rating
times its TOE strength points, with **no division by ten**, unlike every
other combat strength ([actual strength](../60-combat.md#actual-strength)).
The ratings are on the characteristics charts (`anti_air` in
`data/tables/unit-characteristics.json` and
`data/tables/weapon-systems.json`); air facilities add their own built-in
point ([air facilities](20-air-facilities.md)). Firing uses ammunition.

### Procedure

1. Flak is fired only after all air-to-air combat and all flak-suppression
   missions in the hex are over.
2. The player whose aircraft are over the hex sorts them into **target
   groups** (below) and announces each group's size and aircraft types, but
   not its mission.
3. The firing player takes the groups one at a time, in any order, choosing
   which AA points (units and facilities) fire at each. Each attack is
   finished (losses, aborts and ammunition) before the next.
4. **Fighter-type groups:** roll two dice read in order (11 to 66) and find
   the result in the fighter section of the Anti-Aircraft Combat Results
   Table, in the column of the AA points firing; it gives the number of
   aircraft destroyed.
5. **Other groups:** first shift the column in the firing player's favour
   if the number of enemy aircraft other than fighters over the hex calls
   for it (the Flak Adjustment Chart; night missions count separately). Then roll two dice twice in that column: once on the
   *destroyed* rows, once on the *aborted* rows. Losses are taken first,
   then aborts.
6. Which aircraft of a group are hit is chosen at random by any fair method
   both players accept. *Our example:* number the aircraft in the group
   from 1 and draw numbered slips from a cup.

### Units that fire

::: spi 46.1 46.11 46.15 46.16

Any unit with an AA rating may fire, within the limits below. Most are AA
(flak) units, with the AA symbol on the counter; a unit with that symbol is
a **pure flak** unit. Many others carry an AA rating too: HQs, artillery,
heavy weapons, and some tanks and reconnaissance units, whose AA is per TOE
strength point (four points of a tank with AA rating 1 give 4 AA points).
Tanks may fire their AA only at fighters strafing their hex and at dive
bombers.

::: spi 46.12 46.13 46.14

Flak units are artillery for every other purpose: they carry their own
transport unless stated otherwise (those without it are towed, one AA
point per medium or heavy truck point), and they draw supply as artillery
does. A flak unit whose defensive close-assault rating is in parentheses
defends against assault only when alone in its hex; the German 88 mm and
Italian 90 mm units have a real defensive rating and are attacked as
artillery with assault ratings.

::: spi 46.17

**Stacking.** Pure flak units cost nothing to stack in a major city. One
may also stack free in a landing-strip hex, and three in an airfield hex.

### Restrictions

::: spi 46.2 46.21 46.22 46.23 46.24 46.27 46.28

- Flak reaches only aircraft on missions in the **same hex**.
- Infantry, reconnaissance and tank units fire only at the fighter-type
  group, strafers and dive bombers.
- Fighters on flak-suppression missions and aircraft on naval convoy
  reconnaissance are never fired on.
- A player may fire at as many target groups as he likes.
- Replacement points have no AA until absorbed by a unit.

### Target groups

::: spi 46.25 46.26

The aircraft over a hex form these groups, each attacked separately:

| Group | Aircraft |
|---|---|
| a | non-fighter missions by day, one group per mission |
| b | non-fighter missions by night, one group per mission |
| c | fighters on combat air patrol, scramble or interception by day |
| d | the same by night |
| e | fighters strafing or dive-bombing |

Groups c, d and e use the fighter section of the table; a and b the other
section, with the density shift.

### The tables

::: spi 46.3 46.4

The Anti-Aircraft Combat Results Table and the Flak Adjustment Chart are
data:
[`data/tables/anti-aircraft-results.json`](https://github.com/basmith7/cna/blob/main/data/tables/anti-aircraft-results.json).
Ten columns of flak points, from 1–4 up to 37 or more; in each, the two-dice
ranges for each number of aircraft destroyed (and, for other missions,
aborted). The Flak Adjustment Chart shifts one column per band of 24
non-fighter aircraft over the hex, up to three; the notes under the results
table count differently.

::: ruling R-113 — which density shift applies to flak

## Engine notes

- AA points are never divided by ten; sum the points chosen to fire at one
  group and use that column.
- Keep day and night separate throughout, for target groups and for the
  density count.
