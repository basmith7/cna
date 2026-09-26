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

::: errata E-001 — 11.32 printed "+" for the multiplication; the formula is rating × strength

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

::: spi 12.6

The table itself is data, not prose: `data/tables/barrage-results.json`
holds every cell (target class × barrage-point band → dice range → result),
transcribed from the chart sheet and cross-checked against a second scan.
Its shape: at 1–2 points only infantry and armour can even be pinned and
trucks are untouchable; from 13 points up every class can lose points, and
at 17+ a truck column is hit on a 33 or better.

- **P — pinned.** The target unit — that one battalion-equivalent, never
  the hex or the division it belongs to — is pinned for the rest of the
  combat segment: it may not move, fire anti-armour or close assault, and it
  still takes casualties (SPI 15.12). Mark it; remove the marker when the
  segment ends. Gun-class units and artillery HQs are never pinned by
  barrage.

::: errata E-002 — 12.44: barrage is always against a specific target, so a pin covers only the battalion-equivalent fired at

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

::: spi 14.6

The table is data: `data/tables/anti-armour-results.json` holds the full
grid — eighteen dice-pair rows (11–12 up to 65–66) by seventeen point
columns (0 to 16+) of damage points, transcribed from the chart sheet and
cross-checked against a second scan. Damage rises smoothly with both
points and dice, from nothing at all below three points on a low roll to
32 damage at 16+ points on a 63 or better. The starred 0 column is only
reached by a firing side with fewer than five raw points, or by shifts
(SPI 14.33). The phasing player reads one row lower than rolled (an 11 or
12 stays put).

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

- Self-propelled guns absorb by armour protection like any other armoured
  point. An SP gun barraging from a *back* position is outside anti-armour
  fire altogether: it neither absorbs damage nor suffers it.
- If the only points in the hex that anti-armour fire could touch are
  **halftracks** (some Axis motorised infantry), their protection is doubled
  and no more than **two** halftrack points can be lost to anti-armour fire
  in one segment. A halftrack loss removes the infantry point and its
  carrying truck points.

::: errata E-003 — 14.47 as printed (protection plus vulnerability) is withdrawn; SP guns use protection only, and a back SP gun is untouched

::: errata E-004 — 14.48 addition: two-point cap per segment on halftrack losses

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

## Close assault

::: spi 15.0

