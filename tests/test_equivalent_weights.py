"""Equivalent Weights Chart (SPI 54.5): tons per supply point, per replacement and truck point, and stacking-point equivalents."""
import json
import pathlib
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_cells():
    t = json.loads((ROOT / "data" / "tables" / "equivalent-weights.json").read_text())
    tons = {k: Fraction(v) for k, v in t["supply_tons"].items()}
    assert tons == {"ammo": 4, "fuel": Fraction(1, 8), "stores": 1, "water": Fraction(1, 6)}
    assert t["replacement_point_tons"] == {"axis-naval-convoy": "axis-replacement-pool", "interport": None,
                                           "railroad": None, "air": "2"}
    assert t["truck_point_tons"] == {"axis-naval-convoy": "axis-replacement-pool", "railroad": None,
                                     "interport": "50", "air": "prohibited"}
    assert {k: Fraction(v) for k, v in t["rail_interport_stacking_points"].items()} == {
        "truck-point": Fraction(1, 10), "replacement-point": Fraction(1, 5),
        "sgsu": Fraction(1, 2), "unit-stacking-point": Fraction(1, 2)}
