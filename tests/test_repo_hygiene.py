import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_licence_files_exist_and_pointer_names_the_split():
    for name in ["LICENSE", "LICENSE-TEXT", "LICENSE-DATA", "LICENSE-CODE"]:
        assert (ROOT / name).is_file(), name
    pointer = (ROOT / "LICENSE").read_text()
    assert "CC-BY-SA-4.0" in pointer and "rules/" in pointer
    assert "CC0-1.0" in pointer and "data/" in pointer
    assert "MIT" in pointer and "tools/" in pointer and "site/" in pointer


def test_licence_texts_are_the_real_licences():
    assert "Attribution-ShareAlike 4.0 International" in (ROOT / "LICENSE-TEXT").read_text()
    assert "CC0 1.0 Universal" in (ROOT / "LICENSE-DATA").read_text()
    assert "MIT License" in (ROOT / "LICENSE-CODE").read_text()


def test_readme_states_legal_posture():
    readme = (ROOT / "README.md").read_text()
    for phrase in ["not copyrightable", "no legal review", "tonicebrian", "show original"]:
        assert phrase in readme, phrase


def test_extraction_log_has_format_section():
    text = (ROOT / "EXTRACTION.md").read_text()
    assert "## Format" in text


def test_rulings_readme_defines_statuses_and_fork_policy():
    text = (ROOT / "rulings" / "README.md").read_text()
    for word in ["proposed", "accepted", "rejected", "superseded", "## Fork policy", "R-001"]:
        assert word in text, word


def test_no_build_output_or_rasters_are_tracked():
    import subprocess
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    bad = [p for p in tracked if p.startswith("build/")
           or (p.startswith(("data/", "site/public/map/")) and p.lower().endswith((".png", ".jpg", ".jpeg", ".npy", ".xml")))]
    assert bad == [], bad
    assert "build/" in (ROOT / ".gitignore").read_text().splitlines()
