import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote'
import { spiBadgePlugin } from './spi-badge.mjs'

export default defineConfig({
  title: 'CNA Living Rules',
  description: 'A restated, reviewed edition of the Campaign for North Africa Land Game rules',
  base: '/cna/',
  srcDir: '..',
  srcExclude: ['node_modules/**', 'reference/**', 'docs/**', 'tools/**', 'tests/**', 'site/.vitepress/**', '.venv/**', 'EXTRACTION.md', '.superpowers/**', '.claude/**', '.github/**', 'coverage.md', 'site/public/**'],
  outDir: './.vitepress/dist',
  cacheDir: './.vitepress/cache',
  // srcDir is the repo root, so point Vite's public dir at site/public (the rendered map SVGs)
  vite: { publicDir: fileURLToPath(new URL('../public', import.meta.url)) },
  cleanUrls: true,
  lastUpdated: true,
  // Rules files are landing one PR at a time (see AUTOPILOT.md); cross-links to
  // sibling system files that are not written yet are expected until each lands.
  ignoreDeadLinks: [
    /\/(20-sequence-of-play|30-capability-points|40-movement|50-stacking-and-zoc|60-combat|70-organisation|80-engineering|90-special|95-abstract-logistics-and-air)$/,
  ],
  rewrites: {
    'README.md': 'index.md',
    'site/learn.md': 'learn.md',
    'site/map.md': 'map.md',
    'rulings/README.md': 'rulings/index.md',
    'data/README.md': 'data/index.md',
  },
  markdown: {
    config: (md) => { md.use(spiBadgePlugin); md.use(footnote) },
  },
  themeConfig: {
    // Client-side original-text viewer (design: "(generated) original" container). Fetched at view
    // time from the pinned transcription; set enabled: false to switch it off.
    original: {
      enabled: true,
      commit: '75a037f27346a7cd920a765a2f3cae965b1e07a3',
      rawUrlTemplate: 'https://raw.githubusercontent.com/tonicebrian/TheCampaignForNorthAfrica/{commit}/sections/section-{nn}.adoc',
    },
    nav: [
      { text: 'Rules', link: '/rules/00-overview' },
      { text: 'Learn', link: '/learn' },
      { text: 'Map', link: '/map' },
      { text: 'Rulings', link: '/rulings/register' },
      { text: 'Data', link: '/data/' },
    ],
    sidebar: {
      '/learn': [
        { text: 'Learn', items: [
          { text: 'A · One Operations Stage', link: '/learn#part-a' },
          { text: 'B · The combat maths', link: '/learn#part-b' },
          { text: 'C · How supply flows', link: '/learn#part-c' },
          { text: 'D · Graziani on the map', link: '/learn#part-d' },
        ] },
      ],
      '/rulings/': [
        { text: 'Rulings', items: [
          { text: 'Register', link: '/rulings/register' },
          { text: 'How rulings work', link: '/rulings/' },
        ] },
      ],
      '/rules/': [
        { text: 'Rules', items: [
          { text: 'Overview', link: '/rules/00-overview' },
          { text: 'Glossary', link: '/rules/glossary' },
          { text: 'Units and state', link: '/rules/10-units-and-state' },
          { text: 'Sequence of play', link: '/rules/20-sequence-of-play' },
          { text: 'Capability points', link: '/rules/30-capability-points' },
          { text: 'Movement', link: '/rules/40-movement' },
          { text: 'Stacking & ZOC', link: '/rules/50-stacking-and-zoc' },
          { text: 'Combat', link: '/rules/60-combat' },
          { text: 'Organisation', link: '/rules/70-organisation' },
          { text: 'Engineering', link: '/rules/80-engineering' },
          { text: 'Special rules', link: '/rules/90-special' },
          { text: 'Abstract logistics & air', link: '/rules/95-abstract-logistics-and-air' },
        ] },
        { text: 'Provenance', items: [
          { text: 'Changes from the original', link: '/rules/changes' },
          { text: 'Coverage', link: '/rules/coverage' },
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
