"""Record what produced src/steamctypes/_generated, so it can be verified without the SDK."""

import hashlib
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any, cast

from tools.generator.emit import OUTPUT_DIR
from tools.sdk import LOCK_PATH, REPO_ROOT, file_sha256

# Paths relative to the repository root, so a copy of the tree can be verified too.
GENERATOR = Path(__file__).resolve().parent.relative_to(REPO_ROOT)
OUTPUT = OUTPUT_DIR.relative_to(REPO_ROOT)
LOCK = LOCK_PATH.relative_to(REPO_ROOT)
SDK_TOOL = GENERATOR.parent / "sdk.py"
MANIFEST = GENERATOR / "manifest.json"
INPUTS_CHANGED = "generator inputs changed without regenerating"


def inputs_hash(root: Path) -> str:
    """One hash over everything generation reads besides the SDK, as stored on disk."""
    generator = root / GENERATOR
    # The ruff version and settings are not inputs: CI's `ruff format --check` catches output that
    # the current ruff would format differently.
    inputs = [
        *sorted(generator.glob("*.py")),
        generator / "overrides.toml",
        root / SDK_TOOL,
        root / LOCK,
    ]
    digest = hashlib.sha256()
    for path in inputs:
        digest.update(f"{path.relative_to(root).as_posix()}\0{file_sha256(path)}\n".encode())
    return digest.hexdigest()


def manifest_text(root: Path, files: Mapping[str, str]) -> str:
    outputs = {name: hashlib.sha256(source.encode()).hexdigest() for name, source in files.items()}
    manifest = {"inputs": inputs_hash(root), "outputs": outputs}
    return json.dumps(manifest, indent=2, sort_keys=True) + "\n"


def write_manifest(root: Path, files: Mapping[str, str]) -> None:
    (root / MANIFEST).write_text(manifest_text(root, files), encoding="utf-8", newline="\n")


def verify(root: Path) -> list[str]:
    """Compare the generated files and generator inputs with the manifest; empty if they match."""
    try:
        loaded: object = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"{MANIFEST.as_posix()} is missing"]
    manifest = cast(dict[str, Any], loaded) if isinstance(loaded, dict) else {}
    if not isinstance(manifest.get("outputs"), dict):
        return [f"{MANIFEST.as_posix()} is malformed"]
    recorded = cast(dict[str, Any], manifest["outputs"])

    output = root / OUTPUT
    actual: dict[str, str] = {}
    if output.is_dir():
        actual = {p.name: file_sha256(p) for p in output.iterdir() if p.is_file()}
    problems = [f"{name}: missing" for name in sorted(recorded.keys() - actual.keys())]
    problems += [f"{name}: not generated" for name in sorted(actual.keys() - recorded.keys())]
    problems += [
        f"{name}: edited by hand"
        for name in sorted(recorded.keys() & actual.keys())
        if recorded[name] != actual[name]
    ]
    if manifest.get("inputs") != inputs_hash(root):
        problems.append(INPUTS_CHANGED)
    return problems
