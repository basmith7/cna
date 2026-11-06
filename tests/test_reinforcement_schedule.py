import json
import pathlib

import tables_page

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = json.loads((ROOT / "data" / "tables" / "reinforcement-schedule.json").read_text())
OA = {u["id"]: u for p in (ROOT / "data" / "oa").glob("*.json")
      for f in json.loads(p.read_text())["formations"] for u in f["units"]}


# Units whose OA sheet prints a different arrival from the schedule (both charts read twice).
PRINTED_DISAGREEMENTS = {"unit:cw:22-gds", "unit:de:5-pz-regt-hq", "unit:de:i-5-pz-bn", "unit:de:ii-5-pz-bn", "unit:de:2-mg-bn",
                         "unit:cw:102nd-anti-tank-regt", "unit:cw:22-armd-bde-hq", "unit:cw:78-fld"}


def test_schedule_agrees_with_oa_arrivals():
    mismatches = set()
    for row in TABLE["rows"]:
        if any("returns" in n for n in row.get("notes", [])) or row["kind"] != "arrives":
            continue
        for uid in row["units"]:
            if OA[uid]["arrives"] != {"game_turn": row["game_turn"], "opstage": row["opstage"]}:
                mismatches.add(uid)
    assert mismatches == PRINTED_DISAGREEMENTS


def test_rows_stop_at_the_transcribed_turn():
    assert all(r["game_turn"] <= TABLE["through"] for r in TABLE["rows"])


def _patched_rows():
    errata = [json.loads(p.read_text()) for p in sorted((ROOT / "data" / "errata").glob("E-*.json"))]
    out, _ = tables_page.apply_errata(TABLE, [e for e in errata if e["table"] == "reinforcement-schedule"])
    return out["rows"]


def _under(uid, ancestor):
    while uid is not None:
        uid = OA[uid].get("parent")
        if uid == ancestor:
            return True
    return False


def test_every_commonwealth_withdrawal_carries_its_printed_transport():
    for row in _patched_rows():
        if row["kind"] == "withdraws":
            t = row["transport"]
            assert f"Tpt: {t['truck_value']}/{t['motorisation']}" in row["notes"], row


def test_hq_only_and_less_name_units_of_the_row():
    for row in _patched_rows():
        assert set(row.get("hq_only", [])) <= set(row["units"]), row
        for uid in row.get("less", []):
            assert any(_under(uid, head) for head in row["units"]), (uid, row)


def test_returns_name_the_withdrawals_their_transport_left_on():
    rows = _patched_rows()
    for row in rows:
        for at in row.get("transport_from", []):
            assert any(w["kind"] == "withdraws" and w["game_turn"] == at["game_turn"] and w["opstage"] == at["opstage"]
                       for w in rows), row


def test_the_1979_errata_supply_the_withdrawal_the_76_2_return_refers_to():
    rows = _patched_rows()
    ret = next(r for r in rows if (r["game_turn"], r["opstage"], r["kind"]) == (76, 2, "arrives"))
    left = [r for r in rows if r["kind"] == "withdraws" and ret["units"][0] in r["units"]]
    assert [(r["game_turn"], r["opstage"]) for r in left] == [(64, 2)]
    assert ret["transport_from"] == [{"game_turn": 64, "opstage": 2}]


def test_picks_name_a_slot_kind_some_counter_fills():
    kinds = {k for u in OA.values() for k in u.get("fills", [])}
    picks = [r["pick"] for r in _patched_rows() if "pick" in r]
    assert picks and all(p["fills"] in kinds for p in picks)
