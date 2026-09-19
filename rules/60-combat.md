---
title: Combat
status: provisional
---

# Combat

This file defines what happens in the combat segment: the fixed order of
steps, what each step costs, how printed ratings become fighting strength,
and the four activities — barrage, retreat before assault, anti-armour fire
and close assault — plus patrols. The CP budget is in
[Capability points](30-capability-points.md); which hexes *must* be attacked
is in [Stacking & ZOC](50-stacking-and-zoc.md#zoc-combat-requirement-holding-off);
unit ratings and cohesion in [Units & state](10-units-and-state.md).

::: spi-omit 11.0 11.1 11.2 11.3 — section headings and design commentary; the procedure they introduce is restated in full below

## The combat segment

::: spi 11.0

Combat is compulsory, not optional: once every move and reaction of the
segment is over, the phasing player must attack every enemy hex that projects
a zone of control onto a friendly unit, and may attack any other adjacent
enemy hex the terrain allows. Both players then act through the steps below
in order. Every allocation ("which guns are forward", "which units barrage
which hex", "which strength points fire at armour") is written down secretly
before the step resolves, and a unit's ability in each activity is its
printed rating scaled by its current TOE strength — except retreat before
assault, which any unpinned unit may perform regardless of rating.

1. **Gun positions.** Each player marks every gun-class unit adjacent to
   the enemy as *forward* or *back* ([below](#forward-and-back)). The
   choice holds for the whole segment.
2. **Barrage.** Each player secretly picks targets in adjacent enemy hexes,
   then both barrage hex by hex; hits and pins are applied only after every
   barrage is rolled. Barrages that satisfy the holding-off requirement are
   noted as such.
3. **Retreat before assault.** Any unpinned non-phasing unit may pull back
   (the non-phasing player's choice).
4. **Assault assignment.** Both players secretly split their units between
   *anti-armour* and *close assault* roles (forward guns included). A unit
   may do both by dividing its TOE strength points between the two, but a
   single point is never split. Unpinned armour- and gun-class units may
   instead be **withheld** entirely, in which case their strength counts for
   nothing (SPI 15.29, 15.8) — usually to save ammunition.
5. **Anti-armour fire.** Both sides fire at the other's armour. Every
   armoured unit assigned to *either* role is a target; withheld armour is
   not. All losses land before the next step, so a tank assigned to close
   assault can die here first.
6. **Close assault.** The phasing player assaults with the units assigned to
   it, at strengths reduced by anti-armour losses. Casualties, *engaged*
   markers and forced retreats follow from the result.

The segment then ends; the phasing player may release reserves and start
another movement segment ([Movement](40-movement.md#continual-movement)).

## Combat characteristics

::: spi 11.1 11.11 11.12 11.13 11.14 11.15 11.16

A land unit has up to seven combat characteristics, all printed on its OA
sheet and none on the counter (see the
[characteristic list](10-units-and-state.md)):

| Characteristic | What it measures | Who has it |
|---|---|---|
| Barrage | indirect fire at range | artillery only |
| Vulnerability | how far behind the front a gun can work; exposure to close assault (higher = safer) | all guns: artillery and anti-tank |
| Anti-armour | direct fire that kills armoured units | any unit so rated |
| Armour protection | how much anti-armour damage a point absorbs | tanks, recce, armoured cars, self-propelled guns |
| Offensive close assault | fighting ability when assaulting | combat units |
| Defensive close assault | fighting ability when assaulted | combat units |
| Anti-aircraft | shooting down aircraft | AA/flak, plus some tanks and HQs |

The first and the last five are *ratings* that scale with strength. Vulnerability
and armour protection are fixed per point and are used differently
([anti-armour damage](#assessing-damage), [gun losses](#gun-losses)).

## CP cost of combat

::: spi 11.2 11.21 11.22 11.23 11.24 11.25 11.26 11.27

Combat costs CP by *role in the segment*, not by activity, and is charged
once per combat segment:

| Unit | Circumstance | CP |
|---|---|---|
| Phasing | barrages, or fires anti-armour, or close assaults | 5 |
| Phasing | probes only | 2 |
| Phasing | is barraged (and does nothing else) | 3 |
| Non-phasing | barrages; or is assaulted (anti-armour or close), including after retreating into a hex that is then assaulted; or takes a holding-off barrage | 3 |
| Non-phasing | is probed | 2 |
| Non-phasing | defends a full (non-probe) close assault whose final differential is −4 or worse | 1 |

Ceilings: a phasing unit never pays more than 5, a non-phasing unit never
more than 3, in one combat segment, whatever happens to it. A phasing unit
that fights again in a *later* segment of the same phase pays again.

The charge falls on **every unit in the hex**, participating or not. *Our
example:* a brigade of three battalions assaults with two and withholds the
third; all three pay 5 CP. Had only its artillery barraged and nothing else
happened, the whole brigade would still pay 5. Likewise, a probe does not
shield its hex-mates: if they barrage, they pay 5 CP.

## Actual strength

::: spi 11.3 11.31 11.32 11.33 11.34 11.35 11.36 11.37 11.38

Strength in every activity except anti-aircraft is stated in **actual
points**:

> raw points = combat rating × TOE strength points committed
> actual points = raw points ÷ 10, rounded to nearest (.5 rounds up)

Actual points are either applied to a hex or unit (barrage, anti-armour) or
compared with the enemy's (close assault, probe). SPI 12.54 (barrage of dumps
and airfields) is the one place raw points are used directly.

- **Sum raw, then divide.** Add the raw points of every point firing at the
  same target — from one hex or several — and convert once.
- **Four raw points or fewer is zero.** A total under .5 actual rounds to
  nothing. Exception: when neither side of a close assault or probe reaches
  10 raw, compare raw points as if they were actual (see also SPI 15.51).
- **Anti-aircraft** skips the division: raw AA points are used as they
  stand.
- **Vulnerability and armour protection** are never multiplied; they are
  per-point absorbers ([anti-armour damage](#assessing-damage), [gun losses](#gun-losses)).

*Our example:* a division's two artillery units offer 3 points at rating 12
(36 raw) and 2 points at rating 6 plus 3 at rating 12 (12 + 36 = 48 raw);
84 raw → 8 actual barrage points (8.4 rounds down). The owner may instead
fire 2 of the first unit's points at one target and its third point at
another, subject to the position rules below. Its five infantry battalions
might total 61 raw offensive close assault points → 6 actual, and those too
may be split across hexes by allocating whole TOE points; every separate
assault is computed on its own.

Keep a running raw/actual tally per parent formation on the TOE sheet, and
keep it secret until the strength is committed to an attack.

## Barrage

::: spi 12.0

Barrage is the first fire step. Any combat unit or HQ with a barrage rating
and ammunition may fire at enemy units in adjacent hexes ("artillery"
throughout this section means any unit whose TOE points carry a barrage
rating — a §32 clarification): total actual
barrage points, name the targets, fire, deduct ammunition. Results are
simultaneous — rolled target by target in any order, applied together at the
end of the step. To resolve one barrage: name the target (by class and
number, or by unit ID if known), state the actual points against it, roll
two dice read sequentially (larger die first, so 2 and 5 read *25*) on the
Barrage Results Table under the target's class (gun, armour, infantry), then
roll a second time for trucks in the hex. Holding-off barrages resolve the
same way.

::: spi-omit 12.6 — the Artillery Barrage Table is a lookup table on the chart sheet; to `data/tables/barrage-results.json` when the sheet is captured

### Forward and back {#forward-and-back}

::: spi 12.1 12.11 12.12 12.13 12.14 12.15 12.16 12.17 12.18 12.19

An artillery unit that takes part in combat is placed **forward** or
**back** as a whole — every gun in it, however many types — at the start of
the combat segment, and stays there until the segment ends. Note the choice
on the TOE sheet.

| | Forward | Back |
|---|---|---|
| Combine fire with other forward artillery on one target | yes (Italians: only with units in the *same* hex) | no |
| Split TOE points across several targets | yes | no |
| Anti-armour or close assault this segment (given ratings and ammunition) | yes | no — a heavy-weapons unit with its guns back is wholly back |
| Exposed to close assault losses ([gun losses](#gun-losses)) | yes, even if it did not fight | only against an overrun-column result |

A forward artillery unit that joins an **offensive** close assault fights
with its vulnerability rating **halved, rounded up** (7 becomes 4). Any
artillery firing in the **anti-armour** role has a vulnerability of **2**
for that purpose.

### Choosing targets

::: spi 12.2 12.21 12.22 12.23 12.24

Targets are the individual battalion- or company-sized counters that make up
a formation. Every counter in the hex with a stacking-point value is a
target, attached or not, engineers included; trucks, squadron ground support
and the like are not. Nor is an HQ with no TOE strength, or whose only points
carry parenthesised close-assault ratings. Dummy tank formations
([patrols](#dummy-tank-formations)) and Commonwealth warships *are* targets;
a warship always counts as identified (§32 addition to 12.23).

The firing player names the hexes he fires from. The owner answers with how
many targets sit in each adjacent hex and the **class** of each (gun, armour
or infantry) — not their strength, exact type or identity. The firer then
shoots blind at "infantry no. 2", "gun no. 1" and so on; the owner numbers
each class for the step. Only a unit already identified (by patrol or earlier
combat) may be named as a specific target.

### Terrain and other limits

::: spi 12.3 12.31 12.32 12.33 12.34 12.35

- Any adjacent occupied hex may be barraged, whatever the terrain or
  hexside; there is no line of sight. Empty hexes may not be barraged
  (facilities are the exception, [below](#barrage-against-facilities)).
- Each target may be barraged **once per firing hex** per segment. Forward
  artillery in several hexes may pool into that one barrage.
- Terrain shifts the *row* (barrage points) toward the defender by the
  number of columns the Terrain Effects Chart gives, and the best single
  benefit applies — a target in a level-two fortification barraged with 12
  points is resolved on the 7–8 row, not the 11–12. Shifts are not
  cumulative. A shift below the 1–2 row means no effect.

### Results

::: spi 12.4 12.41 12.42 12.43 12.44 12.45 12.46

One table serves every target: rows are the barrage points applied (after
any shift), columns are the sequential two-dice reading, and the body is
split by target class. Read the row, roll, read the cell under the class.

- **P — pinned.** The whole target unit is pinned for the rest of the combat
  segment: it may not move, fire anti-armour or close assault, and it still
  takes casualties (SPI 15.12). Mark it; remove the marker when the segment
  ends. Gun-class units and artillery HQs are never pinned by barrage.
- **A number** is TOE strength points destroyed. Losses are taken after
  every barrage of the step has been rolled.
- **Trucks.** After each barrage against a unit, roll again on the same row
  under *trucks* for any truck points attached to that unit or its parent in
  the hex. The owner chooses which trucks go, spreading losses as evenly as
  possible over truck types and cargo types. Infantry points destroyed while
  mounted take their carrying trucks with them, on top of any truck result.
  Trucks get no terrain shift (§32 clarification).

### Barrage against facilities

::: spi 12.5 12.51 12.52 12.53 12.54 12.55

Artillery may barrage a **facility** instead of a unit — a major city,
fortification, road, railway, supply dump or air facility — under the normal
barrage rules, the facility being the named target. Resolve on the Air
Bombardment Table (SPI 41.5; see [§32 / air](95-abstract-logistics-and-air.md)):
for cities, fortifications, roads and railways use its artillery barrage
points column; for supply dumps and air facilities enter the bombload column
with **raw** barrage points (78 raw reads the 41–80 column). Off-shore naval
bombardment may barrage facilities too (SPI 30.12, [Special](90-special.md)).

## Retreat before assault

::: spi 13.0 13.1

After the barrage step, every unpinned non-phasing unit whose cohesion is
better than −26 may retreat before assault. This is ordinary
voluntary movement paid in CP, not reaction.

::: spi 13.2 13.21 13.22 13.23 13.24 13.25 13.26 13.27 13.28

- It costs CP and fuel, triggers breakdown checks, and pays the contact or
  engaged break-off cost when leaving an enemy ZOC
  ([breaking off](40-movement.md#breaking-off)).
- A unit **adjacent to an enemy combat unit** when the step opens may spend
  as much of its CPA as it likes. One that does not may spend at most **4 CP**
  or move one hex, whichever is more.
- Nothing but movement may be bought — except blowing a supply dump (SPI
  54.14, 32.3).
- Entering an enemy ZOC ends the retreat, and a unit may not go straight from
  one enemy ZOC into another; if it cannot avoid that, it may not retreat.
- Because the retreat is voluntary it is *not* the retreat forced by the
  close assault table ([forced retreats](#forced-retreats)).
- A unit that retreats into a friendly-held hex in enemy ZOC, or into any
  hex that is assaulted this segment, shares that hex's fate: it can be hit
  by anti-armour fire but cannot fire it; it adds no close-assault strength
  either way; and its TOE points count in the base for percentage losses.

## Anti-armour fire

::: spi 14.0

Units with an anti-armour rating fire at enemy points with an armour
protection rating. This happens before close assault and every loss is taken
before it, whichever role the armour was assigned to. A unit's TOE points may
be divided between anti-armour and close assault, never both for the same
point. Withheld units are neither firers nor targets. The procedure: both
players fire regardless of who is phasing, all fire is simultaneous, each
attack is against one hex nominated by the phasing player, and the actual
anti-armour points from every firing hex are totalled, two dice rolled and
the Anti-Armour Combat Results Table read for **damage points**, which the
owner of the target hex spends removing armoured TOE points. Place a
destroyed-tank marker where points were lost.

::: spi-omit 14.6 — the Anti-Armor Combat Results Table is a lookup table on the chart sheet; to `data/tables/anti-armour-results.json` when the sheet is captured

### Who fires and who is hit

::: spi 14.1 14.11 14.12 14.13 14.14

- Only units assigned to the anti-armour role fire; only units committed to
  anti-armour *or* close assault are hit. Withheld armour is untouched.
- The phasing player's fire is aimed at a whole adjacent hex, not at named
  units. The non-phasing player's fire is aimed at the armour-class units
  assaulting his hex.
- Units that retreated before assault into the target hex are hit by
  anti-armour fire, cannot be withheld from it, and cannot fire back.
- Artillery with an anti-armour rating fires only if forward; back artillery
  neither fires nor is hit. Anti-tank guns are always forward when they fire,
  and artillery in the anti-armour role has vulnerability 2.

::: spi 14.15

A **parenthesised** anti-armour rating (see
[fallback ratings](10-units-and-state.md)) may be used only when the hex has
no TOE points with an unparenthesised one; replacement points do not change
this.

The exchange always takes place *in the non-phasing player's hex*, but either
player may be firer, target or both (§32 clarification to 14.0).

### Restrictions

::: spi 14.2 14.21 14.22 14.23 14.24 14.25 14.26 14.27

- A hex is fired on **once** per combat segment; fire from several hexes pools
  into that one attack.
- The firer may not know whether the hex holds any armour. If it turns out to
  hold **none**, up to half (rounded down) of the anti-armour points aimed at
  it may be reassigned to close assault for this segment — only then.
- Ammunition is deducted as fired.
- Terrain column shifts ([below](#terrain-and-anti-armour)) are applied
  before rolling.
- The phasing player may send one unit's TOE points into *different*
  hexes, whether they are all firing anti-armour, all assaulting, or a mix
  (SPI 14.27, a §32 clarification).
- A withheld defender is safe from anti-armour fire but not from close
  assault.

### Terrain and anti-armour fire {#terrain-and-anti-armour}

::: spi 14.3 14.31 14.32 14.33 14.34 14.35

Terrain in the target hex shifts the points row toward the defender by the
amount on the Terrain Effects Chart (a rough hex takes 9 actual points down
to the 8 row). In-hex effects, fortifications included, are not cumulative —
the defender takes the best one — but a **hexside** effect adds to the in-hex
one. A shift below row 1 uses row 0.

No anti-armour fire crosses, in either direction, a ridge hexside without a
road or track, a slope hexside *downward* without road or track, or an
escarpment hexside *downward* without a track, when the phasing points
assault across it.

### Assessing damage {#assessing-damage}

::: spi 14.4 14.41 14.42 14.43 14.44 14.45 14.46 14.47 14.48

The table yields **damage points**. Each armoured TOE point absorbs damage
equal to its armour protection rating before it is destroyed; the owner must
remove enough points to absorb *at least* the damage rolled, from any unit
in the hex with an armour protection rating whichever role it was assigned
to. Excess damage is lost.

*Our example:* 6 damage points against a hex holding light tanks
(protection 2) and cruisers (protection 4). The owner may remove one cruiser
and one light tank (4 + 2 = 6), or three light tanks, but not one cruiser and
nothing else.

- Self-propelled guns absorb protection **plus** vulnerability per point
  (vulnerability as modified by the role they are in).
- If the only points in the hex that anti-armour fire could touch are
  **halftracks** (some Axis motorised infantry), their protection is doubled.
  A halftrack loss removes the infantry point and its carrying truck points.
- Destroyed tanks stay on the map as **destroyed-tank markers**: they cannot
  move but may be retrieved in the repair segment. Record exactly what each
  marker stands for.

### Capturing destroyed tanks

::: spi 14.5 14.51 14.52 14.53 14.54 14.55

Only destroyed *tanks* can be captured and repaired; every other destroyed
vehicle is removed at once. When enemy units enter a hex holding a
destroyed-tank marker and no friendly combat unit, the enemy decides on the
spot: eliminate the points for good, or own them from then on. Captured
tanks may be shifted up to three hexes immediately, avoiding enemy units,
enemy ZOC and impassable terrain; otherwise they are like any other unit
awaiting repair; the owner tows them to a repair facility in his repair
phase. Capturing destroyed tanks differs from capturing broken-down vehicles
(SPI 21.5, [Special](90-special.md)).
