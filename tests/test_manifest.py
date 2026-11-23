from pathlib import Path

from tools.generator.emit import write_files
from tools.generator.manifest import GENERATOR, INPUTS_CHANGED, LOCK, OUTPUT, verify, write_manifest


def test_verify_detects_hand_edits_and_stale_inputs(tmp_path: Path) -> None:
    generator = tmp_path / GENERATOR
    generator.mkdir(parents=True)
    (generator / "emit.py").write_bytes(b"WIDGETS = 1\n")
    (generator / "overrides.toml").write_bytes(b"")
    (tmp_path / LOCK).write_bytes(b'version = "9.99"\n')
    files = {"__init__.py": 'SDK_VERSION = "9.99"\n', "structs.py": "class Widget_t: ...\n"}
    write_files(files, tmp_path / OUTPUT)
    write_manifest(tmp_path, files)
    assert verify(tmp_path) == []

    (tmp_path / OUTPUT / "structs.py").write_bytes(b"class Widget_t: pass\n")
    assert verify(tmp_path) == ["structs.py: edited by hand"]

    write_files(files, tmp_path / OUTPUT)
    (generator / "emit.py").write_bytes(b"WIDGETS = 2\n")
    assert verify(tmp_path) == [INPUTS_CHANGED]
