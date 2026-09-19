import { defineConfig } from 'vitepress'
import { spiBadgePlugin } from './spi-badge.mjs'

export default defineConfig({
  title: 'CNA Living Rules',
  description: 'A restated, reviewed edition of the Campaign for North Africa Land Game rules',
  base: '/cna/',
  srcDir: '..',
  srcExclude: ['node_modules/**', 'reference/**', 'docs/**', 'tools/**', 'tests/**', 'site/**', '.venv/**', 'EXTRACTION.md', '.superpowers/**', '.claude/**', '.github/**', 'coverage.md'],
  outDir: './.vitepress/dist',
  cacheDir: './.vitepress/cache',
  cleanUrls: true,
  lastUpdated: true,
  // Rules files are landing one PR at a time (see AUTOPILOT.md); cross-links to
  // sibling system files that are not written yet are expected until each lands.
  ignoreDeadLinks: [
    /\/(20-sequence-of-play|30-capability-points|40-movement|50-stacking-and-zoc|60-combat|70-organisation|80-engineering|90-special|95-abstract-logistics-and-air)$/,
  ],
  rewrites: {
    'README.md': 'index.md',
    'rulings/README.md': 'rulings/index.md',
    'data/README.md': 'data/index.md',
  },
  markdown: {
    config: (md) => { md.use(spiBadgePlugin) },
  },
  themeConfig: {
    nav: [
      { text: 'Rules', link: '/rules/00-overview' },
      { text: 'Rulings', link: '/rulings/' },
      { text: 'Data', link: '/data/' },
    ],
    sidebar: {
      '/rules/': [
        { text: 'Rules', items: [
          { text: 'Overview', link: '/rules/00-overview' },
          { text: 'Glossary', link: '/rules/glossary' },
          { text: 'Units and state', link: '/rules/10-units-and-state' },
          { text: 'Sequence of play', link: '/rules/20-sequence-of-play' },
          { text: 'Capability points', link: '/rules/30-capability-points' },
          { text: 'Movement', link: '/rules/40-movement' },
        ] },
      ],
    },
    search: { provider: 'local' },
    editLink: { pattern: 'https://github.com/basmith7/cna/edit/main/:path', text: 'Propose an edit' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/basmith7/cna' }],
    outline: [2, 3],
    footer: { message: 'Rules CC-BY-SA-4.0 · Data CC0 · Code MIT. Not affiliated with SPI or its successors.' },
  },
})
