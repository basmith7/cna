#!/usr/bin/env python3
"""Build docs/learn/index.html — an illustrated introduction to CNA.

Part A: one Operations Stage on a small illustrative map.
Part B: the combat maths with the real 1979 tables.
Part C: supply flow in the Logistics Game.
Part D: Graziani's Offensive deployments on the real Map C.

Terrain costs [8.37], CP costs [6.3], CRT [15.79], barrage [12.6], anti-armor [14.6],
port/truck charts [55.3, 54.2] are the real 1979 values; unit ratings in Part A are illustrative.

Scan pages are fetched from archive.org into ~/.cache/cna-scans and cropped into docs/learn/;
those crops are SPI material and are git-ignored.

Usage: python3 tools/learn_page.py          (then open docs/learn/index.html)
       python3 tools/learn_page.py --site   (writes site/learn.md: Parts A-C, no SPI material;
                                             tests/test_learn_site.py fails when it is stale)
"""
import html, math, os, pathlib, re, sys

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "learn"
CACHE = pathlib.Path(os.path.expanduser("~/.cache/cna-scans"))

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fetch import scan_page  # noqa: E402


def scan(page):
    """jp2 index (0-based); XML page n == jp2 n-1."""
    return Image.open(scan_page(page))


# ---------------------------------------------------------------- table crops
def make_table_crops():
    im = scan("0096"); w, h = im.size
    im.crop((40, int(h * 0.62), w - 30, h - 40)).save(OUT / "tbl_barrage.jpg", quality=85)
    im = scan("0097"); w, h = im.size
    im.crop((60, 80, w - 40, int(h * 0.56))).save(OUT / "tbl_aa.jpg", quality=85)
    im = scan("0098").rotate(90, expand=True); w, h = im.size
    im.crop((60, 60, w - 40, int(h * 0.64))).save(OUT / "tbl_crt.jpg", quality=85)


# ---------------------------------------------------------------- Map C overlay
def make_map_overlay():
    """Pointy-top hexes, RRCC numbering, rows increase northward, odd rows shifted half a hex west.
    Reference measured on the scan: C4023 centre ~(2136, 1910) on the 3344x5293 image."""
    COLW, ROWH, X0, Y0 = 94.0, 81.0, 2136, 1910

    def centre(rr, cc):
        return X0 + (cc - 23) * COLW - (COLW / 2 if rr % 2 == 1 else 0), Y0 - (rr - 40) * ROWH

    ITALIAN = [("4218", "1 CCNN Div"), ("4120", "63 Cirene Div"), ("4020", "1 Libyan Div"), ("3920", "2 Libyan Div"),
               ("3919", "Aresca Regt"), ("3918", "62 Marmarica Div"), ("3617", "Maletti Gp"), ("4321", "Bardia garrison")]
    CW = [("4131", "2 Scots Gds · 31 Fd Arty"), ("3926", "French Motor Marines"),
          ("3922", "3 Coldstream · 1 KRRC · 4 RHA · 7 Med Arty"), ("3721", "1 RNF · 3 RHA (AT)"),
          ("3520", "1 RTR"), ("3320", "2 Rifle Bde"), ("3020", "11 Hussars")]
    im = scan("0189").convert("RGBA")
    box = (1400, 1480, 3250, 2900)
    crop = im.crop(box)
    ov = Image.new("RGBA", crop.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    try:
        font = ImageFont.truetype("/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf", 22)
    except Exception:
        font = ImageFont.load_default()

    def mark(hexid, label, fill, outline, dy=0):
        x, y = centre(int(hexid[:2]), int(hexid[2:]))
        x -= box[0]; y -= box[1]; r = 40
        d.ellipse((x - r, y - r, x + r, y + r), fill=fill, outline=outline, width=4)
        tw = d.textlength(label, font=font)
        d.rectangle((x - tw / 2 - 6, y + r + 2 + dy, x + tw / 2 + 6, y + r + 30 + dy), fill=(255, 255, 255, 230), outline=outline, width=2)
        d.text((x - tw / 2, y + r + 4 + dy), label, fill=(0, 0, 0, 255), font=font)

    for h_, l in ITALIAN:
        mark(h_, l, (70, 110, 50, 120), (40, 80, 20, 255), dy=(30 if h_ == "3919" else 0))
    for h_, l in CW:
        mark(h_, l, (200, 120, 20, 120), (150, 70, 0, 255), dy=(30 if h_ == "3922" else 0))
    ax = [centre(40, 20), centre(40, 21), centre(39, 23), centre(39, 26), centre(39, 28), centre(40, 30), centre(41, 31)]
    ax = [(x - box[0], y - box[1]) for x, y in ax]
    d.line(ax, fill=(180, 0, 0, 220), width=8)
    x, y = ax[-1]
    d.polygon([(x + 30, y), (x - 10, y - 22), (x - 10, y + 22)], fill=(180, 0, 0, 220))
    out = Image.alpha_composite(crop, ov).convert("RGB")
    out = out.resize((1200, int(1200 * out.size[1] / out.size[0])))
    out.save(OUT / "graziani.jpg", quality=88)


# ---------------------------------------------------------------- Part A hex sketch
R = 54
H = math.sqrt(3) * R
OX, OY = 60, 40
COLS, ROWS = 8, 5


def center(col, row):
    return OX + col * 1.5 * R, OY + row * H + (H / 2 if col % 2 else 0)


def corners(cx, cy):
    return [(cx + R * math.cos(math.radians(60 * i)), cy + R * math.sin(math.radians(60 * i))) for i in range(6)]


def to_cube(col, row):
    q = col; r = row - (col - (col & 1)) // 2
    return q, r, -q - r


def adjacent(a, b):
    qa, ra, sa = to_cube(*a); qb, rb, sb = to_cube(*b)
    return max(abs(qa - qb), abs(ra - rb), abs(sa - sb)) == 1


def edge_between(a, b):
    ca, cb = center(*a), center(*b)
    return sorted(corners(*ca), key=lambda p: (p[0] - cb[0]) ** 2 + (p[1] - cb[1]) ** 2)[:2]


SEA = {(c, 0) for c in range(COLS)}
ROUGH = {(3, 2), (4, 2), (5, 2), (4, 3)}
BIR = (6, 3)
ROAD = [(c, 1) for c in range(COLS)]
TRACK = [(4, 1), (4, 2), (4, 3), (5, 3), (6, 3)]
ESCARP = []
for c in range(COLS):
    for nb in [(c, 2), (c + 1, 2), (c - 1, 2), (c + 1, 1), (c - 1, 1)]:
        if 0 <= nb[0] < COLS and nb[1] >= 2 and adjacent((c, 1), nb) and not ((c, 1) == (4, 1) and nb == (4, 2)):
            ESCARP.append(((c, 1), nb))


def terrain_svg():
    out = []
    for col in range(COLS):
        for row in range(ROWS):
            cx, cy = center(col, row)
            pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in corners(cx, cy))
            fill = "#9ec9e2" if (col, row) in SEA else ("url(#rough)" if (col, row) in ROUGH else "#f3e6bf")
            out.append(f'<polygon points="{pts}" fill="{fill}" stroke="#8a7a55" stroke-width="1"/>')
            if (col, row) not in SEA:
                out.append(f'<text x="{cx:.1f}" y="{cy + R - 8:.1f}" font-size="9" fill="#8a7a55" text-anchor="middle">{col}-{row:02d}</text>')
    pts = " ".join(f"{center(*h)[0]:.1f},{center(*h)[1]:.1f}" for h in ROAD)
    out.append(f'<polyline points="{pts}" fill="none" stroke="#333" stroke-width="4"/>')
    out.append(f'<polyline points="{pts}" fill="none" stroke="#f3e6bf" stroke-width="1.5" stroke-dasharray="6 6"/>')
    pts = " ".join(f"{center(*h)[0]:.1f},{center(*h)[1]:.1f}" for h in TRACK)
    out.append(f'<polyline points="{pts}" fill="none" stroke="#7a5a2a" stroke-width="2.5" stroke-dasharray="7 5"/>')
    for a, b in ESCARP:
        (x1, y1), (x2, y2) = edge_between(a, b)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#7a3b1e" stroke-width="6" stroke-linecap="round"/>')
    bx, by = center(*BIR)
    out.append(f'<circle cx="{bx:.1f}" cy="{by - 14:.1f}" r="5" fill="#2b6cb0"/><text x="{bx:.1f}" y="{by - 22:.1f}" font-size="10" text-anchor="middle" fill="#2b6cb0">Bir Sofafi</text>')
    sx, sy = center(0, 0)
    out.append(f'<text x="{sx + 30:.1f}" y="{sy + 4:.1f}" font-size="13" fill="#2b5c7a" font-style="italic">Mediterranean</text>')
    px, py = center(4, 1)
    out.append(f'<text x="{px + 4:.1f}" y="{py + R + 4:.1f}" font-size="10" fill="#7a3b1e" font-weight="bold" text-anchor="middle">Halfaya Pass</text>')
    lx, ly = center(1, 4)
    out.append(f'<text x="{lx:.1f}" y="{ly + 4:.1f}" font-size="11" fill="#8a7a55" font-style="italic" text-anchor="middle">Libyan plateau</text>')
    return "\n".join(out)


