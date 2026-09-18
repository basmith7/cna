#!/usr/bin/env python3
"""Overlap gate: fail if any N-word run (default 8) in our prose — rules/, rulings/, and the
READMEs the site renders — also occurs in the source transcription. A control against verbatim
copying only.

  python3 tools/check_overlap.py [--n 8] [path ...]     # each path a .md file or a directory
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fetch  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "tools" / "overlap-allowlist.txt"
TOKEN = re.compile(r"[a-z0-9']+")


def normalize(text: str) -> list[str]:
    text = text.lower().replace("‘", "'").replace("’", "'")
    return TOKEN.findall(text)


def strip_markdown(md: str) -> str:
    if md.startswith("---"):
        end = md.find("\n---", 3)
        if end != -1:
            md = md[end + 4:]
    out = []
    for line in md.splitlines():
        s = line.strip()
        if s.startswith(":::"):
            continue
        if re.fullmatch(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?", s):
            continue
        s = re.sub(r"^#{1,6}\s+", "", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        # These replace calls document intent; tokenization already treats them as boundaries
        s = s.replace("|", " ").replace("`", " ").replace("*", " ").replace("_", " ")
        out.append(s)
    return "\n".join(out)


def strip_asciidoc(adoc: str) -> str:
    out = []
    for line in adoc.splitlines():
        s = line.strip()
        if (re.fullmatch(r"\[#[^\]]+\]", s) or re.fullmatch(r"\[[^\s\]]+\]", s) or
                re.fullmatch(r"=+", s)):
            continue
        s = re.sub(r"^=+\s+", "", s)
        s = re.sub(r"\*\[[\d.]+\]\*", "", s)
        s = re.sub(r"<<[^,>]+,([^>]+)>>", r"\1", s)
        # These replace calls document intent; tokenization already treats them as boundaries
        s = s.replace("*", " ").replace("_", " ")
        out.append(s)
    return "\n".join(out)


def ngrams(tokens: list[str], n: int = 8) -> set[tuple[str, ...]]:
    return {tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def load_allowlist_text(text: str, n: int = 8) -> set[tuple[str, ...]]:
    allow: set[tuple[str, ...]] = set()
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            allow |= ngrams(normalize(line), n)
    return allow


def load_allowlist(path: pathlib.Path = ALLOWLIST, n: int = 8) -> set[tuple[str, ...]]:
    return load_allowlist_text(path.read_text(), n) if path.exists() else set()


def find_overlaps(rules_md: str, source_grams: set, allow: set, n: int = 8) -> list[tuple[str, ...]]:
    grams = ngrams(normalize(strip_markdown(rules_md)), n)
    return sorted((grams & source_grams) - allow)


def source_ngrams(n: int = 8) -> set[tuple[str, ...]]:
    grams: set[tuple[str, ...]] = set()
    for p in fetch.all_source_sections():
        grams |= ngrams(normalize(strip_asciidoc(p.read_text(errors="replace"))), n)
    return grams


def main(argv: list[str]) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=[str(ROOT / "rules"), str(ROOT / "rulings"),
                                                 str(ROOT / "README.md"), str(ROOT / "data" / "README.md")])
    ap.add_argument("--n", type=int, default=8)
    a = ap.parse_args(argv)
    files = sorted({f for p in map(pathlib.Path, a.paths)
                    for f in (p.rglob("*.md") if p.is_dir() else [p] if p.is_file() else [])})
    if not files:
        print("check_overlap: OK (no files)")
        return
    grams, allow = source_ngrams(a.n), load_allowlist(n=a.n)
    total = 0
    for f in files:
        for hit in find_overlaps(f.read_text(), grams, allow, a.n):
            total += 1
            print(f"{f.relative_to(ROOT)}: {' '.join(hit)}")
    print(f"check_overlap: {'FAIL' if total else 'OK'} ({total} shared {a.n}-word runs)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
