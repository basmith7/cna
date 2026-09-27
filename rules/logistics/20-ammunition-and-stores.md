---
title: Ammunition and stores
status: provisional
---

# Ammunition and stores

Fighting costs **ammunition**; simply being in the desert costs **stores**.
This file covers both: what each is measured in, who spends it and when,
where it must be, what happens to captured stocks, and what a unit suffers
when either runs out. It replaces the per-battalion ammunition charge of the
Land Game played alone
([Abstract logistics and air](../95-abstract-logistics-and-air.md#supply-expenditure)).

::: spi-omit 50.1 51.1 51.2 — subsection headings; the rules under them are restated below

## Ammunition Points

::: spi 50.0 50.11

Ammunition is counted in **Ammunition Points**. One point is a rough
stand-in for about four tons of shells and cartridges. Land units spend it
when they fire their TOE Strength Points; aircraft spend it when they carry
bombs or fight in the air. A unit's ammunition must be tracked for each of
its TOE Strength Points, on its TOE sheet.

## Who must have ammunition

::: spi 50.12

::: ruling R-013 — pinned units spend no ammunition in a close assault

A land unit spends ammunition whenever it uses any of these:

- its barrage strength (including flak from AA points);
- its anti-armour strength;
- any of its assault strengths, attacking or defending.

Only points actually committed to the fire or the assault pay. Pinned units,
units that retreated into the hex and units held back share any losses but
spend nothing ([R-013](../../rulings/R-013.md)).

::: ruling R-050 — out of ammunition means none in the unit or its hex; surrender on being attacked or at the end of an Enemy phase in an Enemy ZOC

A unit is **without ammunition** only when neither it nor its hex (attached
trucks or a dump) holds any Ammunition Points. Such a unit is useless in combat:

1. It may not fire or assault, and may not even defend in an assault.
2. It has **no Zone of Control**.
3. It **surrenders** and is captured the moment an Enemy unit barrages or
   assaults it, or at the end of any Enemy phase in which it is in an
   Enemy ZOC.
4. It may not move into an Enemy ZOC unless the hex it enters already holds
   a Friendly unit that has ammunition, or a supply dump. It may also enter
   in company with such a unit.


## Consumption rates

::: spi 50.13 50.14 50.2

Every combat function has a **consumption rate**: the Ammunition Points
spent for each TOE Strength Point that performs it. The rates are in the
[Ammunition Consumption Rates Chart](../../data/tables/ammunition-consumption.json)
(use its *Logistics Game Played* half):

| Action | Ammunition Points per TOE Strength Point |
|---|---|
| Barrage (and flak) | 4 |
| Anti-armour fire | 3 |
| Close assault (armor-class, gun-class, MG and heavy-weapons infantry) | 2 |
| Anti-air fire at one target group | 2 |
| Rearm any part of a squadron's tacair rating | 1 |
| Rearm one plane with bombs, torpedoes or mines | 1 |
| Air-to-air combat and/or strafing | the plane's tacair rating / bombload |

1. A unit with more than one kind of strength (a tank has anti-armour and
   assault strengths) pays the rate of the function it is using at that
   moment.
2. The cost depends only on how many TOE Strength Points take part, never on
   the Actual Barrage Points or other derived strength they produce.
3. A player may fire fewer than all of a unit's Strength Points to save
   ammunition; only those that fire pay.

*Example.* A battery of five TOE Strength Points of field guns barrages. If
all five fire, they spend 5 × 4 = **20** Ammunition Points. If the player
fires only two, they spend **8**, and the barrage is made with those two.

The chart's *Logistics Game Abstracted* half is the per-unit schedule used
when this game is not played; it is restated in
[Abstract logistics and air](../95-abstract-logistics-and-air.md#supply-expenditure).

## Where ammunition must be

::: spi 50.15 50.17

1. Ammunition can be spent only if it is **in the hex**: carried by the
   unit itself, in first-line trucks attached there, or in a supply dump
   there. Any unit may draw on ammunition present in its hex.
2. A TOE Strength Point may carry, without trucks, only enough ammunition to
   fire **once**.
3. Ammunition in a truck convoy (second- or third-line trucks) may not be
   spent until it has been **off-loaded**.
4. Spend ammunition the moment it is used, and reduce the record for that
   unit, truck or dump at once.
5. Ammunition may be moved by truck or by air, and may be airdropped.

## Captured ammunition

::: spi 50.16

Each side's ammunition fits only its own weapons. When a player captures
Enemy ammunition, he may keep **one-third** of it, rounded up; the rest is
destroyed. When a dump is taken back by its original owner, he too may keep
only one-third of what remains in it.

*Example.* A dump holding 50 Ammunition Points is captured. The captor keeps
17 (50 ÷ 3 = 16.7, rounded up). If the original owner retakes the dump with
those 17 still in it, he keeps 6 (rounding up again).

::: note
Open question, not yet decided: rounding on recapture, and on the 50 % of captured stores ([R-051](../../rulings/R-051.md)).
:::

## Stores

::: spi 51.0 51.11 51.13 51.14

**Stores** are everything a force needs other than fuel, ammunition and
water: chiefly food, but also clothing, paper and the rest. Unlike the
other supplies, stores are handed out once, at the start of each
Game-Turn, not during each Operations Stage; and a unit may go without them
for a while, at a cost.

Each Game-Turn, a unit needs these **Stores Points**:

| Who | Stores Points per Game-Turn |
|---|---|
| Each TOE Strength Point in play | 4 |
| Each HQ or engineer unit (in place of the per-point rate) | 1 |
| Each Guard Point (51.17) | 2 |

Prisoners have their own rate, below. Stores are also spent on some
construction ([Construction](../80-engineering.md#construction)).

::: variant V-004 — stores paid in instalments

## Prisoners and guards

::: spi 51.12 51.17

1. Prisoners need **1 Stores Point per 5 Prisoner Points** in every
   **Operations Stage** (see [Prisoners](../90-special.md#prisoners)).
2. Prisoners are fed **first**, before any other unit.
3. If there are no stores in the prisoners' hex, deduct them from the
   **nearest supply dump**, however far away it is. Only prisoners and
   guards may draw at a distance like this.
4. Guards may draw from the nearest dump in the same way.

::: note
Open question, not yet decided: how the per-stage prisoner charge fits a per-turn stores distribution ([R-053](../../rulings/R-053.md)).
:::

## Moving and capturing stores

::: spi 51.15 51.16

1. One Stores Point weighs **one ton**.
2. Stores may be moved by truck or by air, and may be airdropped.
3. A unit may use only stores that are **in its hex**; stores in a truck
   convoy must be off-loaded first.
4. A player who captures Enemy stores may use **half** of them; the rest
   are lost.

## Going without stores

::: spi 51.21 51.22

1. **Disorganisation.** When even one Strength Point of a unit (the parent
   formation included) goes unfed in a Game-Turn, the whole unit gains
   **1 Disorganization Point** for that turn, and one more for each
   further turn without stores.
2. **Attrition.** Units in a hex that go **two consecutive Game-Turns**
   unfed lose **2 %** of their Strength Points (round to the nearest whole
   point). Each further pair of unfed turns in a row adds 2 % to the rate:
   4 % after four turns, 6 % after six, and so on. A fed turn ends the run.
3. Only **infantry-type** Strength Points are removed by attrition; guns
   and tanks never are.

*Example.* An infantry battalion of 30 TOE Strength Points goes unfed for
four turns running. At the end of the second turn it loses 1 point (2 % of
30 is 0.6, rounded to 1); at the end of the fourth it loses 4 % of what is
left.

::: note
Open question, not yet decided: when the attrition is taken, what it is a percentage of, and whether 2 % of a small unit can round to nothing ([R-052](../../rulings/R-052.md)).
:::

## Half rations

::: spi 51.23

When there are **not enough stores to go round**, a player may put units on
**half rations**. A unit on half rations needs 2 Stores Points per TOE
Strength Point instead of 4. While on half rations it:

- may not choose to exceed its CPA;
- may not choose to move into an Enemy Zone of Control.

Half rations are a response to shortage only: a player who has enough
stores may not use them to build a reserve.

---

*Drawn on: SPI §50.0–50.2, §51.0–51.2.*