Close assault is the last step. The phasing player attacks; the non-phasing
player defends; any adjacent enemy-held hex may be assaulted unless terrain
forbids it. Each side totals its actual close-assault points (offensive for
the attacker, defensive for the defender) for that one assault; the
**differential** is attacker minus defender. Terrain, morale, combined arms
and the size of the formations engaged then shift the *column*, not the
number. Each player rolls two dice once, reads them sequentially (large die
first: 6 and 3 is *63*) on his own half of the Close Assault CRT under the
adjusted column, and takes the result — a percentage loss, possibly with
*engaged*, *retreat* or *captured* — before the next hex is assaulted. Both
sides spend ammunition. A weak attack is a **probe** ([below](#probes)).

::: spi 15.89

The Prisoners Captured Results Table is data: `data/tables/prisoners-captured.json`
— one die, and a tenth to three-quarters of the losses just taken are
prisoners, rising with the roll (a 4 and a 5 both give half).

### Who takes part

::: spi 15.1 15.11 15.12 15.13 15.14 15.15 15.16 15.17 15.18

- Any unit with a close-assault rating may add it, offensively or
  defensively; units without one may still be present, adding nothing.
- Only units *committed* to the assault contribute points. But on the
  defending side, units that add nothing can still lose: **pinned** units,
  units that **retreated before assault** into the hex, units **out of
  ammunition**, and individual TOE points the defender **withholds** all
  count in the base from which percentage losses are taken. On the attacking
  side, out-of-ammunition and withheld points are simply ignored.
- A unit out of ammunition cannot assault or defend. If *every* defending
  unit in an assaulted hex is out of ammunition, the whole hex surrenders.
- Back guns are untouched by close assault except in an overrun
  ([gun losses](#gun-losses)); forward guns may fight, at the vulnerability
  penalties in [forward and back](#forward-and-back).
- An attacker may split a unit's TOE points between assaults, or hold some
  back. A hex is never close-assaulted twice in one segment.
- **Parenthesised** close-assault ratings count only when the unit is in a
  hex with no combat units. Such a unit stacked with combat units stays out
  of the loss base unless the losing player wants it in, and then it absorbs
  at most 25 % of the losses. When one attack covers two hexes and one of
  them holds only a parenthesised-rating unit, that unit fights at its
  rating.
- Against a hex defended *only* by parenthesised ratings, an attacker with at
  least **three times** the defender's raw strength ignores the first 20 % of
  his own losses, and if the defender's result is 20 % or worse every
  surviving defending TOE point is captured (provided the attacker survives).
  A flak battery can see off a patrol; not a battalion.

### Procedure

::: spi 15.2 15.21 15.22 15.23 15.24 15.25 15.26 15.27 15.28 15.29

1. The attacker names the hexes he assaults. Units assigned to anti-armour
   fire cannot join (except for points released under the "no armour"
   rule, SPI 14.23). A hex may be assaulted or probed **once** per segment, by
   as many units from as many adjacent hexes as terrain allows; the attacker
   may not split a hex's defenders between separate attacks. One unit may
   assault **several hexes at once** if every assaulted hex is adjacent both
   to the unit's hex and to each other.
2. Each side totals its actual points; the attacker declares assault or
   probe — a declaration he may defer until the fight is over
   ([probes](#probes)). Assaults resolve one at a time, results applied as
   they come.
3. **Basic differential** = attacker's actual points − defender's. 6 against
   8 is −2.
4. **Adjusted differential**: shift the column for terrain
   ([below](#terrain-and-close-assault)), combined arms, size difference and
   morale; the shifts accumulate. Roll on the adjusted column, dice read
   sequentially.

The **50 % rule**: an attack is a full close assault only if the attacking
units have committed at least half their available TOE points to *some*
assault this segment — otherwise every one of their attacks is a probe.
*Our example:* a 6-point battalion sends 2 points at one hex and 1 at
another, keeping 3 back: two probes. Send 3 at the first hex instead and both
attacks are full assaults.

Raw-point floors, for close assault and probe only: a side with **fewer than
5 raw** points has zero; if **both** sides are under 10 raw, use raw as
actual.

If the **defender** commits nothing at all, his whole hex retreats three
hexes and takes 3 DP (as for a 30 % loss), on top of DP for the move. If the
**attacker** commits nothing there is no assault — which can only arise from
the holding-off rule (SPI 10.31).

### Terrain and close assault {#terrain-and-close-assault}

::: spi 15.3 15.31 15.32 15.33 15.34 15.35 15.36

Terrain shifts come from the Terrain Effects Chart (SPI 8.37,
`data/tables/terrain-effects.json`) and, unlike barrage and anti-armour, **accumulate**:

- The defender's hex either does nothing (clear, sand/gravel) or shifts
  columns his way — a +4 assault on a mountain hex with a three-column
  benefit is fought at +1. Salt marsh is the reverse: one column *for the
  attacker*.
- A hexside the attackers cross shifts the column too (a wadi costs the
  attacker one). If *any* attacking unit crosses a given hexside, the whole
  assault is adjusted as if all did. The defender benefits from only one
  hexside type, unless a single hexside genuinely carries two (rare; some
  southern wadis run along slopes).
- Assaulting *down* a slope or escarpment favours the attacker. Where an
  assault comes both up and down, the two offset: +1 for a down-slope side
  and −3 for an up-escarpment side is a net −2.

*Our example:* a defender in a level-two fortification on rough ground,
assaulted across a ridge, gets two + two + two = six columns.

Prohibitions: motorised units never assault **up an escarpment** (track or
no track — dismount first) and never assault a defender in **salt marsh**. A
combat unit in the ZOC of an enemy it cannot attack must retreat one hex
unless another unit attacks that enemy.

### Combined arms

::: spi 15.4

Tanks — tanks only, not recce or self-propelled guns — need infantry beside
them. For every TOE point of tanks in an assault there must be a TOE point of
infantry, machine-gun or heavy-weapons units assaulting **from the same
hex**. Each 1–3 unsupported tank points cost the tanks **one actual** point
of close-assault strength, to a maximum reduction of four. It applies on
defence as on attack. Two unsupported points of tanks rated 7 (14 raw → 1
actual) drop to zero; four unsupported points (28 raw → 3 actual, two
bands of 1–3) drop to 1.

::: errata E-005 — 15.4 example corrected: four unsupported points reduce to one, not two

### Size of formation

::: spi 15.5 15.51 15.52 15.53 15.54 15.55

Organisation counts independently of strength:

- **Double raw strength.** Whatever the differential, a side with at least
  twice the other's raw close-assault points shifts **two columns** its way.
  24 raw against 12 (2 actual against 1: a +1 differential) fights at +3.
  Only SPI 15.54 below suspends this.
- **All defenders pinned.** If every unit in the assaulted hex is pinned,
  the hex defends at **zero** and the column shifts **two** to the attacker
  (standing in for the double-strength shift).

::: errata E-007 — 15.56 addition

- **Largest unit.** If the largest unit equivalent
  ([Stacking & ZOC](50-stacking-and-zoc.md#unit-equivalents)) on one side
  outranks the other's, the larger side shifts by the table below
  (`data/tables/assault-size-shifts.json`). A brigade counts as part of a
  division only if its **HQ counter** is attached: nine infantry battalions
  under a divisional HQ with no brigade HQs are a shell here. The two Italian
  "m" brigade counters each stand for a whole brigade.

::: errata E-006 — 15.53 table: "brigade" is a smaller-side entry (3-point / 2-point brigade), misprinted under the shift column

| Larger side ↓ / smaller side → | 3-SP brigade | 2-SP brigade | battalion | company |
|---|---|---|---|---|
| division | 1 | 2 | 4 | 8 |
| brigade (any) | — | — | 2 | 4 |
| battalion | — | — | — | 2 |

- **No defensive rating.** Some guns (heavy howitzers) have no defensive
  close-assault rating at all. Alone in an assaulted hex such a unit defends
  at zero, the attacker takes **no losses**, and the column shifts **three**
  more the attacker's way on top of the size table; the double-strength shift
  does not apply.

### Morale

::: spi 15.6 15.61 15.62 15.63 15.64

Each side finds its adjusted morale for the assault
([Units & state](10-units-and-state.md), SPI 17.2), using the largest-unit
rule for mixed forces. **Attacker's minus defender's** is the number of
columns to shift: positive to the right (for the attacker), negative to the
left.

*Our example:* two Axis divisions at basic morale +3 and +1 average to +2;
their cohesion is −4, and the Morale Modification Table roll gives −2, so
the adjusted Axis morale is 0. The defending division is at +1 with cohesion
+2 and rolls no change: +1. Final adjustment 0 − 1 = **−1**, one column for
the defender.

### Reading the CRT

::: spi 15.7 15.71 15.72 15.73 15.74 15.75 15.76 15.77 15.78

Each player rolls two dice **once** per assault and reads them three ways.
Both use the same adjusted column but their own half of the table (attacker
or defender):

1. **Sequential** (large die first, 2 and 5 → 25): find where it falls in
   the column; the row gives the percentage loss. At +3 an attacker rolling
   34 might land in the 5 % row.
2. **Summed** (3 + 4 = 7): read the *engaged* line (attacker's half) or the
   *retreat* line (defender's half) at the bottom of the column. A defender
   whose 7 sits in the "retreat one hex" range must move or lose a further
   10 %.
3. **Summed again** against the *captured* line of the column: if it hits,
   roll one die on the Prisoners Captured Results Table for the share of the
   losses that are prisoners rather than dead.

A zero-loss roll can still produce engaged or retreat. If the same assault
yields both a retreat and an engaged result, the retreat wins and engaged is
ignored.

::: spi 15.79

The table is data: `data/tables/close-assault-results.json` holds both
halves — eighteen differential columns from −11-and-worse to +17-and-better,
nine loss rows (50 % down to 0) of sequential-reading ranges per side, and
the summed-dice lines for capture, engaged and retreat of one to three
hexes. Its shape: at −11 an attacker loses 50 % on any 11–15 and never
escapes unhurt, while a defender there cannot lose more than 10 %; at 0 the
two halves are near mirror images; from +11 the defender's table runs from
40 % on a low roll to nothing only on a 66, and the attacker's stops at 10 %.
The +4 column carries SPI's one errata correction to this table (E-008);
two further printed oddities are declared in the file's notes and await a
ruling.

::: errata E-008 — 15.79: defender losses, +4 column, 10 % row, read 34–45 (the printed 24–45 overlapped the 15 % row)

The **+11 and higher** columns are the *overrun* zone. Overrun is not
chosen; it means the attacker's mass has broken the line and reached the
guns: all defender losses round **up**, and every defending gun is exposed
([gun losses](#gun-losses)).

### Casualties {#casualties}

::: spi 15.8 15.81 15.82 15.83 15.85 15.86 15.87 15.88

#### Engaged

Every unit in the assault is locked to the enemy: leaving the
ZOC costs the engaged break-off price
([breaking off](40-movement.md#breaking-off)). Mark them; markers come off at
the end of the operations stage. Units that fought and are still adjacent but
not engaged are in *contact*.

#### Forced retreats {#forced-retreats}

A retreat of *n* hexes: everything in the hex — pinned,
withheld, out of ammunition included — must end at least *n* hexes from the
enemy that forced it, by the easiest path toward the nearest friendly supply
dump or city, paying CP as for any move. Each hex of the *n* not retreated,
by choice or necessity, costs a further **10 %** loss. Units in a major city,
or retreating into one, may stop there and ignore the rest.

#### Percentage losses

::: ruling R-011 — each side's percentage is taken of its own raw points, not the combined total

Take the percentage from the table, then:

1. Each side totals **its own** raw close-assault points in the assault
   ([R-011](../rulings/R-011.md)). The defender adds the raw points of his
   pinned and retreated-in units, and in an overrun of *every* withheld unit
   too.
2. Multiply. The attacker rounds **up**, the defender **down** — except in
   an overrun, where the defender rounds up too (35.1 → 36 attacker, 35
   defender; 1.1 → 2 for an overrun defender). Add any hexes-not-retreated
   percentage.
3. Remove TOE points whose ratings absorb the raw points lost — an infantry
   point with defensive rating 2 absorbs 2 raw — using the rating that was
   in use (offensive for the attacker). Only participating units, plus for
   the defender pinned or withheld ones, may absorb.
4. Where the points came from more than one hex, share the losses across
   hexes in proportion to the raw points each supplied.

#### Captured

The captured share, rounded **up**, of the losses just taken
becomes prisoners or captured equipment for the enemy: decide which TOE
points died, take the captured percentage of them (any type of point may be
used, remembering the percentage is of raw assault points, not TOE points),
and hand them over — one prisoner point per infantry-type TOE point; guns
and tanks pass to the enemy to use (SPI 28.0, [Special](90-special.md)).

#### Disorganisation

A side that loses **30 % or more** of the TOE points it
committed (from committed units or not) gives every unit involved **3 DP**.
Both sides can suffer this in one assault.

#### Surrender

A player may surrender units rather than see them destroyed.
Units out of ammunition, or at cohesion **−17 or worse**, surrender
automatically when assaulted (SPI 17.25,
[voluntary surrender](10-units-and-state.md)). The two thresholds differ:
−17 needs an actual assault, whereas a unit at **−26** surrenders as soon
as an enemy moves adjacent ([cohesion](10-units-and-state.md), SPI 6.26).

::: errata E-009 — 15.88 clarified against 6.26: −17 surrenders when assaulted, −26 when approached

### Gun losses {#gun-losses}

::: spi 15.84

Guns — artillery, anti-tank and the like — lose in close assault as follows:

- **Overrun:** every defending gun, forward or back, adds its defensive
  close-assault points to the loss base and may be used to absorb losses.
- **Forward guns**, whether or not they fought, are hit by vulnerability
  loss: remove forward-gun TOE points whose vulnerability ratings total at
  least **half** the raw points lost in the assault, and at least one
  vulnerability point whenever any raw point was lost. Vulnerability absorbs
  exactly like armour protection ([assessing damage](#assessing-damage)).
  AA/flak units are exempt.
- In an overrun, back guns take the vulnerability loss too, after the
  percentage loss.

*Our example:* an attacker with artillery forward loses 4 raw points; he must
strip 2 vulnerability points, and since each of his guns is rated 9 that
means one whole gun TOE point.

### Probes {#probes}

::: spi 15.9 15.91 15.92 15.93 15.94 15.95 15.96

A **probe** is any close assault by the phasing player made with less than
half of his available TOE points committed to any attack that segment
(the 50 % rule above; see also the holding-off rule, SPI 10.31). Any number of
units may probe. It resolves exactly as an assault, except:

- *Engaged* results are ignored and neither side ends in contact.
- The attacker need not say it was a probe until it is over; assignment to
  close assault still happens before anti-armour fire.
- If every probing unit is recce, the probers' losses are cut by 10 %.
- Defenders of a probe whose adjusted differential ends worse than −3 pay
  no CP at all (compare the −4 refund for a full assault in the
  [CP table](#cp-cost-of-combat)).

## Patrols and reconnaissance

::: spi 16.0

A patrol buys information. In the patrol phase of a stage in which the
phasing player has fired no anti-armour and made no close assault, he may
detach **patrol points** from eligible units to reconnoitre an enemy hex.
Nothing moves; the procedure is abstract: announce the points and the target
hex, pay fuel and ammunition, roll one die on the Patrol Survival Table for
patrol losses (skipped when the target holds no combat units), roll one die
on the Reconnaissance Table against the surviving points to learn how many
units the enemy must describe, then roll one die on the Objective Loss Table
for casualties among the units patrolled. Nothing is recorded as moving.

::: spi 16.7 16.8

The Reconnaissance and Objective Loss tables are data:
`data/tables/patrol-reconnaissance.json` (die × net patrol points → how many
battalion-equivalents are described; three points on a 6 reveal everything,
one point on a 1 or 2 nothing) and `data/tables/objective-loss.json` (a 5
captures one TOE point, a 6 kills one, anything lower does nothing; a
capture by a patrol that was itself wiped out counts as a kill).

::: spi 16.6

The Patrol Survival Table is data: `data/tables/patrol-survival.json` — a
4 costs the patrol a captured point, a 5 a killed one, a 6 both; an
all-recce patrol takes one off the die.

### Who may patrol

::: spi 16.1 16.11 16.12 16.13 16.14 16.15 16.16 16.17

- Patrol points come only from **recce**, **light tank** (CV/33, L/6, Mark VI
  Light, Stuart, Panzer I), **motorised infantry** and **mechanised infantry**
  (Panzergrenadiers included) TOE points.

::: errata E-010 — 16.11 addition: L/6, Stuarts and mechanised infantry join the patrol list
 The owner detaches
  the points on his TOE log and notes any losses against them.
- At most **2** points may leave any one hex, however many units it holds;
  at most **3** may be sent against one target hex, pooled from several
  hexes.
- A unit at cohesion **−8 or worse** cannot supply patrol points.
- Each point costs **1 ammunition and 2 fuel**, taken from the hex it
  starts in, win or lose.
- No patrol starts in or enters a hex under **rainstorm or sandstorm**.

### When and where

::: spi 16.2 16.21 16.22

Patrols are allowed in any stage in which the phasing player has not fired
anti-armour or close-assaulted anyone. Barrage does not forbid patrolling,
but a hex that has been barraged or bombed this stage cannot be patrolled.
There is no limit on the number of patrols. The target may be any
enemy-occupied hex within **five hexes** by a path the patrolling unit types
could pass, avoiding enemy-occupied or enemy-controlled hexes other than the
target's own ZOC.

### Patrol losses

::: spi 16.3 16.31 16.32 16.33 16.34

Both sides check for losses, at different moments.

1. **Patroller first.** Unless the defender declares that the hex holds no
   combat units (AA/flak and engineers do not count as combat units here),
   roll on the Patrol Survival Table, subtracting **1** if every patrol point
   is recce. Losses — eliminated or captured points, trucks included — come
   off at once, the patroller choosing which unit type; captured points
   become prisoner points. A wiped-out patrol learns nothing.
2. **Patrolled second.** After the information step (or after the patrol is
   destroyed, whichever is first), the patroller rolls on the Objective Loss
   Table regardless of his own losses. If his patrol was wholly destroyed, a
   *captured* result there reads as *eliminated*. The defender picks the TOE
   points lost, from a combat unit if he has one; otherwise from trucks, then
   AA/flak, then engineers, then HQ points, in that order.

### Dummy tank formations {#dummy-tank-formations}

::: spi 16.4 16.41 16.42 16.43 16.44 16.45 16.46 16.47

A **dummy tank formation** is the size of a tank battalion, is worth nothing
in combat and has CPA 0. There is no counter: it is created in the
construction segment by spending **10 stores** present in the hex, and it
may carry the identity of a real tank battalion that is elsewhere on the
map. Limits: **three** per player at once, **one** per hex, and never in an
Italian formation, even a mixed one.

Its one use is deception. When the hex is reconnoitred its owner may report
the dummy as a tank battalion of any strength he likes; the patroller cannot
tell until he attacks. It dies as soon as its formation is close-assaulted,
or when the formation takes anti-armour fire while holding no real armour
(or after losing all of it). Anti-armour fire aimed at dummies cannot be
diverted to close assault under the "no armour" rule when the only armour
was the dummy. (The Household Cavalry Regiment, which ran the Commonwealth
dummies, is not on the OA sheets for this reason.)

### What a patrol learns

::: spi 16.5 16.51 16.52 16.53 16.54 16.55

The Reconnaissance Table gives the number of battalion-sized units the
defender must describe; two points rolling well might reveal two units. For
each, the defender states its historical designation, its unit type, whether
it is motorised, and its TOE strength **to within two** of the true figure —
not the types of point inside it, so a tank battalion of eight mixed marks
can be reported simply as a six-point tank battalion (§32 clarification).

The defender chooses which units to describe if the hex holds more than the
number required, within these limits: battalions, unless the hex holds
nothing but smaller or larger units; never HQ or AA/flak units while combat
units are in the hex (engineers may be named); and never a unit the
patroller has explicitly excluded beforehand — typically one he already knows
from an earlier patrol or fight.

---

*Drawn on: SPI §11, §12, §13, §14, §15, §16, the §32 addenda to 12.0–16.51, and the September 1979 errata (E-001–E-010).*
