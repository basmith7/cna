import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SC = ROOT / "data" / "scenarios"


def load(slug):
    return json.loads((SC / f"{slug}.json").read_text())


def _total(blocks, key):
    return sum(b.get(key, 0) * b.get("count", 1) for b in blocks)


def test_graziani_length_and_initiative():
    g = load("grazianis-offensive")
    assert (g["start"], g["end"]) == ({"game_turn": 1, "opstage": 1}, {"game_turn": 6, "opstage": 3})
    assert g["initiative"] == {"side": "axis", "through": {"game_turn": 1, "opstage": 3}}


def test_graziani_dump_totals_as_printed():
    g = load("grazianis-offensive")
    ax = [b for b in g["sides"]["axis"]["supply"] if b["kind"] == "dump"]
    cw = [b for b in g["sides"]["cw"]["supply"] if b["kind"] == "dump"]
    # 60.34 and 60.44 column sums, from the source-text transcription (an independent reading of the same tables)
    assert [_total(ax, k) for k in ("ammo", "fuel", "stores", "water")] == [2750, 11550, 3650, 400]
    assert [_total(cw, k) for k in ("ammo", "fuel", "stores")] == [1750, 4250, 4600]


def test_graziani_second_line_trucks_as_printed():
    g = load("grazianis-offensive")
    ax = g["sides"]["axis"]["trucks"]
    assert [sum(b["trucks"].get(k, 0) for b in ax) for k in ("light", "medium", "heavy")] == [65, 290, 65]
    cw = g["sides"]["cw"]["trucks"]
    assert [sum(b["trucks"].get(k, 0) for b in cw) for k in ("light", "medium", "heavy")] == [30, 130, 35]


def test_land_only_supply_units_replace_dumps():
    g = load("grazianis-offensive")
    lo = g["abstractions"]["air_and_logistics"]["replaces"]
    real = lambda side: sum(b.get("count", 1) for b in lo[side]["supply"] if b["kind"] == "supply-unit")
    assert real("axis") == 3 + 2 + 1 + 1 + 8 + 3 + 3 + 1
    assert real("cw") == 5 + 1 + 3


def test_every_deployment_names_units_or_explains_why_not():
    g = load("grazianis-offensive")
    for side in ("axis", "cw"):
        for d in g["sides"][side]["deployments"]:
            assert d["units"] or d.get("notes"), d


def test_italian_campaign_extends_graziani():
    c = load("italian-campaign")
    assert c["extends"] == "scenario:grazianis-offensive"
    assert c["end"] == {"game_turn": 20, "opstage": 3}
    assert c["victory"]["kind"] == "points"


def test_graziani_detached_units_start_elsewhere_or_arrive_later():
    g = load("grazianis-offensive")
    oa = {u["id"]: u for p in (ROOT / "data" / "oa").glob("*.json")
          for f in json.loads(p.read_text())["formations"] for u in f["units"]}
    placed, detached = [], set()
    for side in ("axis", "cw"):
        for d in g["sides"][side]["deployments"]:
            for e in d["units"]:
                if "unit" in e:
                    placed.append(e["unit"])
                placed += e.get("attached", [])
                detached |= set(e.get("detached", []))
    assert sorted(set(placed)) == sorted(placed), "a counter is placed twice"
    for uid in detached:
        assert uid in placed or isinstance(oa[uid]["arrives"], dict), uid


def test_rommels_arrival_set_up():
    r = load("rommels-arrival")
    assert (r["start"], r["end"]) == ({"game_turn": 26, "opstage": 3}, {"game_turn": 38, "opstage": 3})
    assert r["initiative"] == {"side": "axis", "through": {"game_turn": 27, "opstage": 3}}
    ports = {p["place"]: p["efficiency"] for p in r["construction"]["ports"]}
    assert ports["tobruk"] == 2 and ports["benghazi"] == 0  # R-027
    sched = json.loads((ROOT / "data" / "tables" / "reinforcement-schedule.json").read_text())
    due = {u for row in sched["rows"] if row["side"] == "axis" and row["kind"] == "arrives"
           and (row["game_turn"], row["opstage"]) < (26, 3) for u in row["units"] if u.startswith("unit:de:")}
    placed = {e["unit"] for d in r["sides"]["axis"]["deployments"] for e in d["units"] if e.get("unit", "").startswith("unit:de:")}
    assert placed == due
    assert load("desert-fox-campaign")["extends"] == "scenario:rommels-arrival"


def test_operation_crusader():
    c = load("operation-crusader")
    assert (c["start"], c["end"]) == ({"game_turn": 57, "opstage": 3}, {"game_turn": 65, "opstage": 1})
    assert c["victory"]["kind"] == "points" and len(c["victory"]["points"]) == 9
    assert [m["min"] for m in c["victory"]["margins"]] == [10, 6, 1, 0]


def test_el_alamein_pair():
    lc, lr = load("the-last-chance"), load("the-long-retreat")
    assert (lc["start"], lc["end"]) == ({"game_turn": 102, "opstage": 1}, {"game_turn": 102, "opstage": 3})
    assert lr["extends"] == "scenario:the-last-chance"
    assert sorted(p["axis"] for p in lr["victory"]["points"]) == [1, 1, 1, 2, 3, 3, 5]
    assert len(lc["construction"]["minefields"]) == 24
