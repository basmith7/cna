import gen_spi_cases as g

SAMPLE = """[#8_0]
== LAND MOVEMENT

GENERAL RULE: some text

[#8_1]
=== HOW TO MOVE UNITS

[#8_11]
*[8.11]* Units may be moved ...
[#8_12]
*[8.12]* Under certain conditions ...
[#8_11]
duplicate anchor should be ignored
[#17.6]
=== malformed dot anchor
"""


def test_parse_anchors_kinds_and_normalisation():
    got = g.parse_anchors(SAMPLE)
    assert got[0] == {"id": "8.0", "section": 8, "kind": "section", "anchor": "8_0"}
    assert got[1] == {"id": "8.1", "section": 8, "kind": "primary", "anchor": "8_1"}
    assert got[2] == {"id": "8.11", "section": 8, "kind": "secondary", "anchor": "8_11"}
    assert [c["id"] for c in got] == ["8.0", "8.1", "8.11", "8.12", "17.6"]


def test_build_cases_sorts_dedupes_and_adds_empty_label_and_page():
    cases = g.build_cases({17: "[#17_0]\n[#17_6]\n", 8: SAMPLE})
    ids = [c["id"] for c in cases]
    assert ids == ["8.0", "8.1", "8.11", "8.12", "17.0", "17.6"]
    assert all(c["label"] == "" and c["page"] is None for c in cases)


def test_no_source_text_leaks_into_records():
    cases = g.build_cases({8: SAMPLE})
    assert set().union(*(set(c) for c in cases)) == {"id", "section", "kind", "anchor", "label", "page"}