AXIS, CW_C = "#8fa77a", "#d9b46a"


def unit_svg(hexpos, name, side, sub="", offset=0, dim=False, marker=None):
    cx, cy = center(*hexpos)
    cx += offset * 6; cy += offset * -30 + 4
    fill = AXIS if side == "axis" else CW_C
    op = ' opacity="0.45"' if dim else ""
    s = [f'<g{op}><rect x="{cx - 30:.1f}" y="{cy - 13:.1f}" width="60" height="26" rx="3" fill="{fill}" stroke="#222" stroke-width="1.2"/>',
         f'<text x="{cx:.1f}" y="{cy - 2:.1f}" font-size="9" font-weight="bold" text-anchor="middle" fill="#111">{html.escape(name)}</text>',
         f'<text x="{cx:.1f}" y="{cy + 8:.1f}" font-size="8" text-anchor="middle" fill="#222">{html.escape(sub)}</text></g>']
    if marker:
        s.append(f'<rect x="{cx + 18:.1f}" y="{cy - 22:.1f}" width="30" height="14" rx="2" fill="#fff" stroke="#b00" stroke-width="1.2"/>')
        s.append(f'<text x="{cx + 33:.1f}" y="{cy - 12:.1f}" font-size="8" text-anchor="middle" fill="#b00" font-weight="bold">{marker}</text>')
    return "\n".join(s)


def arrow(path, color="#b00", label=None, dashed=False):
    pts = [center(*h) for h in path]
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    dash = ' stroke-dasharray="6 4"' if dashed else ""
    s = [f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arr-{color[1:]})"{dash}/>']
    if label:
        mx, my = pts[0]
        s.append(f'<text x="{mx + 40:.1f}" y="{my - 34:.1f}" font-size="10" fill="{color}" font-weight="bold" text-anchor="middle">{html.escape(label)}</text>')
    return "\n".join(s)


def burst(hexpos, text):
    cx, cy = center(*hexpos)
    pts = [(cx + R * (0.95 if i % 2 == 0 else 0.6) * math.cos(math.radians(22.5 * i)),
            cy + R * (0.95 if i % 2 == 0 else 0.6) * math.sin(math.radians(22.5 * i))) for i in range(16)]
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<polygon points="{p}" fill="#ff5a36" opacity="0.35" stroke="#b00" stroke-width="1.5"/>'
            f'<text x="{cx:.1f}" y="{cy + R + 12:.1f}" font-size="10" fill="#b00" font-weight="bold" text-anchor="middle">{html.escape(text)}</text>')


def panel(title, body_svg, note_html, ledger_html=""):
    width = int(OX + (COLS - 1) * 1.5 * R + R + 40)
    height = int(OY + ROWS * H + H / 2 + 10)
    svg = f'''<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<defs>
 <pattern id="rough" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#e2cf9e"/><path d="M0 8 L8 0" stroke="#a88d55" stroke-width="1.2"/></pattern>
 <marker id="arr-b00" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#b00"/></marker>
 <marker id="arr-1d4ed8" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1d4ed8"/></marker>
</defs>
{terrain_svg()}
{body_svg}
</svg>'''
    return f'<section class="panel"><h2>{title}</h2><div class="row"><div class="map">{svg}</div><div class="note">{note_html}</div></div>{ledger_html}</section>'


ROSTER = {
    "I/Lib": dict(name="I/1 Libyan", sub="Inf regt · CPA 8 · M−1", side="axis"),
    "II/Lib": dict(name="II/1 Libyan", sub="Inf regt · CPA 8 · M−1", side="axis"),
    "Art": dict(name="1 Lib Art", sub="Arty · Bar 9 · CPA 8", side="axis"),
    "L3": dict(name="IX L3", sub="Tankette bn · CPA 25", side="axis"),
    "RNF": dict(name="1 RNF", sub="MG bn · CPA 8 · M+1", side="cw"),
    "11H": dict(name="11 Hussars", sub="Armd cars · CPA 25 · M+2", side="cw"),
    "RHA": dict(name="4 RHA", sub="Arty · Bar 9 · CPA 10", side="cw"),
}


def U(key, pos, **kw):
    r = ROSTER[key]; return unit_svg(pos, r["name"], r["side"], r["sub"], **kw)


