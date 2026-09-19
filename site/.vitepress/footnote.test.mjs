import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import footnote from 'markdown-it-footnote'

// Rulings and variants quote third-party sources with a footnote after each quote
// (rulings/README.md, "Quoting a third-party source"). This is the plugin the site wires in.
const md = new MarkdownIt().use(footnote)

test('a [^x] reference renders as a footnote link and a footnote block', () => {
  const html = md.render('> quoted text[^nj]\n\n[^nj]: NJHarman, CC-BY-SA 4.0.\n')
  assert.match(html, /<sup class="footnote-ref"><a href="#fn1"/)
  assert.match(html, /<section class="footnotes">/)
  assert.match(html, /NJHarman, CC-BY-SA 4\.0\./)
})
