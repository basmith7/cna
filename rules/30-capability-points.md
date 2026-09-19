---
title: Capability points
status: provisional
---

# Capability points

This file defines the currency every land unit spends to act: the
**capability point allowance (CPA)**, what it covers, how it interacts with
the two halves of a stage, and the cost of each action. What happens when a
unit overspends — disorganisation points and the cohesion level — is in
[Units and state](10-units-and-state.md#cohesion).

::: spi-omit 6.0 6.1 — section heading and design commentary; the rules under them are restated below

## The allowance

::: spi 6.11 6.12 6.13

Every unit has a CPA, read from its OA sheet. It is the number of
**capability points (CP)** the unit may spend in one operations stage
without earning a disorganisation point. Almost every action a unit takes —
moving, retreating, advancing, fighting, loading, carrying, building — costs
CP at the rate in the cost table below; anything not listed as free costs CP.

Some gun units are printed with a CPA of 0. Treat that as **10 for every
purpose except movement**: the unit cannot move on its own but can fight,
attach, load and so on.

## One allowance for the whole stage

::: spi 6.14

The allowance covers **both halves** of the stage. CP spent while the enemy
is phasing — retreating before assault, reacting, defending — come out of the
same pool the unit will use in its own half. Track spent CP per unit on its
TOE sheet or the control sheet as the stage goes on.

*Example (our own).* A foot battalion with CPA 8 is the non-phasing side in
the first half of a stage. It retreats before assault two hexes at 2 CP
each (4 CP). When its own half begins it has 4 CP left before it starts
earning disorganisation points.

## Formations move at the slowest unit's pace

::: spi 6.15

When a parent formation (division, brigade, regiment) moves as one body, it
uses the **lowest CPA among its component units**; the higher allowances of
the rest are irrelevant. Use each component's *effective* CPA: a slow unit
that is being carried by trucks contributes the truck CPA (see below), not
its own.

## No banking, no lending

::: spi 6.16

A unit need not spend its whole allowance. Unspent CP are lost at the end of
the stage — they do not carry over, unlike the cohesion level, which does.
CP cannot be transferred between units. The one way to change a unit's
allowance is motorisation.

## Motorisation

::: spi 6.17

An infantry unit — any unit whose printed CPA is 10 or lower — that is carried
by trucks uses the **truck unit's CPA** instead of its own for as long as it
is carried. Anti-aircraft units printed with a CPA of "0+" may be motorised
by assigning one truck point (medium or heavy) for each strength point of
guns. Loading, capacity and the movement effects are in
[Movement](40-movement.md#trucks).

## Cost table

::: spi 6.3

Costs are per unit per action. **TEC** means the terrain cost for the hex
entered ([Movement](40-movement.md)); **CPA** means the unit's own allowance.
Canonical values: `data/tables/cp-costs.json` (validated by `check_data.py`);
the table below is the readable copy.

| Action | CP |
|---|---|
| Detach (parent *and* unit each pay) | 1 |
| Attach an already-assigned unit (both pay) | 1 |
| Attach an unassigned unit (both pay) | 2 |
| Absorb two replacement strength points (both pay) | 1 |
| Enter a hex with no mines | TEC |
| Friendly mines, engineer present | 0 + TEC |
| Friendly mines, foot, no engineer | 1 + TEC |
| Friendly mines, motorised, no engineer | 4 + TEC |
| Enemy mines, foot, engineer present | 2 + TEC |
| Enemy mines, motorised, engineer present | 4 + TEC |
| Enemy mines, foot, no engineer | 4 + TEC |
| Enemy mines, motorised, no engineer | CPA + TEC |
| Break contact | 2 |
| Disengage | 4 |
| Go into reserve | 0 |
| Phasing: barrage and/or assault other than a probe | 5 |
| Phasing: undergo a barrage | 3 |
| Phasing: probe | 2 |
| Non-phasing: fire or receive barrage, or defend a full assault | 3 † |
| Non-phasing: defend against a probe | 2 † |
| Patrol | 0 |
| Raid (desert raiders) | 5 |
| Poison a well | 1 |
| Sweeten a poisoned well | 5 |
| Blow a supply dump | ⅓ CPA |
| Water draw or truck load/unload in the organisation phase | 0 |
| Water draw at any other time | 1 |
| Truck load/unload at any other time | 2 |
| Construct a real supply dump / a dummy or non-dump | 3 / 2 |
| Build or demolish anything else | 0 |
| Move troops by rail or between ports | 0 |
| Move troops by air; drop paratroops | 0 |
| Paradrop commandos | 5 |
| Commando landing from the sea | 5 or 10, + TEC |
| Ready aircraft | 10 |

† **Refund on a bad attack.** If the final adjusted assault differential is
−4 or worse, each defending unit gets back 2 of the CP it spent to defend —
but only if it neither barraged nor was barraged that segment.

Some actions cost nothing yet still restrict what the unit may spend CP on
afterwards (construction and training in progress, for example); each such
restriction is stated with the action.

## Engine notes

- Store `cp_spent` per unit per stage; reset to 0 at the start of every
  stage, never at the half-stage boundary.
- Overspend is allowed. Each CP beyond the CPA earns disorganisation as
  defined in [Units and state](10-units-and-state.md#earning-disorganisation-points).
- The "CPA 0 → 10 except movement" rule and motorisation are the only two
  cases where the effective CPA differs from the printed one.