def part_a():
    panels = []
    body = "\n".join([U("I/Lib", (0, 1)), U("Art", (1, 1)), U("II/Lib", (1, 1), offset=1), U("L3", (0, 2)),
                      U("11H", (3, 1)), U("RNF", (4, 2)), U("RHA", (5, 2))])
    note = """
<p><b>Sept 1940, Operations Stage 1, Player A = Italy.</b> Italy won Initiative (rating 1 + die) and chose to go first.</p>
<p>Coast road along the strip; the <span class="esc">escarpment</span> blocks vehicles going up except at the <b>Halfaya Pass track</b>. <span class="rough">Hatched</span> = Rough.</p>
<p>Each unit has a <b>CPA</b> to spend this stage: cross Clear = 2 CP, Rough = 3 (non-mot) / 4 (mot), road hex = 1 (non-mot) / ½ (mot), track = 1, up an escarpment = +6 non-mot, <b>prohibited</b> for motorised [8.37].</p>
<p>Both sides' CPs count for the <i>whole</i> stage, including what B spends reacting during A's half [6.14].</p>"""
    panels.append(panel("1 · Start of Player A's half", body, note))

    body = "\n".join([U("I/Lib", (0, 1), dim=True), U("Art", (1, 1), dim=True), U("II/Lib", (1, 1), offset=1, dim=True),
                      U("L3", (0, 2), marker="RES I"),
                      arrow([(0, 1), (1, 1), (2, 1), (3, 1)]), U("I/Lib", (3, 1)),
                      arrow([(1, 1), (2, 1), (3, 1)]), U("II/Lib", (3, 1), offset=1),
                      arrow([(1, 1), (2, 1)]), U("Art", (2, 1)),
                      arrow([(3, 1), (4, 1), (5, 1)], color="#1d4ed8", dashed=True, label="React −2 CP"), U("11H", (5, 1)),
                      U("RNF", (4, 2)), U("RHA", (5, 2))])
    note = """
<p><b>F. Reserve Designation.</b> Italy puts the L3 tankettes in <b>Reserve</b> (0 CP). Reserves may move again later even if far from the enemy [8.23, 18.0].</p>
<p><b>G1. Movement Segment.</b> Both Libyan regiments march 3 road hexes: <b>3 CP</b> each (road = 1 CP/hex for non-motorised). The artillery follows 1 hex (1 CP).</p>
<p>The 11th Hussars, non-phasing, use <b>Reaction</b> to fall back 2 road hexes as the Italians close: motorised road cost ½ × 2 = 1, plus Reaction is limited and costs CPs against their own CPA. Call it <b>2 CP</b>.</p>
<p>Result: two regiments stacked at 3-01 on the coast, directly below the RNF at the top of the pass at 4-02. They are adjacent and in the RNF's <b>Zone of Control</b> — combat is now mandatory [10, 11].</p>"""
    panels.append(panel("2 · Reserve Designation + Movement Segment (cycle 1)", body, note))

    body = "\n".join([U("I/Lib", (3, 1)), U("II/Lib", (3, 1), offset=1), U("Art", (2, 1)), U("L3", (0, 2), marker="RES I"),
                      U("11H", (5, 1), marker="BD 1"), U("RNF", (4, 2)), U("RHA", (5, 2))])
    note = """
<p><b>G2. Breakdown Determination.</b> Every vehicle unit of <i>both</i> sides that moved rolls for breakdown. Breakdown Points accumulate per hex type — road hex ½, clear 4, rough 8, desert 24, down-escarpment +6 — against the vehicle's Breakdown Adjustment Rating [21].</p>
<p>The Hussars moved 2 road hexes (1 BP): a bad roll leaves <b>one armoured-car TOE point broken down</b>. It needs towing to a repair facility or a field repair attempt in the Repair Phase [22]. The L3s haven't moved yet, so no roll.</p>
<p>Desert attrition, no shots fired. In the full Logistics Game each of these moves also burned fuel per vehicle per hex.</p>"""
    panels.append(panel("3 · Breakdown Determination Segment", body, note))

    body = "\n".join([U("I/Lib", (3, 1)), U("II/Lib", (3, 1), offset=1), U("Art", (2, 1), marker="FWD"), U("L3", (0, 2), marker="RES I"),
                      burst((4, 2), "Barrage 3 pts → RNF"), arrow([(3, 1), (4, 2)], label="Close Assault"),
                      U("11H", (5, 1)), U("RNF", (4, 2)), U("RHA", (5, 2), marker="BACK")])
    note = """
<p><b>G3. Combat Segment</b> — strict order:</p>
<ol>
<li><b>Position.</b> Italian guns go <b>Forward</b> (can split fire; vulnerable if overrun). RHA stays <b>Back</b>.</li>
<li><b>Barrage.</b> Both plot secretly. Italy fires at "the infantry in 4-02" — target by <i>type</i>, not unit; it mostly fights blind [12.24]. RNF pays <b>3 CP</b> for being barraged. Italian guns: 3 TOE × Barrage 9 = 27 Raw → <b>3 Actual</b>; on the Barrage table [12.6] the 3–4 column vs Infantry gives <i>No effect</i> on 11–44, <i>Pinned</i> on 45–66 — losses need 5+ points. Italy rolls 52 → <b>RNF is Pinned</b>. RHA's 3 points at the stack below: 23 → no effect.</li>
<li><b>Retreat Before Assault.</b> Pinned units may not retreat [12.6 note] — the RNF must stand. That is what barrage is for.</li>
<li><b>Force Assignment.</b> Both secretly assign TOE points to Anti-Armor or Close Assault. No armour is engaged, so everything to Close Assault.</li>
<li><b>Anti-Armor.</b> Nothing to shoot at.</li>
<li><b>Close Assault.</b> Costs attacker <b>5 CP</b>, defender <b>3 CP</b>. Maths in the box below.</li>
</ol>"""
    ledger = """
<div class="calc">
<h3>Close Assault: 2 Libyan regiments (3-01) vs 1 RNF (4-02)</h3>
<table>
<tr><th>Rule of ten [11.32]</th><td><b>Actual</b> points = (Rating × TOE points used) ÷ 10, rounded (11.4→11, 11.5→12). Everything in combat is compared in Actual points.</td></tr>
<tr><th>Attacker</th><td>2 regts × 12 TOE × Off rating 1 = 24 Raw → <b>2 Actual</b></td></tr>
<tr><th>Defender</th><td>1 RNF: 7 TOE × Def rating 2 = 14 Raw → <b>1 Actual</b></td></tr>
<tr><th>Differential</th><td>2 − 1 = <b>+1</b></td></tr>
<tr><th>2:1 Raw superiority [15.51]</th><td>24 vs 14 — not double → no shift</td></tr>
<tr><th>Terrain [8.37]</th><td>Rough <b>L2</b>, Up Escarpment <b>L3</b> → five columns left → <b>−4</b></td></tr>
<tr><th>Morale [15.6, 17.2]</th><td>Each side rolls on the Morale Modification Table for its Cohesion (both 0 → no change). Italians −1, RNF +1 → attacker minus defender = −2 → two columns left → <b>−6</b></td></tr>
<tr><th>Size [15.53]</th><td>Largest unit regiment (≈ brigade) vs battalion → 2 columns to the larger side → <b>−4</b></td></tr>
<tr><th>Final column</th><td><b>−4/−5</b> on the CRT [15.79]</td></tr>
<tr><th>Attacker rolls 3,4 → "34"</th><td>−4 column, attacker losses: 15% band is 34–44 → <b>Italians lose 15%</b> ≈ 4 of 24 TOE points</td></tr>
<tr><th>Same dice, summed = 7</th><td>Engaged row at −4 is "12" only → <b>not Engaged</b>; Captured row for attacker at −4: 2–4 → no</td></tr>
<tr><th>Defender rolls 1,2 → "12"</th><td>−4 column, defender losses: 15% band is "11", so 12 falls in the 10% band → <b>RNF loses 10%</b> ≈ 1 TOE point. Sum 3 → Captured possible (2–3 at −4): one more die decides what fraction of the loss is prisoners [15.89]</td></tr>
<tr><th>Outcome</th><td>RNF holds the pass at 6 TOE. Italians bloodied: 4 points gone, 3 DP each from over-CPA (next box). Both remain adjacent, in contact.</td></tr>
</table>
<p class="fine">Five column shifts for terrain is why nobody storms an escarpment frontally. In real play the Italians would send the Bersaglieri and tankettes round by a track, or barrage for two stages first. The escarpment also blocks vehicles entirely, so no Combined Arms bonus is even possible here.</p>
</div>"""
    panels.append(panel("4 · Combat Segment", body, note, ledger))

    ledger = """
<div class="calc">
<h3>CP ledger after cycle 1 — the whole game in one table</h3>
<table class="ledger">
<tr><th>Unit</th><th>CPA</th><th>Spent so far</th><th>Left</th><th>Cohesion</th><th>Notes</th></tr>
<tr><td>I/1 Libyan</td><td>8</td><td>3 move + 3 barraged + 5 assault = <b>11</b></td><td>−3</td><td class="bad">−3</td><td>Exceeded CPA by 3 → 3 Disorganization Points [6.21]; lost ~2 TOE in the assault</td></tr>
<tr><td>II/1 Libyan</td><td>8</td><td>3 + 3 + 5 = <b>11</b></td><td>−3</td><td class="bad">−3</td><td>Same. Both regiments will fight at worse morale next time.</td></tr>
<tr><td>1 Lib Art</td><td>8</td><td>1 move + 5 barrage (phasing "barrage and/or assault" = 5) = <b>6</b></td><td>2</td><td>0</td><td>Ammo spent from the Supply Unit.</td></tr>
<tr><td>IX L3</td><td>25</td><td><b>0</b></td><td>25</td><td>0</td><td>In Reserve, untouched.</td></tr>
<tr><td>1 RNF</td><td>8</td><td>3 barraged + 3 defend = <b>6</b></td><td class="warn">2</td><td>0</td><td>Pinned this segment; 6 TOE left. Only 2 CP for <i>its own</i> half of the stage [6.14] — it cannot both move and fight.</td></tr>
<tr><td>11 Hussars</td><td>25</td><td>2 react = <b>2</b></td><td>23</td><td>0</td><td>1 TOE point broken down.</td></tr>
<tr><td>4 RHA</td><td>10</td><td>3 barrage = <b>3</b></td><td>7</td><td>0</td><td></td></tr>
</table>
</div>"""
    body = "\n".join([U("I/Lib", (3, 1)), U("II/Lib", (3, 1), offset=1), U("Art", (2, 1)), U("L3", (0, 2), marker="RES I"),
                      U("11H", (5, 1), marker="BD 1"), U("RNF", (4, 2)), U("RHA", (5, 2))])
    note = """
<p><b>What the ledger says.</b> The Italians took the fight to the pass and paid for it in Cohesion: at −3 each, both regiments now get a morale penalty in their next assault, and only recover +5 per stage of doing <i>nothing</i> [6.24].</p>
<p>The RNF held, but it has 2 CP left for the Commonwealth half. Pinned by the barrage this segment; pinned by arithmetic next.</p>
<p>In the Logistics Game, add: fuel burned by the Hussars, ammo per TOE point for every shot, water drawn at Bir Sofafi, stores issued at turn start. That's the paperwork.</p>"""
    panels.append(panel("5 · The ledger: Capability Points and Cohesion", body, note, ledger))

    body = "\n".join([U("I/Lib", (3, 1), dim=True), U("II/Lib", (3, 1), offset=1, dim=True), U("Art", (2, 1)),
                      arrow([(0, 2), (1, 2), (2, 2), (3, 2)], label="Released: 2 clear + 1 rough = 8 CP"), U("L3", (3, 2)),
                      U("11H", (5, 1)), U("RNF", (4, 2)), U("RHA", (5, 2)),
                      f'<text x="{center(3,1)[0]:.1f}" y="{center(3,1)[1] + R + 14:.1f}" font-size="10" fill="#b00" text-anchor="middle" font-weight="bold">within 2 hexes: may move again</text>'])
    note = """
<p><b>G4. Reserve Release, then Player A chooses: another cycle?</b></p>
<p>Under <b>Continual Movement</b> [8.2] Italy may repeat Move → Breakdown → Combat as often as it likes. Only units that ended within two hexes of the enemy may move again — the two regiments qualify; the artillery does not [8.23]. The L3s, released from Reserve, may move regardless.</p>
<p><b>Option A:</b> assault again now with the regiments. Cost another 5 CP each → cohesion −8, a Morale Modification roll at −8 likely costs them another column, and they attack at −4 again with 20 TOE instead of 24. The RNF, no longer Pinned, may now Retreat Before Assault at 2 CP/hex — it has exactly 2.</p>
<p><b>Option B:</b> stop. Release the L3s along the plateau (Clear 2 CP × 2 + Rough 4 = 8 of 25) to threaten the RNF's flank at 3-02 next stage, let the regiments rest a stage to recover 5 cohesion, and barrage the pass again first.</p>
<p>That choice — push exhausted units now for tempo, or accept the delay to keep them coherent — is the game. Then Player B does phases F–L with what it has left.</p>"""
    panels.append(panel("6 · Reserve Release and the Continual Movement decision", body, note))
    return "".join(panels)


