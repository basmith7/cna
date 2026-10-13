// A code span naming a table file (`data/tables/<name>.json`) renders as a link to that table's
// page, labelled with its title. Rules files keep the path; only the rendered page changes.
// Unknown names and fenced code are left alone. `tables` is tables.json (tools/tables_page.py).
const RE = /^data\/tables\/([\w-]+)\.json$/

export function tableLinksPlugin(md, tables) {
  md.core.ruler.after('inline', 'table_links', (state) => {
    for (const block of state.tokens) {
      if (block.type !== 'inline' || !block.children) continue
      block.children = block.children.flatMap((t) => {
        const m = t.type === 'code_inline' && RE.exec(t.content)
        const table = m && tables[m[1]]
        if (!table) return [t]
        const open = new state.Token('link_open', 'a', 1)
        open.attrs = [['href', `/tables/${m[1]}`], ['class', 'table-link'], ['title', t.content]]
        const text = new state.Token('text', '', 0)
        text.content = table.title
        return [open, text, new state.Token('link_close', 'a', -1)]
      })
    }
  })
}
