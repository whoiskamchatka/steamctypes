"""Locate the local Steamworks SDK and pin it in sdk.lock."""

import argparse
import hashlib
import os
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SDK_PATH = REPO_ROOT / "vendor" / "steamworks"
LOCK_PATH = REPO_ROOT / "sdk.lock"

JSON_PATH = "public/steam/steam_api.json"
REDIST_DIR = "redistributable_bin"
LOCKED_FILES = (
    JSON_PATH,
    f"{REDIST_DIR}/win64/steam_api64.dll",
    f"{REDIST_DIR}/linux64/libsteam_api.so",
    f"{REDIST_DIR}/osx/libsteam_api.dylib",
)

# Readme.txt is a changelog, newest release first. Each release starts with a line such as
# "v1.65 <date>".
_VERSION_HEADER = re.compile(rb"^v(\d+\.\d+[a-z]?)\s", re.MULTILINE)


class SdkError(Exception):
    pass


@dataclass(frozen=True)
class Lock:
    version: str
    sha256: dict[str, str]


def locate_sdk() -> Path:
    env_path = os.environ.get("STEAMWORKS_SDK_PATH")
    root = Path(env_path) if env_path else DEFAULT_SDK_PATH
    origin = "from STEAMWORKS_SDK_PATH" if env_path else "default location"
    if not root.is_dir():
        raise SdkError(
            f"no Steamworks SDK at {root} ({origin}); set STEAMWORKS_SDK_PATH or copy the "
            f"contents of the SDK's sdk/ folder to {DEFAULT_SDK_PATH}"
        )
    missing: list[str] = []
    if not (root / JSON_PATH).is_file():
        missing.append(JSON_PATH)
    if not (root / REDIST_DIR).is_dir():
        missing.append(f"{REDIST_DIR}/")
    if missing:
        raise SdkError(
            f"incomplete Steamworks SDK at {root} ({origin}): missing {', '.join(missing)}"
        )
    return root


def sdk_version(root: Path) -> str:
    readme = root / "Readme.txt"
    try:
        match = _VERSION_HEADER.search(readme.read_bytes())
    except FileNotFoundError:
        raise SdkError(f"cannot determine the SDK version: {readme} not found") from None
    if match is None:
        raise SdkError(f"cannot determine the SDK version: no version header in {readme}")
    return match.group(1).decode()


def file_sha256(path: Path) -> str:
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def compute_lock(root: Path) -> Lock:
    missing = [name for name in LOCKED_FILES if not (root / name).is_file()]
    if missing:
        raise SdkError(f"incomplete Steamworks SDK at {root}: missing {', '.join(missing)}")
    return Lock(sdk_version(root), {name: file_sha256(root / name) for name in LOCKED_FILES})


def write_lock(lock: Lock, path: Path) -> None:
    lines = [f'version = "{lock.version}"', "", "[sha256]"]
    lines += [f'"{name}" = "{digest}"' for name, digest in lock.sha256.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def read_lock(path: Path) -> Lock:
    try:
        with path.open("rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        raise SdkError(f"{path} not found; run `uv run python -m tools.sdk lock`") from None
    return Lock(data["version"], data["sha256"])


def check_sdk(root: Path, lock_path: Path) -> list[str]:
    """Describe every way the SDK at root differs from the lock file; empty if it matches."""
    locked = read_lock(lock_path)
    actual = compute_lock(root)
    problems: list[str] = []
    if locked.version != actual.version:
        problems.append(f"SDK version is {actual.version}, {lock_path.name} has {locked.version}")
    for name, digest in actual.sha256.items():
        locked_digest = locked.sha256.get(name)
        if locked_digest is None:
            problems.append(f"{name}: not in {lock_path.name}")
        elif locked_digest != digest:
            problems.append(f"{name}: sha256 differs from {lock_path.name}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m tools.sdk", description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("lock", help=f"write {LOCK_PATH.name} from the local SDK")
    commands.add_parser("check", help=f"verify the local SDK matches {LOCK_PATH.name}")
    args = parser.parse_args()

    try:
        root = locate_sdk()
        if args.command == "lock":
            lock = compute_lock(root)
            write_lock(lock, LOCK_PATH)
            print(f"wrote {LOCK_PATH.name} for Steamworks SDK {lock.version} at {root}")
            return 0
        problems = check_sdk(root, LOCK_PATH)
    except SdkError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    if problems:
        print(f"Steamworks SDK at {root} does not match {LOCK_PATH.name}:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    print(f"Steamworks SDK at {root} matches {LOCK_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
