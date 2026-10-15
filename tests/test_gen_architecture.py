import pathlib
import subprocess
import sys

import gen_architecture as ga

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_architecture_doc_is_fresh():
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "gen_architecture.py"), "--check"])
    assert r.returncode == 0, "run tools/gen_architecture.py"


def test_schema_edges_follow_the_id_refs():
    edges = ga.schema_edges(ROOT / "data" / "schema")
    assert ("SCENARIO", "UNIT") in edges and ("SCENARIO", "HEX") in edges
    assert ("PLACE", "HEX") in edges


def test_render_replaces_only_between_markers():
    text = "a\n<!-- generated:x -->\nold\n<!-- /generated:x -->\nb"
    assert ga.render(text, {"x": "new"}) == "a\n<!-- generated:x -->\nnew\n<!-- /generated:x -->\nb"


def test_every_tool_is_listed():
    listed = ga.tools_list()
    assert all(f"tools/{p.name}" in listed for p in (ROOT / "tools").glob("*.py"))


def test_entity_schemas_exist():
    for stem, _ in ga.ENTITIES.values():
        if not stem.startswith("("):
            assert (ROOT / "data" / "schema" / f"{stem}.schema.json").exists(), stem
