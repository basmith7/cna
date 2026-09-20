"""The close assault CRT (SPI 15.79) as data. For each side and differential column the loss-row
dice ranges must tile the 36 sequential readings 11–66 once — after the E-008 overlay is applied and
except for the printed gap the table declares. Capture / engaged / retreat rows are dice-sum sets 2–12."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DICE = [10 * a + b for a in range(1, 7) for b in range(1, 7)]
LOSS_ROWS = ["50", "40", "30", "25", "20", "15", "10", "5", "0"]


def _table():
    return json.loads((ROOT / "data" / "tables" / "close-assault-results.json").read_text())


def _patched():
    t = _table()
    patch = json.loads((ROOT / "data" / "errata" / "E-008.json").read_text())
    assert patch["table"] == "close-assault-results"
    for op in patch["patches"]:
        assert op["op"] == "replace"
        parts = op["path"].strip("/").split("/")
        node = t
        for k in parts[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        last = parts[-1]
        if isinstance(node, list):
            node[int(last)] = op["value"]
        else:
            node[last] = op["value"]
    return t


def _covered(cell):
    if cell is None:
        return []
    return [d for d in DICE if cell["from"] <= d <= cell["to"]]


def test_columns_and_loss_rows_are_complete():
    t = _table()
    cols = [c["id"] for c in t["columns"]]
    assert cols[0] == "-11" and cols[-1] == "+17" and len(cols) == 18
    for side in ("attacker", "defender"):
        assert list(t["losses"][side]) == LOSS_ROWS
        for row in LOSS_ROWS:
            assert list(t["losses"][side][row]) == cols


def test_loss_ranges_tile_the_dice_once_per_column_after_errata():
    t = _patched()
    cols = [c["id"] for c in t["columns"]]
    gaps = {(g["side"], g["column"]): set(g["readings"]) for g in t.get("known_gaps", [])}
    for side in ("attacker", "defender"):
        for col in cols:
            covered = sorted(d for row in LOSS_ROWS for d in _covered(t["losses"][side][row][col]))
            expected = sorted(set(DICE) - gaps.get((side, col), set()))
            assert covered == expected, f"{side} {col}: {covered} != {expected}"


def test_printed_anomalies_are_the_two_known_ones():
    t = _table()   # as printed, before E-008
    assert t["losses"]["defender"]["10"]["+4"] == {"from": 24, "to": 45}       # overlaps the 15 % row: E-008
    assert t["losses"]["attacker"]["20"]["-2"] == {"from": 13, "to": 18}       # 18 is not a reading; reads as 13–16
    assert t["known_gaps"] == [{"side": "defender", "column": "+2", "readings": [34, 35, 36]}]


def test_sum_rows_are_valid_dice_sums():
    t = _table()
    for name in ("capture_attacker", "capture_defender", "engaged", "retreat_1", "retreat_2", "retreat_3"):
        for col, sums in t["sums"][name].items():
            assert sums is None or (sums == sorted(set(sums)) and all(2 <= s <= 12 for s in sums)), (name, col)