# ---------------------------------------------------------------- Part B
PART_B = """
<h1 class="part">Part B · The combat maths, in full</h1>
<p class="sub">Every combat step uses the same currency and the same dice convention. Once you have those two, the tables are just lookups.</p>
<section class="panel">
<h2>B1 · Two conventions that run all of combat</h2>
<div class="cols">
<div class="calc">
<h3>Raw → Actual [11.3]</h3>
<p><b>Raw points</b> = Combat Rating × TOE Strength Points used. <b>Actual points</b> = Raw ÷ 10, rounded to nearest (11.4 → 11, 11.5 → 12). Under 5 Raw = 0 Actual [11.33]. All Raw points from every unit firing at the same target are summed <i>before</i> dividing [11.34].</p>
<p>Example from the rules [11.35]: 90th Leichte's artillery, 3 TOE × Barrage 9 = 27 Raw plus 3 TOE × 9 = 27 Raw → 54 Raw → <b>5 Actual Barrage Points</b>.</p>
<p>Consequence: a single battalion's 8 TOE × rating 1 = 8 Raw = <b>1 Actual</b>. Small units round to almost nothing. Concentration is forced on you by arithmetic.</p>
</div>
<div class="calc">
<h3>Two dice, read three ways [15.73]</h3>
<p>Every roll is two dice of different sizes. The <b>same</b> throw is read:</p>
<ol>
<li><b>Sequentially</b>, big die first: 3 and 4 = "34". Range 11–66. Used for losses on every table.</li>
<li><b>Summed</b>: 3 + 4 = 7. Used for Engaged (attacker) and Retreat (defender) rows on the Close Assault CRT.</li>
<li><b>Summed again</b> against the Captured row: if it hits, one more die on the Prisoners table [15.89] says what fraction of the losses are prisoners.</li>
</ol>
<p>Each player throws once per assault and gets all their results from it. Barrage and Anti-Armor only use the sequential read.</p>
</div>
</div>
</section>
<section class="panel">
<h2>B2 · Barrage [12]</h2>
<div class="row">
<div class="map"><img src="tbl_barrage.jpg" width="620" alt="Barrage table"></div>
<div class="note">
<p><b>Who:</b> anything with a Barrage Rating and ammo, into an <i>adjacent</i> hex. Ranges are abstracted away — that is the big simplification in CNA.</p>
<p><b>Position first.</b> Each gun unit is Forward or Back [12.1]. Forward guns can coordinate with other Forward guns on one target and can split fire between targets; Back guns fire alone. Forward guns are exposed: their Vulnerability rating decides whether they get captured or destroyed if the hex is overrun. Italian guns have extra restrictions on coordinating.</p>
<p><b>Target by type.</b> You barrage "the infantry in 4-02", not a named unit, unless a patrol has told you what is there [12.24]. The table has four target classes: Infantry, Armor, Gun, Truck. You roll separately for the trucks in the hex.</p>
<p><b>Reading the table.</b> Column = Actual Barrage Points. Find where your sequential roll falls. Results: <i>No effect</i>; <i>Pinned</i> = may not Retreat Before Assault, may not assault; <i>1</i> / <i>2</i> = lose that many TOE points (and Pinned for infantry/armor).</p>
<p><b>What the numbers say.</b> With 3–4 points vs Infantry you can only Pin (45–66). You need 5–6 points for any chance of a kill (66 only), 13+ for a real one. Killing with artillery is expensive; <b>pinning is the job</b> — it strips the defender's option to retreat and sets up the assault.</p>
<p><b>Cost.</b> Firing costs the unit 5 CP (phasing) and ammo per TOE point fired [50.14] — 4 TOE of German 150mm at ammo rate 4 = 16 Ammo Points for one shoot, regardless of result. Being barraged costs the target 3 CP.</p>
</div>
</div>
</section>
<section class="panel">
<h2>B3 · Anti-Armor fire [14]</h2>
<div class="row">
<div class="map"><img src="tbl_aa.jpg" width="620" alt="Anti-Armor CRT"></div>
<div class="note">
<p><b>Who:</b> anything with an Anti-Armor rating — AT guns, tanks, some infantry — at a hex containing units with an <b>Armor Protection Rating</b>. Both sides fire, simultaneously, before Close Assault.</p>
<p><b>Assignment.</b> Before this step both players secretly split each unit's TOE points between Anti-Armor and Close Assault, or withhold them. A TOE point does one or the other this segment, never both [14.0]. Withheld armor cannot be hit.</p>
<p><b>Reading the table.</b> Column = Actual Anti-Armor Points; row = sequential roll; cell = <b>Damage Points</b>. The phasing player reads one row <i>higher</i> (the defender is dug in, the attacker is moving) [14.6 note]. Terrain shifts columns left: rough/vegetation/L1 fort −1, mountain/L2–3 fort −2, attacking up a slope −1, up a ridge −2.</p>
<p><b>Absorbing damage [14.4].</b> The target owner must remove TOE points whose Armor Protection ratings <i>sum to at least</i> the Damage Points. Rules example: 5 Actual points, roll 35 → 7 Damage. Target hex has M11s (protection 2) and M13s (protection 3). Owner removes one M13 (3) + two M11 (4) = 7. Thick armour absorbs more per point lost — Matildas shrug off what would gut a tankette company.</p>
<p><b>Then:</b> a Destroyed Tanks marker goes in the hex. Dead tanks are recoverable — by either side — through the Repair and Tank Delivery rules [22.4, 14.5]. In the desert the wrecks were the prize.</p>
</div>
</div>
</section>
<section class="panel">
<h2>B4 · Close Assault [15] — the modifier ladder</h2>
<div class="row">
<div class="map"><img src="tbl_crt.jpg" width="620" alt="Close Assault CRT"></div>
<div class="note">
<p>Start with <b>Actual Off − Actual Def = Differential</b>, then walk the ladder. Every step is a <i>column shift</i> on the CRT, not a number change:</p>
<table class="ledger">
<tr><th>Step</th><th>Rule</th><th>Shift</th></tr>
<tr><td>Probe?</td><td>Attacker may declare a 2-CP Probe: same fight, restricted losses, gives information [15.9]</td><td>—</td></tr>
<tr><td>2:1 Raw</td><td>Either side with ≥ double the other's Raw points [15.51]</td><td>2 in their favour</td></tr>
<tr><td>Terrain</td><td>Terrain Effects Chart, Close Assault column [8.37]: Rough L2, Mountain L3, Up Escarpment L3, Wadi L1, Ridge L2, Fortifications up to L6 …</td><td>as listed</td></tr>
<tr><td>Combined Arms</td><td>Tanks need ≥ equal infantry TOE in the same hex; each 1–3 unsupported tank TOE = −1 Actual (max −4) [15.4]</td><td>changes points, not columns</td></tr>
<tr><td>Morale</td><td>Each side: Basic Morale ± a roll on the Morale Modification Table for its Cohesion [17.2], clamped ±3. Attacker minus defender = columns [15.6]</td><td>±1 per point</td></tr>
<tr><td>Size</td><td>Largest organisation on each side [15.53]: Div vs Bn 4, Bde vs Bn 2, Bn vs Coy 2, Div vs Coy 8</td><td>to the larger</td></tr>
<tr><td>Minefields / engineers</td><td>Enemy minefield: defender L1 [8.37 n.13]; engineers help the attacker</td><td>as listed</td></tr>
<tr><td>Gun alone</td><td>A gun unit with no defensive rating, alone: attacker takes no losses, +3 columns [15.54]</td><td>+3</td></tr>
</table>
<p>Then each side throws once. <b>Attacker</b> section: losses by sequential read, Engaged by sum, Captured by sum. <b>Defender</b> section: losses, Retreat (1/2/3 hexes, or 10% more instead), Captured. Overrun columns (+11 and up) are where whole units vanish.</p>
<p><b>Losses</b> are a percentage of the TOE points committed, rounded, taken by the owner from any committed unit [15.8]. A side losing 30%+ in one assault also takes 3 Disorganization Points [6.21] — a rout feeds on itself.</p>
<p><b>Ammo:</b> both sides pay per TOE point that fought [50.12]. The defender pays to be attacked. Running a defence out of ammunition is a legitimate way to win.</p>
</div>
</div>
</section>
"""


