#!/usr/bin/env python3
"""Spike: derive hex and hexside terrain from the CNA VASSAL module (v2.1.0).

The module's buildFile.xml gives exact hex geometry per map sheet (a sideways
HexGrid inside each Zone plus a HexGridNumbering), so every hex ID the module
displays (e.g. C4807) maps deterministically to a pixel centre on Mitch
Guthrie's 2021 redraw.  The redraw is flat-colour vector art, so terrain is
read by sampling colours at hex centres and hexside midpoints.

Nothing from the module is committed: the map PNG is cached under
~/.cache/cna-vassal/ and only the derived CSVs go to --out.

Usage:
  python3 tools/map_extract.py ~/Downloads/CNAv2.1.0.vmod [--zone "Map C"] [--out build/map]
    --debug X0 Y0 W H   also write an overlay crop with hex IDs and classes
"""
import argparse, csv, math, os, pathlib, re, zipfile
from collections import Counter

from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
CACHE = pathlib.Path(os.path.expanduser("~/.cache/cna-vassal"))
BOARD = "CNA Original"
MAP_IMAGE = "CNA Map Vassal Mitch Guthrie 2021.png"

# Flat colours in the redraw, from a histogram of the full image and of sample
# crops.  Names on the right are *palette* classes; mapping them to the terrain
# types of the Terrain Effects Chart [8.37] is a separate, legend-driven step.
PALETTE = {
    "clear":        (251, 250, 239),
    "sea":          (138, 181, 207),
    "rough":        (194, 185, 149),   # plain tan
    "rough_lined":  (186, 175, 129),   # tan with yellow crack pattern
    "sand":         (223, 207, 100),   # yellow dune fields
    "cultivated":   (164, 178, 171),   # Nile delta grey-green
    "olive_fill":   (151, 136,  66),   # dark olive area fill (south of Maradah, Qattara?)
    "green":        (203, 216,  91),   # green blobs, Jebel Akhdar
    "band_olive":   (160, 146,  80),   # olive hexside band
    "band_dark":    ( 94,  97,  98),   # dark grey hexside band (escarpment)
    "wadi":         (127, 148, 142),   # teal hexside line
    "road":         ( 72,  63,  34),   # brown double line
    "rail":         ( 84,  88,  89),   # dark grey with cross-ties
    "hexline":      ( 51,  53,  51),
    "town":         ( 74, 138, 179),   # town dot / label blue
    "city":         ( 91, 149, 185),   # hatched urban blocks
    "river":        (121, 168, 195),
    "white":        (233, 232, 223),
}
HEX_CLASSES = ("sea", "clear", "rough", "rough_lined", "sand", "cultivated", "olive_fill", "green")
SIDE_CLASSES = ("band_dark", "band_olive", "wadi", "road", "rail", "river")
# A solid olive hexside band fills most of a 7px-radius disc; the speckled
# olive fringe around rough patches (same colour) does not, hence its higher
# minimum in SIDE_MIN.


# --------------------------------------------------------------- buildFile
def parse_module(vmod):
    """Return (image_path, zones).  zones: list of dicts with polygon, grid, numbering."""
    with zipfile.ZipFile(vmod) as z:
        xml = z.read("buildFile.xml").decode("utf-8")
        CACHE.mkdir(parents=True, exist_ok=True)
        img = CACHE / MAP_IMAGE
        if not img.exists():
            img.write_bytes(z.read(f"images/{MAP_IMAGE}"))
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
    return img, zones


# ---------------------------------------------------------------- geometry
# Port of VASSAL HexGrid / HexGridNumbering for the sideways case.  VASSAL
# swaps x and y for a sideways grid, then treats it as a flat-top grid whose
# "columns" step by dx and "rows" by dy; so on the real map columns run down
# the page and rows across it.

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
    if g["sideways"]:
        if num["vDescend"]: col = max_rows - col
        if num["hDescend"]: row = max_cols - row
        if num["stagger"] and nx % 2 != 0:
            row += -1 if num["hDescend"] else 1
    else:
        raise NotImplementedError("non-sideways grids not needed for CNA")
    c, r = fmt(col + num["hOff"], num["hLeading"]), fmt(row + num["vOff"], num["vLeading"])
    grid_loc = c + num["sep"] + r if num["first"] == "H" else r + num["sep"] + c
    return zone["fmt"].replace("$name$", zone["name"]).replace("$gridLocation$", grid_loc)


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
                yield hex_name(zone, nx, ny), (cx, cy)


