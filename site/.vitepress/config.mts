import { defineConfig } from 'vitepress'
import { spiBadgePlugin } from './spi-badge.mjs'

export default defineConfig({
  title: 'CNA Living Rules',
  description: 'A restated, reviewed edition of the Campaign for North Africa Land Game rules',
  base: '/cna/',
  srcDir: '..',
  srcExclude: ['node_modules/**', 'reference/**', 'docs/**', 'tools/**', 'tests/**', 'site/**', '.venv/**', 'EXTRACTION.md'],
  outDir: './.vitepress/dist',
  cacheDir: './.vitepress/cache',
  cleanUrls: true,
  lastUpdated: true,
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
