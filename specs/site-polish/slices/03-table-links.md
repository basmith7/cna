# 03 Prose links to tables

Contract: a code span whose whole content is `data/tables/<name>.json` (name exists)
renders as a link to `/tables/<name>` labelled with the table's title; unknown names
and fenced code are untouched. Rules files are not edited.
Seam: `site/.vitepress/table-links.mjs` (markdown-it core/inline rule, reads titles
from the generated sidebar JSON). Test: `table-links.test.mjs`. Visual: rules/60-combat.
Factor the hard-coded `/cna/` base in `spi-badge.mjs` into one shared constant used by both plugins.
