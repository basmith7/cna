#!/usr/bin/env python3
"""Derive hex and hexside terrain from the CNA VASSAL module (v2.1.0).

The module's buildFile.xml gives exact hex geometry per map sheet (a sideways
HexGrid inside each Zone plus a HexGridNumbering), so every hex ID the module
displays (e.g. C4807) maps deterministically to a pixel centre on Mitch
Guthrie's 2021 redraw.  The redraw is flat-colour vector art, so terrain is
read by sampling colours at hex centres and hexside midpoints.  Class names
follow the Terrain Key and the Terrain Effects Chart [8.37] printed on Map A
(archive.org scan p0187).

Nothing from the module is committed: buildFile.xml, the map PNG and the
derived class map are cached under ~/.cache/cna-vassal/ (extracted from the
.vmod on the first run); debug CSVs and crops go to --out (git-ignored), and
the game-fact raw document goes to --write-raw.

Usage:
  python3 tools/map_extract.py [--vmod PATH] [--cache-only] [--zone "Map C"] [--out build/map]
    --write-raw data/map/raw   write raw/<sheet>.json (game facts only)
    --debug X0 Y0 W H          also write an overlay crop with hex IDs and classes
    --check                    score village/city detection against known locations
"""
import argparse, csv, json, math, os, pathlib, re, sys, zipfile
from collections import Counter, defaultdict

import numpy as np
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
CACHE = pathlib.Path(os.path.expanduser("~/.cache/cna-vassal"))
ROOT = pathlib.Path(__file__).resolve().parents[1]
BOARD = "CNA Original"
MAP_IMAGE = "CNA Map Vassal Mitch Guthrie 2021.png"
BUILDFILE = "buildFile.xml"
VMOD = "CNAv2.1.0.vmod"
MODULE_REF = "vassal:CNAv2.1.0"

# Flat colours in the redraw.  Left: class; right: what the Terrain Key calls it.
PALETTE = {
    # hex fills
    "clear":        (251, 250, 239),
    "sea":          (138, 181, 207),   # also river water
    "rough":        (194, 185, 149),   # plain tan
    "salt_marsh":   (186, 175, 129),   # tan with yellow net
    "desert":       (223, 207, 100),   # yellow; also the salt-marsh net lines
    "delta":        (164, 178, 171),
    "mountain":     (151, 136,  66),
    "heavy_veg":    (203, 216,  91),
    "swamp":        ( 91, 161, 102),   # green dashes on clear
    "gravel":       (170, 157,  97),   # ring outlines on clear (Rock/Gravel)
    # hexside bands
    "escarpment":   ( 94,  97,  98),
    "ridge_slope":  (160, 146,  80),   # ridge: both sides; slope: one side
    "wadi":         (127, 148, 142),
    "river_edge":   (121, 168, 195),
    # lines crossing hexsides
    "road":         ( 72,  63,  34),   # solid = Road, dashed = Unfinished Road
    "rail":         ( 84,  88,  89),   # with ties = Railroad, dashed = Track
    # symbols
    "dot_blue":     ( 74, 138, 179),   # village dot (also labels, frontier dots)
    "hexline":      ( 51,  53,  51),
    "city":         ( 91, 149, 185),   # hatched blocks
    "dot_dark":     ( 66,  70,  73),   # village dots on Map E; also city icons
    "white":        (233, 232, 223),
}
CLASS = {name: i for i, name in enumerate(PALETTE)}
NONE = 255
FILLS = ("clear", "sea", "rough", "salt_marsh", "desert", "delta", "mountain", "heavy_veg")
TOLERANCE = 12    # fills are exact flat colours; keep anti-aliased edge pixels out
RAIL_THR = 3          # rail-class pixels needed on each side of a hexside (dashed tracks are sparse)
RIDGE_THR = 60        # ridge/slope band pixels in a 7px disc beside the hexside (the band is ~8px wide)
RAIL_OFFS = (6, 13)   # distances from the hexside at which the rail band is sampled


