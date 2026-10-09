---
title: Air Game — air combat and flak
status: provisional
---

# Air combat and flak

Aircraft on a mission meet two kinds of opposition in the target hex:
enemy aircraft (air-to-air combat, §45) and then fire from the ground
(anti-aircraft fire, or flak, §46).

## Air-to-air combat {#air-to-air}

::: spi 45.0

Air fighting is resolved operationally, aircraft against aircraft in pairs,
inside the target hex, before flak and before any mission takes effect. Only
fighters with a TacAir rating not in parentheses may start it, and fighters
on offensive CAP must. Each pairing compares the two aircraft's TacAir,
raised by the pilot's rating (fighters) or a formation bonus (bombers), and
shifted for the difference in maneuver.

### Sequence

1. Scrambles and interceptions bring their fighters into the hex.
2. Each player says whether he starts combat; offensive CAP must.
3. The **attacker** is decided (45.16).
4. The defender lays out the aircraft being attacked with spare counters
   (34.75); the attacker allocates his fighters against them.
5. Fighters fight fighters (and screens) first; then surviving fighters may
   go for the bombers and transports (unescorted ones at once).
6. Survivors take flak, then complete their missions.

**Ratings.** Each fighter adds its pilot's rating to its TacAir. Bombers
in formation add **1** with 6 to 17 bombers on the mission, **2** with 18 or
more; dive bombers get no bonus. The **TacAir differential** of each
aircraft in a pairing is its adjusted TacAir minus its opponent's.

**Maneuver.** Subtract the lower maneuver rating from the higher and read
the Maneuver Adjustment Chart; add the adjustment to the more maneuverable
aircraft's differential and take it from the other's. Equal ratings, no
adjustment. Two aircraft at +2 and −2 whose maneuver ratings differ by 9,
the −2 aircraft being the nimbler, end at −1 and +1.

**Who fires first.** Between fighters, the one with the **minus**
differential fires first; at 0, the better pilot, and on equal pilots the
attacker. A lone fighter attacked by several fires before them. A
non-fighter always fires before the fighter attacking it.

**Firing.** The firer rolls two dice in order (a 3 then a 5 is 35) on the
TacAir Kill Table under his final differential: at or under the kill
number, the target is shot down. If it survives, it fires back the same
way; if both miss, the pairing is over. A non-fighter fires separately at
every fighter matched against it; a fighter fires at one aircraft only,
however many attack it.

**Laying out the fight.** The defender numbers his aircraft and names each
type (and, for identical aircraft from different squadrons, the squadron),
but not its pilot's rating. The attacker then matches his aircraft to
them, covering every defender at least once, in any pattern. Where several
attack one defender who can answer only one of them, the attacker gives the
order of their attacks. SPI's worked example shows the attacker throwing
his weakest fighter at the defender's best and doubling up on the weakest
defenders.

::: spi-omit 45.1 45.2 45.3 — subsection headings; the rules under them are restated below

### When it happens

::: spi 45.11 45.12 45.13

Only aircraft in the same hex fight each other, air ZOC or not: fighters
with an air ZOC move into the adjacent hex to engage, and fighters on
offensive CAP over an empty hex must do so to fight. Everything in the hex
can be attacked, but only fighters, and fighter-bombers on a fighter
mission, can start a fight. Air fighting comes before flak and before any
mission is completed, after scrambles and interceptions.

::: spi 45.14

Offensive CAP must attack every enemy aircraft in its hex, so it always
starts combat. Without offensive CAP, both players secretly choose whether
to fight and reveal together; one yes is enough. If both say no, both send
their aircraft home and every mission in the hex is cancelled: a free
abort. A player may still try an ordinary abort against an opponent who
wants to fight (39.3).

::: spi 45.15

Once combat is joined, aircraft on any mission other than CAP are
**screened** if they have defensive CAP as escort; without escort they are
not. Screened aircraft are set aside while the CAP fighters fight.

::: spi 45.16 45.17

The side with more fighters (by count) is the **attacker**; on equal
numbers, the player with the initiative that Game-Turn (§7). Aborts are
tried now (39.3). An aircraft out of ammunition (bombs apart) cannot fire,
but its ratings still count when it is fired on.

::: spi 45.18 45.19

