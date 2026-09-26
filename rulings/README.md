# Rulings

A **ruling** is a written decision on a gap, contradiction or ambiguity in
the 1979 rules (after errata). The rules prose always shows the *result* of
an accepted ruling; the ruling file shows the problem, the options and why.

## Files and numbering

One file per ruling: `rulings/R-nnn.md`, numbered sequentially from `R-001`
in the order they are opened. Numbers are never reused. Frontmatter:

```yaml
---
id: R-012
status: proposed            # proposed | accepted | rejected | superseded
affects: [8.37, 8.42]       # SPI cases the ruling touches
sources:                    # where the problem or a prior answer comes from
  - CNA1979:8.37
  - https://friendorfoe.com/war/cfna/houserules/#…   (NJHarman, CC-BY-SA 4.0)
supersedes: R-004           # optional
discussion: https://github.com/basmith7/cna/discussions/…
---
```

Body, in this order: **Problem** · **Options** (each with its consequence)
· **Decision** · **Rationale** · **Discussion** (link). Rules prose that
reflects the ruling carries `::: ruling R-012` above the block.

## Statuses

| Status | Meaning |
|---|---|
| `proposed` | Opened; not yet reflected in the rules prose. Seeded entries from NJHarman start here. |
| `accepted` | Reflected in the prose; the current rule. |
| `rejected` | Considered and not adopted; kept for the record. |
| `superseded` | Replaced by a later ruling named in `supersedes` of the newer file. |

Community **CHANGE** and **ADDITION** items (house rules that alter the game
rather than resolve it) are recorded as variants, never as rulings.
**REMINDER** items restate a printed rule and are not imported at all.

## Variants

A **variant** is a community change we record but do not adopt. One file per
variant, `rulings/V-nnn.md`, numbered sequentially from `V-001`; the same
frontmatter as a ruling, with `status: recorded` (or `superseded`). Body, in
this order: **What the printed rules say** · **The change** (quoted verbatim,
with the footnote, exactly as for a ruling) · **Effect on play** · **Why it is
recorded as a variant** · **Discussion**. The rules prose keeps the printed
rule and carries a `::: variant V-nnn — summary` badge below the block the
variant would alter; it never gets a `::: ruling` badge. A variant can be
reopened as a `proposed` ruling if discussion concludes the printed rule is a
misprint rather than a design choice.

## Quoting a third-party source

A seeded ruling quotes its source verbatim in **Problem** and **Options**,
as a blockquote, with a footnote after it that links to the section of the
source page the item came from:

```markdown
> On map printed Flak such as in Tripoli is considered heavy flak.[^nj-map]

[^nj-map]: NJHarman, *CfNA House Rules & Interpretations*, § Map,
  <https://friendorfoe.com/war/cfna/houserules/#map>, CC-BY-SA 4.0. See `ATTRIBUTION.md`.
```

The quoted text is not edited. **Decision** and **Rationale** are ours and
are never quoted. Every quoted source is listed in `ATTRIBUTION.md` at the
repo root; no SPI text is ever quoted.

## Process

1. Open a GitHub Discussion describing the problem with the case numbers.
2. Open a PR adding `R-nnn.md` as `proposed`, with the options written out.
3. Review. One maintainer accepts or rejects; the PR that accepts also edits
   the rules prose and adds the `::: ruling` annotation.
4. Anyone may dispute an accepted ruling by opening a new Discussion and a
   new `proposed` ruling that names the old one in `supersedes`.

## Who decides

Since 2026-09-26 the maintainer has delegated deciding rulings to this
project's unattended agent (see `AUTOPILOT.md`). It follows the order of
preference written there: the printed text first, then consistency, then
ease of implementation. Where a ruling can be tested numerically it cites a
probe from [cna-engine](https://github.com/basmith7/cna-engine). An accepted
ruling is no more final than any other: dispute it as in step 4 above.

## Fork policy

Disagreement is expected. If you want a different ruling than the one
accepted here, you are welcome and encouraged to fork: the rules and rulings
are CC-BY-SA 4.0, so a fork can keep everything, change any ruling, and
publish. We ask only that a fork say which rulings it changed. An engine
that consumes these rules should be able to point at a fork's `rules/` and
`rulings/` instead of ours.
