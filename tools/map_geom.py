"""Hex ID grammar, per-sheet adjacency and pointy-top pixel geometry for data/map/.

Convention (data/README.md, data/map/sheets.json): rows increase northward,
columns eastward; each sheet says whether odd rows sit half a hex west or
east of even rows.  A row shifted west of its neighbours has diagonal
neighbours at columns (c-1, c); a row shifted east has (c, c+1).
"""
import math
import re

SHEET_LETTERS = "ABCDEM"
SIDES = ("E", "SE", "SW", "W", "NW", "NE")
_ID = re.compile(r"^([A-Z])(\d{2})(\d{2})$")
SQRT3 = math.sqrt(3)


def parse_hex_id(hid, letters=SHEET_LETTERS):
    """"C4023" -> ("C", 40, 23).  `letters` is the set of sheets that exist; the
    adjacency functions pass the keys of the sheets dict they were given."""
    m = _ID.match(hid)
    if not m or m.group(1) not in letters:
        raise ValueError(f"bad hex id {hid!r}")
    return m.group(1), int(m.group(2)), int(m.group(3))


def format_hex_id(sheet, row, col, letters=SHEET_LETTERS):
    if sheet not in letters or not (0 <= row < 100 and 0 <= col < 100):
        raise ValueError(f"bad hex ({sheet}, {row}, {col})")
    return f"{sheet}{row:02d}{col:02d}"


def row_shifted_east(row, sheet):
    """True when this row sits half a hex east of the rows above and below it."""
    odd_east = sheet["odd_rows_shift"] == "east"
    return (row % 2 == 1) == odd_east


def neighbours(hid, sheets):
    s, r, c = parse_hex_id(hid, sheets)
    lo, hi = (c, c + 1) if row_shifted_east(r, sheets[s]) else (c - 1, c)
    return {format_hex_id(s, r, c - 1, sheets), format_hex_id(s, r, c + 1, sheets),
            format_hex_id(s, r - 1, lo, sheets), format_hex_id(s, r - 1, hi, sheets),
            format_hex_id(s, r + 1, lo, sheets), format_hex_id(s, r + 1, hi, sheets)}


def is_adjacent(a, b, sheets):
    return a[0] == b[0] and b in neighbours(a, sheets)


def hexside_key(a, b, side=None):
    if b is None:
        if side not in SIDES:
            raise ValueError("edge hexside needs a side")
        return f"{a}|{side}"
    return "|".join(sorted((a, b)))


def centre(hid, sheets, size=20.0):
    """Pixel centre; the sheet's row/col minima sit at the top-left margin."""
    s, r, c = parse_hex_id(hid, sheets)
    sh = sheets[s]
    w, pitch = SQRT3 * size, 1.5 * size
    x = (c - sh["cols"][0]) * w + (w / 2 if row_shifted_east(r, sh) else 0) + w
    y = (sh["rows"][1] - r) * pitch + size * 2
    return x, y


def corners(cx, cy, size=20.0):
    return [(cx + size * math.cos(math.radians(60 * i - 30)), cy + size * math.sin(math.radians(60 * i - 30)))
            for i in range(6)]
