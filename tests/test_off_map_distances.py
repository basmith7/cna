"""Off-Map Land Unit Movement Distance Chart (SPI 8.89): stages of continuous movement between the
west-edge boxes, by CPA band."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_pairs_and_bands():
    t = json.loads((ROOT / "data" / "tables" / "off-map-distances.json").read_text())
    assert t["places"] == ["tunis", "gabes", "tripoli", "tripolitania", "nofilia"]
    assert t["cpa_bands"] == [{"min": 25}, {"min": 15, "max": 20}, {"max": 14}]
    by = {(r["a"], r["b"]): r["stages"] for r in t["rows"]}
    assert len(by) == len(t["rows"]) == 10
    assert all(a < b for a, b in by)  # stored sorted, one row per unordered pair
    assert by[("gabes", "tunis")] == [1, 2, 5]
    assert by[("tripoli", "tunis")] == [2, 3, 8] and by[("gabes", "tripoli")] == [1, 1, 3]
    assert by[("tripolitania", "tunis")] == [3, 4, 11] and by[("gabes", "tripolitania")] == [2, 2, 6]
    assert by[("nofilia", "tunis")] == [4, 5, 14] and by[("gabes", "nofilia")] == [3, 3, 9] and by[("nofilia", "tripoli")] == [2, 2, 6]
    assert by[("nofilia", "tripolitania")] == [1, 1, 3] and by[("tripoli", "tripolitania")] == [1, 1, 3]
    # slower units never take fewer stages
    assert all(s[0] <= s[1] <= s[2] for s in by.values())
