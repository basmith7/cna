<script setup lang="ts">
// Client-side only: after each page renders, attach a collapsed "original text" block to every
// primary SPI badge. The SPI text is fetched from the pinned tonicebrian transcription at view
// time, never bundled, never server-rendered, never indexed. Disabled by themeConfig.original.enabled.
import { onMounted, watch, nextTick } from 'vue'
import { useData, useRoute } from 'vitepress'
import { extractCase, sourceUrl, sectionOf, renderAdoc } from '../original.mjs'

const { theme } = useData()
const route = useRoute()
const cache = new Map<number, Promise<string | null>>()

function fetchSection(section: number): Promise<string | null> {
  const cfg = theme.value.original
  if (!cache.has(section)) {
    cache.set(section, fetch(sourceUrl(cfg.rawUrlTemplate, cfg.commit, section))
      .then(r => (r.ok ? r.text() : null))
      .catch(() => null))
  }
  return cache.get(section)!
}

function attach() {
  const cfg = theme.value.original
  if (!cfg || cfg.enabled === false) return
  document.querySelectorAll<HTMLElement>('p.spi-badge.spi-primary[data-cases]').forEach(badge => {
    if (badge.nextElementSibling?.classList.contains('spi-original')) return
    const cases = (badge.dataset.cases || '').split(' ').filter(Boolean)
    if (!cases.length) return
    const details = document.createElement('details')
    details.className = 'spi-original'
    const summary = document.createElement('summary')
    summary.textContent = `Original text (SPI ${cases.join(', ')})`
    details.appendChild(summary)
    let loaded = false
    details.addEventListener('toggle', async () => {
      if (!details.open || loaded) return
      loaded = true
      const blocks: string[] = []
      for (const c of cases) {
        const adoc = await fetchSection(sectionOf(c))
        const text = adoc ? extractCase(adoc, c) : null
        if (text) blocks.push(text)
      }
      if (!blocks.length) { details.remove(); return }
      // renderAdoc escapes the fetched text and emits only its own tags.
      const box = document.createElement('div')
      box.className = 'spi-original-text'
      box.innerHTML = blocks.map(renderAdoc).join('')
      const cite = document.createElement('p')
      cite.className = 'spi-original-cite'
      cite.textContent = `SPI, The Campaign for North Africa (1979), transcription ${cfg.commit.slice(0, 7)}. Shown for comparison; not part of this edition.`
      details.append(box, cite)
    })
    badge.after(details)
  })
}

onMounted(() => { attach() })
watch(() => route.path, () => nextTick(attach))
</script>

<template><span style="display:none" /></template>
