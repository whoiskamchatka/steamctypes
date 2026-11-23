"""Generate src/steamctypes/_generated from the local Steamworks SDK."""

import argparse
import sys

from tools.generator.ctype import UnknownTypesError
from tools.generator.emit import OUTPUT_DIR, EmitError, compare_files, generate, write_files
from tools.generator.load import ApiError, load_api
from tools.generator.overrides import OverrideError
from tools.generator.parser import SchemaError
from tools.sdk import LOCK_PATH, REPO_ROOT, SdkError, check_sdk, locate_sdk, read_lock

_ERRORS = (SdkError, SchemaError, OverrideError, UnknownTypesError, ApiError, EmitError)


def _fail(message: str, details: list[str]) -> int:
    print(message, file=sys.stderr)
    for detail in details:
        print(f"  {detail}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m tools.generator", description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare the generated files with the ones on disk instead of writing them",
    )
    args = parser.parse_args()
    target = OUTPUT_DIR.relative_to(REPO_ROOT).as_posix()

    try:
        root = locate_sdk()
        if problems := check_sdk(root, LOCK_PATH):
            return _fail(f"Steamworks SDK at {root} does not match {LOCK_PATH.name}:", problems)
        version = read_lock(LOCK_PATH).version
        files = generate(load_api(root), version)
    except _ERRORS as error:
        return _fail(f"error: {error}", [])

    if args.check:
        if problems := compare_files(files, OUTPUT_DIR):
            return _fail(f"{target} does not match SDK {version}:", problems)
        print(f"{target} matches SDK {version}")
        return 0
    write_files(files, OUTPUT_DIR)
    print(f"wrote {len(files)} files to {target} for SDK {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
