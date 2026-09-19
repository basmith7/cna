---
title: Overview
status: provisional
---

# Overview

This edition restates the **Land Game** of *The Campaign for North Africa*
(SPI, 1979) as definitions and procedures precise enough to build a
rules-enforcing engine from. It is written in our own words and organised
around the game's *systems* rather than SPI's section numbering. SPI's case
numbers are kept everywhere as citations so that paper players, the errata
and community discussions can be cross-referenced.

## How to read this edition

- The plain text of every section is the **current rule**: the 1979 rule
  with the September 1979 errata applied and our accepted rulings folded in.
- A tag such as **SPI 8.35, 8.36** above a block names the cases of the
  original that the block was derived from. "Show original" (when enabled)
  fetches the community transcription of those cases into your browser for
  comparison; it is never part of this site.
- Boxed annotations record *why* the current rule reads as it does:
  **errata** (what SPI corrected), **ruling** (an ambiguity we resolved,
  linking to the decision record), **note** (intent and advice, not
  binding), **variant** (a community change recorded but not adopted).
- Every rules file is `provisional` until an engine has been built against
  it and its rulings reopened.

New to the game? Build the illustrated primer with
`python3 tools/learn_page.py` and open `docs/learn/index.html`. It is not
published here because it contains crops of the original charts.

## Three games in one box

::: spi-ref 1.0 32.0

CNA is three interlocking games, each playable alone or combined:

| Game | SPI sections | Covers |
|---|---|---|
| **Land Game** | 1–32 | Units, movement, combat, organisation, engineering, weather. **This edition.** |
| Air Game | 33–46 | Aircraft, missions, airfields, anti-aircraft fire. |
| Logistics Game | 47–58 | Fuel, ammunition, water and stores; trucks, ports, convoys, rail. |

Played alone, the Land Game replaces the other two with abstractions from
§32: supply arrives as **Supply Units** that hold fuel and ammunition
points, and air power and naval convoys are simplified. Everything in this
edition assumes those abstractions; the full Air and Logistics Games will be
restated separately. A hex is roughly eight kilometres across.

## Time

::: spi-ref 5.1 7.1

| Unit | Real time | What happens |
|---|---|---|
| **Game-Turn** | about a week | Initiative is rolled and convoy and replacement planning is done, once per turn. |
| **Operations Stage** | 2–3 days; three per turn | Everything else — organisation, movement, combat, repair — once for each player. |

The Operations Stage is the unit of action. Each stage has an **A half**
and a **B half**. The side holding the Initiative for the turn chooses, at
the start of every stage, whether to be **Player A** (first) or **Player B**
(second). Within a half, the side whose turn it is is the **phasing
player**; the other side may still react, retreat and fire.

## The shape of a stage

::: spi-ref 5.2

SPI letters the phases A–L and skips I. Phases A–E occur once per stage;
Player A then does F–L in full, and Player B does F–L in full.

| Phase | Who | What |
|---|---|---|
| A · Initiative declaration | Initiative holder | Chooses to be A or B this stage. |
| B · Weather | Initiative holder | Rolls weather: normal, hot, sandstorm or rainstorm. |
| C · Organisation | Both | Attach and detach units; finish and start construction; finish and start training. |
| D · Arrivals | Both | Reinforcements, replacements and supplies appear at ports and entry hexes. |
| E · Commonwealth fleet | Commonwealth | Assigns and repairs ships. |
| F · Reserve designation | Phasing | Marks units as Reserve so they may move later regardless of distance to the enemy. |
| G · Movement and combat | Phasing (the other reacts) | The core cycle, below. May be repeated. |
| H · Truck convoys | Phasing | Moves unattached second- and third-line trucks, and prisoners. |
| J · Rail | Commonwealth only | Moves units and supplies by rail. |
| K · Repair | Phasing | Tows, then repairs, broken-down vehicles. |
| L · Patrol | Phasing | Reconnaissance, only if no assault was made this half. |

::: spi-ref 8.2 8.23 18.0

Phase G is a **cycle** of four segments — *move → check breakdown → resolve
combat → release reserves* — which the phasing player may run as many
times as they like (**continual movement**). Every repetition includes all
four segments. From the second cycle on, only units that ended the previous
cycle within two hexes of an enemy unit, plus units just released from
Reserve, may move again. This is where tempo comes from: a player keeps
pressing with the units in contact while the rest of the army waits.

Combat within a cycle is a fixed sequence of steps: guns and armour declare
a forward or back **position**; both sides plot, then fire, **barrages**;
the non-phasing side may **retreat before assault**; both sides secretly
assign strength to **anti-armour fire** or **close assault**; anti-armour
fire is resolved simultaneously; close assaults are resolved one at a time
in the order the phasing player chooses, who then reveals which of them
were only **probes**.

## The currency: Capability Points

::: spi-ref 6.11 6.14 6.21 6.22 6.26

Each unit carries a **Capability Point Allowance (CPA)**: the budget of
**Capability Points (CP)** it can spend across one Operations Stage. Moving a
hex, firing, being fired on, assaulting, defending, retreating, building,
training — everything costs CP. The allowance covers *both halves* of the
stage: what a unit spends reacting during the enemy's half is gone for its
own.

