---
title: Organisation
status: provisional
---

# Organisation

This file defines how units belong to formations — assignment and
attachment, their limits and costs — and how the armies grow and shrink:
rebuilding, battle groups, ad hoc anti-tank, reinforcements, replacement
points, upgrades and Commonwealth withdrawals. The reserve state (SPI §18)
is in [Stacking & ZOC](50-stacking-and-zoc.md#reserve); morale training
(SPI 17.3) in [Units & state](10-units-and-state.md#training); the CP costs
themselves in [Capability points](30-capability-points.md).

::: spi-omit 19.0 19.1 19.7 19.9 20.0 20.1 20.4 20.5 20.6 20.7 — section headings and design commentary; the rules under them are restated below

## Assigned and attached

::: spi 19.11 19.12 19.13 19.14

Every counter is **independent** or belongs to a **parent formation** in one
or both of two ways:

- **Assigned**: the unit is part of the parent's organisation on paper —
  the O/A Chart lists where each unit starts. Assignment does not depend on
  location.
- **Attached**: the unit is physically merged into the parent's counter,
  in the same hex, and acts as part of it.

A unit may be assigned to one parent and attached to a different one at the
same moment (a battalion detached from its own division and taken in by
another), but never assigned to two, or attached to two. A parent can itself
be assigned or attached to a larger parent, and what hangs off the smaller
parent may block that larger attachment ([below](#attachment-limits)).
Companies, battalions and brigades can be assigned or attached; a divisional
HQ is always independent.

::: errata E-011 — 19.14 example corrected: the KRRC ends attached to the New Zealand division and assigned to 7th Armoured

## Assignment

::: spi 19.2 19.21 19.22 19.23 19.24 19.25 19.26 19.27 19.28

Each parent has a ceiling on the units of each type it may have assigned,
given on the Formation Organisation Chart (SPI 19.3, one table per
nationality); units with singular structures are limited by their O/A notes
instead. Units arrive assigned, and assignment is normally permanent; changes
happen in the reorganisation segment and are written on the parent's TOE log.
An assigned unit occupies its slot in the parent's structure wherever it is.

- A parent with a free slot may take an **independent** unit into it — and
  only an independent unit; a unit assigned elsewhere cannot be reassigned
  (Commonwealth battalions excepted, below). The unit must be *attached* to
  the parent at the time.
- If a parent is eliminated, its surviving assigned units become
  independent. If an assigned unit is eliminated, its slot is free.
- Some units carry an asterisk: their parent never reached Africa, and they
  may not be reassigned except under the Commonwealth shuffle rule.
- **Historical shifts.** Where the O/A Chart notes a historical change of
  parent (a regiment moving from one panzer division to another), the owner
  may make it in the month named, or never.
- **Commonwealth armour.** The assignment limits of Commonwealth armoured
  divisions and brigades change three times; the owner may fill slots that
  open and must unassign units that a tighter limit excludes.
- **Commonwealth battalion shuffle.** The Commonwealth player may swap
  assigned battalions between brigades (or with the unassigned pool) at
  will; the incoming battalion becomes assigned to its new brigade. This is
  the only exception to the rules above, and it is a swap — a battalion may
  not simply be cut loose as independent.

::: spi-omit 19.3 19.31 19.32 19.33 — the Formation Organisation Charts (Allied, Italian, German) are on the player chart sets; to `data/tables/formation-organisation.json` when captured

::: spi 19.5

The Maximum Attachment Chart is data: `data/tables/max-attachments.json` —
per nation and parent type, how many battalion-equivalents may be attached
and of what kinds. Commonwealth divisions take two (three for an armoured
division from turn 68), at most one of them infantry and, before turn 68,
never a tank battalion; German divisions take a brigade plus a unit or up to
four units, never tanks; Italian battalions take nothing. Any division or
brigade may add two small company-equivalents for free.

## Attachment and detachment {#attachment-limits}

::: spi 19.4 19.41 19.42 19.43 19.44 19.45 19.46 19.47

An assigned unit may attach to or detach from its own parent freely. Beyond
its assigned structure a parent may also carry *attached-only* units, up to
the numbers and types on the Maximum Attachment Chart (SPI 19.5), which
applies to every unit of a given size and type whether or not its
organisation is standard. These extra attachments ride on top of the
assigned slots — even slots whose assigned unit is currently elsewhere.

| Move | When | CP (each of unit and parent) |
|---|---|---|
| attach an assigned unit | any time, same hex | 1 |
| attach a non-assigned unit | reorganisation segment only, same hex | 2 |
| detach an assigned unit | any time | 1 |
| detach a non-assigned unit | reorganisation or movement segment | 1 |

Attaching removes the unit's counter from the map; the parent's stacking
value is unchanged unless it was a shell
([stacking](50-stacking-and-zoc.md#unit-equivalents)). Moving into the
parent's hex must happen in an earlier movement segment under the usual
stacking limits. A unit detached during a movement segment stops there, as
does its parent, unless the two go on together as a stack.

::: spi 4.25

An attached unit has no counter on the map: the parent's counter stands for
it and its log sheet records it. At the start of a scenario every unit that
is assigned to a parent and set up in the parent's hex begins **attached**,
and so is not placed, unless the scenario says otherwise.

- **Substitution.** A parent short of an assigned unit (never arrived, or
  reassigned) may attach an independent unit in its place, provided the
  substitute's own structure fits the slot: an infantry brigade with four
  battalions assigned cannot stand in for a three-battalion brigade.
- **Nesting.** A unit attached to a parent that is itself attached to a
  larger parent counts as attached to the larger one too, and may therefore
  not fit — unless it is a substitute under the previous rule.
- **Detach-and-pair.** Units detached from the same parent may attach to one
  another at no cost beyond the detachment itself.

## Rebuilding depleted units

::: spi 19.6 19.61 19.62 19.63 19.64 19.65 19.66 19.67 19.68

Losses are made good with [replacement points](#replacement-points),
absorbed in the reorganisation segment only, at **1 CP per two points**
absorbed (charged to the unit and its parent). No unit may ever exceed its
printed maximum TOE strength, though units that arrive below their paper
strength may be built up to it. Taking many points in one stage can push a
unit over its CPA into disorganisation, so refit in the rear.

- A unit reduced to **zero** by combat or attrition is gone and cannot be
  rebuilt (breakdown losses are different). Exception: a unit whose maximum
  is one or two TOE points may be recreated; if its assigned slot has been
  filled meanwhile, it returns independent (§32 addition to 19.62).
- The parent's **HQ is its cadre**: while the HQ lives, the formation can be
  rebuilt or re-assigned, and an HQ that has lost every assigned battalion
  may take new ones up to its O/A ceiling. A destroyed HQ can be revived
  only if at least half its assigned units survive and are not attached
  elsewhere, for **2 infantry replacement points**; otherwise it is gone.
- A slot emptied by elimination or reassignment may be filled by a
  previously unassigned battalion, which is then assigned there even if it
  could not normally have been.
- Which points rebuild what: infantry points rebuild infantry-type units,
  HQs and engineers; artillery accepts any gun type; any tank type fits any
  tank battalion; heavy-weapons points cost an infantry *and* a gun point;
  recce and armoured-car units use recce points, or light tanks
  ([upgrades](#upgrading-recce)).

## Axis battle groups

::: spi 19.71 19.72 19.73

In an organisation phase (only) the Axis player may form **battle groups**
from any units sharing a hex, within stacking. German groups use the
Kampfgruppe HQ counters (historical names, any composition): up to **four**
battalion-sized units, of which at most one tank and two infantry, plus up
to two companies. Italian groups have no counters and are named from the
Italian O/A sheet: at most **three** battalions (at most two infantry, one
armour) plus one company, and never more than **two** in being at once.

## Axis ad hoc anti-tank batteries

::: spi 19.8 19.81 19.82 19.83 19.84 19.85 19.86 19.87

The Axis player may turn anti-tank **gun replacement points** into new
batteries carried by a brigade-level HQ (Kampfgruppen included) that bears an
infantry symbol: up to **6** TOE points of one gun type per HQ, at least 3 in
the first allocation, assigned as if the HQ were an anti-tank unit and trained
at the gun rate. He may do so only while every anti-tank unit he has on the
map and in the Tripoli–Tunisia boxes is at **67 %** or more of maximum; captured
guns are never used. If the battery is wiped out he may start again with any
type. The HQ's CPA becomes that of the guns; its stacking value stays **0**.

## Commonwealth infantry anti-tank

::: spi 19.91 19.92 19.93 19.94 19.95 19.96 19.97 19.98

From **turn 75 (1 April 1942)** the Commonwealth player may give anti-tank
guns to infantry battalions of CPA 10 (or 10+) with close-assault ratings
1/2 or 2/2, so that the battalion carries a second weapon system. A
historically motorised battalion (10+) holds **2** anti-tank points, a foot
battalion (10) holds **1**. The points come in as ordinary gun replacement
points, trained at the gun rate, and only while every anti-tank regiment
assigned to the battalion's parents is at full strength. Once absorbed they
move at the infantry's CPA (10 on foot, 20 or 25 in trucks) and are ignored
in shell calculations.

## Reinforcements

::: spi 20.11 20.12 20.13 20.14 20.15

**Reinforcements** are whole units on the Reinforcement Track. They appear
when the stated stage's naval convoy arrival phase opens, pay no CP
to land or for their first hex, may move in that same stage and are
thereafter ordinary units.

- Commonwealth units arrive at **Cairo** unless the track says otherwise;
  Layforce (turn 19) and the Tiger convoy of tank replacement points (turn
  32) come in at Alexandria; returning withdrawn units choose either, within
  stacking.
- Axis units arrive at **Tripoli**. While no Commonwealth land combat unit
  is at or west of Mersa Matruh, one battalion-equivalent (or two
  company-equivalents) plus up to ten truck or motorisation points arriving
  with it may be diverted to **Benghazi**, provided stacking allows and
  Benghazi's efficiency is level three or better; the diversion consumes
  Benghazi port capacity for the stage (SPI 55.1).

::: spi 4.42

Reading an arrival goes chart by chart. The Reinforcement Track names the
units due in the current stage; each is looked up on its parent formation's
**O/A sheet**, which lists every unit of the parent with a characteristics
code; the code is looked up on the nationality's **Unit Characteristics
Chart** for ratings, CPA and strength; and the result is written onto a TOE
log for the parent. A parent brings every unit its O/A sheet lists except
those with a later arrival date of their own or marked excluded on the
track. Detachments that arrive alone are listed under their parent so that
the same sheet serves.

## Replacement points {#replacement-points}

::: spi 20.2 20.21 20.22 20.23 20.24

**Replacement points** are TOE strength points of a class — infantry, gun,
tank, recce — that arrive in a naval convoy arrival phase: on the stage the
Reinforcement Track names (Commonwealth track entries are by exact type, "27
points of Matildas"), from the Axis Replacement Pool on a stage the Axis
player planned **two turns** ahead, or from Commonwealth Production on a
stage planned ahead under [production](#commonwealth-production). Pool and
production points are by type, with per-turn maxima per type. Replacement die
rolls may be kept secret, even from team-mates.

::: spi 20.3

The Replacement Point Conversion Chart is data: `data/tables/replacement-conversion.json`
— what one TOE point of each unit type costs in replacement points. Most
infantry costs one infantry point; HQs, paratroops, Bersaglieri, machine-gun,
engineer battalions and light reconnaissance cost two, commandos three, and
heavy weapons one infantry plus one gun. Armour rebuilds point for point;
armoured cars take two armoured-recce points, or a light tank when upgrading;
the construction battalions cost nothing and return six stages after being
wiped out. The chart's SGSU line is void (E-012).

::: errata E-012 — 20.3: ignore the chart's SGSU entry

### Handling replacement points

::: spi 20.41 20.42 20.43 20.44 20.45 20.46 20.47 20.48 20.49

On arrival every point is earmarked for a specific unit (re-earmarked at
once if that unit dies or is withdrawn), and it is absorbed only in the
**reorganisation segment**, in the unit's hex — the points go to the unit,
even into an enemy ZOC. Absorption costs CP as an *assigned* attachment
([CP costs](30-capability-points.md)); once absorbed the points take on the
unit's cohesion, breakdown state and so on.

Until then a replacement counter is a unit with four differences: it may not
voluntarily enter an enemy ZOC unless a friendly unit is already there; it
fights only to defend against close assault; its basic morale is **−3**; and
it may never exceed its CPA (that of its destination unit) — if it does, for
any reason, it is at cohesion **−26**. Five points make a battalion for every
purpose, stacking included. Points need stores, and fuel if vehicles, to
move; ammunition is allowed but pointless. Points heading for the front are
truck convoys and move in the truck convoy phase; infantry is usually trucked,
while tank, gun and recce points can drive themselves or, for the
Commonwealth, go by rail. Track them on the availability and assignment
sheets.

**Training.** Every point trains first — Axis points in Tripoli or a major
city, Commonwealth points at the sites in SPI 17.32 — under the training
rules of [Units & state](10-units-and-state.md#training), for the stages in
`data/tables/replacement-training.json` (the arrival stage counts):

| Class | Stages |
|---|---|
| gun | 1 (uncrating, really) |
| infantry | 3 |
| tank, armoured car, recce | 6 |

This is separate from Commonwealth morale training.

## Upgrading recce and armoured cars {#upgrading-recce}

::: spi 20.51 20.52 20.53 20.54 20.55

Armoured recce and armoured car units (Italian code *ww*, German *go*,
Commonwealth *hh*–*tt*) that arrive with anti-armour rating **0** may be
upgraded, except Commonwealth recce assigned to infantry divisions (18th
Brigade of 7th Australian counts as a division). Add one TOE point of the
right tanks — Stuarts for the Commonwealth, Pz II for Germans, M/11, L6/40 or
recce points for Italians — either to replace a lost point or, at full
strength, without raising the total. Each upgraded point has anti-armour
**1** and offensive close assault **3**. Nothing upgrades before **turn
1/39**.

## Axis planned replacements

::: spi 20.61 20.62 20.63 20.64 20.65

The **Axis Replacement Pool** lists the campaign's whole stock of each point
type (scenarios give their own), with a per-turn limit per type; nothing
beyond it ever comes. Any mix may arrive in one stage, but every point counts
against that turn's shipping tonnage at the rate in the pool table — ten
Italian infantry points need 300 tons — and replacement points take shipping
priority over supplies, so the Axis logistics commander must plan against an
unknown future tonnage and Commonwealth air raids. Arrivals are planned during
the convoy arrival phase of the last stage of the turn **two turns**
before (planned in June III, arriving any stage of July I) and scheduled at
least two weeks ahead of the convoy that carries them (§32 addendum to
20.63). Points cannot be absorbed by a unit with no room for them.

::: errata E-013 — 20.62 example: 300 tons, not 350

::: spi-omit 20.66 20.67 — the Axis Replacement Pool Table and Type Limitations Chart are on the chart sheet; to `data/tables/axis-replacement-pool.json` when captured (errata: its next-to-last note refers to the M 11/39)

::: errata E-014 — 20.66 note: M 11/39, not 13/39

## Commonwealth production {#commonwealth-production}

::: spi 20.71 20.72 20.73 20.74 20.75 20.76 20.77

Most Commonwealth units come by the Reinforcement Track; most replacements —
drafts and transport — come by the **Commonwealth Production Tables**. The
player plans **one month** ahead (unless the scenario says otherwise) in the
first naval convoy schedule phase, reading the production table for the
month in which the points are to *arrive*. Production works like the Axis
pool except that infantry and truck points are rolled for per turn by date.
A turn's points, all types together, are spread as evenly as possible across
its stages (ten trucks one stage, ten infantry the next). Track replacements
arrive on top of production; there is no shipping to worry about. Planned
points land in any Cairo or Alexandria hex and then train.

::: errata E-015 — 20.72: plan one month ahead, not two, and read the table for the arrival month

**Infantry upgrade.** From turn **July 1/I 1942** (so planned from June) the
Commonwealth player may raise a 1/2 infantry battalion to **2/2** by
spending one *untrained* infantry replacement point per TOE point in it, all
points at once; the strength does not rise. Thereafter that unit's
replacements cost one infantry point per TOE point rather than two.

::: spi 20.78

The Commonwealth Production System is data: `data/tables/cw-production.json`
— the truck table (one die per truck type, more from turn 31), the infantry
table (two dice against the game-turn band of the turn planned for) and the
production chart (per type: lifetime total, cap per turn or month or
fortnight, first and last turn it may be planned). Trucks and infantry
arrive four turns after the roll; no more than a quarter of a turn's trucks
may land at Alexandria; the Tiger convoy of turn 32 is on top of it all.

## Commonwealth withdrawals

::: spi 20.8 20.81 20.82 20.83 20.84 20.85

The Reinforcement Schedule also **withdraws** Commonwealth units, named or
by type ("any two armoured brigades"). A unit picked by type must be at
**75 %** or more of maximum strength — or, failing any such unit, the
strongest of its type. A unit under 75 % must be brought up with replacement
points before the date, or a like unit at 75 % substituted. The unit must
reach Cairo or Alexandria by the stated turn or stage, where it is simply
removed; one not there, or not at strength, in time is eliminated instead and
never returns, even where the schedule would later bring it back.

::: errata E-016 — 20.83: the reference to 20.75 is void; the strength requirement is 20.82's

::: spi 20.9

The Commonwealth player may also withdraw small forces **voluntarily** at any
time for victory points, and is penalised for bringing them back; the
schedule is in the Campaign Game victory conditions.

---

*Drawn on: SPI §19, §20, the §32 addenda to 19.62 and 20.63, and the September 1979 errata (E-011–E-016).*
