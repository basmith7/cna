#!/usr/bin/env python3
"""Generate data/spi-cases.json — the canonical list of SPI case IDs — from the
anchors in the pinned source-text repo. Only IDs and structure are taken; no text.

  python3 tools/gen_spi_cases.py           # rewrites data/spi-cases.json
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fetch  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "spi-cases.json"
ANCHOR = re.compile(r"^\[#(\d{1,2})[._](\d{1,2})\]\s*$", re.M)


def parse_anchors(adoc_text: str) -> list[dict]:
    """Anchors in file order, de-duplicated (first wins). '.' in an anchor is a source typo for '_'."""
    seen, out = set(), []
    for m in ANCHOR.finditer(adoc_text):
        section, case = int(m.group(1)), m.group(2)
        anchor = f"{section}_{case}"
        if anchor in seen:
            continue
        seen.add(anchor)
        kind = "section" if case == "0" else "primary" if len(case) == 1 else "secondary"
        out.append({"id": f"{section}.{case}", "section": section, "kind": kind, "anchor": anchor})
    return out


def build_cases(section_texts: dict[int, str]) -> list[dict]:
    """All cases across sections, sorted (section, case-number), first occurrence wins."""
    by_anchor = {}
    for n in sorted(section_texts):
        for c in parse_anchors(section_texts[n]):
            by_anchor.setdefault(c["anchor"], c)
    cases = sorted(by_anchor.values(), key=lambda c: (c["section"], int(c["anchor"].split("_")[1])))
    return [dict(c, label="", page=None) for c in cases]


def main() -> None:
    src = fetch.load_sources()["source_text"]
    texts = {int(p.stem.split("-")[1]): p.read_text(errors="replace") for p in fetch.all_source_sections()}
    fresh = build_cases(texts)
    if OUT.exists():  # keep labels/pages already authored
        old = {c["id"]: c for c in json.loads(OUT.read_text())["cases"]}
        for c in fresh:
            if c["id"] in old:
                c["label"], c["page"] = old[c["id"]]["label"], old[c["id"]]["page"]
    OUT.write_text(json.dumps({"source": {"repo": src["repo"], "commit": src["commit"]}, "cases": fresh},
                              indent=1, ensure_ascii=False) + "\n")
    print(f"{len(fresh)} cases → {OUT}")


if __name__ == "__main__":
    main()
