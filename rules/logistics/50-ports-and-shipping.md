---
title: Ports and shipping
status: provisional
---

# Ports and shipping

In the Logistics Game everything the Axis fights with crosses the sea, and
every ton of it passes through a port. This file covers what a port can
handle, how ports are damaged and repaired, how the Axis plans and sends its
naval convoys, how Axis coastal ships move cargo along the shore, and where
the Commonwealth draws its supplies. It replaces the simplified convoys and
port rules of the Land Game played alone
([Abstract logistics and air](../95-abstract-logistics-and-air.md#simplified-axis-convoys)).

::: spi-omit 55.1 55.2 56.1 56.2 56.3 — subsection headings; the rules under them are restated below

## Ports

::: spi 55.0 55.11

Every port is either a **major port** or a **minor port**. Both kinds may
ship men and supplies out. A major port may also receive troops; a minor
port may receive only supplies.

::: note Open question
The rules give no list of major ports. The chart below gives each port an
incoming stacking-point figure instead; whether that figure is what makes a
port major is [R-081](../../rulings/R-081.md).
:::

### Efficiency level and capacity

::: spi 55.12 55.13 55.14

Each port has two ratings on the
[Port Capacity and Efficiency Level Chart](#port-capacity-chart):

- an **efficiency level**, an abstract measure of how well the port is
  working. Its chart value is the port's **maximum level**; enemy action
  lowers the **current level**;
- a **port capacity**: the most stacking points of troops, and the most tons
  of supplies, that may pass in and out.

A port at its maximum level uses its full capacity. Below it, every figure
of capacity is scaled by current level over maximum level, rounding up to
the whole ton. For example, a port with maximum level 4 and a capacity of
1,000 tons that has been knocked down to level 3 handles 750 tons; knocked
down to 1, it handles 250 tons.

::: note Open question
Case 55.12 names Tobruk's level as 5, and the chart prints 5; the campaign
set-ups start Tobruk at 7. Which figure holds is
[R-027](../../rulings/R-027.md).
:::

### Troops landing and the period of capacity

::: spi 55.15 55.16

1. Troops landed at a port that the players have chosen to ship (not those
   arriving by the Reinforcement Schedule) may cut the port's supply
   capacity for the stage or turn they land. How much is set by the naval
   transport rule as corrected by the errata:
   [Naval transport of troops](../90-special.md#naval-transport-of-troops).
   Scheduled reinforcements never touch a port's capacity or level.
2. Some ports receive shipments only in a Strategic Phase; others may be
   used in every Operations Stage. A port's capacity covers all it receives,
   whichever phase the cargo arrives in; keep one running total.

::: note Open question
The chart gives capacity per Operations Stage; case 55.16 speaks of a
Game-Turn. Which period the running total covers is
[R-080](../../rulings/R-080.md).
:::

### Bizerta

::: spi 55.17

Bizerta (in the Tunis Box) may not be used at all before the June I, 1941
Game-Turn. From that turn on, the Axis player rolls two dice once each
Game-Turn; on a 12 Bizerta opens for good, from that turn. Until he rolls
the 12 it stays shut.

### Recovery

::: spi 55.18

A port that loses no levels to enemy bombs in an Operations Stage regains
one level, up to its maximum. Levels lost to blocking or to mines do **not**
come back this way; they must be cleared (below).

## Blocking and clearing harbours

::: spi 55.21 55.22 55.23 55.24

A player who holds a port may **block** its harbour by sinking ships in it.
Five ports are immune to blocking: Tripoli, Bizerta, Alexandria, Aboukir
(E3815) and Rosetta (E4019). To block a port:

1. Have an engineer battalion, or a Commonwealth HQ with engineer
   capability, in the port hex.
2. In the Construction Phase, spend from supplies in that hex **25
   Ammunition Points and 10 Stores Points** (Tobruk: **50 and 25**).
3. The port's current level drops by one. A port may lose at most one level
   per Operations Stage to blocking, however much is spent.

These costs are also on the
[Construction Chart](../80-engineering.md#construction).

::: spi 55.25

When play begins, the wreck of the *San Giorgio*, an Italian cruiser, lies
in Tobruk harbour and costs the port **three** levels.

::: note Open question
How those three levels are won back — by clearing, by removing the ship, or
both — is [R-082](../../rulings/R-082.md).
:::

::: variant V-001 — the San Giorgio as a live gun battery that never reduces Tobruk's efficiency (NJHarman)

::: spi 55.26

Only the owning side's engineers — an engineer battalion or a Commonwealth
HQ with engineer capability — may **clear** a blocked harbour. Clearing is
blocking in reverse: one level per Operations Stage, paid from supplies in
the hex:

| Port | Ammunition | Stores | Other |
|---|---|---|---|
| Tobruk | 25 | 10 | — |
| Benghazi | 100 | 50 | two engineer units present |
| any other | 50 | 25 | — |

::: note Open question
Tobruk is the one port that costs more to block than to clear. Whether the
figures are swapped is [R-083](../../rulings/R-083.md).
:::

### Mines

::: spi 55.27

Enemy bombers may lay mines in a harbour
(SPI 41.3; the Air Game is not yet restated here); each mine laid lowers the port one
level. To sweep:

1. The port's owner must have an engineer unit (as for clearing) in the port.
2. In the Construction Stage, roll one die for each mine: 1–3 removes it,
   4–6 leaves it.
3. That engineer unit may not move, spend CPA voluntarily, or do any other
   construction or clearing in that stage.

### Enemy ships in a port

::: spi 55.28

Commonwealth ships in an Axis-held port hex do not stop or reduce Axis
convoy arrivals there.

### Port capacity chart {#port-capacity-chart}

::: spi 55.3

Data: [`data/tables/port-capacity.json`](../../data/tables/port-capacity.json).
Stacking points and tons are per Operations Stage at maximum level; "na"
means none. Stacking points and tons are separate allowances; replacement
points landed by an Axis convoy count against stacking points, not tons.

| Port | Max level | SP in | SP out | Max tons |
|---|---|---|---|---|
| Tripoli | 10 | 10 | 15 | 15,000 |
| Bizerta (a) | 10 | 10 | 15 | 3,333 |
| Alexandria | 10 | 5 | 10 | 15,000 |
| Tobruk (b) | 5 | 1 | 3 | 1,700 |
| Benghazi | 3 | 2 | 5 | 2,500 |
| Mersa Matruh | 1 | 1 | 2 | 250 |
| Bardia | 1 | 0 (c) | 1 | 400 |
| Sollum | 1 | 0 (c) | 1 | 250 |
| Derna | 1 | na | 1 | 300 |
| All others | 1 | na | na | 100 |

(a) Closed to the Axis before Game-Turn 35 (June I, 1941); see
[Bizerta](#bizerta). (b) Starts below its listed level because of the
*San Giorgio*. (c) Any one unit of zero stacking points may land.

## Axis naval convoys

::: spi 56.0

Almost all Axis supplies and replacements reach Africa by **naval
convoy**. Each Game-Turn the Axis player learns how many tons he may send
the following turn, chooses what to send and by which lanes, and then the
Commonwealth may bomb the convoys at sea. Axis supplies of every kind are
unlimited in Europe; only tonnage and ports hold him back.

### Shipping lanes

::: spi 56.11 56.12 56.14

1. There are six **shipping lanes**. They are not drawn on the map; each is
   a fixed pair of origin and destination ports, listed on the Axis Naval
   Convoy Air Distance Chart. The Axis may not invent new pairs.
2. A **convoy** is all the tonnage sent down one lane in a Game-Turn, so the
   Axis has between one and six convoys a turn.
3. Lanes 4 and 5, the lanes from Greece, may not be used before the second
   Game-Turn of May 1941. Bizerta has its own opening rule
   ([above](#bizerta)).

::: spi 56.13 56.16 56.26

A convoy may be attacked by Commonwealth bombers
(SPI 41.6; the Air Game is not yet restated here). If its lane is not
attacked, everything arrives at the lane's destination port. If it is, the
convoy fires back with **one Flak/AA point per 1,000 tons** it carries
(15,000 tons gives 15) and losses follow the strategic bombing
rules. A lane ending near the front is quick but within reach of more
Commonwealth aircraft; a lane ending far back is safer but leaves a long
haul by truck.

::: spi 56.15

A convoy's lane is fixed when it is planned and may not change, whatever
happens on land. One exception: a convoy bound for a port the Commonwealth
captures before it sails is cancelled, and never sails.

::: spi 56.17

A lane has no tonnage limit of its own; only the turn's tonnage allowance
and the destination port's capacity limit it.

### Planning a convoy

::: spi 56.21 56.4 56.5

In the Axis Convoy Planning Phase of each Game-Turn, the Axis player plans
the next Game-Turn's convoys:

1. Find the **convoy level**, a letter A–G, for the month the convoys will
   sail, on the [Axis Naval Convoy Level Chart](#axis-convoy-level-chart).
2. On the [Axis Naval Convoy Capacity Table](#axis-convoy-capacity-table),
   roll one die: the turn's allowance is that level's fixed tonnage plus
   its variable tonnage times the roll, rounded up to the next 1,000 tons.
3. Choose the cargo within that allowance (next section).
4. Allot the whole cargo to lanes and so to destination ports, all at once,
   and write it on the Convoy Control Sheet.

For example, planning in late February 1942 for the March I turn: March
1942 is level B, and a roll of 3 gives 7,000 + 3 × 1,500 = 11,500, rounded
up to 12,000 tons.

::: spi 56.22 56.25

Within the allowance the Axis may send any mix of fuel, ammunition and
stores. Once lanes and destinations are chosen they may not change (see
[Shipping lanes](#shipping-lanes)).

### Replacements by convoy

::: spi 56.23

Supplies are converted to tons with the Equivalent Weights Chart (SPI 54.5, restated with trucks and dumps). Replacement points the Axis
planned earlier to ship from Italy or Greece
([Replacements](../70-organisation.md)) also take tonnage, at the rates on
the Axis Replacement Pool
([`data/tables/axis-replacement-pool.json`](../../data/tables/axis-replacement-pool.json)).
Only planned replacements use convoy tonnage; reinforcements and scheduled
replacements do not travel by convoy.

::: note
The SPI text of this replacement rule is printed as case 56.24 but misnumbered
36.24 in the source, so it has no case id of its own here; it is restated
under the 56.23 badge above.
:::

### Arrival

::: spi 56.27 56.28

1. A convoy may not land more than its destination port can take
   ([port capacity chart](#port-capacity-chart)); plan accordingly.
2. Cargo is unloaded the moment it arrives and may be used at once. Every
   port where convoys land (Tripoli, Bizerta, Tobruk and the rest) counts as
   holding a built supply dump.

### Axis Naval Convoy Level Chart {#axis-convoy-level-chart}

Data: [`data/tables/axis-convoy-level.json`](../../data/tables/axis-convoy-level.json).
A dash means no convoys that month.

| Year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1940 | – | – | – | – | – | – | – | – | B | B | B | B |
| 1941 | B | E | F | E | D | G | C | E | C | D | E | A |
| 1942 | C | B | B | G | F | A | F | B | D | A | G | C |

### Axis Naval Convoy Capacity Table {#axis-convoy-capacity-table}

Data: [`data/tables/axis-convoy-capacity.json`](../../data/tables/axis-convoy-capacity.json).
Tons = fixed + (variable × one die), rounded up to the nearest 1,000.

| Level | Fixed tons | Variable tons per pip |
|---|---|---|
| A | 6,000 | 1,000 |
| B | 7,000 | 1,500 |
| C | 10,000 | 1,500 |
| D | 11,000 | 2,000 |
| E | 11,000 | 2,500 |
| F | 15,000 | 2,000 |
| G | 32,000 | 3,000 |

## Axis coastal shipping

::: spi 56.31 56.33 56.35

The Axis also has a few small **coastal ships** for moving supplies between
its own African ports. Each is a counter with its cargo capacity in tons
printed on it.

- A coastal ship has a CPA of **50**, for movement only; each sea hex costs
  1 CP. It needs no fuel.
- It may call at several ports in one move, unloading at each, while its CP
  last.
- It may not be attacked from the air or from land.
- It may not enter a port at efficiency level zero, nor any port held by
  the enemy.

::: spi 56.32 56.34

Coastal ships move in the **Truck Convoy Phase** only.

1. At the start of that phase, load supplies at a port for **5 CP**. A ship
   carries one type of supply at a time, and never personnel, tanks, guns or
   other equipment.
2. Move the ship.
3. Unload for another **5 CP**.

::: note Open question
The sequence of play puts coastal shipping in the Tactical Shipping Segment
instead; which governs is [R-025](../../rulings/R-025.md).
:::

## Commonwealth supply base

::: spi 57.0

The Commonwealth never ships supplies into Africa. Its stock in **Cairo** of every
supply type (fuel, ammunition, water, stores) never runs out; its problem is only
moving them forward. Commonwealth ships use no supplies. Its troops and
equipment come by the Reinforcement Schedule and the Commonwealth
replacement system ([Replacements](../70-organisation.md)).

::: note Open question
The Italian campaign's set-up places unlimited supply in Alexandria as well;
which holds is [R-026](../../rulings/R-026.md).
:::

---

*Drawn on: SPI §55.0–57.0.*
