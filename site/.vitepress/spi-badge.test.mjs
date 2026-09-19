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
  const html = md.render('::: warning\nhi\n:::\n')
  assert.doesNotMatch(html, /spi-badge/)
  assert.doesNotMatch(html, /spi-note/)
})

test('a badge directly after a prose line terminates the paragraph', () => {
  const html = md.render('Some prose here.\n::: spi 8.35\n')
  assert.match(html, /<p>Some prose here\.<\/p>/)
  assert.match(html, /<p class="spi-badge spi-primary">/)
})

test('an omit reason containing a second em-dash keeps the whole reason', () => {
  const html = md.render('::: spi-omit 4.6 — component inventory — see also 4.7\n')
  assert.match(html, /SPI 4\.6 omitted — component inventory — see also 4\.7/)
})

test('errata badge renders id and paraphrase', () => {
  const html = md.render('::: errata E-001 — 12.44: only the target battalion is pinned\n')
  assert.match(html, /<p class="spi-badge spi-errata">Errata E-001 — 12\.44: only the target battalion is pinned<\/p>/)
})

test('ruling badge links to the ruling file', () => {
  const html = md.render('::: ruling R-001 — cohesion level, not DP count\n')
  assert.match(html, /<p class="spi-badge spi-ruling">Ruling <a href="\/cna\/rulings\/R-001">R-001<\/a> — cohesion level, not DP count<\/p>/)
})

test('errata badge without a paraphrase renders bare', () => {
  const html = md.render('::: errata E-002\n')
  assert.match(html, /<p class="spi-badge spi-errata">Errata E-002<\/p>/)
})

test('note container wraps its body in a spi-note div', () => {
  const html = md.render('::: note\nDesigner intent **here**.\n:::\n\nAfter.\n')
  assert.match(html, /<div class="spi-note"><p class="spi-note-title">Note<\/p>\n<p>Designer intent <strong>here<\/strong>\.<\/p>\n<\/div>/)
  assert.match(html, /<p>After\.<\/p>/)
})

test('note container accepts a custom title', () => {
  const html = md.render('::: note Designer\'s note\nBody.\n:::\n')
  assert.match(html, /<p class="spi-note-title">Designer's note<\/p>/)
})
