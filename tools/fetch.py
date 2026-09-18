#!/usr/bin/env python3
"""Fetch pinned sources into ~/.cache/cna-scans. Nothing fetched here is ever committed.

  python3 tools/fetch.py pages 96 97 98     # scan pages (jp2 index) -> cache/p0096.jpg ...
  python3 tools/fetch.py sections           # all 65 source-text sections at the pinned commit
  python3 tools/fetch.py verify             # download the jp2 zip, check SHA-1, print SHA-256
"""
import hashlib
import json
import os
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = ROOT / "tools" / "sources.json"
CACHE = pathlib.Path(os.path.expanduser("~/.cache/cna-scans"))


def load_sources() -> dict:
    return json.loads(SOURCES.read_text())


def _download(url: str, dest: pathlib.Path) -> None:
    """The only network call in this module; tests replace it. Callers create the parent dir."""
    urllib.request.urlretrieve(url, dest)


def scan_page(page) -> pathlib.Path:
    """Return the cached JPEG for a jp2 index (int or 4-digit string)."""
    page = f"{int(page):04d}"
    dest = CACHE / f"p{page}.jpg"
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        _download(load_sources()["archive_org"]["page_url_template"].format(page=page), dest)
    return dest


def source_section(n: int) -> pathlib.Path:
    """Return the cached AsciiDoc for source section n at the pinned commit."""
    src = load_sources()["source_text"]
    dest = CACHE / "source" / src["commit"] / f"section-{n:02d}.adoc"
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        _download(src["raw_url_template"].format(commit=src["commit"], nn=f"{n:02d}"), dest)
    return dest


def all_source_sections() -> list[pathlib.Path]:
    lo, hi = load_sources()["source_text"]["sections"]
    return [source_section(n) for n in range(lo, hi + 1)]


def _verify_zip() -> None:
    s = load_sources()["archive_org"]
    name = "The Campaign for North Africa_jp2.zip"
    dest = CACHE / "jp2.zip"
    if not dest.exists():
        url = f"https://archive.org/download/{s['identifier']}/{name.replace(' ', '%20')}"
        print(f"downloading {url} ({s['files'][name]['size'] / 1e6:.0f} MB) …", file=sys.stderr)
        dest.parent.mkdir(parents=True, exist_ok=True)
        _download(url, dest)
    sha1, sha256 = hashlib.sha1(), hashlib.sha256()
    with dest.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            sha1.update(chunk)
            sha256.update(chunk)
    ok = sha1.hexdigest() == s["files"][name]["sha1"]
    print(f"sha1   {sha1.hexdigest()}  {'OK' if ok else 'MISMATCH'}")
    print(f"sha256 {sha256.hexdigest()}")
    sys.exit(0 if ok else 1)


def main(argv: list[str]) -> None:
    cmd, args = (argv + [None])[0], argv[1:]
    if cmd == "pages":
        for p in args:
            print(scan_page(p))
    elif cmd == "sections":
        for p in all_source_sections():
            print(p)
    elif cmd == "verify":
        _verify_zip()
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
