// Pure helpers for the client-side "original text" viewer: locate an SPI case in the pinned
// tonicebrian transcription (AsciiDoc, one file per section, `[#S_C]` anchors on their own line).

export function sectionOf(caseId) {
  return Number(caseId.split('.')[0])
}

export function sourceUrl(template, commit, section) {
  return template.replace('{commit}', commit).replace('{nn}', String(section).padStart(2, '0'))
}

export function extractCase(adoc, caseId) {
  const anchor = `[#${caseId.replace('.', '_')}]`
  const lines = adoc.split('\n')
  const start = lines.indexOf(anchor)
  if (start === -1) return null
  const out = []
  for (let i = start + 1; i < lines.length; i++) {
    if (/^\[#\d+_\d+\]\s*$/.test(lines[i])) break
    out.push(lines[i])
  }
  return out.join('\n').trim()
}

// Render the AsciiDoc subset the transcription uses (paragraphs, headings, *bold*, _italic_,
// <<S_C,label>> xrefs, [style] + ==== delimited blocks, * / . lists, |=== tables) to HTML.
// Everything from the source is escaped first; only our own tags are emitted.

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

function inline(s) {
  return escapeHtml(s)
    .replace(/&lt;&lt;[^,&]+,([^&]+?)&gt;&gt;/g, '<span class="spi-xref">$1</span>')
    .replace(/\*([^*\n]+)\*/g, '<strong>$1</strong>')
    .replace(/(^|[^A-Za-z0-9])_([^_\n]+)_(?=[^A-Za-z0-9]|$)/g, '$1<em>$2</em>')
}

export function renderAdoc(text) {
  const lines = text.split('\n')
  const out = []
  let para = []
  let list = null // { tag, items }
  let openBlock = false

  const flushPara = () => {
    if (para.length) out.push(`<p>${inline(para.join(' '))}</p>`)
    para = []
  }
  const flushList = () => {
    if (list) out.push(`<${list.tag}>${list.items.map(i => `<li>${inline(i)}</li>`).join('')}</${list.tag}>`)
    list = null
  }
  const flush = () => { flushPara(); flushList() }

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]
    const t = line.trim()
    if (t === '') { flush(); continue }
    if (/^\[[^\]]*\]$/.test(t)) continue // [note], [WARNING], [upperroman] … style lines
    if (/^={2,}\s+\S/.test(t)) { flush(); out.push(`<h4>${inline(t.replace(/^=+\s+/, ''))}</h4>`); continue }
    if (/^={4}$/.test(t)) { flush(); out.push(openBlock ? '</div>' : '<div class="spi-block">'); openBlock = !openBlock; continue }
    if (t === '|===') {
      flush()
      // One row per line; the first row is the header when a blank line follows it.
      const rows = []
      let headerBreak = false
      for (i++; i < lines.length && lines[i].trim() !== '|==='; i++) {
        const r = lines[i].trim()
        if (r === '') { if (rows.length === 1) headerBreak = true; continue }
        rows.push(r.split('|').slice(1).map(c => c.trim()))
      }
      const cells = (cs, tag) => `<tr>${cs.map(c => `<${tag}>${inline(c)}</${tag}>`).join('')}</tr>`
      const body = headerBreak ? rows.slice(1) : rows
      const head = headerBreak ? `<thead>${cells(rows[0], 'th')}</thead>` : ''
      out.push(`<table>${head}<tbody>${body.map(r => cells(r, 'td')).join('')}</tbody></table>`)
      continue
    }
    const m = /^([*.])\s+(.*)$/.exec(t)
    if (m) {
      flushPara()
      const tag = m[1] === '*' ? 'ul' : 'ol'
      if (!list || list.tag !== tag) { flushList(); list = { tag, items: [] } }
      list.items.push(m[2])
      continue
    }
    if (list) { list.items[list.items.length - 1] += ' ' + t; continue }
    para.push(t)
  }
  flush()
  if (openBlock) out.push('</div>')
  return out.join('')
}