A unit may exceed its CPA, but each point over becomes a **Disorganisation
Point**, and Disorganisation Points lower the unit's **Cohesion Level**.
Cohesion feeds the morale checks in combat, and a badly disorganised unit
eventually cannot act at all. Cohesion recovers slowly, chiefly by doing
nothing for a stage. The whole game is a negotiation with this ledger:
push tired units now for tempo, or rest them and hand the enemy time.

## Units and strength

::: spi-ref 3.21 3.22 6.15

A **unit** is a counter standing for a battalion, regiment, brigade,
headquarters, artillery group, truck column or similar. Its strength is
counted in **TOE Strength Points** — think companies or gun batteries —
which are what combat removes and replacements restore. Each unit also
carries **ratings**: close-assault offence and defence, barrage, anti-armour,
armour protection, breakdown adjustment, and its CPA. Units belong to
**parent formations** (divisions, brigades) by **attachment**, which
governs whom they may stack and fight alongside and which headquarters
they draw on.

Units are grouped in two ways. **Type** — infantry, tank, reconnaissance,
anti-tank, anti-aircraft, artillery, engineer, and several support and
transport types — governs what a unit may do. **Class** — infantry, armour,
gun, truck — governs what happens to it when it is the target of a barrage
or an air attack.

## Movement

::: spi-ref 8.37 10.0 21.0

Units move hex by hex, paying the **Terrain Effects Chart** cost in CP for
each hex entered and each hexside crossed. Roads and tracks are cheap; open
desert and rough ground are dear; escarpments cost a great deal to climb and
are impassable to vehicles except at passes. Motorised units have large
allowances but risk **breakdown**: vehicles accumulate Breakdown Points by
the terrain they cross and roll against their rating after every movement
segment; a broken-down vehicle must be towed and repaired. Entering an enemy
**Zone of Control** stops movement and, as a rule, forces combat. The
non-phasing player may **react** with some units during the phasing
player's movement, paying CP from the same allowance.

## Combat

::: spi-ref 11.3 11.33 15.5 15.73

Combat strength is computed, not read off the counter. **Raw points** are
rating × TOE Strength Points committed; **Actual points** are raw ÷ 10,
rounded to the nearest whole number with halves rounding up (11.4 → 11,
11.5 → 12), and anything under five raw counts as nothing — with an exception for very small engagements, given in Combat. All contributions against one target are summed before dividing,
so a lone small unit contributes almost nothing and concentration is
enforced by arithmetic.

Every combat roll uses two dice of different sizes, read more than one way
from the same throw: as a two-digit number (11–66) for losses on the
tables, and as a sum for secondary results such as capture. Barrage,
anti-armour fire and close assault each have their own table. Close assault
is resolved on a **differential** (attacker Actual minus defender Actual),
shifted by columns for terrain, relative size, morale and raw superiority;
results are percentage losses of the TOE points committed, plus possible
engagement and prisoners.

## Resource loops

The systems connect through a few loops an engine has to model explicitly:

- **CP ↔ Cohesion.** Spending over the allowance lowers cohesion; low
  cohesion worsens combat; only rest restores it.
- **TOE ↔ Replacements and repair.** Combat and breakdown remove strength;
  replacement points, training and repair put it back, each costing time in
  the Organisation and Repair Phases.
- **Supply ↔ Operations.** Even abstracted, movement and fire draw fuel and
  ammunition from a Supply Unit within reach; a unit that cannot reach one
  stops.
- **Contact ↔ Tempo.** Continual movement lets units in contact act
  repeatedly, at a price in CP and cohesion; Reserve trades a segment of
  inactivity for freedom to move later.

## Roles

::: spi-ref 2.0

SPI describes the game for teams: a commander-in-chief, a front-line
commander, a rear-area commander, an air commander and a logistics
commander per side, each with their own log sheets. Roles divide the
paperwork; they never change what a side may do. This edition treats each
side as one decision-maker, and an engine may assign roles to people
however it likes.

## Where to go next

The rules are organised by system, not by SPI section:

| File | System | Draws on SPI |
|---|---|---|
| [Glossary](./glossary.md) | Defined terms | §2, §3 |
| Units and state | Unit characteristics, TOE, cohesion, morale | §3, §6.2, §17 |
| Sequence of play | The turn and the stage in full | §5, §7 |
| Capability points | CPA, costs, disorganisation | §6 |
| Movement | Continual movement, terrain, rail, reaction | §8 |
| Stacking and zones of control | | §9, §10 |
| Combat | Barrage, retreat before assault, anti-armour, close assault, probes, patrols | §11–16 |
| Organisation | Attachment, reinforcements, replacements, reserve, training | §18–20 |
| Engineering | Engineers, construction, fortifications, minefields, repair | §22–26 |
| Special | Breakdown, raiders, prisoners, weather, fleet, Rommel | §21, §27–31 |
| Abstract logistics and air | | §32 |

Files not yet written are listed so the shape of the edition is visible;
they are added one system at a time.

---

*Provenance: drawn on SPI §1, §2, §3.2, §5, §6.1–6.2, §7.1, §8.2, §8.37,
§10, §11.3, §15.5, §15.7, §18, §21, §32.1. This page only refers; every
primary citation lives in the system file that restates the case.*
