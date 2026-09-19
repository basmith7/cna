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

// renderAdoc: the subset of AsciiDoc the transcription actually uses, to safe HTML.
import { renderAdoc } from './original.mjs'

test('renderAdoc joins soft-wrapped lines into paragraphs and separates on blank lines', () => {
  assert.equal(renderAdoc('one\ntwo\n\nthree'), '<p>one two</p><p>three</p>')
})

test('renderAdoc renders bold, italic and case xrefs inline', () => {
  assert.equal(
    renderAdoc('*[8.11]* Units _may_ move (see <<8_34,8.34>>).'),
    '<p><strong>[8.11]</strong> Units <em>may</em> move (see <span class="spi-xref">8.34</span>).</p>',
  )
})

test('renderAdoc escapes HTML from the source', () => {
  assert.equal(renderAdoc('a <b> & c'), '<p>a &lt;b&gt; &amp; c</p>')
})

test('renderAdoc renders headings at any level as h4', () => {
  assert.equal(renderAdoc('=== TERRAIN\n\ntext'), '<h4>TERRAIN</h4><p>text</p>')
  assert.equal(renderAdoc('===== Sub'), '<h4>Sub</h4>')
})

test('renderAdoc renders delimited blocks as a div and drops style attribute lines', () => {
  assert.equal(
    renderAdoc('[note]\n====\nInside *here*.\n====\nAfter'),
    '<div class="spi-block">' + '<p>Inside <strong>here</strong>.</p>' + '</div><p>After</p>',
  )
  assert.equal(renderAdoc('[upperroman]\n. one\n. two'), '<ol><li>one</li><li>two</li></ol>')
})

test('renderAdoc renders bullet and numbered lists', () => {
  assert.equal(renderAdoc('* a\n* b'), '<ul><li>a</li><li>b</li></ul>')
})

test('renderAdoc renders simple |=== tables with a header row', () => {
  assert.equal(
    renderAdoc('|===\n|Action |Cost\n\n|Detach |1\n|Attach |2\n|==='),
    '<table><thead><tr><th>Action</th><th>Cost</th></tr></thead>' +
      '<tbody><tr><td>Detach</td><td>1</td></tr><tr><td>Attach</td><td>2</td></tr></tbody></table>',
  )
})
