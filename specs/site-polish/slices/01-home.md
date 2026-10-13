# 01 Home page and nav

Contract: `/cna/` is a product landing page, not the README.

- `site/index.md` (layout: home): hero naming the game and what the site is in one
  sentence; actions "Start with Learn" and "Read the rules"; feature cards for
  Learn, Rules, Tables, Map, Rulings, each one line of plain language; a short
  "How to find a rule" block (search by topic or SPI case number, sidebar by system,
  case numbers in brackets) and "What this is / is not" (not affiliated, own words,
  errata folded in). No build commands, licences only in the footer.
- `config.mts`: rewrite `site/index.md` → `index.md`; `README.md` into `srcExclude`;
  description updated to cover Land, Logistics and Air games. Nav: Rules, Learn,
  Tables, Map, Rulings (Data conventions reachable from the Tables index).
- Check: dead-link check in build; README links from other pages (rulings link
  `rulings/README.md`, unaffected).
- Visual: home at desktop and mobile; screenshot-critique; compare with before/home.
- Delegated: card wording and order, hero tagline.