# ---------------------------------------------------------------- Part C
def flow_svg():
    W, Hh = 1180, 215
    o = [f'<svg viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}" xmlns="http://www.w3.org/2000/svg">',
         '<defs><marker id="fa" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#5a3d1a"/></marker></defs>']

    def node(x, y, w, h, title, lines, fill):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#5a3d1a" stroke-width="1.5"/>')
        o.append(f'<text x="{x + w/2}" y="{y + 22}" font-size="14" font-weight="bold" text-anchor="middle" fill="#222">{title}</text>')
        for i, ln in enumerate(lines):
            o.append(f'<text x="{x + w/2}" y="{y + 42 + i*16}" font-size="11.5" text-anchor="middle" fill="#333">{ln}</text>')

    def arr(x1, y1, x2, y2, label):
        o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#5a3d1a" stroke-width="3" marker-end="url(#fa)"/>')
        o.append(f'<text x="{(x1+x2)/2}" y="{y1 - 12}" font-size="10.5" text-anchor="middle" fill="#7a3b1e" font-weight="bold">{label}</text>')

    node(10, 40, 150, 160, "Italy / Sicily", ["Naval Convoy Stage", "planned 1 turn ahead [56]", "Ammo · Fuel · Stores", "Replacement Points", "RN + Malta can sink it"], "#e8eef7")
    arr(160, 120, 213, 120, "sea")
    node(215, 40, 175, 160, "Port of entry", ["Tripoli 15,000 t/stage", "Benghazi 2,500 · Tobruk 1,700", "Bardia 400 · Sollum 250", "Efficiency Level ÷ bombing", "1 Fuel Pt = ⅛ t · 1 Ammo Pt = 4 t", "Stores 1 t · Water ⅙ t [54.5]"], "#f3e6bf")
    arr(390, 120, 443, 120, "3rd-line trucks")
    node(445, 40, 195, 160, "Forward dump(s)", ["any hex; cities are dumps", "one OpStage truck ride apart [54.16]", "capacity by hex type [54.12]", "evaporation −6 % / turn (CW −9 %)", "+5 % in hot weather [49.3]", "can be blown, bombed, captured"], "#f3e6bf")
    arr(640, 120, 693, 120, "2nd-line trucks")
    node(695, 40, 195, 160, "Divisional / 1st-line", ["trucks attached to the unit", "carry men or supply, not both", "unit takes truck CPA when riding", "load / unload = 2 CP", "(0 in Organization Phase)", "cannot detach if cohesion ≤ −5"], "#e6efd9")
    arr(890, 120, 928, 120, "in hex")
    node(930, 40, 240, 160, "Consumption per unit", ["Fuel: rate × ⌈CP moved ÷ 5⌉ per TOE pt [49.13]", "Ammo: rate × TOE pts that fired [50.14]", "each pt carries one shot's worth", "Stores: 4 per TOE pt per turn [51.11]", "Water: 1 per bn + 1 per vehicle pt", "per stage [52.4]; +1 pasta pt (Italian bns)", "Weekly issue; without → DPs, attrition"], "#fbe3d6")
    o.append('</svg>')
    return "\n".join(o)