# --------------------------------------------------------------- buildFile
def load_zones(cache_dir=CACHE, vmod=None):
    """(image_path, zones).  Reads buildFile.xml and the PNG from the cache; extracts
    them from the .vmod (given, or the cached copy) only when missing."""
    cache_dir = pathlib.Path(cache_dir)
    xml_path, img = cache_dir / BUILDFILE, cache_dir / MAP_IMAGE
    if not xml_path.exists() or not img.exists():
        vmod = pathlib.Path(vmod) if vmod else cache_dir / VMOD
        if not vmod.exists():
            raise SystemExit(f"no {BUILDFILE} in {cache_dir} and no .vmod at {vmod}; see tools/sources.json → vassal")
        with zipfile.ZipFile(vmod) as z:
            cache_dir.mkdir(parents=True, exist_ok=True)
            if not xml_path.exists():
                xml_path.write_bytes(z.read(BUILDFILE))
            if not img.exists():
                img.write_bytes(z.read(f"images/{MAP_IMAGE}"))
    return img, parse_zones(xml_path.read_text("utf-8"))


def parse_zones(xml):
    """zones: list of dicts with polygon, grid, numbering, from buildFile.xml text."""
    i = xml.index(f'name="{BOARD}"')
    j = xml.index("</VASSAL.build.module.map.boardPicker.Board>", i)
    board = xml[i:j]
    zones = []
    attrs = lambda tag: dict(re.findall(r'(\w+)="([^"]*)"', tag))
    tag_re = re.compile(r"<(/?)VASSAL\.build\.module\.map\.boardPicker\.board\.(mapgrid\.Zone|HexGrid|mapgrid\.HexGridNumbering)\b([^>]*)>")
    cur = None
    for m in tag_re.finditer(board):
        closing, kind, rest = m.groups()
        if kind == "mapgrid.Zone" and not closing:
            a = attrs(rest)
            cur = {"name": a["name"], "fmt": a["locationFormat"],
                   "poly": [tuple(map(int, p.split(","))) for p in a["path"].split(";")]}
        elif kind == "mapgrid.Zone":
            if cur and "grid" in cur:
                zones.append(cur)
            cur = None
        elif closing:
            continue
        elif kind == "HexGrid" and cur is not None:
            a = attrs(rest)
            cur["grid"] = {k: float(a[k]) for k in ("dx", "dy")} | {k: int(a[k]) for k in ("x0", "y0")} \
                          | {"sideways": a["sideways"] == "true"}
        elif kind == "mapgrid.HexGridNumbering" and cur is not None:
            a = attrs(rest)
            cur["num"] = {"hOff": int(a["hOff"]), "vOff": int(a["vOff"]), "hLeading": int(a["hLeading"]),
                          "vLeading": int(a["vLeading"]), "stagger": a["stagger"] == "true",
                          "vDescend": a["vDescend"] == "true", "hDescend": a["hDescend"] == "true",
                          "first": a["first"], "sep": a["sep"]}
    return zones


# ---------------------------------------------------------------- geometry
# Port of VASSAL HexGrid / HexGridNumbering for the sideways case.  VASSAL
# swaps x and y for a sideways grid, then treats it as a flat-top grid whose
# "columns" step by dx and "rows" by dy; so on the real map columns run down
# the page and rows across it.  Hexes are pointy-top; inradius = dy/2.

def hex_center(g, nx, ny):
    """Raw index -> board pixel (VASSAL truncation reproduced)."""
    dx, dy = g["dx"], g["dy"]
    x = int(dx * nx + g["x0"])
    y = int(dy * ny + g["y0"]) if nx % 2 == 0 else int(dy * ny + int(dy / 2) + g["y0"])
    return (y, x) if g["sideways"] else (x, y)


def fmt(n, leading):
    s = "-" if n < 0 else ""
    n = abs(n)
    while leading > 0 and n < 10 ** leading:
        s += "0"; leading -= 1
    return s + str(n)


def hex_name(zone, nx, ny):
    g, num, poly = zone["grid"], zone["num"], zone["poly"]
    xs, ys = [p[0] for p in poly], [p[1] for p in poly]
    w, h = max(xs) - min(xs), max(ys) - min(ys)
    max_rows = math.floor(h / g["dx"] + 0.5)
    max_cols = math.floor(w / g["dy"] + 0.5)
    col, row = nx, ny
    if not g["sideways"]:
        raise NotImplementedError("non-sideways grids not needed for CNA")
    if num["vDescend"]: col = max_rows - col
    if num["hDescend"]: row = max_cols - row
    if num["stagger"] and nx % 2 != 0:
        row += -1 if num["hDescend"] else 1
    c, r = fmt(col + num["hOff"], num["hLeading"]), fmt(row + num["vOff"], num["vLeading"])
    grid_loc = c + num["sep"] + r if num["first"] == "H" else r + num["sep"] + c
    return zone["fmt"].replace("$name$", zone["name"]).replace("$gridLocation$", grid_loc)