# ------------------------------------------------------------- classifying
def nearest(rgb, classes=None):
    best, bd = None, 1e9
    for name, c in PALETTE.items():
        if classes and name not in classes:
            continue
        d = sum((a - b) ** 2 for a, b in zip(rgb, c))
        if d < bd:
            best, bd = name, d
    return best if bd < 30 ** 2 else None


def sample(px, cx, cy, r, classes=None):
    """Colour-class histogram of a disc; pixels not matching any class are dropped."""
    h = Counter()
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx * dx + dy * dy > r * r:
                continue
            try:
                k = nearest(px[cx + dx, cy + dy][:3], classes)
            except IndexError:
                continue
            if k:
                h[k] += 1
    return h


# Pointy-top hex (sideways grid): edge midpoints at 0,60,..300 degrees,
# inradius = dy/2.  Directions named by compass for the CSV.
SIDES = [("E", 0), ("SE", 60), ("SW", 120), ("W", 180), ("NW", 240), ("NE", 300)]


BANDS = ("band_dark", "band_olive", "wadi")        # lie along a hexside
CROSSINGS = ("road", "rail", "river")               # cross a hexside between two hexes
SIDE_MIN = {"band_dark": 25, "band_olive": 110, "wadi": 25, "road": 12, "rail": 12, "river": 15}


def has_town_dot(px, cx, cy, r):
    """A town is a solid blue disc ~12px across; coastline strokes, labels and
    the dotted frontier are the same blue but never fill a 9px disc."""
    for y in range(cy - r, cy + r + 1, 3):
        for x in range(cx - r, cx + r + 1, 3):
            if (x - cx) ** 2 + (y - cy) ** 2 > r * r:
                continue
            try:
                if nearest(px[x, y][:3]) != "town":
                    continue
            except IndexError:
                continue
            if sample(px, x, y, 4).get("town", 0) >= 42:   # 49px disc, ~12px dot
                return True
    return False


def classify_hex(px, cx, cy, g):
    inr = g["dy"] / 2
    centre = sample(px, cx, cy, 16, HEX_CLASSES)
    terrain = centre.most_common(1)[0][0] if centre else "unknown"
    town = terrain != "sea" and has_town_dot(px, cx, cy, int(inr * 0.75))
    # coverage of each class over a wider disc, for mixed hexes
    wide = sample(px, cx, cy, int(inr * 0.8), HEX_CLASSES)
    tot = sum(wide.values()) or 1
    cover = {k: round(v / tot, 2) for k, v in wide.items()}
    sides = {}
    edge = inr / math.sqrt(3)            # half the hexside length
    for name, deg in SIDES:
        a = math.radians(deg)
        nx_, ny_ = math.cos(a), math.sin(a)          # outward normal
        tx, ty = -ny_, nx_                           # along the edge
        mx, my = cx + inr * nx_, cy + inr * ny_
        # Bands lie along the hexside: three discs at the midpoint (on the
        # line, 9px inside, 9px outside).  Crossings (roads etc.) cut the
        # hexside anywhere along its length, so those are looked for in a
        # strip on each side of the line and must appear on both sides.  All
        # palette classes compete so anti-aliased hex lines land on "hexline".
        on, inside, outside = (sample(px, int(mx + t * nx_), int(my + t * ny_), 7) for t in (0, -9, 9))
        strip_in, strip_out = Counter(), Counter()
        for u in (-0.7, -0.35, 0, 0.35, 0.7):
            ex, ey = mx + u * edge * tx, my + u * edge * ty
            strip_in += sample(px, int(ex - 9 * nx_), int(ey - 9 * ny_), 6)
            strip_out += sample(px, int(ex + 9 * nx_), int(ey + 9 * ny_), 6)
        feats = []
        for k in BANDS:
            if max(on[k], inside[k], outside[k]) >= SIDE_MIN[k]:
                feats.append(k)
        for k in CROSSINGS:
            if strip_in[k] >= SIDE_MIN[k] and strip_out[k] >= SIDE_MIN[k]:
                feats.append(k)
        if terrain == "sea" or strip_in["sea"] + strip_out["sea"] > 15:
            feats = [k for k in feats if k != "river"]   # coastline stroke / hexline over sea
        if feats:
            sides[name] = "+".join(feats)
    return terrain, town, cover, sides


