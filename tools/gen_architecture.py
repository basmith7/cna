#!/usr/bin/env python3
"""Regenerate the machine-derived blocks of ARCHITECTURE.md: the data-model ERD, the
table-concept list and the tools list. Each lives between `<!-- generated:<name> -->`
and `<!-- /generated:<name> -->` markers.

  python3 tools/gen_architecture.py           # rewrite the blocks in place
  python3 tools/gen_architecture.py --check   # exit 1 if ARCHITECTURE.md is stale

The ERD's edges come from the `$ref`s to the id types in data/schema (hexId, unitId,
scenarioId, placeId); the few relations a schema cannot state are listed in EXTRA.
"""
import ast
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "ARCHITECTURE.md"

# entity -> (schema file stem, identifying/relating fields shown in the ERD)
ENTITIES = {
    "SPI_CASE": ("spi-cases", ["string id PK"]),
    "TABLE": ("(one per data/tables file)", ["string concept PK", "string[] sources"]),
    "ERRATUM": ("errata-patch", ["string id PK", "string table FK"]),
    "RULING": ("(rulings/R-nnn.md)", ["string id PK", "string status", "string[] affects"]),
    "OA_FORMATION": ("oa", ["string nation", "string id PK"]),
    "UNIT": ("oa", ["string id PK", "string parent FK", "string id_code FK"]),
    "SCENARIO": ("scenario", ["string id PK", "string extends FK"]),
    "SHEET": ("map-sheets", ["string letter PK"]),
    "HEX": ("map-hexes", ["string id PK", "string sheet FK"]),
    "HEXSIDE": ("map-hexsides", ["string key PK", "string a FK", "string b FK"]),
    "PLACE": ("map-places", ["string id PK", "string hex FK"]),
    "MAP_CORRECTION": ("map-correction", ["string id PK", "string key FK"]),
}
# id type in common/scenario schemas -> entity it identifies
ID_ENTITY = {"hexId": "HEX", "unitId": "UNIT", "scenarioId": "SCENARIO", "placeId": "PLACE"}
# schema stem -> entity that owns the references found in it (a table schema is a TABLE)
OWNER = {"scenario": "SCENARIO", "oa": "UNIT", "reinforcement-schedule": "TABLE", "construction": "TABLE",
         "map-places": "PLACE", "map-hexsides": "HEXSIDE", "map-hexes": None, "map-seams": None}
# relations the schemas cannot state: (from, cardinality, to, label)
EXTRA = [
    ("SPI_CASE", "||--o{", "TABLE", "sources"),
    ("SPI_CASE", "}o--o{", "RULING", "affects"),
    ("SPI_CASE", "}o--o{", "ERRATUM", "affects"),
    ("TABLE", "||--o{", "ERRATUM", "patched by"),
    ("OA_FORMATION", "||--o{", "UNIT", "contains"),
    ("UNIT", "|o--o{", "UNIT", "parent"),
    ("TABLE", "|o--o{", "UNIT", "id_code, in unit-characteristics"),
    ("SCENARIO", "}o--o{", "OA_FORMATION", "formation entries"),
    ("SCENARIO", "|o--o{", "SCENARIO", "extends"),
    ("SHEET", "||--o{", "HEX", "contains"),
    ("HEX", "||--o{", "HEXSIDE", "a, b"),
    ("HEX", "||--o{", "PLACE", "hex, hexes"),
    ("MAP_CORRECTION", "}o--o|", "HEX", "target"),
    ("MAP_CORRECTION", "}o--o|", "HEXSIDE", "target"),
]


def _ref_ids(node) -> set[str]:
    """Names of the id types a schema refers to."""
    found: set[str] = set()
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.rsplit("/", 1)[-1] in ID_ENTITY:
            found.add(ref.rsplit("/", 1)[-1])
        for v in node.values():
            found |= _ref_ids(v)
    elif isinstance(node, list):
        for v in node:
            found |= _ref_ids(v)
    return found


def schema_edges(schema_dir: pathlib.Path) -> set[tuple[str, str]]:
    edges = set()
    for stem, owner in OWNER.items():
        p = schema_dir / f"{stem}.schema.json"
        if owner and p.exists():
            for ident in _ref_ids(json.loads(p.read_text())):
                edges.add((owner, ID_ENTITY[ident]))
    return edges


def erd(schema_dir: pathlib.Path = ROOT / "data" / "schema") -> str:
    lines = ["```mermaid", "erDiagram"]
    for (a, b) in sorted(schema_edges(schema_dir)):
        if a != b:
            lines.append(f"    {a} }}o--o{{ {b} : \"refs (schema)\"")
    for a, card, b, label in EXTRA:
        lines.append(f"    {a} {card.strip()} {b} : \"{label}\"")
    for name, (_, attrs) in ENTITIES.items():
        lines.append(f"    {name} {{")
        lines += [f"        {a}" for a in attrs]
        lines.append("    }")
    lines.append("```")
    return "\n".join(lines)


def table_concepts(data_dir: pathlib.Path = ROOT / "data") -> str:
    names = sorted(p.stem for p in (data_dir / "tables").glob("*.json"))
    return f"{len(names)} concepts: " + ", ".join(f"`{n}`" for n in names)


def tools_list(tools_dir: pathlib.Path = ROOT / "tools") -> str:
    rows = ["| Tool | Does |", "|---|---|"]
    for p in sorted(tools_dir.glob("*.py")):
        doc = ast.get_docstring(ast.parse(p.read_text())) or ""
        first = " ".join(doc.split("\n\n")[0].split())
        rows.append(f"| `tools/{p.name}` | {first.replace('|', '/')} |")
    return "\n".join(rows)


def blocks() -> dict[str, str]:
    return {"erd": erd(), "tables": table_concepts(), "tools": tools_list()}


def render(text: str, new: dict[str, str]) -> str:
    for name, body in new.items():
        pat = re.compile(rf"(<!-- generated:{name} -->\n).*?(<!-- /generated:{name} -->)", re.S)
        if not pat.search(text):
            raise SystemExit(f"gen_architecture: missing markers for {name} in {DOC.name}")
        text = pat.sub(lambda m, body=body: m.group(1) + body + "\n" + m.group(2), text)
    return text


def main(argv: list[str]) -> None:
    old = DOC.read_text()
    new = render(old, blocks())
    if "--check" in argv:
        print(f"gen_architecture --check: {'OK' if new == old else 'FAIL (run tools/gen_architecture.py)'}")
        sys.exit(0 if new == old else 1)
    DOC.write_text(new)


if __name__ == "__main__":
    main(sys.argv[1:])