def sheet_letter(zone_name):
    return "M" if zone_name == "Malta" else zone_name.replace("Map ", "")


def hex_id(zone, nx, ny):
    """(sheet letter, printed row, printed col).  VASSAL's 'col' (nx, down the page,
    vDescend) is the printed row; its 'row' (ny, across) is the printed column."""
    g, num, poly = zone["grid"], zone["num"], zone["poly"]
    xs, ys = [p[0] for p in poly], [p[1] for p in poly]
    max_rows = math.floor((max(ys) - min(ys)) / g["dx"] + 0.5)
    max_cols = math.floor((max(xs) - min(xs)) / g["dy"] + 0.5)
    col, row = nx, ny
    if num["vDescend"]: col = max_rows - col
    if num["hDescend"]: row = max_cols - row
    if num["stagger"] and nx % 2 != 0:
        row += -1 if num["hDescend"] else 1
    return sheet_letter(zone["name"]), col + num["hOff"], row + num["vOff"]


def observed_shift(zone):
    """'west' if odd printed rows sit half a hex west of even rows on this sheet.
    nx 0 and 1 are consecutive printed rows (vDescend only reverses the order);
    for a sideways grid hex_center()[0] is the across-the-page (screen x) coordinate."""
    g = zone["grid"]
    x = {nx: hex_center(g, nx, 0)[0] for nx in (0, 1)}
    odd = 1 if hex_id(zone, 1, 0)[1] % 2 == 1 else 0
    return "west" if x[odd] < x[1 - odd] else "east"


def in_bounds(ident, bounds):
    _, r, c = ident
    return bounds["rows"][0] <= r <= bounds["rows"][1] and bounds["cols"][0] <= c <= bounds["cols"][1]


def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            inside = not inside
    return inside


def enumerate_hexes(zone):
    g, poly = zone["grid"], zone["poly"]
    xs, ys = [p[0] for p in poly], [p[1] for p in poly]
    # sideways: nx indexes y, ny indexes x
    nx_lo, nx_hi = int((min(ys) - g["x0"]) / g["dx"]) - 1, int((max(ys) - g["x0"]) / g["dx"]) + 1
    ny_lo, ny_hi = int((min(xs) - g["y0"]) / g["dy"]) - 1, int((max(xs) - g["y0"]) / g["dy"]) + 1
    for nx in range(nx_lo, nx_hi + 1):
        for ny in range(ny_lo, ny_hi + 1):
            cx, cy = hex_center(g, nx, ny)
            if point_in_poly(cx, cy, poly):
                yield (nx, ny), (cx, cy)


# Pointy-top hex: edge midpoints at 0,60,..300 degrees from +x (east, clockwise
# on screen since y grows downward).
SIDES = [("E", 0), ("SE", 60), ("SW", 120), ("W", 180), ("NW", 240), ("NE", 300)]


# ------------------------------------------------------------- class map
def class_map(img_path):
    """uint8 array of palette class per pixel (NONE where no colour is within TOLERANCE)."""
    cached = CACHE / (img_path.stem + ".classes.npy")
    if cached.exists():
        return np.load(cached)
    im = np.asarray(Image.open(img_path).convert("RGB"), dtype=np.int32)
    pal = np.array(list(PALETTE.values()), dtype=np.int32)
    out = np.full(im.shape[:2], NONE, dtype=np.uint8)
    for y in range(0, im.shape[0], 256):
        chunk = im[y:y + 256]
        d = ((chunk[:, :, None, :] - pal[None, None, :, :]) ** 2).sum(-1)
        best = d.argmin(-1)
        ok = d.min(-1) < TOLERANCE ** 2
        out[y:y + 256] = np.where(ok, best, NONE)
    np.save(cached, out)
    return out


def disc_offsets(r):
    ys, xs = np.mgrid[-r:r + 1, -r:r + 1]
    m = xs * xs + ys * ys <= r * r
    return ys[m], xs[m]


DISCS = {r: disc_offsets(r) for r in (4, 6, 7, 16, 30)}


def sample(cm, cx, cy, r):
    """Counter of palette classes in a disc of radius r."""
    dy, dx = DISCS[r]
    ys, xs = cy + dy, cx + dx
    ok = (ys >= 0) & (ys < cm.shape[0]) & (xs >= 0) & (xs < cm.shape[1])
    vals = cm[ys[ok], xs[ok]]
    counts = np.bincount(vals, minlength=256)
    return {name: int(counts[i]) for name, i in CLASS.items() if counts[i]}


