"""Every OA headquarters names its Maximum Attachment Chart row (19.5) and Formation Organisation row (19.3)."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _j(rel):
    return json.loads((ROOT / rel).read_text())


def _hqs():
    for nat in ("cw", "de", "it"):
        for f in _j(f"data/oa/{nat}.json")["formations"]:
            for u in f["units"]:
                if "echelon" in u:
                    yield nat, u


def test_every_hq_points_at_rows_that_exist():
    att = {(r["nation"], r["parent"]) for r in _j("data/tables/max-attachments.json")["rows"]}
    org = {(r["nation"], r["parent"]) for r in _j("data/tables/formation-organisation.json")["rows"]}
    n = 0
    for nat, u in _hqs():
        n += 1
        assert "attachment_parent" in u and "organisation" in u, u["id"]
        for key in u["attachment_parent"]:
            assert (nat, key) in att, (u["id"], key)
        if u["organisation"] is not None:
            assert (nat, u["organisation"]) in org, (u["id"], u["organisation"])
        if u["echelon"] != "corps":
            assert u["attachment_parent"], u["id"]
    assert n > 190


def test_split_rows_cover_every_turn_once():
    rows = _j("data/tables/max-attachments.json")["rows"]
    for nat, u in _hqs():
        if len(u["attachment_parent"]) > 1:
            spans = sorted((r["turns"]["from"], r["turns"]["to"] or 111) for r in rows
                           if r["nation"] == nat and r["parent"] in u["attachment_parent"])
            assert spans[0][0] == 1 and spans[-1][1] == 111, u["id"]
            assert all(b[0] == a[1] + 1 for a, b in zip(spans, spans[1:])), u["id"]


def test_spot_checks():
    by = {u["id"]: u for _, u in _hqs()}
    assert by["unit:cw:7th-armored-div-hq"]["attachment_parent"] == ["armour-division", "armour-division-late"]
    assert by["unit:cw:7th-armored-div-hq"]["organisation"] == "armoured-division"
    assert by["unit:cw:7-mtr-hq"]["organisation"] == "support-group"  # the Motor Brigade Group (19.31)
    assert by["unit:cw:polish-hq"]["organisation"] == "infantry-brigade-3sp"
    assert by["unit:de:15-schutzen-bde-hq"]["organisation"] == "15-infantry-brigade"
    assert by["unit:de:kg-marcks"]["attachment_parent"] == ["battle-group"] and by["unit:de:kg-marcks"]["organisation"] is None
    assert by["unit:de:dak-hq"]["attachment_parent"] == [] and by["unit:de:dak-hq"]["organisation"] is None
    assert by["unit:it:maletti-div-hq"]["organisation"] == "libyan-or-parachute-infantry-division"  # named on 19.32
    assert by["unit:it:101st-trieste-div-hq"]["organisation"] == "motorised-infantry-division"
    assert by["unit:it:libyan-tank-command-hq"]["organisation"] == "tank-group"
