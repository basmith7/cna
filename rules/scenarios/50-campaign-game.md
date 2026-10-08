---
title: Group Five — the campaign game
status: provisional
---

# Group Five — the campaign game

The whole war in North Africa, played to the end of 1942. SPI expects a
team on each side (ideally a commander per division plus air, logistics and
supreme commanders, and no fewer than three players a side) and warns that
planning and paperwork are much of the game.

::: spi 64.0 64.1

## The two campaigns {#campaigns}

::: spi 64.2 64.3 64.4

| Campaign | Starts | Set-up and initiative | Data |
|---|---|---|---|
| **Full** | Game-Turn 1, OpStage 1 (September 1940) | [Group One](10-the-italians.md) | `data/scenarios/campaign-game.json` |
| **Shorter** | Game-Turn 26, OpStage 3 (Rommel's arrival, March 1941) | [Group Two](20-desert-fox.md) | `short-campaign-game.json` |

Both end after Game-Turn 111, OpStage 3.

## Special rules {#special}

::: spi 64.5 64.51 64.52 64.53 64.54

- Nothing that the scenario groups forbid is forbidden here: raids on
  Rommel, the Commonwealth fleet and so on all follow their own rules.
- Axis air availability against Malta uses the campaign row of the Axis
  Strategic Air Force Commitment Chart.
- **Shorter campaign only**, the production that 1940 has already used up
  is removed: Axis truck production totals fall to 800 light, 2,400 medium
  and 500 heavy; half of the Italian replacement points plannable up to
  Game-Turn 24 are lost (rounding up), except 60 light-tank points; German
  production is unchanged; and several Commonwealth replacement totals are
  cut to the figures 64.54 gives (recorded in the data's notes), the rest
  unchanged.

## Without the Air or Logistics Game {#abstractions}

::: spi 64.6

Use the abstract rules ([§32](../95-abstract-logistics-and-air.md),
[§58](../logistics/60-abstract-air.md)) with the abstracted set-up of the
starting group and the replacement adjustments above. SPI doubts anyone
will want to.

## Victory {#victory}

::: spi 64.7 64.71 64.72

**Automatic victories.**

- **Axis:** occupy every hex of Alexandria and Cairo for a whole
  Game-Turn, with a convoy supply line of at most 90 truck movement points
  to a dump that is itself supplied from Tobruk or Tripoli. This wins at
  once, whatever the date.
- **Commonwealth:** from Game-Turn 35 on, if no Axis combat unit (air and
  coastal shipping aside) can trace such a line of at most 60 truck
  movement points, the Commonwealth wins at once.

::: spi 64.73 64.74 64.75

**Points**, counted at the end otherwise:

1. **Places held** (`victory.points`), each by a combat unit of at least
   one TOE point that ends the game with a week's stores and water, and
   fuel and ammunition to fire three times and move 20 CP.
2. **Unused replacements:** one point for every replacement point a
   player's production charts allowed him and he never used (not planes or
   trucks, and for the Commonwealth not infantry).
3. **Withdrawals** (Commonwealth only): a combat battalion or equivalent
   (not anti-aircraft) at 75 % TOE or more, voluntarily withdrawn from
   Alexandria or Cairo, earns half a point a week it is away, at most three.
   Bringing it back costs two points, and it may not be withdrawn again for
   six months.

::: spi 64.76

The totals are compared as a ratio, larger to smaller: equal is a draw; up
to 1½ to 1 a marginal victory; above that up to 2½ to 1 a decisive one;
anything greater a smashing one.

::: ruling R-109 — open points in the campaign victory rules

::: spi-omit 65.0 — the designer's notes and bibliography: commentary, no rules
