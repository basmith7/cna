import test from 'node:test'
import assert from 'node:assert/strict'
import { fit, clamp, zoomAt, pan } from './map-view.mjs'

const content = { w: 1000, h: 1200 }

test('fit scales to the tighter axis and centres the other', () => {
  const v = fit({ w: 600, h: 600 }, content)
  assert.equal(v.k, 0.5)
  assert.equal(v.x, 50)
  assert.equal(v.y, 0)
})

test('zoomAt keeps the anchored content point stationary', () => {
  const v = { k: 1, x: -100, y: -40 }
  const z = zoomAt(v, 2, 300, 200, 0.1)
  const before = [(300 - v.x) / v.k, (200 - v.y) / v.k]
  const after = [(300 - z.x) / z.k, (200 - z.y) / z.k]
  assert.deepEqual(after, before)
  assert.equal(z.k, 2)
})

test('zoomAt respects min and max scale', () => {
  assert.equal(zoomAt({ k: 3, x: 0, y: 0 }, 10, 0, 0, 0.5).k, 4)
  assert.equal(zoomAt({ k: 1, x: 0, y: 0 }, 0.001, 0, 0, 0.5).k, 0.5)
})

test('clamp centres small content and keeps large content reachable', () => {
  const box = { w: 800, h: 600 }
  const small = clamp({ k: 0.4, x: 999, y: 999 }, box, content, 0.1)
  assert.equal(small.x, (800 - 400) / 2)
  const big = clamp({ k: 2, x: 5000, y: -9999 }, box, content, 0.1)
  assert.equal(big.x, 800 - 48)
  assert.equal(big.y, 48 - 2400)
})

test('pan offsets without changing scale', () => {
  assert.deepEqual(pan({ k: 2, x: 1, y: 2 }, 3, 4), { k: 2, x: 4, y: 6 })
})
