"""Abstract Truck / Motorisation Point Loss Chart (SPI 32.59; headed 58.5 on the sheet): monthly
percentage of Commonwealth and Axis motorisation points lost."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_months_and_values():
    t = json.loads((ROOT / "data" / "tables" / "motorisation-losses.json").read_text())
    by = {r["month"]: r for r in t["rows"]}
    assert len(by) == len(t["rows"]) == 28
    assert min(by) == "1940-10" and max(by) == "1943-01"
    assert by["1940-10"]["cw_percent"] == 6 and by["1940-10"]["axis_percent"] == 2
    assert by["1941-03"] == {"month": "1941-03", "cw_percent": 10, "axis_percent": 1, "sources": ["CNA1979:32.59", "scan:p107"]}
    assert by["1941-06"]["cw_percent"] == 5 and by["1941-06"]["axis_percent"] == 4
    assert by["1941-11"]["axis_percent"] == 5 and by["1942-11"]["axis_percent"] == 6 and by["1942-11"]["cw_percent"] == 4
    assert by["1943-01"]["cw_percent"] == 2 and by["1943-01"]["axis_percent"] == 4
    assert all(1 <= r["cw_percent"] <= 10 and 1 <= r["axis_percent"] <= 6 for r in t["rows"])
