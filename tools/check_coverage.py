#!/usr/bin/env python3
"""Coverage report: which SPI cases have no primary badge in rules/. A report, not a gate —
exits 1 only for malformed badges (unknown case, duplicate primary).

  python3 tools/check_coverage.py [--sections 1-32] [--markdown] [rules_dir]
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BADGE = re.compile(r"^:::\s+(spi|spi-ref|spi-omit)\s+(.*?)\s*$")
CASE = re.compile(r"^\d{1,2}\.\d{1,2}$")


def parse_badges(md: str) -> list[dict]:
    out = []
    for i, line in enumerate(md.splitlines(), 1):
        m = BADGE.match(line)
        if not m:
            continue
        kind, rest = m.group(1), m.group(2)
        reason = None
        if kind == "spi-omit":
            parts = re.split(r"\s+(?:—|--)\s+", rest, maxsplit=1)
            rest, reason = parts[0], (parts[1].strip() if len(parts) > 1 else None)
        out.append({"kind": kind, "cases": rest.split(), "reason": reason, "line": i})
    return out


def parse_sections(spec: str) -> set[int]:
    out: set[int] = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return out


def coverage(case_ids: list[str], badges_by_file: dict[str, list[dict]], sections: set[int] | None) -> dict:
    known = set(case_ids)
    in_scope = [c for c in case_ids if sections is None or int(c.split(".")[0]) in sections]
    primary: dict[str, str] = {}
    omitted: dict[str, str] = {}
    errors: list[str] = []
    for f, badges in badges_by_file.items():
        for b in badges:
            for c in b["cases"]:
                where = f"{f}:{b['line']}"
                if not CASE.match(c) or c not in known:
                    errors.append(f"{where}: unknown case {c}")
                    continue
                if b["kind"] == "spi":
                    if c in primary:
                        errors.append(f"{where}: second primary badge for {c} (first in {primary[c]})")
                    else:
                        primary[c] = where
                elif b["kind"] == "spi-omit":
                    omitted[c] = b["reason"] or ""
                    if not b["reason"]:
                        errors.append(f"{where}: spi-omit {c} needs a reason after ' — '")
    scope = set(in_scope)
    return {
        "total": len(in_scope),
        "primary": len(scope & set(primary)),
        "omitted": len(scope & set(omitted) - set(primary)),
        "uncovered": [c for c in in_scope if c not in primary and c not in omitted],
        "errors": sorted(errors),
    }


def render_markdown(rep: dict) -> str:
    covered = rep["primary"] + rep["omitted"]
    lines = [f"### SPI case coverage: {covered} / {rep['total']} "
             f"({rep['primary']} restated, {rep['omitted']} omitted with reason)", ""]
    if rep["errors"]:
        lines += ["**Errors:**"] + [f"- {e}" for e in rep["errors"]] + [""]
    if rep["uncovered"]:
        lines += [f"<details><summary>{len(rep['uncovered'])} cases without a primary badge</summary>", "",
                  " ".join(f"`{c}`" for c in rep["uncovered"]), "", "</details>"]
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("rules_dir", nargs="?", default=str(ROOT / "rules"))
    ap.add_argument("--sections", default=None, help="e.g. 1-32 or 1-3,8")
    ap.add_argument("--markdown", action="store_true")
    a = ap.parse_args(argv)
    ids = [c["id"] for c in json.loads((ROOT / "data" / "spi-cases.json").read_text())["cases"]]
    files = sorted(pathlib.Path(a.rules_dir).rglob("*.md"))
    badges = {str(f.relative_to(ROOT)): parse_badges(f.read_text()) for f in files}
    rep = coverage(ids, badges, parse_sections(a.sections) if a.sections else None)
    if a.markdown:
        print(render_markdown(rep), end="")
    else:
        print(f"coverage: {rep['primary'] + rep['omitted']} / {rep['total']} "
              f"(primary {rep['primary']}, omitted {rep['omitted']}, uncovered {len(rep['uncovered'])})")
        for e in rep["errors"]:
            print(f"ERROR {e}")
    sys.exit(1 if rep["errors"] else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
