// Single-line SPI badge syntax:  ::: spi 8.35 8.36 | ::: spi-ref 8.35 | ::: spi-omit 4.6 — reason
// No closing marker; scope is implicit (to the next badge or heading). Metadata only.
const RE = /^:::\s+(spi|spi-ref|spi-omit)\s+(.*?)\s*$/

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

export function spiBadgePlugin(md) {
  md.block.ruler.before('fence', 'spi_badge', (state, startLine, _endLine, silent) => {
    const line = state.src.slice(state.bMarks[startLine] + state.tShift[startLine], state.eMarks[startLine])
    const m = RE.exec(line)
    if (!m) return false
    if (silent) return true
    let cases = m[2], reason = null
    if (m[1] === 'spi-omit') {
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
      return `<p class="spi-badge spi-primary">${anchors}SPI ${esc(list)}</p>\n`
    }
    if (kind === 'spi-ref') return `<p class="spi-badge spi-ref">see SPI ${esc(list)}</p>\n`
    return `<p class="spi-badge spi-omit">SPI ${esc(list)} omitted${reason ? ' — ' + esc(reason) : ''}</p>\n`
  }
}
