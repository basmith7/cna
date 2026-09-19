import test from 'node:test'
import assert from 'node:assert/strict'
import { extractCase, sourceUrl, sectionOf } from './original.mjs'

const ADOC = `[#8_3]
=== TERRAIN

[#8_35]
*[8.35]* Ridges are symmetric.
Second line.

[#8_36]
*[8.36]* Wadis cost more.
`

test('extractCase returns the text between a case anchor and the next anchor', () => {
  assert.equal(extractCase(ADOC, '8.35'), '*[8.35]* Ridges are symmetric.\nSecond line.')
  assert.equal(extractCase(ADOC, '8.36'), '*[8.36]* Wadis cost more.')
})

test('extractCase returns null for a case that is not in the section', () => {
  assert.equal(extractCase(ADOC, '8.99'), null)
})

test('sourceUrl fills the template from tools/sources.json', () => {
  const url = sourceUrl('https://x/{commit}/sections/section-{nn}.adoc', 'abc123', 8)
  assert.equal(url, 'https://x/abc123/sections/section-08.adoc')
})

test('sectionOf reads the section number of a case id', () => {
  assert.equal(sectionOf('8.35'), 8)
  assert.equal(sectionOf('32.11'), 32)
})