TRUCKS_HTML = """
<div class="cols" style="margin-top:14px">
<div class="calc"><h3>The truck itself [53, 54.2]</h3>
<p>1 Truck Point = 10 lorries. <b>Light</b>: carries 50 fuel / 2 ammo / 6 stores / 40 water, convoy CPA 40. <b>Medium</b>: 120 / 4 / 15 / 100, CPA 30. <b>Heavy</b>: 250 / 8 / 30 / 200, CPA 30.</p>
<p>Convoys are restricted to the dedicated truck-movement sub-phase and can never spend beyond their extended CPA (they break down on the spot if forced to). Road hex = ½ CP → about 60 road hexes per stage.</p>
<p>Every truck point burns 1 Fuel Point per 5 CP moved, drinks 1 Water Point per stage, and rolls for Breakdown like any vehicle.</p>
<p>Third-line: port → dump. Second-line: dump → units. First-line: on the unit's own sheet, not a counter. A recommended system, not a rule [53.14].</p></div>
<div class="calc"><h3>Rail and sea (Commonwealth)</h3>
<p>Railway Alexandria → Mersa Matruh: 1,500 t per stage, one commodity at a time, troops or supplies not both; rail hexes count as water pipeline [54.3]. One stage a month it carries only water.</p>
<p>Coastal shipping between African ports limited only by port capacity [5.2 II.B]. The Axis have coastal-ship counters instead, and must run them past the RAF and the Mediterranean Fleet.</p></div>
<div class="calc"><h3>Worked example: one medium truck point, Tripoli → Sollum</h3>
<p>Loaded with 120 Fuel Points. Route: Tripoli → Nofilia is off-map, 2 OpStages [8.89]; Nofilia → Bardia is 138 road hexes [56.26] = 69 CP = 3 stages at CPA 30. <b>Five stages one way</b> (≈ 1⅔ Game-Turns), ten round trip.</p>
<p>Truck's own fuel: 30 CP per stage ÷ 5 × rate 1 = 6 FP per stage → 30 FP out, 30 FP home. It arrives with 90 of its 120 and needs 30 of those to get back: <b>half the cargo goes to the trip</b> [49.18].</p>
<p>Meanwhile every dump it passed lost 6 % per turn to evaporation, it drank 10 Water Points, and rolled Breakdown ten times (≈ 70 BP of road vs its 2L rating). Ten such trips is one division's fuel for a week of movement.</p></div>
</div>
"""

PART_C_TAIL = """
<section class="panel">
<h2>C2 · Why it dominates</h2>
<div class="cols">
<div class="calc"><h3>Distance is the enemy</h3><p>Tripoli is the only big Axis port (15,000 t/stage). Tobruk takes 1,700 and starts damaged; Bardia and Sollum are rounding errors. Benghazi is 2,500 but its harbour was blocked historically. Everything for the front either lands at Tripoli and drives ~1,000 km, or comes through Tobruk under the RAF. The Commonwealth mirror image: Alexandria 15,000 t, a railway to Mersa Matruh, then trucks. Whoever is far from their port is starving — which is why the front oscillated between El Agheila and El Alamein for two years, and why the game does too.</p></div>
<div class="calc"><h3>Trucks are the binding constraint</h3><p>Trucks are mobility <i>and</i> supply. The Graziani scenario gives Italy 205 truck points at Tripoli plus 155 "anywhere in Libya", and each division has only 20–50 of its own [60.31, 60.33]. Every truck point hauling fuel is a truck point not motorising infantry. The Logistics Commander's whole job is deciding that split, then keeping the convoys moving every stage so nothing sits idle. The rules say it plainly: "Trucks are the game" [53.0].</p></div>
<div class="calc"><h3>Four commodities, four failure modes</h3><p><b>No fuel:</b> vehicles don't move; fuel must be in the hex, no debt. <b>No ammo:</b> can't fire — and a unit only carries one shot's worth itself. <b>No stores:</b> a Disorganization Point per turn, then 2 %, 4 %, 6 % attrition [51.2]. <b>No water:</b> vehicles can't move or assault; infantry can't exceed CPA, then worse [52.5]; Italian battalions without their pasta point at −10 cohesion disintegrate outright [52.6]. Each is tracked per unit on its TOE sheet. There are 1,800 counters.</p></div>
</div>
</section>
"""

