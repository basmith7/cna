// Pure maths for the map viewer. A view is {x, y, k}: the content is drawn at scale k,
// offset by (x, y) CSS pixels from the viewport's top-left.
export const MIN_K_FACTOR = 0.5 // allow a little less than "fit"
export const MAX_K = 4          // 400 % of the SVG's natural size

export function fit(box, content) {
  const k = Math.min(box.w / content.w, box.h / content.h)
  return { k, x: (box.w - content.w * k) / 2, y: (box.h - content.h * k) / 2 }
}

// Keep the content from being flung off-screen: at least `margin` px of it stays visible,
// and content smaller than the box is centred.
export function clamp(view, box, content, minK, maxK = MAX_K, margin = 48) {
  const k = Math.min(maxK, Math.max(minK, view.k))
  const cw = content.w * k, ch = content.h * k
  const axis = (pos, b, c) => (c <= b ? (b - c) / 2 : Math.min(b - margin, Math.max(margin - c, pos)))
  return { k, x: axis(view.x, box.w, cw), y: axis(view.y, box.h, ch) }
}

// Scale by `factor` keeping the content point under (px, py) fixed on screen.
export function zoomAt(view, factor, px, py, minK, maxK = MAX_K) {
  const k = Math.min(maxK, Math.max(minK, view.k * factor))
  const r = k / view.k
  return { k, x: px - (px - view.x) * r, y: py - (py - view.y) * r }
}

export const pan = (view, dx, dy) => ({ ...view, x: view.x + dx, y: view.y + dy })
