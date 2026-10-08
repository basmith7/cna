import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote'
import { spiBadgePlugin } from './spi-badge.mjs'

export default defineConfig({
  title: 'CNA Living Rules',
  description: 'A restated, reviewed edition of the Campaign for North Africa Land Game rules',
  base: '/cna/',
  srcDir: '..',
  srcExclude: ['node_modules/**', 'reference/**', 'docs/**', 'tools/**', 'tests/**', 'site/.vitepress/**', '.venv/**', 'EXTRACTION.md', 'AUTOPILOT.md', 'ATTRIBUTION.md', '.superpowers/**', '.claude/**', '.github/**', 'coverage.md', 'site/public/**'],
  outDir: './.vitepress/dist',
  cacheDir: './.vitepress/cache',
  // srcDir is the repo root, so point Vite's public dir at site/public (the rendered map SVGs)
  vite: { publicDir: fileURLToPath(new URL('../public', import.meta.url)) },
  cleanUrls: true,
  lastUpdated: true,

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
        { text: 'Logistics Game', items: [
          { text: 'Overview & sequence', link: '/rules/logistics/00-overview-and-sequence' },
          { text: 'Fuel', link: '/rules/logistics/10-fuel' },
          { text: 'Ammunition & stores', link: '/rules/logistics/20-ammunition-and-stores' },
          { text: 'Water', link: '/rules/logistics/30-water' },
          { text: 'Trucks & dumps', link: '/rules/logistics/40-trucks-and-dumps' },
          { text: 'Ports & shipping', link: '/rules/logistics/50-ports-and-shipping' },
          { text: 'Abstract air', link: '/rules/logistics/60-abstract-air' },
        ] },
        { text: 'Air Game', items: [
          { text: 'Overview & sequence', link: '/rules/air/00-overview-and-sequence' },
          { text: 'Air facilities', link: '/rules/air/20-air-facilities' },
          { text: 'Flight & maintenance', link: '/rules/air/30-flight-and-maintenance' },
        ] },
        { text: 'Scenarios', items: [
          { text: 'Reading a scenario', link: '/rules/scenarios/00-reading-scenarios' },
          { text: 'Group One — the Italians', link: '/rules/scenarios/10-the-italians' },
          { text: 'Group Two — the Desert Fox', link: '/rules/scenarios/20-desert-fox' },
          { text: 'Group Three — Crusader', link: '/rules/scenarios/30-crusader' },
          { text: 'Group Four — El Alamein', link: '/rules/scenarios/40-el-alamein' },
          { text: 'Group Five — the campaign game', link: '/rules/scenarios/50-campaign-game' },
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
