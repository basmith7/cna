# 04 Map viewer

Contract: each sheet on `/map` can be zoomed and panned until hex numbers are legible,
on desktop (wheel/buttons/drag) and touch (buttons, drag, pinch if cheap).
Seam: `render_page` emits `<MapSheet sheet="A" title="…" />` per sheet (plus a sheet
jump list and a short legend sentence); `theme/MapSheet.vue` owns events;
`site/.vitepress/map-view.mjs` owns pure maths (`zoomAt`, `clamp`, `fit`) with node tests.
SVG loaded with `withBase`. Page uses a wide layout so the sheet uses the screen.
Gates: `map_render.py --check` after regenerating, `map-page.test.mjs` updated, pytest.
Visual: map at desktop/mobile, zoomed shot of sheet C at 400 %.
Delegated: control styling, max zoom.
