import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import { spiBadgePlugin } from './spi-badge.mjs'

const md = new MarkdownIt().use(spiBadgePlugin)

test('primary badge renders tag with an anchor per case', () => {
  const html = md.render('::: spi 8.35 8.36\n\nBody.\n')
  assert.match(html, /<p class="spi-badge spi-primary">/)
  assert.match(html, /<a id="spi-8\.35" class="spi-anchor"><\/a>/)
  assert.match(html, /<a id="spi-8\.36" class="spi-anchor"><\/a>/)
  assert.match(html, /SPI 8\.35, 8\.36/)
  assert.match(html, /<p>Body\.<\/p>/)
})

test('spi-ref renders without anchors', () => {
  const html = md.render('::: spi-ref 8.35\n')
  assert.match(html, /<p class="spi-badge spi-ref">see SPI 8\.35<\/p>/)
  assert.doesNotMatch(html, /id="spi-/)
})

test('spi-omit renders reason', () => {
  const html = md.render('::: spi-omit 4.6 — component inventory\n')
  assert.match(html, /<p class="spi-badge spi-omit">SPI 4\.6 omitted — component inventory<\/p>/)
})

test('other ::: lines are untouched', () => {
  const html = md.render('::: note\nhi\n:::\n')
  assert.doesNotMatch(html, /spi-badge/)
})
