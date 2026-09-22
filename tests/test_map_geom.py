import math
import pytest
import map_geom as g

SHEETS = {"C": {"odd_rows_shift": "west", "rows": [1, 60], "cols": [1, 40]},
          "X": {"odd_rows_shift": "east", "rows": [1, 10], "cols": [1, 10]}}


def test_parse_and_format_round_trip():
    assert g.parse_hex_id("C4023") == ("C", 40, 23)
    assert g.parse_hex_id("M0304") == ("M", 3, 4)
    assert g.format_hex_id("C", 40, 23) == "C4023"
    assert g.format_hex_id("M", 3, 4) == "M0304"
    with pytest.raises(ValueError):
        g.parse_hex_id("Z4023")


def test_neighbours_even_row_odd_shift_west():
    # even row 40, odd rows to the west: diagonals are (c, c+1) in rows 39 and 41
    assert g.neighbours("C4023", SHEETS) == {"C4022", "C4024", "C3923", "C3924", "C4123", "C4124"}


def test_neighbours_odd_row_odd_shift_west():
    assert g.neighbours("C3923", SHEETS) == {"C3922", "C3924", "C3822", "C3823", "C4022", "C4023"}


def test_neighbours_odd_shift_east_flips_diagonals():
    assert g.neighbours("X0505", SHEETS) == {"X0504", "X0506", "X0405", "X0406", "X0605", "X0606"}
    assert g.neighbours("X0405", SHEETS) == {"X0404", "X0406", "X0304", "X0305", "X0504", "X0505"}


def test_adjacency_is_symmetric():
    for a in ("C4023", "C3923", "X0505", "X0405"):
        for b in g.neighbours(a, SHEETS):
            assert g.is_adjacent(a, b, SHEETS) and g.is_adjacent(b, a, SHEETS)
    assert not g.is_adjacent("C4023", "C4025", SHEETS)
    assert not g.is_adjacent("C4023", "X0505", SHEETS)


def test_hexside_key_is_sorted_or_edge():
    assert g.hexside_key("C4024", "C4023") == "C4023|C4024"
    assert g.hexside_key("C4023", None, "W") == "C4023|W"
    with pytest.raises(ValueError):
        g.hexside_key("C4023", None)


def test_centre_and_corners_share_edges_between_neighbours():
    size = 20.0
    for a in ("C4023", "C3923"):
        ca = g.corners(*g.centre(a, SHEETS, size), size)
        for b in g.neighbours(a, SHEETS):
            cb = g.corners(*g.centre(b, SHEETS, size), size)
            shared = [p for p in ca if any(math.dist(p, q) < 0.01 for q in cb)]
            assert len(shared) == 2, (a, b, shared)


def test_north_is_up_and_east_is_right():
    x40, y40 = g.centre("C4023", SHEETS)
    x41, y41 = g.centre("C4123", SHEETS)
    x24, _ = g.centre("C4024", SHEETS)
    assert y41 < y40 and x24 > x40
