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
rather than resolve it) are recorded as variants `V-nnn` with `::: variant`
containers, never as rulings.

## Process

1. Open a GitHub Discussion describing the problem with the case numbers.
2. Open a PR adding `R-nnn.md` as `proposed`, with the options written out.
3. Review. One maintainer accepts or rejects; the PR that accepts also edits
   the rules prose and adds the `::: ruling` annotation.
4. Anyone may dispute an accepted ruling by opening a new Discussion and a
   new `proposed` ruling that names the old one in `supersedes`.

## Fork policy

Disagreement is expected. If you want a different ruling than the one
accepted here, you are welcome and encouraged to fork: the rules and rulings
are CC-BY-SA 4.0, so a fork can keep everything, change any ruling, and
publish. We ask only that a fork say which rulings it changed. An engine
that consumes these rules should be able to point at a fork's `rules/` and
`rulings/` instead of ours.
