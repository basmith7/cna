"""Simplified Supply Availability Tables (SPI 32.46 Axis, 32.47 Commonwealth): one die -> supply units."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_axis_and_cw_tables():
    t = json.loads((ROOT / "data" / "tables" / "simplified-supply.json").read_text())
    ax = {r["die"]: r["units"] for r in t["axis"]["rows"]}
    assert sorted(ax) == [1, 2, 3, 4, 5, 6] and t["axis"]["letters"] == list("ABCDEFG")
    assert ax[1] == [0, 0, 1, 1, 1, 1, 2] and ax[4] == [1, 2, 2, 3, 3, 4, 4] and ax[6] == [2, 3, 3, 3, 4, 4, 6]
    assert all(ax[d][i] <= ax[d][i + 1] for d in ax for i in range(6))  # more availability never yields fewer units
    cw = {r["die"]: r["units"] for r in t["cw"]["rows"]}
    assert sorted(cw) == [1, 2, 3, 4, 5, 6]
    assert cw[1] == [1, 2, 3] and cw[3] == cw[4] == [2, 3, 5] and cw[6] == [3, 4, 7]
    assert [p["period"] for p in t["cw"]["periods"]] == ["I", "II", "III"]
    assert t["cw"]["periods"][0]["to"] == "1941-04" and t["cw"]["periods"][1]["from"] == "1941-05" and t["cw"]["periods"][2]["from"] == "1942-06"
    assert t["axis"]["arrive_turns_later"] == 2 and t["cw"]["arrive_turns_later"] == 4