The fighter-against-fighter round comes first; then screened aircraft may
be attacked (below). An aircraft allocated to a pairing stays in it, even if
its opponent falls before it can fire.

### Fighter against fighter

::: spi 45.21 45.22

Fighters are those with TacAir not in parentheses. The defender lays out
his fighters and names their types, keeping pilot ratings secret.

::: spi 45.23 45.24

The attacker must put at least one fighter on each defending fighter; once
all are covered he may add as many more to any of them as he likes. A
defending fighter fires at one of its attackers; all its attackers may fire
at it. Every pairing is resolved alone (strengths are never added) and in
any order.

::: spi 45.25

Some fighters may then fire again, at the bombers and other screened
aircraft.

### Fighter against screened aircraft

::: spi 45.31 45.32

After the fighter round, surviving fighters *may* attack screened enemy
aircraft, even on offensive CAP, which must attack only if there were no
enemy fighters in the hex at all. Only the **excess** may: the fighters
the player has left over the enemy's surviving fighters. With 15 fighters
left against 6 escorts, 9 may go for the bombers.

::: spi 45.33 45.34 45.35

The owner of the screened aircraft is the defender and lays them out; the
attacker may now spread his fighters as he likes, all on one bomber or
across several. Pairings are fought as between fighters, except that a
screened aircraft fires at **every** fighter attacking it, not just one (a
dive bomber at one only). Screened aircraft that survive go on to the flak.

::: spi 45.36

**Formation bonus**: +1 TacAir to each bomber with 6–17 bombers on the
mission, +2 with 18 or more.

### Tables

::: spi 45.4 45.5

The Maneuver Adjustment Chart and the TacAir Kill Table are data:
[`data/tables/maneuver-adjustment.json`](https://github.com/basmith7/cna/blob/main/data/tables/maneuver-adjustment.json)
(maneuver difference 0: no adjustment; 1–3: 1; 4–7: 2; 8–14: 3; 15–20: 4;
21 or more: 5) and
[`data/tables/tacair-kill.json`](https://github.com/basmith7/cna/blob/main/data/tables/tacair-kill.json)
(−13 or worse: no kill possible; then kill numbers from 11 at −5 to −12, up
to 56 at +12 or better).

### Recovering aircraft and pilots

::: spi 45.6 45.61

Fighters shot down, and aircraft destroyed on the ground by strafing
(40.63), may be recovered on the Pilot and Plane Recovery Table:
[`data/tables/pilot-plane-recovery.json`](https://github.com/basmith7/cna/blob/main/data/tables/pilot-plane-recovery.json).

::: spi 45.62

**Strafed aircraft**: one die each; on **1–2** the aircraft can be repaired,
on 3–6 it is lost for good. Repair costs **1 stores and 1 fuel** per
aircraft, spent only when the roll succeeds and needed for the repair to
happen. A repaired aircraft flies again one full Game-Turn later.

::: spi 45.63 45.64 45.66

**Fighters shot down** (by aircraft or flak): one die each, which settles
pilot and aircraft together. On **1** the fighter limped home and the pilot
lives; on **2** the pilot baled out and lives but the fighter is lost; on
3–6 both are lost. A fighter that limps home is repaired by paying the
1 stores and 1 fuel, no roll needed. A surviving pilot, wherever he came
down, flies again three Operations Stages later.

::: spi 45.65

Fighters recovered this way do not count as kills for making aces (40.18).

### Extended range

::: spi 45.7

An aircraft with two maneuver ratings uses the lower on a mission at
extended range, unless it drops its extra tank, which gives it the higher
rating in the fight but limits its return to its normal range; with no
friendly facility in reach it must crash-land afterwards (37.23), if it
survives. A fighter-bomber attacked on a bombing mission may jettison its
bombs, to no effect on the target, to fight at its better maneuver rating.

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

- Air-to-air: final differential = (own TacAir + pilot or formation) −
  (enemy's) ± maneuver adjustment; look up `kill_max` in `tacair-kill.json`.
- The first worked example in 45.36 reads the kill table wrongly at +2
  (11–22 is the +3 entry); the table stands.

- AA points are never divided by ten; sum the points chosen to fire at one
  group and use that column.
- Keep day and night separate throughout, for target groups and for the
  density count.
