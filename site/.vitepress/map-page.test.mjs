import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync, existsSync } from 'node:fs'

test('map page is generated, linked from the nav and served from site/public', () => {
  const cfg = readFileSync(new URL('./config.mts', import.meta.url), 'utf8')
  assert.match(cfg, /'site\/map\.md': 'map\.md'/)
  assert.match(cfg, /text: 'Map', link: '\/map'/)
  assert.match(cfg, /publicDir/)
  assert.ok(existsSync(new URL('../map.md', import.meta.url)))
  assert.ok(existsSync(new URL('../public/map/M.svg', import.meta.url)))
})
