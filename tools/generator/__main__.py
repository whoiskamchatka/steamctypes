"""Generate src/steamctypes/_generated from the local Steamworks SDK."""

import argparse
import sys

from tools.generator.ctype import UnknownTypesError
from tools.generator.emit import OUTPUT_DIR, EmitError, compare_files, generate, write_files
from tools.generator.load import ApiError, load_api
from tools.generator.manifest import (
    INPUTS_CHANGED,
    MANIFEST,
    manifest_text,
    verify,
    write_manifest,
)
from tools.generator.overrides import OverrideError
from tools.generator.parser import SchemaError
from tools.sdk import LOCK_PATH, REPO_ROOT, SdkError, check_sdk, locate_sdk, read_lock

_ERRORS = (SdkError, SchemaError, OverrideError, UnknownTypesError, ApiError, EmitError)
_REGENERATE = "Run `uv run python -m tools.generator` to regenerate."
_DO_NOT_EDIT = (
    "Generated files must not be edited: change tools/generator instead and run "
    "`uv run python -m tools.generator`."
)


def _fail(message: str, details: list[str], hint: str | None = None) -> int:
    print(message, file=sys.stderr)
    for detail in details:
        print(f"  {detail}", file=sys.stderr)
    if hint:
        print(hint, file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m tools.generator", description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="compare the generated files with the ones on disk instead of writing them",
    )
    mode.add_argument(
        "--verify",
        action="store_true",
        help=f"without the SDK, compare the generated files and their inputs with {MANIFEST.name}",
    )
    args = parser.parse_args()
    target = OUTPUT_DIR.relative_to(REPO_ROOT).as_posix()
    manifest = MANIFEST.as_posix()

    if args.verify:
        if problems := verify(REPO_ROOT):
            hint = _REGENERATE if problems == [INPUTS_CHANGED] else _DO_NOT_EDIT
            return _fail(f"{target} does not match {manifest}:", problems, hint)
        print(f"{target} matches {manifest}")
        return 0

    try:
        root = locate_sdk()
        if problems := check_sdk(root, LOCK_PATH):
            return _fail(f"Steamworks SDK at {root} does not match {LOCK_PATH.name}:", problems)
        version = read_lock(LOCK_PATH).version
        files = generate(load_api(root), version)
    except _ERRORS as error:
        return _fail(f"error: {error}", [])

    if args.check:
        problems = compare_files(files, OUTPUT_DIR)
        manifest_path = REPO_ROOT / MANIFEST
        if not manifest_path.is_file():
            problems.append(f"{manifest}: missing")
        elif manifest_path.read_bytes() != manifest_text(REPO_ROOT, files).encode():
            problems.append(f"{manifest}: differs")
        if problems:
            return _fail(f"{target} does not match SDK {version}:", problems)
        print(f"{target} and {manifest} match SDK {version}")
        return 0
    write_files(files, OUTPUT_DIR)
    write_manifest(REPO_ROOT, files)
    print(f"wrote {len(files)} files to {target} and {manifest} for SDK {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
