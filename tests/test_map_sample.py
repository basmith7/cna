import map_geom
import map_sample as ms

SHEETS = {"C": {"zone": "Map C", "odd_rows_shift": "west", "rows": [1, 51], "cols": [1, 33]}}
GRID = {"ref_hex": "C4023", "x": 2136, "y": 1910, "col_w": 94.0, "row_h": 81.0}


def test_sample_is_fifty_distinct_valid_ids_and_stable():
    a, b = ms.sample("C"), ms.sample("C")
    assert a == b and len(a) == 50 == len(set(a))
    assert all(map_geom.parse_hex_id(i)[0] == "C" for i in a)


def test_scan_centre_follows_the_printed_grid():
    assert ms.scan_centre("C4023", GRID, SHEETS) == (2136, 1910)
    assert ms.scan_centre("C4024", GRID, SHEETS) == (2230, 1910)      # one column east
    assert ms.scan_centre("C4123", GRID, SHEETS) == (2089, 1829)      # odd row: half a hex west, one row north
    assert ms.scan_centre("C3923", GRID, SHEETS) == (2089, 1991)      # odd row: half a hex west, one row south
