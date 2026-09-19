---
title: Stacking, zones of control and reserve
status: provisional
---

# Stacking, zones of control and reserve

This file covers three things that constrain where units may be: how many
may share a hex (stacking), how a hex adjacent to the enemy behaves (zones of
control), and the reserve state that lets a unit react outside its own
segment. Movement procedure is in [movement](./40-movement.md); combat
results that force retreats are in combat.

::: spi-omit 9.0 9.1 9.2 9.4 — section and subsection headings, and a pointer to the counter sheet; rules restated below

## Stacking points

::: spi 9.11 9.12 9.15

Every counter carries a **stacking point** (SP) value on its face. Markers
and air units of every kind have none.

HQ counters (division, brigade, regiment) print their value in parentheses.
Such an HQ counts as **0 SP** while nothing is attached to it; the printed
number applies when the HQ is standing in for its formation as a combat unit
(see [unit equivalents](#unit-equivalents)).

::: spi 9.13

SP measure organisation as much as manpower. A full division is 5 SP even
when the counters attached to it add up to far more, because the divisional
HQ supplies the administration that lets them act as one body.

::: spi 9.14

Each terrain type has a stacking ceiling, given on the Terrain Effects Chart
(SPI 8.37, pending transcription to `data/`). The ceiling is enforced at the
end of every movement segment.

::: spi 9.16

Three kinds of unit ignore stacking in specific places:

- **Garrison** units (a "G" printed above the SP number) are 0 SP inside the
  city or village they garrison, and their printed value anywhere else.
- **Pure AA/flak** units are 0 SP in a major city. Beyond that, one AA unit
  may stack free at any air landing strip and three at any airfield.
- Units of **0+ CPA** that are currently *not* motorised (their trucks are
  attached but carrying them) are 0 SP.

## Unit equivalents

::: spi 9.21

A **division** means every unit assigned *and currently attached* to that
divisional HQ — not merely stacked with it. Units on the TOE sheet that have
been detached elsewhere are not part of the division for stacking.

::: spi 9.22 9.23 9.24

Below the division sits the **brigade equivalent**; below that the
**battalion equivalent**, the basic combat unit. Counter names mislead here:
Italian regiments are brigade equivalents, and the British called many
battalion-sized units "brigade" or "regiment". Read the SP value, not the
name, and look it up in the unit basic stacking table (counter sheet) to find
the organisational level. Every artillery unit is 1 SP regardless of its title,
apart from a few scattered batteries and the occasional larger artillery HQ.

::: spi 9.25

Companies and batteries printed with SP "?" are too small to count, but no
more than five such unattached units may be in one hex on top of whatever
else is there. There is no such limit in a major city hex. An HQ with nothing
attached is 0 SP.

::: spi 9.26 9.27 9.28

A formation is a **shell** (see [units & state](./10-units-and-state.md))
when too little of it is present:

| Formation | Shell when |
|---|---|
| Division | 50% or fewer of its assignable brigade equivalents are attached (independent battalions ignored) |
| Brigade | fewer than two-thirds of its assignable battalions are attached — but a two-battalion brigade with both attached is not a shell if at least one of them is itself not a shell |
| Battalion | under 50% of its TOE strength points are attached; artillery units only under 25% |

A shell attached to a parent does not count toward the parent's quota: a
three-brigade division with three attached, two of them shells, is itself a
shell. A shell is treated one level smaller (division as brigade, brigade as
battalion, battalion as company) for unit differentiation in close assault and
for any other rule that keys on formation size.

::: spi 9.29

Attached (first-line) trucks never count toward formation size or road
stacking. Unattached truck convoys count toward **road space only**, never
toward the terrain ceiling.

## Effects of stacking {#roads}

::: spi 9.3 9.31 9.32

The ceiling applies once a friendly movement segment ends and again at the end
of an operations stage; it never applies mid-move. Units may pass through
friendly units freely, and may never *end* movement over the limit. Two
qualifications follow.

::: spi 9.33 9.34

**Road space.** A motorised unit using a road or track bonus may not pass
through friendly units on that road if doing so would exceed the **5 SP road
or track limit**. It must instead enter the hex without the road bonus, which
may be impossible where the terrain bars motorised movement — this is how
friendly units can block a track over an escarpment. A unit that ended its
move in a hex by road counts against that limit for later movers. Truck
convoys are counted separately. Off-road markers mark units that entered a
road hex without the bonus and so are not "on the road". Splitting a unit to
slip its parts through one at a time and recombining beyond is forbidden.

::: spi 9.35

**Retreats.** Involuntary retreats from the close assault table obey stacking.
A stack or formation may split and retreat into different hexes, but no part
may retreat *through* a hex in violation. Anything that cannot retreat for
this reason must stand and take extra losses (combat, SPI 15.82).

## Zones of control

::: spi-omit 10.0 10.1 10.2 10.3 — section and subsection headings; rules restated below

The six hexes around a unit are its **zone of control** (ZOC) if the unit is
big enough to exert one. Enemy units entering a controlled hex must stop.

### Who exerts a ZOC

::: spi 10.11 10.12 10.13 10.14 10.15

A hex exerts a ZOC when it holds **more than 1 SP** of combat units, whether
that is one larger-than-battalion unit or several small ones adding up.
Truck convoys, bare HQs, aircraft, squadron ground support units, warships,
and markers (dumps, minefields, airfields) never do. Nor do units at
**cohesion −26 or worse**, nor any hex whose contents total **fewer than 10
raw defensive close assault points** — anti-tank units are always taken as
up front for that count.

::: spi 10.16

Whenever a phasing unit starts a movement segment in, or moves into, a hex
that a non-phasing unit *could* control, the non-phasing player must say
whether that unit exerts a ZOC.

### What a ZOC does

::: spi 10.21

A ZOC reaches every adjacent hex except across all-sea, major river, lake
and escarpment hexsides, and except into a hex the unit itself could not
enter from where it stands (a tank battalion projects no ZOC into salt marsh
unless a road or track joins the two hexes).

::: spi 10.22 10.23 10.24 10.25

Entering an enemy ZOC costs no CP, but the unit must stop there and cannot
leave until a later movement segment; leaving then costs the break-off price
([movement](./40-movement.md)). A unit may never move straight from one
controlled hex into another, and may never *retreat* into one. The single
exception: a unit may always follow into an adjacent hex the enemy has just
vacated through combat, retreat before assault or reaction — this is ordinary
movement in the next movement segment, paid in CP, not an advance after
combat. Hexes next to an enemy unit that it does not control are free to
pass through.

::: spi 10.26 10.27 10.28

A friendly combat unit in a hex cancels enemy ZOC there for all movement
purposes, and friendly ZOCs never hinder friendly units. Two opposing units
projecting ZOC onto each other are each in the other's ZOC; a hex both sides
project into is controlled by both. Several units controlling the same hex
have no extra effect.

::: spi 10.29

Truck convoys may enter an enemy ZOC only where a friendly combat unit already
sits. No non-combat unit (bare HQ, engineer, squadron ground support, etc.)
may ever voluntarily enter an *unoccupied* enemy-controlled hex, and one that
is alone in an enemy ZOC during the enemy movement/combat phase with no
strength of any kind is **captured**.

### ZOC combat requirement (holding off)

::: spi 10.31 10.32

Every enemy hex that projects a ZOC onto friendly combat units must be
attacked in the friendly combat segment, by barrage or by close assault. A
probe counts if its basic differential is −4 or better. Exempt: hexes whose
friendly contents are only artillery, anti-tank, AA or non-combat units, or
whose other units are pinned.

::: spi 10.33 10.34 10.35

The attack may be a **holding-off barrage**: a barrage on the enemy hex with
actual barrage strength (barrage rating × TOE strength + 10) at least equal to
the number of non-gun enemy battalion equivalents in it (sub-1-SP units and
gun units are not counted). A division of eleven battalion equivalents needs
11 points. A formation in the ZOC of two enemy hexes may hold off one and
close-assault the other. If the barrage cannot be mustered, the hex must be
close-assaulted; there is no minimum for that.

::: spi 10.36

A unit that can do neither must **retreat three hexes** away from the enemy
unit — no doubling back, spending all its CP — and takes 3 disorganisation
points on top of any the retreat itself causes. The route may not pass through
enemy ZOC; if it is forced into one the whole unit surrenders.

## Reserve {#reserve}

*Pending — SPI §18.*
