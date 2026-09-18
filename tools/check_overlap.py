#!/usr/bin/env python3
"""Overlap gate: fail if any N-word run (default 8) in our prose also occurs in the source
transcription. A control against verbatim copying only.

  python3 tools/check_overlap.py [--n 8] [path ...]

With no paths, the default scope is every tracked text file (via `git ls-files`, filtered
to a fixed set of extensions, excluding LICENSE*, package-lock.json and the allowlist
itself; falls back to the old rules/rulings/README default if git is unavailable). Given
explicit paths, each is a file, or a directory expanded to every file under it with one
of those tracked extensions.
"""
import argparse
import pathlib
import re
import subprocess
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


def find_overlaps(rules_md: str, source_grams: set, allow: set, n: int = 8,
                   markdown: bool = True) -> list[tuple[str, ...]]:
    text = strip_markdown(rules_md) if markdown else rules_md
    grams = ngrams(normalize(text), n)
    return sorted((grams & source_grams) - allow)


MIN_SOURCE_TOKENS = 100_000


def source_ngrams(n: int = 8) -> set[tuple[str, ...]]:
    grams: set[tuple[str, ...]] = set()
    total_tokens = 0
    for p in fetch.all_source_sections():
        text = p.read_text(errors="replace")
        tokens = normalize(strip_asciidoc(text))
        if not text.strip():
            print(f"check_overlap: source section {p} is empty; refusing to run on a "
                  "degraded corpus", file=sys.stderr)
            sys.exit(1)
        total_tokens += len(tokens)
        grams |= ngrams(tokens, n)
    if total_tokens < MIN_SOURCE_TOKENS:
        print(f"check_overlap: source corpus has only {total_tokens} tokens "
              f"(expected >= {MIN_SOURCE_TOKENS}); refusing to run on a degraded corpus",
              file=sys.stderr)
        sys.exit(1)
    return grams


SCAN_EXTENSIONS = {".md", ".py", ".json", ".txt", ".yml", ".yaml", ".mts", ".mjs", ".ts",
                    ".css", ".html"}
DEFAULT_FALLBACK = [str(ROOT / "rules"), str(ROOT / "rulings"),
                     str(ROOT / "README.md"), str(ROOT / "data" / "README.md")]


def _is_excluded(rel: pathlib.PurePosixPath) -> bool:
    name = rel.name
    if name.startswith("LICENSE"):
        return True
    if name == "package-lock.json":
        return True
    if rel == pathlib.PurePosixPath("tools/overlap-allowlist.txt"):
        return True
    return False


def default_scope_files() -> list[pathlib.Path]:
    """Every tracked text file, discovered with `git ls-files` and filtered to
    SCAN_EXTENSIONS. Falls back to the old rules/rulings/README default if git is
    unavailable or fails."""
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, check=True,
                              capture_output=True, text=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return sorted({f for p in map(pathlib.Path, DEFAULT_FALLBACK)
                       for f in (p.rglob("*.md") if p.is_dir() else [p] if p.is_file() else [])})
    files = []
    for line in out.splitlines():
        rel = pathlib.PurePosixPath(line)
        if rel.suffix not in SCAN_EXTENSIONS or _is_excluded(rel):
            continue
        p = ROOT / line
        if p.is_file():
            files.append(p)
    return sorted(files)


def _resolve_path_for_report(p: pathlib.Path) -> str:
    p = p.resolve()
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def main(argv: list[str]) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=None)
    ap.add_argument("--n", type=int, default=8)
    a = ap.parse_args(argv)
    if a.paths:
        files = sorted({f for p in map(pathlib.Path, a.paths)
                        for f in (p.rglob("*") if p.is_dir() else [p] if p.is_file() else [])
                        if f.is_file() and f.suffix in SCAN_EXTENSIONS})
    else:
        files = default_scope_files()
    if not files:
        print("check_overlap: OK (no files)")
        return
    grams, allow = source_ngrams(a.n), load_allowlist(n=a.n)
    total = 0
    for f in files:
        is_md = f.suffix == ".md"
        for hit in find_overlaps(f.read_text(errors="replace"), grams, allow, a.n, markdown=is_md):
            total += 1
            print(f"{_resolve_path_for_report(f)}: {' '.join(hit)}")
    print(f"check_overlap: {'FAIL' if total else 'OK'} ({total} shared {a.n}-word runs)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
