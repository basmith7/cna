// Single-line SPI badge syntax:  ::: spi 8.35 8.36 | ::: spi-ref 8.35 | ::: spi-omit 4.6 — reason
// Provenance annotations use the same shape:  ::: errata E-001 — paraphrase | ::: ruling R-001 — summary
// No closing marker; scope is implicit (to the next badge or heading). Metadata only.
const RE = /^:::\s+(spi|spi-ref|spi-omit|errata|ruling)\s+(.*?)\s*$/
const BASE = '/cna/'

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

const NOTE_OPEN = /^:::\s+note(?:\s+(.*?))?\s*$/
const NOTE_CLOSE = /^:::\s*$/

export function spiBadgePlugin(md) {
  // ::: note [title] … :::  — a non-binding block (designer intent, play advice).
  md.block.ruler.before('fence', 'spi_note', (state, startLine, endLine, silent) => {
    const first = state.src.slice(state.bMarks[startLine] + state.tShift[startLine], state.eMarks[startLine])
    const m = NOTE_OPEN.exec(first)
    if (!m) return false
    let next = startLine + 1
    for (; next < endLine; next++) {
      const l = state.src.slice(state.bMarks[next] + state.tShift[next], state.eMarks[next])
      if (NOTE_CLOSE.test(l)) break
    }
    if (next >= endLine) return false
    if (silent) return true
    const open = state.push('spi_note_open', 'div', 1)
    open.meta = { title: m[1] || 'Note' }
    open.map = [startLine, next]
    state.md.block.tokenize(state, startLine + 1, next)
    state.push('spi_note_close', 'div', -1)
    state.line = next + 1
    return true
  }, { alt: ['paragraph', 'reference', 'blockquote', 'list'] })

  md.renderer.rules.spi_note_open = (tokens, idx) =>
    `<div class="spi-note"><p class="spi-note-title">${esc(tokens[idx].meta.title)}</p>\n`
  md.renderer.rules.spi_note_close = () => '</div>\n'

  md.block.ruler.before('fence', 'spi_badge', (state, startLine, _endLine, silent) => {
    const line = state.src.slice(state.bMarks[startLine] + state.tShift[startLine], state.eMarks[startLine])
    const m = RE.exec(line)
    if (!m) return false
    if (silent) return true
    let cases = m[2], reason = null
    if (m[1] === 'spi-omit' || m[1] === 'errata' || m[1] === 'ruling') {
      const m2 = /^(.*?)\s+(?:—|--)\s+(.*)$/s.exec(cases)
      if (m2) {
        cases = m2[1]
        reason = m2[2]
      }
    }
    const token = state.push('spi_badge', '', 0)
    token.meta = { kind: m[1], cases: cases.split(/\s+/), reason }
    token.map = [startLine, startLine + 1]
    state.line = startLine + 1
    return true
  }, { alt: ['paragraph', 'reference', 'blockquote', 'list'] })

  md.renderer.rules.spi_badge = (tokens, idx) => {
    const { kind, cases, reason } = tokens[idx].meta
    const list = cases.join(', ')
    if (kind === 'spi') {
      const anchors = cases.map(c => `<a id="spi-${esc(c)}" class="spi-anchor"></a>`).join('')
      return `<p class="spi-badge spi-primary" data-cases="${esc(cases.join(' '))}">${anchors}SPI ${esc(list)}</p>\n`
    }
    if (kind === 'spi-ref') return `<p class="spi-badge spi-ref">see SPI ${esc(list)}</p>\n`
    const tail = reason ? ' — ' + esc(reason) : ''
    if (kind === 'errata') return `<p class="spi-badge spi-errata">Errata ${esc(list)}${tail}</p>\n`
    if (kind === 'ruling') {
      const links = cases.map(c => `<a href="${BASE}rulings/${esc(c)}">${esc(c)}</a>`).join(', ')
      return `<p class="spi-badge spi-ruling">Ruling ${links}${tail}</p>\n`
    }
    return `<p class="spi-badge spi-omit">SPI ${esc(list)} omitted${reason ? ' — ' + esc(reason) : ''}</p>\n`
  }
}
