---
title: Water
status: provisional
---

# Water

In the Logistics Game every unit needs **water**. It is rarely short, but it
is never free: somebody has to draw it, carry it and hand it out every
Operations Stage. This file covers where water comes from (wells, oases and
pipelines), how much each unit uses, what happens to a unit that goes
without, and the extra water the Italians need for their rations. It
replaces the Land Game's rule that water is ignored
([Abstract logistics and air](../95-abstract-logistics-and-air.md#supply-units)).

::: spi 52.0

Water is counted in **Water Points**. Almost all of it is at the wells along
the coast, so an army that pushes inland has to haul it. Wells can be
drunk dry or spoiled by the enemy; rain refills dry wells, and spoiled wells
can be cleaned. Players may also lay pipelines out from the big sources.

::: spi-omit 52.1 52.2 52.4 52.5 — subsection headings; the rules under them are restated below

## Wells

::: spi 52.11

Water exists only at **wells**, and a pipeline can carry it onward from
one. Every major city, village and bir hex holds a well, and so does every
oasis; no other hex has one. The Tripoli and Tunisia boxes count as holding
as many wells as anyone needs.

There are three kinds of source, and they behave differently:

| Source | Roll to draw? | Amount | Can be depleted? | Can be poisoned? |
|---|---|---|---|---|
| Major city, oasis, pipeline (or Commonwealth railway) | no | unlimited | no | no |
| Village | yes | Water Availability Table, *Town* row | yes | yes |
| Bir | yes | Water Availability Table, *Bir* row | yes | yes |

### Drawing water {#drawing-water}

::: spi 52.12 52.13 52.7

To **draw** water:

1. Bring a unit into a hex with a well.
2. Pay **1 CP** for the unit (the CP cost table has the exceptions:
   [Capability points — costs](../30-capability-points.md)).
3. At a major city or oasis, take as many Water Points as you want. You are
   done.
4. At a village or bir, roll one die and read the
   [Water Availability Table](../../data/tables/water-availability.json)
   in the row for that source. The number is the Water Points drawn. The
   chart names the village row *Town*.
5. If the result is starred, roll one more die in secret. On a **1** the
   well is now **depleted**.

| Die | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Town (village) | 100 | 150 | 200 | 300 | 350\* | 500\* |
| Bir | 50 | 100 | 150 | 200\* | 300\* | 400\* |

\* Roll again in secret for depletion.

*Example.* A British battalion reaches a bir, pays 1 CP and rolls a 4: it
draws 200 Water Points. The result is starred, so the owner rolls again
behind his hand and gets a 1. He writes the bir down as dry and says
nothing.

::: ruling R-020 — one draw per village or bir well per Operations Stage

A village or bir well can be drawn from **once** per Operations Stage. The
first unit to pay its CP makes the roll; after that the well is closed to
every unit, friend or foe, until the next stage, whether or not the roll
depleted it. Major-city, oasis and pipeline sources have no such limit
(ruling [R-020](../../rulings/R-020.md)).

### Depleted wells

::: spi 52.14 52.15

The player whose draw depleted a well keeps a written note of it and need
not tell his opponent. When an enemy unit later tries to draw from that
well, it pays its CP first, and only then is told the well is dry. At that
point put a depleted marker in the hex.

A depleted well stays dry until a **rainstorm** hits its map section. The
instant one does, every depleted well on that section is full again
([Weather](../90-special.md#weather)).

### Poisoning wells {#poisoning}

::: spi 52.16 52.8

A village or bir well may be **poisoned** — in practice salted. Major-city
and oasis wells may not.

1. Any unit in the hex pays **1 CP** and rolls one die.
2. On a **1** the well is poisoned. On 2–6 nothing happens, and no one may
   try again at that well for the rest of the Operations Stage.
3. The poisoning player may keep the result secret, exactly as for a
   depleted well: the enemy learns of it only after paying to draw there.

The die bands are in the
[Poisoning and Sweetening Wells Table](../../data/tables/well-poisoning.json).

### Sweetening wells

::: spi 52.17

A poisoned well may be **sweetened** so that it can be drawn from again.

1. A land unit in the hex pays **5 CP** and rolls one die.
2. On **1–3** the well is clean and water may be drawn from it as usual. On
   4–6 it stays poisoned.
3. Further attempts may follow, at 5 CP each, but a unit may not go beyond
   its CPA making them.

::: note
Open question, not yet decided: whether that CPA limit applies per unit or to the whole effort at one well ([R-021](../../rulings/R-021.md)).
:::

## Water pipelines {#pipelines}

::: spi 52.21 52.22 52.23

A **water pipeline** stretches water from a major city to hexes that have
no well of their own.

- A pipeline must start at a well in a major city (never at an oasis,
  village or bir), and may run as many hexes as its builder likes.
- Every hex of pipeline is a source like a major city: unlimited, never
  depleted, never poisoned. It can, however, be destroyed.
- **Commonwealth** only: every railway hex in working order already counts
  as pipeline, and a new pipeline may start from any railway hex. The Axis
  may not use the disused Barce–Benghazi line this way.

::: spi 52.24

To build pipeline:

1. Use an engineer battalion, or a Commonwealth HQ acting as engineers.
2. Spend **10 stores** and one Construction Phase per hex.
3. Build no more than **one** hex of pipeline in an Operations Stage.

Repairs cost and take the same as new construction
([Engineering — construction](../80-engineering.md#construction)).

::: spi 52.25

Pipeline can be destroyed by a desert raider raid, by strafing, or simply by
an enemy unit standing in the hex ([Special — raids](../90-special.md#raids)).
Railway pipeline is not attacked directly; it is lost when the railway hex
is destroyed. When a hex is lost, water still flows up to the last hex that
remains joined to the source, and no further. Counters are supplied for
pipeline and for destroyed pipeline.

::: note
Open question, not yet decided: which hexes of a broken pipeline may still be drawn from ([R-061](../../rulings/R-061.md)).
:::

## Oases {#oases}

::: spi 52.3

An **oasis** hex has the terrain it is printed on for every purpose except
supply. For supply it is a free dump of water and food:

- its well has no limit, never runs dry and may not be poisoned;
- it gives every unit there all the stores it needs for ordinary upkeep
  (not for construction; SPI 51.1);
- a unit that stays in an oasis never lacks water or ordinary stores, for
  as long as it remains.

No pipeline may be laid from an oasis.

## Water usage {#usage}

::: spi 52.41 52.42

Each Operations Stage, units need water as follows:

| Who | Need per Operations Stage |
|---|---|
| Each infantry battalion or company, whatever its TOE Strength | 1 Water Point |
| Each TOE Strength Point of vehicles (tanks, recce, artillery and so on) and each Truck Point | 1 Water Point, **only** if it spends any of its CPA that stage |

A vehicle that sits still all stage uses no water.

*Example.* An Italian stack holds one infantry battalion and an artillery
battalion of 4 TOE Strength Points with 3 Truck Points. In a stage where
only the infantry moves, the stack needs 1 Water Point. If the artillery
also moves, it needs 1 + 4 + 3 = **8**.

::: note
Open question, not yet decided: where a unit's water must be for it to count as watered ([R-062](../../rulings/R-062.md)).
:::

::: spi 52.43 52.44 52.45

- **Hot weather** raises the need; in hot weather each unit uses twice the
  table above ([Weather](../90-special.md#weather)).
- Water held anywhere other than a well or a pipeline — in dumps, trucks or
  units — loses points to evaporation and spillage at the same rates as
  fuel (SPI 49.3; see the Fuel file of this module).
- Trucks carry water at the rates on the Truck Characteristics Chart
  (SPI 54.2).

## Going without water {#lack-of-water}

::: spi 52.51

A **vehicle** unit with no water in a stage:

1. may not move;
2. may not make an offensive close assault;
3. if close-assaulted, halves its total raw strength before its actual
   strength is worked out.

::: note
Open question, not yet decided: whether gun units count as vehicles here ([R-022](../../rulings/R-022.md)).
:::

::: spi 52.52 52.53

An **infantry** unit — for this rule, any unit that moves on foot rather
than by vehicle — with no water in a stage:

1. may not spend more than its CPA by choice that stage;
2. may not make an offensive close assault;
3. defends at half strength.

For each further stage in a row without water, after the first, each such
infantry unit also loses **1 TOE Strength Point**.

*Example.* A company goes dry for three stages running. In the first it
suffers only the three limits above. It loses one TOE point in the second
and another in the third.

## The Italian pasta rule {#pasta}

::: spi 52.6

Italian troops lived largely on pasta, which needs water to cook. So:

1. Whenever an Italian battalion receives its stores, it must also receive
   **1 extra Water Point** — its **Pasta Point**.
2. A battalion-sized unit that misses its Pasta Point may not spend more
   than its CPA by choice that turn.
3. If it misses its Pasta Point while at a Cohesion Level of **−10 or
   lower**, it becomes Disorganized at once, as though it had fallen to
   −26 ([Cohesion](../10-units-and-state.md#cohesion)).
4. When it does get its Pasta Point, it returns to the Cohesion Level it
   had before it fell apart.

::: note
Open question, not yet decided: how often the Pasta Point is due and how long its penalty lasts ([R-060](../../rulings/R-060.md)).
:::

---

*Drawn on: SPI §52.0–52.8.*
