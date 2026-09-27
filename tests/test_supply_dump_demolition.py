"""Supply Dump Demolition Table (SPI 54.17), as printed and with the E-032 errata overlay."""
import copy
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _table():
    return json.loads((ROOT / "data" / "tables" / "supply-dump-demolition.json").read_text())


def _apply(t, patch):
    t = copy.deepcopy(t)
    for p in patch["patches"]:
        assert p["op"] == "replace"
        parts = p["path"].strip("/").split("/")
        node = t
        for k in parts[:-1]:
            node = node[int(k)] if isinstance(node, list) else node[k]
        node[int(parts[-1]) if isinstance(node, list) else parts[-1]] = p["value"]
    return t


def test_as_printed():
    t = _table()
    assert [r["die"] for r in t["rows"]] == list(range(-2, 9))
    assert [r["percent"] for r in t["rows"]] == [0, 33, 0, 10, 20, 33, 50, 75, 100, 33, 100]
    assert t["rows"][-1]["or_more"] is True
    assert len(t["modifiers"]) == 8


def test_errata_makes_it_monotone():
    t = _apply(_table(), json.loads((ROOT / "data" / "errata" / "E-032.json").read_text()))
    pct = [r["percent"] for r in t["rows"]]
    assert pct == [0, 0, 0, 10, 20, 33, 50, 75, 100, 100, 100]
    assert pct == sorted(pct)
