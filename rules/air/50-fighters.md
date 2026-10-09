---
title: Air Game — fighters
status: provisional
---

# Fighters

Fighters fly **combat air patrol** (CAP), **scramble** from the ground to
meet raiders, **strafe** targets on the ground and **suppress flak**. Those
that carry bombs, fighter-bombers above all, may also bomb (§41). Every
fighter has a **pilot**, whose rating counts in air-to-air combat.

::: spi 40.0

A fighter flies one mission per Operations Stage (so up to three a
Game-Turn) or one in the strategic phase, combined missions aside
([missions](40-missions.md#combined-missions)). The player gives each
fighter or squadron a mission and a hex; only when the aircraft are over the
hex does he pick the particular target of the kind chosen: which enemy
aircraft an offensive CAP attacks, or, for a strafing of first-line trucks,
which formation's trucks, once air-to-air combat and flak are over.

::: spi-omit 40.1 40.2 40.3 40.5 40.6 40.7 40.9 — subsection headings; the rules under them are restated below

## Pilots

::: spi 40.11 40.12 40.16

Pilots have no counters: they arrive as ratings (34.83) and the player
writes each onto a squadron's list. A pilot is ready for his squadron from the
turn of his arrival, starting with its first Operations Stage, and is trained on its aircraft type.
Within his squadron he may fly any aircraft (subject to training, below). An
aircraft flown without an assigned pilot has a **zero-rated** pilot, of whom
there are always enough.

::: spi 40.13 40.14

A pilot may move to another squadron at any time by moving his name between
lists; he does not fly in the stage or phase he moves. If the new squadron
flies a type he was not trained on, he needs a full Game-Turn (three
Operations Stages) of training before he flies: a pilot moving from
Tomahawks to Kittyhawks sits out three stages.

::: spi 40.15

A pilot is rated **1 to 4**, as the Pilot Arrival Tables give them, or
**6**, a rating held only by Hans-Joachim Marseille; there are no 5s
(except as earned under the optional aces rule below). In
air-to-air combat, and only there, the pilot's rating is added to the
aircraft's TacAir: a rating-3 pilot in an aircraft of TacAir 8 fights at 11.

::: ruling R-115 — no rating-5 pilots

::: spi 40.17

A pilot shot down may have baled out and be recovered (45.65). A recovered
pilot goes back to his own squadron and sits out three Operations Stages
before flying again.

::: spi 40.18

*Optional, campaign game only:* **make your own aces.** Every pilot starts
at zero and no pilot reinforcements arrive; each **five kills** (enemy
aircraft destroyed air to air) raise a pilot's rating by one, without limit.
Not for the shorter scenarios.

## Combat air patrol

::: spi 40.21 40.22

Any aircraft with **F** capability may fly CAP; write CAP, the hex and
**O** (offensive) or **D** (defensive) on the squadron sheet. Offensive CAP
goes to a hex to shoot down enemy aircraft. Defensive CAP escorts and
screens friendly bombers or transports, or guards a place on the ground. The
line between them is not always sharp.

::: spi 40.23

**Air ZOC.** Three or more fighters on offensive CAP over a hex also patrol
the six hexes around it, and may engage enemy aircraft entering any of the
seven.

::: spi 40.24

CAP may be flown over any hex within range, with these limits on convoys:
no aircraft based in Africa (on the map) flies CAP of any kind for or
against Axis naval convoys; Commonwealth aircraft on Malta may fly CAP only
against Axis convoys; the Axis may cover its convoys with CAP from bases in
Italy, Sicily and Crete. An aircraft on CAP flies no other mission that stage.

::: spi 40.25 40.26

**Offensive or defensive.** Suppose Axis bombers raid Benghazi with
fighters as escort, and Commonwealth fighters wait on CAP over the port.
On **defensive** CAP the Commonwealth fighters have no air ZOC and do not
start the fighting themselves, but the raid must still get past them to
bomb; they may also decline combat and abort. On **offensive** CAP they have
an air ZOC, may start combat, and *must* attack enemy aircraft entering
their hex or air ZOC to fly a mission there (only those in one such hex need
be attacked), and they may not abort.

::: spi 40.27

**Interception.** Once all aircraft counters are on their target hexes, and
before numbers are revealed, the owner of an offensive CAP may demand an
enemy mission's path of flight. If it crosses his fighters' hex or
air ZOC he may intercept it there: air-to-air combat follows, and survivors
fly on to their mission. Offensive CAP may intercept one mission per
Operations Stage.

## Scramble

::: spi 40.3 40.31

Scrambling fighters wait on the ground, saving fuel and keeping options
open, and take off only when raiders come near. Only aircraft with **S**
capability may be given a scramble mission, written **SC** with no hex, and
only in the land support air phase.

::: spi 40.32 40.33

When every mission has been placed, as the mission deployment segment
closes,
each player secretly picks a target hex for any fighters on scramble he
chooses to send; the choices are revealed together. He need not scramble
them, but nothing else may scramble. The path may not cross a hex holding
other enemy fighters, except the target hex. For each squadron, roll one die
on the Scramble Table by its distance in hexes from base to target: at or
under the number, the squadron makes contact and fights as **offensive
CAP**; above it, the squadron has flown for nothing and must still be
refuelled and refitted.

::: spi 40.34 40.4

Each squadron rolls separately, even when several head for one target, and
a squadron is never split between hexes. The Scramble Table is data:
[`data/tables/scramble.json`](https://github.com/basmith7/cna/blob/main/data/tables/scramble.json)
(6 or less at up to 2 hexes, falling by one per two hexes to 1 or less at
11–15; no scramble beyond 15).

## Strafing

::: spi 40.51 40.52

Aircraft with strafing capability may strafe ground targets; most are
fighters. Strafing is a mission and excludes any other, except for aircraft
that may strafe and bomb together (39.2). A strafing mission names a hex and
a kind of target, for instance `STR/C2414/dump`, and runs like any mission
([missions](40-missions.md)).

::: spi 40.53

Each aircraft strafes one target in the hex, however many there are, in a
single attack: not a run against every truck of a convoy in turn. Aircraft
on one mission may share out targets of the chosen kind: a group sent
against infantry may hit two battalions of a brigade, each aircraft
attacking one of them.

::: spi 40.54 40.55

The targets are: infantry-type units; trucks moving in convoy; a unit's
attached first-line trucks; supply dumps; grounded aircraft; tanks (Hurricane IIDs
only); ports; and the water pipeline. Nothing may be strafed in a major
city hex.

### Resolving a strafing attack

::: spi 40.61

**Infantry.** Total the TacAir of the aircraft attacking one battalion or
company (pilot ratings do **not** count) and roll two dice on the Strafing
Table in that column. The result is TOE strength points lost; trucks
carrying them are lost too.

::: spi 40.62

**Trucks in convoy**, and first-line trucks (attack the parent unit and
name its attached trucks): the result is truck points lost. The defender
picks them, but spreads the losses as evenly as he can over what they carry
(water, fuel, replacement points and so on).

::: spi 40.63

**Grounded aircraft**: the result is a number of dice; roll them, and their
total is the aircraft destroyed on the ground. Strafed aircraft may be
recovered (45.6).

::: spi 40.64

**Supply dumps**: the result is tenths: 1 destroys 10 % of every kind of
supply in the dump, 2 destroys 20 %, and so on.

::: spi 40.65

**Tanks.** Only late in the campaign could aircraft pierce tank armour, and
only the Commonwealth's Hurricane IIDs, with their 40 mm guns, are given the
mission. Resolve as for grounded aircraft: the dice total is the *minimum*
armour protection points lost. Any unit that has an armour protection rating is
a legal target; a dummy tank unit strafed is removed.

::: spi 40.66

**Ports**: strafing only adds to a bombing raid on the port. Halve the
strafing TacAir (round down), add it to the bomb points delivered, and
resolve on the Air Bombardment Table (41.5).

::: spi 40.67

**Water pipeline**: a result of 2 or more destroys the pipeline in that hex.
SPI notes it is a poor use of fighters.

::: spi 40.8

The Strafing Table is data:
[`data/tables/strafing.json`](https://github.com/basmith7/cna/blob/main/data/tables/strafing.json):
ten TacAir columns (1–5 up to 46+), results 0 to 3, read on two dice in
order. Under it the chart prints column shifts the rules text does not:
**one right** against trucks in convoy or a supply dump; for infantry **one
left** in a fortification level 0 or 1 hex and **two left** at level 2; for
armour **one left** at level 2.

## Flak suppression

::: spi 40.71 40.72 40.73

Fighters may draw enemy flak away from the other aircraft. Flak suppression
is a mission flown after air-to-air combat and before flak fires. It
destroys nothing on either side; flak not suppressed may fire at any
aircraft over the hex, the suppressing fighters included.

::: spi 40.74 40.75 40.76

Every **three** fighters on flak suppression neutralise **one** AA point for
the rest of that Operations Stage. Light AA and ships' AA can be suppressed;
heavy AA never. The fighters spend ammunition, and so do
the AA points they neutralise, which are firing at them. AA units are
destroyed only by bombing (41.3).

Flak printed on the map or in an off-map box (Tripoli's, for instance) counts
as **heavy**, so fighters cannot suppress it.

::: ruling R-111 — printed map flak is heavy

::: spi 40.77

Ships may be strafed to suppress their flak, as an ordinary suppression run,
but strafing never damages a ship; only bombs and torpedoes do (41.34). A
combined mission (39.2) can suppress and bomb.

## Night fighters

::: spi 40.91 40.92

Night fighters (marked on the characteristics charts) are fighters in every
way, but may also scramble against a night bombing mission, adding **2** to
the scramble die. The Blenheim IVF, Bf 110 and Ju 88C lose **4** maneuver
by day.

::: spi 40.93 40.94

Offensive CAP has no air ZOC at night. CAP flown at night must be
designated so, and it does nothing for missions flown by day.

## Engine notes

- Pilot rating is added to TacAir in air-to-air combat only; strafing and
  bombing use the aircraft's TacAir alone.
- Strafing: sum TacAir per target, pick the column, apply the shifts in
  `strafing.json`, roll two dice in order, and read the result by target as
  its notes say.
