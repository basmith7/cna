"""Training Chart (SPI 17.6): stages to train each replacement-point type, plus the six-stage
Commonwealth unit morale training. Values must agree with the 20.43 table where both list a class."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_training_chart_rows_and_agreement_with_replacement_training():
    t = json.loads((ROOT / "data" / "tables" / "training.json").read_text())
    by = {r["type"]: r["stages"] for r in t["rows"]}
    assert by == {"infantry": 3, "tank-or-recce": 6, "gun": 1, "commando": 12, "commonwealth-unit-morale": 6}
    rt = {r["class"]: r["stages"] for r in json.loads((ROOT / "data" / "tables" / "replacement-training.json").read_text())["rows"]}
    assert rt["infantry"] == by["infantry"] and rt["gun"] == by["gun"] and rt["tank"] == rt["recce"] == by["tank-or-recce"]
