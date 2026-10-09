---
title: Air Game — aircraft and squadrons
status: provisional
---

# Aircraft and squadrons

Aircraft are individual counters by type; each belongs to a **squadron**,
and each squadron has a ground echelon on the map, its **squadron ground
support unit** (SGSU). This file restates the aircraft themselves, their
reinforcements and withdrawals (§34), and the squadrons and their SGSUs
(§35).

## The aircraft {#aircraft}

::: spi 34.0

Each aircraft in the game is tracked individually by type. The types fall
into seven kinds: **fighters**, **fighter-bombers**, **bombers** (some able
to bomb by night), **dive bombers**, **transports**, **pure
reconnaissance** aircraft (others may also scout) and **flying boats**.
Whatever an aircraft does is one of four roles: patrol (protecting other
aircraft or a place), combat (bombing or strafing), reconnaissance, or
transport. An aircraft is of use only once it has been fuelled and refitted
after its last mission ([maintenance](30-flight-and-maintenance.md#maintenance)).

::: spi-omit 34.1 34.2 34.3 34.5 34.7 — subsection headings; the rules under them are restated below

### Ratings

::: spi 34.19 34.6

No aircraft counter carries a number. Every rating is on the Aircraft
Characteristics Charts (printed as 4.44, cited as 34.6), which are data:
[`data/tables/aircraft-characteristics.json`](https://github.com/basmith7/cna/blob/main/data/tables/aircraft-characteristics.json),
one row per type and configuration, id `aircraft:<nation>:<slug>`. Players
keep the ratings on their squadron sheets.

::: spi 34.11 34.12

- **Range**, in hexes: how far the aircraft may fly *out* to its mission
  hex, and separately how far it may fly *back*. Hexes not used on the way
  out are not saved for the way back: an aircraft of range 30 that flies 12
  hexes out still has 30 for the return, not 48. Aircraft normally return
  to the base they left. A **transfer** mission (from one air facility to
  another, nothing else) may cover **twice** the range. Where a type lists
  more than one range (drop tanks, a lighter load), the owner picks one per
  mission.

::: spi 34.13

- **TacAir**: the air-to-air rating, from the aircraft's guns. A rating in
  parentheses means the aircraft may never start air-to-air combat.

::: spi 34.14 34.15

- **Bomb load**: bomb points (not real tons); torpedo capacity, if any, is
  given with it. **Transport capacity**: TOE strength points of infantry,
  tons of supply, or both, converted with the Equivalent Weights Chart
  ([trucks and dumps](../logistics/40-trucks-and-dumps.md), 54.5).

::: spi 34.16

- **Maneuver**: speed, ceiling and agility in one comparative figure; it
  changes the basic TacAir differential in air-to-air combat (§45).

::: spi 34.17

- **Fuel**: fuel points burnt by every mission or emergency flight
  ([flight](30-flight-and-maintenance.md#emergency-flight)), the whole
  amount whatever the mission or distance.

::: spi 34.18

- **Missions**: the missions the type may fly (§39); it may fly no others.

### Fighters

::: spi 34.21 34.22

The fighter class is fighters (F) and fighter-bombers (FB). A
fighter-bomber flies a mission either as a fighter or as a bomber, never
both: on a bombing mission it may defend itself in air-to-air combat but
never start it. Fighters mostly fly **combat air patrol**, guarding bombers
or a place on the ground; some may also strafe.

::: spi 34.23 34.24

Every fighter and fighter-bomber flies with a **pilot** (40.1), whose
rating changes its air-to-air combat. Some fighters may fly reconnaissance;
on such a mission they may neither start air-to-air combat nor bomb.

### Bombers

::: spi 34.31 34.32 34.33

The bomber class is bombers, dive bombers and fighter-bombers. Most bomber
missions drop bombs to destroy or weaken a target, and types differ in how
well they do it. A bomber may also be a night bomber (NB), dive bomber (DB)
or torpedo bomber (TB), or more than one of these.

::: spi 34.34

A **dive bomber** is an ordinary bomber that may strafe as well as bomb the
same target during one mission.

::: spi 34.35 34.36

Bombers never start air-to-air combat; they only defend. Flying in large
formations raises their TacAir (45.36). Some bombers can also carry
personnel or supplies (TT).

### Flying boats

::: spi 34.4

**Flying boats** (FlyBt) are aircraft like any other, except where they
are based: never at an airfield or landing strip, only at a flying-boat
basin or alighting area ([air facilities](20-air-facilities.md)).

### Transports

::: spi 34.51 34.52 34.53

Both sides have **transports** (TT): aircraft of little fighting value that
carry personnel or supplies, up to their transport capacity in TOE strength
points or tons. They never carry vehicles or motorised units of any kind,
motorcycle units excepted. Transports never start air-to-air combat and gain
nothing from formation flying; without strong fighter cover they are easy
prey.

### Counters

::: spi 34.71 34.72 34.73 34.74 34.75

Aircraft counters stand for no particular aircraft. Aircraft on the ground
have no counter at all: the squadron's sheet lists its types and numbers,
and its SGSU marks where it is. When aircraft fly to a mission hex, the
owner puts **one lettered counter per class** (fighter, bomber, transport)
there and notes on his sheet which aircraft it stands for. Losses are
written off the sheet; the counter stays. For air-to-air combat players may
borrow spare counters to lay the fight out aircraft by aircraft.

## Reinforcements and withdrawals {#reinforcements}

::: spi 34.8

Air reinforcements come as **pilots**, **aircraft** and **SGSUs**. Pilots
rated zero come whenever needed and better pilots by die roll; SGSUs come
when called for; aircraft follow a fixed schedule. The Commonwealth must
also withdraw squadrons at set dates.

### Where reinforcements go

::: spi 34.81

**Commonwealth** aircraft may arrive at any air facility on Malta, in Cairo
or Alexandria, or off-map, Ethiopia excepted, divided as the player likes,
but: at most **10 %** of a month's aircraft may go to Malta, and none to a
Malta or North African off-map facility beyond its current squadron
capacity. **Axis** aircraft may arrive at the bases of the Tripoli and
Tunisia boxes and of Italy, Sicily and Crete as the player likes, within the
rules for basing German bombers in the Mediterranean (43.1).

### SGSUs

::: spi 34.82

SGSUs come on in any Operations Stage, at its naval convoy arrival phase: Axis
ones in any Tripoli or Tunisia box, Commonwealth ones in any Cairo or
Alexandria hex. A player brings them in as he likes, within these limits:

- **Both sides**: an SGSU lost to enemy action cannot be replaced for one
  full Game-Turn.
- **Commonwealth**: USAAF SGSUs (CPA 30) not before August 1942 (Game-Turn
  91; see also [35.18](#the-sgsu-counter)). At most **(aircraft at on-map
  facilities ÷ 12) + 2** SGSUs in play, the division rounded up: with 250
  aircraft on the map, 21 + 2 = 23. If the counters run out, extra SGSUs may
  be made only while the Commonwealth North African off-map facilities hold
  as many aircraft as their *printed* capacity allows; they still count
  against the limit and may not be USAAF.
- **Axis**: at most **(German aircraft at on-map facilities ÷ 10)** German
  SGSUs, rounded up, and the same for Italian; captured Commonwealth
  aircraft count for the nation whose SGSU holds them. Extra counters for a
  nation may be made only while at least **30 %** of that nation's aircraft
  (all types together) are at off-map North African or Mediterranean
  facilities.

### Pilots

::: spi 34.83 34.88 34.89

Pilots rated **one to six** arrive at the start of each month, in the
**first Operations Stage**'s naval convoy arrival phase; zero-rated pilots are always
available in any number, for emergency flight too. At that moment the
player reads his Pilot Arrival Table (34.88 Commonwealth, 34.89 Axis) and,
if the month has pilots, rolls two dice once (Germans and Italians
separately) and reads the total across every rating column for the number
of pilots of each rating. The German ace Marseille arrives without a roll.
The tables are data:
[`data/tables/pilot-arrival.json`](https://github.com/basmith7/cna/blob/main/data/tables/pilot-arrival.json)
(Commonwealth and Italian pilots November 1940 to October 1942, German
March 1941 to October 1942, ratings 1 to 4 on every table; Marseille in
Game-Turn 29).

### Aircraft

::: spi 34.84 34.86 34.87

Aircraft come on at a naval convoy arrival phase, listed as a month's
total of each type (early in the campaign, by named Game-Turns instead). The owner
spreads a month's aircraft over its four Game-Turns as evenly as he can,
and all of a Game-Turn's aircraft may come in its first Operations Stage.
Which individual aircraft of a type arrive is up to him. Say a month brings
20 fighters and 6 bombers: 5 fighters a turn, with the bombers 2, 2, 1 and
1, or any split as close.

The Commonwealth schedule (34.86, printed with 34.84) is data:
[`data/tables/air-reinforcement-schedule.json`](https://github.com/basmith7/cna/blob/main/data/tables/air-reinforcement-schedule.json).
No Axis schedule (34.87) was found in either scan; see *Engine notes*.

### Commonwealth withdrawals

::: spi 34.85

At the start of each month the schedule names, the Commonwealth removes the
squadrons it lists (type and minimum aircraft), from any facility on Malta
or on map E: all their aircraft and pilots leave play. Their SGSUs stay,
unless they now exceed the limit above.


## Squadrons and their SGSUs

::: spi 35.0

The squadron is the only level of air organisation the game uses (a German
*Staffel*, an Italian *squadriglia*). Every aircraft is assigned to one, and
the squadron's record sheet lists its aircraft, its pilots and its supplies.
The squadron's SGSU is its ground crew, workshops and transport: it keeps
the squadron's aircraft fuelled, refitted and armed.

### The SGSU counter

::: spi 35.1 35.11 35.12

An SGSU marks where its squadron is based, normally at an air facility. It
is not an air unit and does not carry the aircraft with it. It is a
**vehicle** unit, as medium trucks are, with its CPA printed on the counter,
and it moves in the truck convoy phase. It has **no stacking value** and no
combat strength of any kind. When an enemy combat unit moves next to an SGSU
with no friendly combat unit in its hex, the SGSU may react if it can; if it
cannot, it is eliminated. How many squadrons a facility can actually work is
set by the facility's capacity ([air facilities](20-air-facilities.md)).

::: spi 35.13

SGSUs enter play when their player calls them in, under the air
reinforcement rules (§34, 34.8). Their squadron numbers are historical but
need not be used historically. An eliminated SGSU may come back one
Game-Turn later by the same rules.

::: spi 35.14 35.15

**Its own supply.** For its own upkeep every SGSU needs, each Operations
Stage, **1 fuel and 1 water**, and each Game-Turn **1 stores**. An
SGSU lacking any of these cannot repair its aircraft. Servicing the aircraft
costs fuel and ammunition on top
([maintenance](30-flight-and-maintenance.md#maintenance)). Trucks may be
attached to an SGSU as its first-line transport, to carry what it needs.

::: spi 35.16 35.17

SGSUs may build landing strips and flying-boat alighting areas
([construction](../80-engineering.md#air-facilities)). Only SGSUs refuel
and refit aircraft. Any SGSU may refuel any aircraft; refitting is best done
by the aircraft's own squadron's SGSU, and costs +1 on the refit roll at any
other. Nothing is serviced beyond the facility's capacity.

::: spi 35.18

SGSUs marked USAF (United States Army Air Forces) may not be used before
**1 August 1942**.

### What a squadron may hold

::: spi 35.2 35.21

A squadron holds one class of aircraft: **fighters**, **bombers** or
**transports**. Fighter-bombers may go in a fighter or a bomber squadron,
and reconnaissance aircraft in any. Keeping one aircraft type per squadron
is advised for bookkeeping but is not a rule.

::: spi 35.28

German and Italian aircraft never share a squadron, since they need
separate servicing; but an Italian squadron may consist entirely of German
aircraft (not the reverse).

::: spi 35.23 35.26

**Size.** A squadron has a **ready capacity**, the most aircraft it can keep
ready to fly, and may hold a further **reserve** of a third as many:

| Squadron | Ready | Reserve | Total |
|---|---|---|---|
| Italian squadriglia | 9 | 3 | 12 |
| German Staffel | 12 | 4 | 16 |
| Commonwealth, to June 1941 | 15 | 5 | 20 |
| Commonwealth, from July 1941 | 18 | 6 | 24 |

The Squadron Capacity Chart prints the Commonwealth rows differently
(12/4/16 for 1940–41, 18/6/24 for 1942–43); the rules text, as
above, governs.

::: ruling R-116 — Commonwealth squadron size before July 1941

Reserve aircraft may be readied and armed, but fly only to make up for
ready aircraft that were not readied: never while the full ready capacity is
flying. Reserves may not scramble; they may take emergency flight
([flight](30-flight-and-maintenance.md#emergency-flight)).

::: spi 35.24

**Pilots** of fighters and fighter-bombers belong to the squadron, not to
an aircraft; the squadron sheet lists them, and each mission pairs pilots
with aircraft (§40).

::: spi 35.22 35.25

**Changing squadron.** Aircraft stay in their squadron, with two
exceptions: when their SGSU has been eliminated (they may join any other
squadron or go into reserve), and when a squadron is below half its ready
capacity (aircraft from other squadrons may join it until it is above
half). An aircraft that must fly to its new squadron does so as a transfer
mission in the mission deployment segment; if the new SGSU is in its own
hex, the change is made in the organisation phase.

::: spi 35.27

**Capture.** When an SGSU is eliminated, aircraft on the ground with it are
captured. Their captor may use them from one Game-Turn later, or destroy
them.

::: spi 35.29

*Colour, not rule:* German SGSU counters carry their unit types (JG
fighters, St.G dive bombers, KG bombers, ZG fighter-bombers, H and F
reconnaissance), unlike the Italian and Commonwealth ones. Players need not
follow them.

## Engine notes

- An aircraft's ratings come from its row in
  `aircraft-characteristics.json`; a row with `alternative_of` is the same
  type in another configuration, picked per mission (34.12).
- SGSU limits round up: Commonwealth `ceil(on_map / 12) + 2`; German and
  Italian each `ceil(on_map_nation / 10)`.
- The Axis air reinforcement schedule (34.87) was not found in either
  scan.

- A squadron needs: nation, class, ready capacity and reserve (by date for
  the Commonwealth), its SGSU (hex, CPA, supplies, attached trucks), its
  aircraft (each with type, readied, refitted, fuelled, armed) and pilots.
- An SGSU is a vehicle for movement, breakdown and supply, with zero
  stacking and no combat values.