# ---------------------------------------------------------------- Part D
PART_D = """
<h1 class="part">Part D · Graziani's Offensive on the real map (§60)</h1>
<p class="sub">Scenario 1: Game-Turn 1 OpStage 1 (13 Sept 1940) to Game-Turn 6 OpStage 3. 25–50 hours on the table. Map C, the Libya–Egypt frontier. Green = Italian starting hexes [60.31], orange = Commonwealth [60.41]; red = the historical axis of advance.</p>
<section class="panel">
<h2>D1 · Initial deployment</h2>
<img src="graziani.jpg" width="1200" alt="Map C with deployments">
<p class="fine">Map C, SPI 1979, from the archive.org scan; hex positions computed from the printed grid, ±half a hex. Sollum C4021, Halfaya Pass C3922, Bardia C4321, Sidi Barrani C4131, Fort Maddalena C3019. Not shown: 64 Catanzaro and 4 CCNN at C4707/C4507 (Tobruk area), Matruh garrison and 7th Armoured / 4th Indian on Map D.</p>
</section>
<section class="panel">
<h2>D2 · The situation</h2>
<div class="cols">
<div class="calc"><h3>Italy</h3><p>Five divisions and the Maletti Group stacked behind the wire between Bardia and Sidi Omar, plus Libyan Tank Command at Tobruk. Enormous infantry, feeble armour (L3 tankettes, a few M11s), morale mostly −1 to −3, and <b>almost no trucks</b>: 1 Libyan Div has 25 truck points for a division [60.31]. Supply is a 1,000 km road from Tripoli. Initiative rating 1 vs Commonwealth 3 [7.2]. Historically Graziani was ordered forward by Mussolini, marched 60 miles to Sidi Barrani in four days, stopped, and built fortified camps.</p></div>
<div class="calc"><h3>Commonwealth</h3><p>A screen, not a line: 11th Hussars' armoured cars on the wire, 1 RTR, 2nd Rifle Brigade, the Coldstream/KRRC/RHA group at Halfaya, French marines and Scots Guards on the coast. Behind them 7th Armoured Division at D3612 and 4th Indian at Matruh with real trucks, morale +1/+2, initiative 3, a railway to Matruh, and Alexandria's 15,000 t port. Historically they traded space, harassed, and lost almost nothing.</p></div>
<div class="calc"><h3>Victory [60.81]</h3><p><b>Italian tactical:</b> take and hold Sidi Barrani, keep Sollum, Fort Maddalena and Giarabub, all in supply back to Tobruk. <b>Decisive:</b> Mersa Matruh and Siwa. <b>Strategic:</b> Alexandria or Cairo (never happened). <b>CW tactical:</b> Sollum and Halfaya Pass plus Siwa, in supply to Alexandria. <b>Decisive:</b> Bardia, Ft Maddalena, Sidi Omar, Sollum, Siwa. <b>Strategic:</b> Tobruk. Note "in supply" is in every condition: you can take Sidi Barrani; the question is whether you can feed it.</p></div>
</div>
<div class="calc" style="margin-top:14px"><h3>What the six turns are actually about</h3>
<p>Turn 1: Italy has to go <i>now</i> — five divisions with 25 trucks each can only walk, at CPA 8 on a road (8 hexes a stage, ~64 km), and each stage of marching in September heat is drinking water the trucks must haul. The Commonwealth screen Reacts and Retreats Before Assault every stage, so contact rarely becomes assault; the 11th Hussars at CPA 25 can run rings round infantry. By turn 2–3 Italy is at Sidi Barrani with the tactical victory in hand and a supply line of 138 road hexes to Tobruk's 1,700 t/stage port. Turns 4–6 are the real game: can Italy stock enough dumps forward to keep the Sidi Barrani camps in stores and water before 7th Armoured arrives from the east with trucks and fuel? Historically the answer was no, and the December counterstroke (Operation Compass, the longer "Italian Campaign" scenario to turn 20) took 130,000 prisoners.</p>
<p>That is the whole design in one scenario: the fighting is easy, the arithmetic decides it, and the arithmetic is on the trucks.</p></div>
</section>
"""

CSS = """
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:#faf6ec;color:#222;margin:0;padding:24px;max-width:1240px}
h1{margin:0 0 4px;font-size:26px} .sub{color:var(--learn-muted,#666);margin:0 0 20px}
.part{margin:34px 0 4px;font-size:24px;color:var(--learn-accent,#5a3d1a);border-top:3px solid var(--learn-rule,#c9b98f);padding-top:18px}
.panel{background:var(--learn-panel,#fff);border:1px solid var(--learn-line,#d8cfb5);border-radius:8px;padding:16px 20px;margin:0 0 22px}
.panel h2{margin:0 0 12px;font-size:18px;color:var(--learn-accent,#5a3d1a)}
.row{display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap} .map{flex:1 1 560px;min-width:0} .note{flex:1 1 300px;font-size:14px;line-height:1.45}
.panel svg{display:block;max-width:100%;height:auto}
.note p{margin:0 0 10px} .note ol{margin:0 0 10px 18px;padding:0} .note li{margin:0 0 6px}
.cols{display:flex;gap:14px;align-items:stretch;flex-wrap:wrap} .cols .calc{flex:1 1 280px;margin-top:0}
.esc{border-bottom:4px solid #7a3b1e} .rough{background:repeating-linear-gradient(135deg,#e2cf9e 0 3px,#a88d55 3px 4px);padding:0 3px}
.calc{margin-top:14px;background:var(--learn-calc,#f7f1de);border:1px solid var(--learn-line,#d8cfb5);border-radius:6px;padding:10px 14px;font-size:13px}
.calc h3{margin:0 0 8px;font-size:15px}
table{border-collapse:collapse;width:100%} th,td{text-align:left;vertical-align:top;padding:4px 8px;border-bottom:1px solid var(--learn-line,#e3dac1)}
th{white-space:nowrap;color:var(--learn-accent,#5a3d1a);font-weight:600}
.ledger th{border-bottom:2px solid var(--learn-rule,#c9b98f)} .bad{color:var(--learn-bad,#b00);font-weight:bold} .warn{color:var(--learn-warn,#b8600b);font-weight:bold}
.fine{color:var(--learn-muted,#666);font-size:12px;margin:8px 0 0}
.legend{display:flex;gap:18px;font-size:13px;color:var(--learn-muted,#444);margin:0 0 18px;flex-wrap:wrap}
.sw{display:inline-block;width:22px;height:14px;vertical-align:middle;border:1px solid var(--learn-swatch,#222);margin-right:5px;border-radius:2px}
"""

# Site-only rules, already scoped. `layout: page` hands the primer the full column (the doc layout's 688px
# would squeeze the notes into a strip beside the map), so the page supplies what .vp-doc would have: link
# and code styling, page margins, and a palette for the dark scheme through the --learn-* variables above.
SITE_CSS = """
.learn{max-width:1240px;margin:0 auto;padding:24px 32px 96px;line-height:1.5} .learn .panel{overflow-x:auto}
.dark .learn{--learn-accent:#d9b46a;--learn-rule:#5a4a2e;--learn-line:var(--vp-c-divider);--learn-panel:var(--vp-c-bg-soft);--learn-calc:var(--vp-c-bg-alt);--learn-muted:var(--vp-c-text-2);--learn-swatch:var(--vp-c-text-3);--learn-bad:#f0776a;--learn-warn:#e0a24a}
.learn a{color:var(--vp-c-brand-1);text-decoration:underline;text-underline-offset:2px}
.learn code{font-family:var(--vp-font-family-mono);font-size:0.9em;background:var(--vp-c-default-soft);padding:2px 5px;border-radius:4px}
.learn .learn-table{margin:0 0 18px;overflow-x:auto} .learn .learn-table h4{margin:0 0 4px;font-size:15px} .learn .learn-table-ref{margin:0 0 8px}
.learn .learn-table .spi-badge{margin:0} .learn table.crt{margin:0 0 12px;font-size:13px} .learn table.crt td{white-space:nowrap} .learn table.crt caption{text-align:left;font-weight:600;padding:4px 0}
@media (max-width:640px){.learn{padding:16px 16px 64px} .learn .panel{padding:12px 14px}}
"""


# ---------------------------------------------------------------- site mode (Part D of mission 2)
SITE_MD = ROOT / "site" / "learn.md"
CASE_RE = re.compile(r"\[([0-9][0-9.,\s]*?)\]")
PART_D_NOTE = """
<h1 class="part">Part D · Graziani's Offensive on the real map</h1>
<p class="sub">Part D walks Scenario 1 (§60) across Map C hex by hex. It is published when the map sub-project has redrawn Map C as our own; until then it lives in the local build of this primer only.</p>
"""