# -------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("vmod")
    ap.add_argument("--zone", action="append", help="restrict to zone name(s), e.g. 'Map C'")
    ap.add_argument("--out", default="build/map")
    ap.add_argument("--debug", nargs=4, type=int, metavar=("X0", "Y0", "W", "H"))
    args = ap.parse_args()

    img_path, zones = parse_module(args.vmod)
    if args.zone:
        zones = [z for z in zones if z["name"] in args.zone]
    im = Image.open(img_path).convert("RGB")
    px = im.load()
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)

    hexes, sides_rows = [], []
    for z in zones:
        n = 0
        for name, (cx, cy) in enumerate_hexes(z):
            terrain, town, cover, sides = classify_hex(px, cx, cy, z["grid"])
            hid = name.replace("Map ", "")
            hexes.append({"hex": hid, "zone": z["name"], "x": cx, "y": cy, "terrain": terrain, "town": int(town),
                          **{f"cov_{k}": cover.get(k, 0) for k in HEX_CLASSES}})
            for side, feat in sides.items():
                sides_rows.append({"hex": hid, "side": side, "feature": feat})
            n += 1
        print(f"{z['name']}: {n} hexes")

    with open(out / "hexes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(hexes[0].keys())); w.writeheader(); w.writerows(hexes)
    with open(out / "hexsides.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["hex", "side", "feature"]); w.writeheader(); w.writerows(sides_rows)
    print(f"terrain: {Counter(h['terrain'] for h in hexes).most_common()}")
    print(f"towns: {sum(h['town'] for h in hexes)}")
    print(f"hexside features: {Counter(r['feature'] for r in sides_rows).most_common()}")

    if args.debug:
        x0, y0, w, h = args.debug
        crop = im.crop((x0, y0, x0 + w, y0 + h)).convert("RGBA")
        d = ImageDraw.Draw(crop)
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 11)
        except OSError:
            font = ImageFont.load_default()
        colour = {"sea": (0, 0, 255), "clear": (0, 0, 0), "rough": (160, 80, 0), "rough_lined": (200, 0, 200),
                  "sand": (220, 160, 0), "cultivated": (0, 140, 0), "olive_fill": (100, 80, 0),
                  "green": (0, 200, 0), "unknown": (255, 0, 0)}
        for hx in hexes:
            cx, cy = hx["x"] - x0, hx["y"] - y0
            if not (0 <= cx < w and 0 <= cy < h):
                continue
            d.text((cx - 14, cy - 6), hx["hex"][-4:], fill=colour[hx["terrain"]] + (255,), font=font)
            if hx["town"]:
                d.rectangle((cx - 4, cy + 8, cx + 4, cy + 16), fill=(0, 100, 255, 255))
        inr = zones[0]["grid"]["dy"] / 2
        for r in sides_rows:
            hx = next(x for x in hexes if x["hex"] == r["hex"])
            deg = dict(SIDES)[r["side"]]; a = math.radians(deg)
            mx, my = hx["x"] - x0 + inr * 0.8 * math.cos(a), hx["y"] - y0 + inr * 0.8 * math.sin(a)
            c = {"band_dark": (255, 0, 0), "band_olive": (255, 140, 0), "wadi": (0, 200, 200),
                 "road": (120, 60, 0), "rail": (0, 0, 0), "river": (0, 0, 255)}.get(r["feature"].split("+")[0], (255, 0, 255))
            d.ellipse((mx - 4, my - 4, mx + 4, my + 4), fill=c + (255,))
        crop.save(out / "debug.png")
        print(f"wrote {out / 'debug.png'}")


if __name__ == "__main__":
    main()
