import shutil
from pathlib import Path

import pytest

from tools.sdk import (
    JSON_PATH,
    LOCKED_FILES,
    SdkError,
    check_sdk,
    compute_lock,
    locate_sdk,
    write_lock,
)


@pytest.fixture
def fake_sdk(tmp_path: Path) -> Path:
    root = tmp_path / "steamworks"
    for name in LOCKED_FILES:
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(f"fake {name}")
    (root / "Readme.txt").write_text("v9.99 1st January 2030\n")
    return root


def test_locate_sdk_from_env(fake_sdk: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("STEAMWORKS_SDK_PATH", str(fake_sdk))
    assert locate_sdk() == fake_sdk

    shutil.rmtree(fake_sdk / "redistributable_bin")
    with pytest.raises(SdkError, match="missing redistributable_bin/"):
        locate_sdk()


def test_check_detects_modified_json(fake_sdk: Path, tmp_path: Path) -> None:
    lock_path = tmp_path / "sdk.lock"
    write_lock(compute_lock(fake_sdk), lock_path)
    assert check_sdk(fake_sdk, lock_path) == []

    (fake_sdk / JSON_PATH).write_text("{}")
    assert check_sdk(fake_sdk, lock_path) == [f"{JSON_PATH}: sha256 differs from sdk.lock"]
