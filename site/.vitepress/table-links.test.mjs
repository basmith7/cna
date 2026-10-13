import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import { tableLinksPlugin } from './table-links.mjs'

const md = new MarkdownIt()
tableLinksPlugin(md, { 'barrage-results': { title: 'Barrage results', group: 'Land Game' } })

test('a table path in a code span becomes a link to its page', () => {
  assert.equal(md.renderInline('see `data/tables/barrage-results.json` here'),
    'see <a href="/tables/barrage-results" class="table-link" title="data/tables/barrage-results.json">Barrage results</a> here')
})

test('unknown tables, other paths and fenced code are untouched', () => {
  assert.match(md.renderInline('`data/tables/nope.json`'), /<code>data\/tables\/nope\.json<\/code>/)
  assert.match(md.renderInline('`data/tables/barrage-results.json` x'.replace('data/', 'other/')), /<code>/)
  assert.match(md.render('```\ndata/tables/barrage-results.json\n```\n'), /<pre><code>data\/tables/)
})
