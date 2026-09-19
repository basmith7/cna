---
title: Units and state
status: provisional
---

# Units and state

This file defines what a **unit** is, the categories an engine must be able
to sort units into, the numbers each unit carries, and the state that changes
during play (strength, cohesion, morale, motorisation). Sequence, movement
and combat procedures that *use* these values live in their own files.

Draft in progress: §3 restated below; §6.2 (CPA ratings and the raw→actual
conversion) and §17 (cohesion) follow in later commits.

## Unit types

::: spi 3.21 3.23

Every counter has exactly one **type**. Types are fixed for the life of the
counter and decide which procedures apply to it.

| Type | Examples | Combat unit? |
|---|---|---|
| Infantry | foot, motorised, mechanised, motorcycle, heavy-weapons, garrison, airborne | yes |
| Tank | tank battalions and regiments | yes |
| Reconnaissance | armoured-car and recce battalions | yes |
| Anti-tank | towed and self-propelled anti-tank guns | yes |
| Anti-aircraft | flak batteries and regiments | yes |
| Artillery | field, medium and heavy guns; self-propelled; coastal | yes |
| Engineer | engineer companies and battalions | no (see [Engineering](80-engineering.md)) |
| Headquarters | divisional, brigade, regimental HQs | conditional (below) |
| Ground support | squadron ground support units (Air Game) | no |
| Recovery | tank recovery squadrons | no |
| Dummy tank formation | no counter; tracked on a log sheet | no |
| Truck | light and heavy trucks | no |

A **combat unit** is any unit of the six types marked *yes*. A headquarters
with combat units attached is also a combat unit. Some non-combat units count
as combat units for particular checks — zones of control, reconnaissance,
barrage targeting — and each such exception is stated where the check is
defined.

## Target classes

::: spi 3.22

For barrage, strafing and bombardment a unit is one of four **classes**.
Class is derived from type and from whether the unit's strength points carry
an armour protection rating (APR):

| Class | Members |
|---|---|
| Infantry | infantry type; engineers; ground support units; recce without APR; HQs that have a defensive close-assault rating but no APR |
| Armour | tank type; dummy tank formations; recovery squadrons; recce, HQ, artillery and anti-tank units that have an APR |
| Gun | artillery, anti-aircraft and anti-tank strength points without an APR, plus HQs and infantry that have a barrage rating |
| Truck | trucks |

An artillery or anti-tank counter whose strength points are partly armoured
and partly not is treated as **two targets**, one Armour-class and one
Gun-class, each with its own points.

## Headquarters

::: spi 3.3 3.31 3.32 3.33

A **headquarters** (HQ) counter stands in for every unit attached to it —
combat units, trucks and the supplies those trucks carry. On the map only
the HQ counter moves; the attached units are recorded on its log sheet.

- **Strength.** An HQ with combat units attached fights with the sum of
  their values and is a combat unit.
- **Speed.** The capability point allowance of an HQ (or any parent unit)
  is that of the slowest unit attached to it.
- **Stacking.** An HQ's printed stacking value assumes a full
  formation; a formation below full strength uses the equivalent rules in
  [Stacking and ZOC](50-stacking-and-zoc.md). An HQ with **no** combat units
  attached occupies zero stacking points, may use its parenthesised
  ratings, is not a combat unit, and may not attack.

::: spi 3.34

Some HQs (chiefly Italian regimental HQs) have guns of their own. Such an HQ
uses its printed combat values and takes gun losses like any unit; when the
last gun point is gone it is not destroyed but becomes a non-combat HQ.

::: spi 3.35

Armoured division and brigade HQs usually carry a small tank element,
visible in their ratings. Those tanks:

1. may fight only while the HQ has no combat units attached;
2. may never be transferred to another unit;
3. are rebuilt from the first tank replacement points available after loss;
4. exempt the HQ from breakdown.

::: spi 3.36

An HQ with no combat values at all (printed or parenthesised) that is alone
in a hex — no friendly combat unit present — is **captured** the moment an
enemy combat unit's zone of control covers the hex. Capture costs no
capability points and yields one prisoner point.

## Unit characteristics

::: spi 3.5

A counter is a bundle of **TOE strength points**; its abilities are those of
its points. A counter with no strength points has only a capability point
allowance. The characteristics an engine stores per unit:

| Characteristic | Meaning | Used by |
|---|---|---|
| Capability point allowance (CPA) | Budget for movement and combat each stage | [Capability points](30-capability-points.md) |
| Barrage rating | Strength when firing indirectly | [Combat](60-combat.md) |
| Vulnerability | How easily a gun is destroyed or captured in a forward position | [Combat](60-combat.md) |
| Anti-armour strength | Ability to destroy armoured vehicles | [Combat](60-combat.md) |
| Armour protection rating (APR) | Resistance to anti-armour fire | [Combat](60-combat.md) |
| Offensive close-assault rating | Strength when attacking in close assault | [Combat](60-combat.md) |
| Defensive assault rating | Strength when defending against close assault | [Combat](60-combat.md) |
| Anti-aircraft rating | Ability to shoot down aircraft | Air Game (abstracted in [§32](95-abstract-logistics-and-air.md)) |
| Maximum TOE strength | Full-strength point count | [Organisation](70-organisation.md) |
| Basic morale rating | Training and spirit, −3 to +3 | [Combat](60-combat.md) |
| Fuel rate | Fuel consumed per movement | [Movement](40-movement.md) |
| Breakdown adjustment | Mechanical reliability modifier | [Movement](40-movement.md) |

One strength point stands for roughly 100–200 men, a platoon of 5–8 armoured
vehicles, or a battery of four guns. Some Commonwealth units reach their
printed basic morale only after training ([Organisation](70-organisation.md)).

### Parenthesised ratings

::: spi 3.4

A rating printed in parentheses is a **fallback** value: it may be used only
when the unit is attacked while no friendly combat unit with an ordinary
(unparenthesised) rating of that kind shares its hex.

### Type notes with rule effect

The type descriptions in the original are mostly colour. These are the
statements in them that change play:

- **Motorised infantry** moves at truck speed only while it actually has
  trucks; otherwise it is foot infantry.
- **Motorcycle units** may not enter hexes closed to light trucks; they use
  no fuel and never break down.
- **Garrison units** (marked *G*) occupy zero stacking points in the town
  they were raised to garrison.
- **Artillery** has built-in transport that may not be stripped, uses fuel
  and water when moving, and does not break down. Guns of several calibres
  on one counter are one unit.
- **Self-propelled artillery** fires as a gun, has a vulnerability rating,
  can be killed by anti-tank fire, uses fuel and water, and does break down.
- **Coastal guns** have a CPA of 10 for combat (or their printed CPA if
  higher), move only with trucks assigned for the purpose, and if printed
  CPA is `0` are emplaced: no vulnerability rating; only barrage, capture
  or air bombardment can remove them. Motorised coastal guns break down.
- **Anti-tank units** are unarmoured unless self-propelled. Some non-AT
  points (British 25-pdr, German 88 mm, Italian 75/90 mm AA) also have
  anti-armour strength as printed.

---

*Drawn on: SPI §3 (in progress: §6.2, §17).*
