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
