<script setup lang="ts">
// One zoomable, pannable map sheet. The SVG is an <img> moved with a CSS transform; the maths
// lives in map-view.mjs. Plain wheel scrolls the page, ctrl/meta+wheel zooms.
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { withBase } from 'vitepress'
import { fit, clamp, zoomAt, pan, MIN_K_FACTOR } from '../map-view.mjs'

const props = defineProps<{ sheet: string; title: string }>()
const src = computed(() => withBase(`/map/${props.sheet}.svg`))

const box = ref<HTMLElement | null>(null)
// Every sheet shares this viewBox size (1 SVG unit = 1 CSS px at 100 %). The SVGs carry no
// width/height, so the image's natural size is unusable.
const content = ref({ w: 1290, h: 1580 })
const size = ref({ w: 0, h: 0 })
const view = ref({ k: 1, x: 0, y: 0 })
const fitK = ref(1)
const dragging = ref(false)
const ready = ref(false)

const minK = () => fitK.value * MIN_K_FACTOR
const set = (v: { k: number; x: number; y: number }) => {
  view.value = clamp(v, size.value, content.value, minK())
}
const style = computed(() => ({
  width: content.value.w + 'px',
  height: content.value.h + 'px',
  transform: `translate(${view.value.x}px, ${view.value.y}px) scale(${view.value.k})`,
}))
const percent = computed(() => Math.round(view.value.k * 100))

function measure() {
  if (!box.value) return
  size.value = { w: box.value.clientWidth, h: box.value.clientHeight }
}
function refit() {
  measure()
  const v = fit(size.value, content.value)
  fitK.value = v.k
  set(v)
  ready.value = true
}

const local = (e: { clientX: number; clientY: number }) => {
  const r = box.value!.getBoundingClientRect()
  return { x: e.clientX - r.left, y: e.clientY - r.top }
}
const zoomBy = (f: number, at = { x: size.value.w / 2, y: size.value.h / 2 }) =>
  set(zoomAt(view.value, f, at.x, at.y, minK()))

// Pointer tracking: one pointer pans, two pinch.
const pointers = new Map<number, { x: number; y: number }>()
let pinchDist = 0
function onDown(e: PointerEvent) {
  box.value!.setPointerCapture(e.pointerId)
  pointers.set(e.pointerId, local(e))
  dragging.value = pointers.size === 1
  if (pointers.size === 2) pinchDist = dist()
}
function dist() {
  const [a, b] = [...pointers.values()]
  return Math.hypot(a.x - b.x, a.y - b.y)
}
function onMove(e: PointerEvent) {
  const prev = pointers.get(e.pointerId)
  if (!prev) return
  const cur = local(e)
  pointers.set(e.pointerId, cur)
  if (pointers.size === 1) {
    set(pan(view.value, cur.x - prev.x, cur.y - prev.y))
  } else if (pointers.size === 2) {
    const d = dist()
    const [a, b] = [...pointers.values()]
    if (pinchDist) zoomBy(d / pinchDist, { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 })
    pinchDist = d
  }
}
function onUp(e: PointerEvent) {
  pointers.delete(e.pointerId)
  dragging.value = false
  pinchDist = 0
}
function onWheel(e: WheelEvent) {
  if (!(e.ctrlKey || e.metaKey)) return
  e.preventDefault()
  zoomBy(Math.exp(-e.deltaY * 0.01), local(e))
}
function onKey(e: KeyboardEvent) {
  if (e.key === '+' || e.key === '=') zoomBy(1.25)
  else if (e.key === '-' || e.key === '_') zoomBy(0.8)
  else if (e.key === '0') refit()
  else return
  e.preventDefault()
}

let ro: ResizeObserver | undefined
onMounted(() => {
  // Wheel must be non-passive so ctrl+wheel can cancel the browser's page zoom.
  box.value!.addEventListener('wheel', onWheel, { passive: false })
  ro = new ResizeObserver(() => { if (ready.value) { const wasFit = Math.abs(view.value.k - fitK.value) < 1e-6; if (wasFit) refit(); else { measure(); set(view.value) } } })
  ro.observe(box.value!)
  refit()
})
onBeforeUnmount(() => {
  ro?.disconnect()
  box.value?.removeEventListener('wheel', onWheel)
})
</script>

<template>
  <figure class="map-sheet">
    <div class="map-toolbar">
      <button type="button" aria-label="Zoom in" @click="zoomBy(1.5)">+</button>
      <button type="button" aria-label="Zoom out" @click="zoomBy(1 / 1.5)">−</button>
      <button type="button" @click="refit()">Fit</button>
      <span class="map-zoom" aria-live="off">{{ percent }}%</span>
      <a :href="src" target="_blank" rel="noopener">Open full size</a>
    </div>
    <div
      ref="box"
      class="map-box"
      :class="{ dragging }"
      tabindex="0"
      role="group"
      :aria-label="`${title}: drag to pan, Ctrl or Cmd plus scroll to zoom, plus and minus keys when focused`"
      @pointerdown="onDown"
      @pointermove="onMove"
      @pointerup="onUp"
      @pointercancel="onUp"
      @keydown="onKey"
    >
      <img :src="src" :alt="title" draggable="false" :style="style" />
    </div>
    <figcaption class="map-hint">Drag to pan. Ctrl or Cmd + scroll to zoom, or pinch.</figcaption>
  </figure>
</template>