def solid_centres(cm, classes, k, frac=0.85):
    """Pixels where a k x k window is >= frac full of `classes`.  k=9 finds the
    ~12px village dots; k=5 finds the city hatch blocks but not the 3px
    coastline stroke drawn in the same blue."""
    mask = np.isin(cm, [CLASS[c] for c in classes]).astype(np.int32)
    s = np.pad(mask, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    win = s[k:, k:] - s[:-k, k:] - s[k:, :-k] + s[:-k, :-k]
    ys, xs = np.nonzero(win >= frac * k * k)
    return list(zip(xs + k // 2, ys + k // 2))


def bucket(points):
    b = defaultdict(list)
    for x, y in points:
        for bx in (-1, 0, 1):
            for by in (-1, 0, 1):
                b[(x // 128 + bx, y // 128 + by)].append((x, y))
    return b


def road_kind(cm, x, y):
    """'solid' (Road) or 'dash' (Unfinished Road) for the brown double line near (x,y).

    The unfinished road is drawn as closed dash rectangles with 2px gaps, so
    along-line occupancy does not separate the two; the dash end-caps do.
    They put road pixels on the line's centre axis, where a solid double line
    has none.  A small window keeps curvature from faking a centre-axis hit."""
    r = 10
    y0, y1 = max(0, y - r), min(cm.shape[0], y + r + 1)
    x0, x1 = max(0, x - r), min(cm.shape[1], x + r + 1)
    ys, xs = np.nonzero(cm[y0:y1, x0:x1] == CLASS["road"])
    if len(xs) < 10:
        return "solid"
    P = np.stack([xs, ys], 1).astype(float)
    c = P.mean(0)
    minor = np.linalg.eigh(np.cov((P - c).T))[1][:, 0]
    on_axis = (np.abs((P - c) @ minor) < 0.9).mean()
    return "dash" if on_axis >= 0.04 else "solid"


def rail_kind(cm, x, y):
    """'tie' (Railroad) or 'dash' (Track) for grey line pixels near (x,y).

    The rail itself is a 1px hairline that anti-aliases out of the palette;
    only the cross-ties classify.  Ties (3x12px every 14px) put ~150-300
    rail-class pixels in a 49px window; a thin dashed track puts 25-40, and a
    junction of two tracks or a stray hex line at most ~70."""
    r = 24
    y0, y1 = max(0, y - r), min(cm.shape[0], y + r + 1)
    x0, x1 = max(0, x - r), min(cm.shape[1], x + r + 1)
    n = int((cm[y0:y1, x0:x1] == CLASS["rail"]).sum())
    return "tie" if n >= 90 else "dash"


# ------------------------------------------------------------- classifying
def classify_hex(cm, cx, cy, inr, blocks):
    centre = sample(cm, cx, cy, 16)
    wide = sample(cm, cx, cy, 30)
    fill = {k: centre.get(k, 0) for k in FILLS}
    terrain = max(fill, key=fill.get) if any(fill.values()) else "unknown"
    if terrain == "sea":
        land = {k: wide.get(k, 0) for k in FILLS if k != "sea"}
        if sum(land.values()) >= 0.3 * sum(wide.get(k, 0) for k in FILLS):
            terrain = max(land, key=land.get)      # coastal hex: land terrain, cov_sea records the water
    r = inr * 0.8
    if sum((dx_ - cx) ** 2 + (dy_ - cy) ** 2 <= r * r for dx_, dy_ in blocks.get((cx // 128, cy // 128), [])) >= 20:
        terrain = "major_city"
    elif wide.get("swamp", 0) >= 30:
        terrain = "swamp"
    elif wide.get("gravel", 0) >= 40 and terrain == "clear":
        terrain = "gravel"
    tot = sum(fill.values()) or 1
    cover = {k: round(v / tot, 2) for k, v in fill.items()}
    return terrain, cover


def classify_side(cm, cx, cy, inr, deg, terrain, nb_terrain, coastal):
    """Features on one hexside, seen from the hex at (cx,cy).  Returns list of
    (feature, band_side) where band_side is 'this'/'other'/'both'/''."""
    a = math.radians(deg)
    nx_, ny_ = math.cos(a), math.sin(a)        # outward normal
    tx, ty = -ny_, nx_                         # along the edge
    mx, my = cx + inr * nx_, cy + inr * ny_
    edge = inr / math.sqrt(3)                  # half hexside length
    on, inside, outside = (sample(cm, int(mx + t * nx_), int(my + t * ny_), 7) for t in (0, -9, 9))
    feats = []

    def side_of(k, thr):
        i, o = inside.get(k, 0) >= thr, outside.get(k, 0) >= thr
        return "both" if i and o else "this" if i else "other" if o else ""

    if max(on.get("escarpment", 0), inside.get("escarpment", 0), outside.get("escarpment", 0)) >= 25:
        feats.append(("escarpment", side_of("escarpment", 15) or "both"))
    rs = side_of("ridge_slope", RIDGE_THR)
    if rs == "both":
        feats.append(("ridge", "both"))
    elif rs:
        feats.append(("slope", rs))
    if max(on.get("wadi", 0), inside.get("wadi", 0), outside.get("wadi", 0)) >= 25:
        feats.append(("wadi", ""))
    if terrain != "sea" and nb_terrain not in ("sea", None) and not coastal:
        water = on.get("sea", 0) + on.get("river_edge", 0)
        if water >= 40:
            feats.append(("major_river" if water >= 120 else "minor_river", ""))
    if terrain != "sea" and nb_terrain not in ("sea", None) and coastal:
        water = on.get("sea", 0) + on.get("river_edge", 0)
        if water >= 0.5 * sum(on.values() or [1]):
            feats.append(("coast", ""))      # an all-sea hexside between two land hexes (inlet, bay)

    # crossings: strip on each side of the hexside, must be present on both
    strip_in, strip_out, first = Counter(), Counter(), {}
    for u in (-0.7, -0.35, 0, 0.35, 0.7):
        ex, ey = mx + u * edge * tx, my + u * edge * ty
        pi = (int(ex - 9 * nx_), int(ey - 9 * ny_)); po = (int(ex + 9 * nx_), int(ey + 9 * ny_))
        si, so = sample(cm, *pi, 6), sample(cm, *po, 6)
        strip_in.update(si); strip_out.update(so)
        for k in ("road", "rail"):
            if k not in first and si.get(k, 0):
                first[k] = pi
    # rail/track lines are thin and dashed: a 6px disc every 9px at one offset often lands in a
    # gap on one side.  Sample a denser band (9 positions x 2 offsets) for the rail class only.
    band_in, band_out = 0, 0
    for u in (-0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8):
        ex, ey = mx + u * edge * tx, my + u * edge * ty
        for off in RAIL_OFFS:
            pi = (int(ex - off * nx_), int(ey - off * ny_)); po = (int(ex + off * nx_), int(ey + off * ny_))
            si, so = sample(cm, *pi, 4), sample(cm, *po, 4)
            band_in += si.get("rail", 0); band_out += so.get("rail", 0)
            if "rail" not in first and si.get("rail", 0):
                first["rail"] = pi
    strip_in["rail"], strip_out["rail"] = band_in, band_out
    # (the blue-white chain in the city-hatch blue is the frontier wire, not terrain: not read)
    for k, thr in (("road", 12), ("rail", RAIL_THR)):
        if strip_in[k] >= thr and strip_out[k] >= thr:
            # locate a pixel of the line near the strip point, then look at its component
            px_, py_ = first[k]
            dy, dx = DISCS[6]
            hit = next(((px_ + ox, py_ + oy) for oy, ox in zip(dy, dx) if cm[py_ + oy, px_ + ox] == CLASS[k]), None)
            if k == "road":
                feats.append(("unfinished_road" if road_kind(cm, *(hit or first[k])) == "dash" else "road", ""))
            else:
                feats.append(("track" if rail_kind(cm, *(hit or first[k])) == "dash" else "railroad", ""))
    return feats


# ------------------------------------------------------------- raw output
TERRAIN_ENUM = {"clear": "clear", "gravel": "gravel", "salt_marsh": "salt-marsh", "heavy_veg": "heavy-vegetation",
                "rough": "rough", "mountain": "mountain", "delta": "delta", "desert": "desert",
                "major_city": "major-city", "swamp": "swamp", "sea": "sea", "unknown": "clear"}
FEATURE_ENUM = {"escarpment": "escarpment", "ridge": "ridge", "slope": "slope", "wadi": "wadi",
                "major_river": "major-river", "minor_river": "minor-river", "road": "road",
                "unfinished_road": "unfinished-road", "railroad": "railroad", "unfinished_railroad": "unfinished-railroad",
                "track": "track", "coast": "coast"}
FEATURE_ORDER = ["escarpment", "ridge", "slope", "wadi", "major-river", "minor-river", "road", "unfinished-road",
                 "railroad", "unfinished-railroad", "track", "coast", "lake"]


def raw_records(sheet, hexes, sides):
    """The committed raw/<sheet>.json document: game-fact fields only."""
    import map_geom
    out_h = []
    for h in hexes:
        settlement = "major-city" if h["terrain"] == "major_city" else ("village" if h.get("village") else None)
        out_h.append({"id": h["hex"], "sheet": sheet, "terrain": TERRAIN_ENUM[h["terrain"]],
                      "settlement": settlement,
                      "coastal": h["terrain"] != "sea" and (bool(h.get("sea_neighbour")) or float(h.get("cov_sea", 0)) > 0.3)})
    by_id = {h["id"]: h for h in out_h}
    merged = {}
    for r in sides:
        key = map_geom.hexside_key(r["hex_a"], r["hex_b"] or None, r["side"] if not r["hex_b"] else None)
        rec = merged.setdefault(key, {"key": key, "a": min(r["hex_a"], r["hex_b"]) if r["hex_b"] else r["hex_a"],
                                      "b": max(r["hex_a"], r["hex_b"]) if r["hex_b"] else None,
                                      "side": None if r["hex_b"] else r["side"], "features": [], "up": None})
        feat = FEATURE_ENUM[r["feature"]]
        if feat not in rec["features"]:
            rec["features"].append(feat)
        if feat == "coast":
            for hid in (r["hex_a"], r["hex_b"]):      # a water hexside makes both land hexes coastal
                if hid in by_id:
                    by_id[hid]["coastal"] = True
        if feat in ("slope", "escarpment") and r["band_hex"] not in ("", "both"):
            # the band is drawn on the DOWN side (Task 5 verifies this convention); up = the other hex
            rec["up"] = r["hex_b"] if r["band_hex"] == r["hex_a"] else r["hex_a"]
            if not rec["up"]:
                rec["up"] = None
    for rec in merged.values():
        rec["features"].sort(key=FEATURE_ORDER.index)
    return {"sources": [MODULE_REF], "sheet": sheet,
            "hexes": sorted(out_h, key=lambda h: h["id"]),
            "hexsides": sorted(merged.values(), key=lambda s: s["key"])}


# ------------------------------------------------------------------ check
# Village/Bir/major-city hexes from the printed Summary of Important Locations
# (Map A, scan p0187) and scenario-book set-up references.
KNOWN = {
    "E3815": "Aboukir", "A2629": "Agadabia", "E3613": "Alexandria", "E3714": "Alexandria",
    "C4321": "Bardia", "A4827": "Benghazi", "A4829": "Benina", "C3419": "Bir Scheferzen",
    "E1730": "Cairo", "B5925": "Derna", "A1816": "el Agheila", "C1715": "el Grein",
    "C3019": "Fort Maddalena", "C1014": "Giarabub", "E1430": "Helwan", "B0513": "Jalo",
    "A2109": "Marble Arch", "B4921": "Mechili", "A2021": "Mersa Brega", "D3714": "Mersa Matruh",
    "A2703": "Nofilia", "A2010": "Ras el Ali", "E4019": "Rosetta", "C4131": "Sidi Barrani",
    "C3618": "Sidi Omar", "C0127": "Siwa", "C4021": "Sollum", "A4130": "Soluch", "C4807": "Tobruk",
    "E2132": "Abbassia", "E2133": "Almaza", "E2212": "Amiriya", "B0707": "Augila", "B5504": "Barce",
    "C4108": "Bir el Gubi", "B5331": "Bomba", "C3926": "Buq Buq", "E3109": "Burg el Arab",
    "C4020": "Fort Capuzzo", "E3512": "Dekheila", "C4507": "El Adem", "A4728": "El Berea",
    "E3007": "El Hamman", "D3323": "Fuka", "C4414": "Gambut", "B4933": "Gazala", "B5410": "Maraua",
    "B5526": "Martuba", "D3520": "Matten Baggush", "C4419": "Bir el Menastir", "D3227": "Qotifiya",
    "D3418": "Sidi Haneish", "B5229": "Tmimi", "B5917": "Ztert",
}


# -------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vmod", help="the .vmod to extract from when the cache is incomplete")
    ap.add_argument("--cache-only", action="store_true", help="fail unless buildFile.xml and the PNG are already cached")
    ap.add_argument("--zone", action="append", help="restrict to zone name(s), e.g. 'Map C'")
    ap.add_argument("--out", default="build/map")
    ap.add_argument("--write-raw", metavar="DIR", help="write <DIR>/<sheet>.json (game facts only)")
    ap.add_argument("--debug", nargs=4, type=int, metavar=("X0", "Y0", "W", "H"))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if args.cache_only and not ((CACHE / BUILDFILE).exists() and (CACHE / MAP_IMAGE).exists()):
        sys.exit(f"--cache-only: {BUILDFILE} or the PNG is missing from {CACHE}")
    img_path, zones = load_zones(CACHE, args.vmod)
    if args.zone:
        zones = [z for z in zones if z["name"] in args.zone]
    sheets = json.loads((ROOT / "data" / "map" / "sheets.json").read_text())["sheets"]
    import map_geom
    cm = class_map(img_path)
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)

    dots = solid_centres(cm, ("dot_blue", "dot_dark"), 9)             # village dots
    blocks = bucket(solid_centres(cm, ("city",), 5, 0.68))           # city hatch blocks (coast stroke peaks ~0.5)

    # pass 1: hexes
    hexes, by_centre = [], {}
    inr = zones[0]["grid"]["dy"] / 2
    for z in zones:
        letter = sheet_letter(z["name"])
        shift = observed_shift(z)
        if shift != sheets[letter]["odd_rows_shift"]:
            sys.exit(f"{z['name']}: odd rows shift {shift} in the module but sheets.json says "
                     f"{sheets[letter]['odd_rows_shift']}; fix data/map/sheets.json")
        n, clipped, rows, cols = 0, 0, [], []
        for (nx, ny), (cx, cy) in enumerate_hexes(z):
            ident = hex_id(z, nx, ny)
            rows.append(ident[1]); cols.append(ident[2])
            if not in_bounds(ident, sheets[letter]):
                clipped += 1
                continue
            terrain, cover = classify_hex(cm, cx, cy, inr, blocks)
            hexes.append({"hex": map_geom.format_hex_id(*ident), "sheet": letter, "x": cx, "y": cy,
                          "terrain": terrain, "village": 0,
                          **{f"cov_{k}": cover.get(k, 0) for k in FILLS}})
            by_centre[(cx, cy)] = hexes[-1]
            n += 1
        print(f"{z['name']} ({letter}): odd rows shift {shift}; observed rows {min(rows)}-{max(rows)}, "
              f"cols {min(cols)}-{max(cols)}; {n} hexes kept, {clipped} outside sheets.json bounds")
    centres = np.array(list(by_centre))

    # a village dot belongs to the hex whose centre is nearest (dots often sit
    # by the eastern hexside, with the label beyond it)
    for x, y in dots:
        d = ((centres - (x, y)) ** 2).sum(1); i = d.argmin()
        h = by_centre[tuple(centres[i])]
        if d[i] < inr ** 2 * 1.2 and h["terrain"] != "major_city":
            h["village"] = 1
            if h["terrain"] == "sea":
                # a village on a water-centred hex: it is a coastal land hex
                land = {k: sample(cm, h["x"], h["y"], 30).get(k, 0) for k in FILLS if k != "sea"}
                h["terrain"] = max(land, key=land.get) if any(land.values()) else "clear"

    def neighbour(cx, cy, deg):
        a = math.radians(deg)
        p = np.array([cx + 2 * inr * math.cos(a), cy + 2 * inr * math.sin(a)])
        d = ((centres - p) ** 2).sum(1)
        i = d.argmin()
        return by_centre[tuple(centres[i])] if d[i] < 20 ** 2 else None

    # pass 2: hexsides, one record per hexside pair
    sides, seen = [], set()
    for h in hexes:
        h["sea_neighbour"] = int(any((nb := neighbour(h["x"], h["y"], deg)) is not None and nb["terrain"] == "sea"
                                     for _, deg in SIDES))
        for sname, deg in SIDES:
            nb = neighbour(h["x"], h["y"], deg)
            key = frozenset([h["hex"], nb["hex"]]) if nb else (h["hex"], sname)
            if key in seen:
                continue
            seen.add(key)
            coastal = h["cov_sea"] > 0.3 or (nb is not None and nb["cov_sea"] > 0.3)   # inlets are not rivers
            for feat, band in classify_side(cm, h["x"], h["y"], inr, deg, h["terrain"], nb["terrain"] if nb else None, coastal):
                band_hex = {"this": h["hex"], "other": nb["hex"] if nb else "", "both": "both", "": ""}[band]
                sides.append({"hex_a": h["hex"], "side": sname, "hex_b": nb["hex"] if nb else "",
                              "feature": feat, "band_hex": band_hex})

    # per-sheet debug CSVs (pixel centres and coverage stay here, never in data/)
    for z in zones:
        letter = sheet_letter(z["name"])
        hs = [h for h in hexes if h["sheet"] == letter]
        ss = [r for r in sides if r["hex_a"][0] == letter]
        with open(out / f"debug-{letter}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(hexes[0].keys())); w.writeheader(); w.writerows(hs)
        with open(out / f"debug-{letter}-hexsides.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["hex_a", "side", "hex_b", "feature", "band_hex"]); w.writeheader(); w.writerows(ss)
        if args.write_raw:
            raw_dir = pathlib.Path(args.write_raw); raw_dir.mkdir(parents=True, exist_ok=True)
            doc = raw_records(letter, hs, ss)
            (raw_dir / f"{letter}.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
            print(f"wrote {raw_dir / f'{letter}.json'}: {len(doc['hexes'])} hexes, {len(doc['hexsides'])} hexsides")
    print(f"terrain: {Counter(h['terrain'] for h in hexes).most_common()}")
    print(f"villages: {sum(h['village'] for h in hexes)}")
    print(f"hexside features: {Counter(r['feature'] for r in sides).most_common()}")

    if args.check:
        byid = {h["hex"]: h for h in hexes}
        hit = miss = 0
        for hid, place in sorted(KNOWN.items()):
            h = byid.get(hid)
            if h is None:
                continue
            ok = h["village"] or h["terrain"] == "major_city"
            hit += ok; miss += not ok
            if not ok:
                print(f"  MISS {hid} {place}: terrain={h['terrain']}")
        print(f"check: {hit}/{hit + miss} known places have a village/city mark")

    if args.debug:
        x0, y0, w, hgt = args.debug
        crop = Image.open(img_path).convert("RGB").crop((x0, y0, x0 + w, y0 + hgt)).convert("RGBA")
        d = ImageDraw.Draw(crop)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 11)
        except OSError:
            font = ImageFont.load_default()
        colour = {"sea": (0, 0, 255), "clear": (0, 0, 0), "rough": (160, 80, 0), "salt_marsh": (200, 0, 200),
                  "desert": (220, 160, 0), "delta": (0, 140, 0), "mountain": (100, 80, 0), "heavy_veg": (0, 200, 0),
                  "swamp": (0, 160, 120), "gravel": (120, 120, 120), "major_city": (255, 0, 0), "unknown": (255, 0, 0)}
        for hx in hexes:
            cx, cy = hx["x"] - x0, hx["y"] - y0
            if not (0 <= cx < w and 0 <= cy < hgt):
                continue
            d.text((cx - 14, cy - 6), hx["hex"][-4:], fill=colour[hx["terrain"]] + (255,), font=font)
            if hx["village"]:
                d.rectangle((cx - 4, cy + 8, cx + 4, cy + 16), fill=(0, 100, 255, 255))
        byid = {h["hex"]: h for h in hexes}
        fc = {"escarpment": (255, 0, 0), "ridge": (255, 140, 0), "slope": (255, 200, 0), "wadi": (0, 200, 200),
              "road": (120, 60, 0), "unfinished_road": (200, 120, 60), "railroad": (0, 0, 0), "track": (120, 120, 120),
              "major_river": (0, 0, 255), "minor_river": (100, 100, 255), "coast": (0, 120, 255),
              "unfinished_railroad": (60, 60, 160)}
        for r in sides:
            hx = byid[r["hex_a"]]; a = math.radians(dict(SIDES)[r["side"]])
            mx, my = hx["x"] - x0 + inr * 0.8 * math.cos(a), hx["y"] - y0 + inr * 0.8 * math.sin(a)
            d.ellipse((mx - 4, my - 4, mx + 4, my + 4), fill=fc[r["feature"]] + (255,))
            if r["band_hex"] and r["band_hex"] != "both":
                # tick towards the hex the band is drawn in
                sign = 1 if r["band_hex"] == r["hex_a"] else -1
                d.line((mx, my, mx - sign * 10 * math.cos(a), my - sign * 10 * math.sin(a)),
                       fill=fc[r["feature"]] + (255,), width=3)
        crop.save(out / "debug.png")
        print(f"wrote {out / 'debug.png'}")


if __name__ == "__main__":
    main()