def case_index():
    """SPI case id -> rules file stem carrying it (primary or omit badge), from tools/check_coverage."""
    from check_coverage import parse_badges
    idx, rank = {}, {"spi": 0, "spi-omit": 1, "spi-ref": 2}   # a primary badge wins over an omit or a cross-reference
    for md in sorted((ROOT / "rules").glob("*.md")):
        if md.stem in ("coverage", "changes", "glossary"):
            continue
        for b in parse_badges(md.read_text()):
            for c in b["cases"]:
                if c not in idx or rank[b["kind"]] < rank[idx[c][1]]:
                    idx[c] = (md.stem, b["kind"])
    return {c: stem for c, (stem, _) in idx.items()}


def link_cases(text, idx=None):
    """[8.37], [15.79, 12.6] -> links into the rules files; unknown cases and SVG text untouched."""
    idx = case_index() if idx is None else idx

    def repl(m):
        parts = [p.strip() for p in m.group(1).split(",")]
        if not all(p in idx for p in parts):
            return m.group(0)
        return "[" + ", ".join(f'<a href="rules/{idx[p]}#spi-{p}">{p}</a>' for p in parts) + "]"

    out, pos = [], 0
    for svg in re.finditer(r"<svg.*?</svg>", text, flags=re.S):
        out.append(CASE_RE.sub(repl, text[pos:svg.start()]))
        out.append(svg.group(0))
        pos = svg.end()
    out.append(CASE_RE.sub(repl, text[pos:]))
    return "".join(out)


def scoped_css():
    """The standalone CSS with every selector scoped under .learn; the page-level body rule dropped."""
    out = []
    for line in CSS.strip().splitlines():
        rules = re.findall(r"([^{}]+)\{([^{}]*)\}", line)
        for sel, body in rules:
            sels = [s.strip() for s in sel.split(",")]
            if sels == ["body"]:
                continue
            out.append(", ".join(f".learn {s}" for s in sels) + "{" + body.strip() + "}")
    return "\n".join(out) + "\n" + SITE_CSS.strip()


def site_markdown():
    import learn_tables
    part_b = PART_B
    for name, img in (("barrage-results", "tbl_barrage.jpg"), ("anti-armour-results", "tbl_aa.jpg"), ("close-assault-results", "tbl_crt.jpg")):
        part_b = re.sub(rf'<div class="map"><img src="{img}"[^>]*></div>', lambda m, n=name: f'<div class="map">{learn_tables.render(n)}</div>', part_b)
    assert "<img" not in part_b
    part_b = part_b.replace('<h1 class="part">Part B', '<h1 id="part-b" class="part">Part B', 1)
    body = f"""<h1>The Campaign for North Africa — illustrated</h1>
<p class="sub">Terrain costs [8.37], CP costs [6.3], CRT [15.79] and the tables are the real 1979 values from <code>data/tables/</code>; unit ratings in Part A are illustrative. Case numbers in brackets link into the rules.</p>
<h1 id="part-a" class="part" style="margin-top:8px;border:0;padding:0;font-size:22px">Part A · One Operations Stage</h1>
<p class="sub">Player A's half of Operations Stage 1, Game-Turn 1 (Sept 1940), on a small sketch map.</p>
<div class="legend">
<span><span class="sw" style="background:{AXIS}"></span>Italian</span>
<span><span class="sw" style="background:{CW_C}"></span>Commonwealth</span>
<span><span class="sw" style="background:#f3e6bf"></span>Clear (2 CP)</span>
<span><span class="sw rough"></span>Rough (3/4 CP, L2 assault)</span>
<span><span class="sw" style="background:#333"></span>Road (1 / ½ CP)</span>
<span><span class="sw" style="border:2px dashed #7a5a2a;background:none"></span>Track (halves the hex)</span>
<span><span class="sw" style="background:#7a3b1e"></span>Escarpment hexside (+6 up, no vehicles)</span>
<span><span class="sw" style="background:#9ec9e2"></span>Sea</span>
</div>
{part_a()}
{part_b}
<h1 id="part-c" class="part">Part C · How supply actually flows (Logistics Game, §47–58)</h1>
<p class="sub">Replace §32's abstract Supply Units with this. Four commodities, three truck lines, and every arrow below is bookkeeping a human had to do by hand.</p>
<section class="panel"><h2>C1 · The pipeline</h2>{flow_svg()}{TRUCKS_HTML}</section>
{PART_C_TAIL}
{PART_D_NOTE}
<p class="fine">Generated by <code>tools/learn_page.py --site</code> from our own prose, SVGs and CC0 data; no SPI material.</p>"""
    body = link_cases(body)
    body = "\n".join(ln for ln in body.splitlines() if ln.strip())
    return f"""---
title: Learn
layout: page
sidebar: false
---
<div class="learn">
<style>
{scoped_css()}
</style>
{body}
</div>
"""


def write_site():
    SITE_MD.write_text(site_markdown())
    print(SITE_MD)


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    make_table_crops()
    make_map_overlay()
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>The Campaign for North Africa — illustrated</title><style>{CSS}</style></head><body>
<h1>The Campaign for North Africa — illustrated</h1>
<p class="sub">Terrain costs [8.37], CP costs [6.3], CRT [15.79] and the charts are the real 1979 values; unit ratings in Part A are illustrative. Case numbers in brackets refer to the SPI rules.</p>
<h1 class="part" style="margin-top:8px;border:0;padding:0;font-size:22px">Part A · One Operations Stage</h1>
<p class="sub">Player A's half of Operations Stage 1, Game-Turn 1 (Sept 1940), on a small sketch map.</p>
<div class="legend">
<span><span class="sw" style="background:{AXIS}"></span>Italian</span>
<span><span class="sw" style="background:{CW_C}"></span>Commonwealth</span>
<span><span class="sw" style="background:#f3e6bf"></span>Clear (2 CP)</span>
<span><span class="sw rough"></span>Rough (3/4 CP, L2 assault)</span>
<span><span class="sw" style="background:#333"></span>Road (1 / ½ CP)</span>
<span><span class="sw" style="border:2px dashed #7a5a2a;background:none"></span>Track (1 CP)</span>
<span><span class="sw" style="background:#7a3b1e"></span>Escarpment hexside (+6 up, no vehicles)</span>
<span><span class="sw" style="background:#9ec9e2"></span>Sea</span>
</div>
{part_a()}
{PART_B}
<h1 class="part">Part C · How supply actually flows (Logistics Game, §47–58)</h1>
<p class="sub">Replace §32's abstract Supply Units with this. Four commodities, three truck lines, and every arrow below is bookkeeping a human had to do by hand.</p>
<section class="panel"><h2>C1 · The pipeline</h2>{flow_svg()}{TRUCKS_HTML}</section>
{PART_C_TAIL}
{PART_D}
<p class="fine">Generated by tools/learn_page.py. Table crops and map are SPI 1979 material from the archive.org scan, for study only; not committed.</p>
</body></html>"""
    (OUT / "index.html").write_text(doc)
    print(OUT / "index.html")


if __name__ == "__main__":
    write_site() if "--site" in sys.argv[1:] else build()
