import ctypes
import importlib
import os
import subprocess
import sys
from pathlib import Path

import pytest

from tools.generator.emit import compare_files, generate, write_files
from tools.generator.model import (
    Accessor,
    AccessorKind,
    Api,
    Array,
    Constant,
    Enum,
    EnumValue,
    Field,
    Function,
    Interface,
    Named,
    NamedKind,
    Pack,
    Param,
    Pointer,
    Primitive,
    Struct,
    Typedef,
    Union,
)
from tools.sdk import REPO_ROOT, Lock

UINT8 = Named("uint8", NamedKind.TYPEDEF)
UINT32 = Named("uint32", NamedKind.TYPEDEF)
UINT64 = Named("uint64", NamedKind.TYPEDEF)

API = Api(
    interfaces=(
        Interface(
            "ISteamWidgets",
            "SteamWidgets001",
            (Accessor(AccessorKind.USER, "SteamWidgets", "SteamAPI_SteamWidgets_v001"),),
            (
                Function(
                    "Inspect",
                    "SteamAPI_ISteamWidgets_Inspect",
                    (
                        Param("pchName", Pointer(Primitive("char"), const=True)),
                        Param("pWidget", Pointer(Named("Platform_t", NamedKind.STRUCT))),
                    ),
                    Primitive("bool"),
                ),
            ),
        ),
    ),
    structs=(
        Struct("Platform_t", None, (Field("a", UINT32), Field("b", UINT64)), callback_id=4201),
        Struct("Packed_t", None, (Field("a", UINT8), Field("b", UINT32)), pack=Pack.ONE),
        Struct("Natural_t", None, (Field("a", UINT32), Field("b", UINT64)), pack=Pack.NATURAL),
        Struct(
            "WithUnion_t",
            None,
            (
                Field(None, Union((Field("x", UINT64), Field("bytes", Array(UINT8, 12))))),
                Field("c", UINT32),
            ),
        ),
        Struct("Empty_t", None, (), callback_id=4202),
    ),
    enums=(
        Enum("EWidgetColor", None, (EnumValue("k_EWidgetColorRed", 1),)),
        Enum(
            "EWidgetFlags",
            None,
            (EnumValue("k_EWidgetFlagShiny", 1), EnumValue("k_EWidgetFlagAll", -1)),
            flags=True,
        ),
    ),
    constants=(Constant("k_cWidgetsMax", None, UINT32, "16", 16),),
    typedefs=(
        Typedef("uint8", Primitive("unsigned char")),
        Typedef("uint32", Primitive("unsigned int")),
        Typedef("uint64", Primitive("unsigned long long")),
    ),
)
LOCK = Lock("9.99", {"redistributable_bin/win64/steam_api64.dll": "0" * 64})


def test_generation_is_deterministic() -> None:
    script = (
        "import sys\n"
        "from tests.test_emit import API, LOCK\n"
        "from tools.generator.emit import generate\n"
        "sys.stdout.write(repr(sorted(generate(API, LOCK).items())))\n"
    )
    outputs = {
        subprocess.run(
            [sys.executable, "-c", script],
            cwd=REPO_ROOT,
            env={**os.environ, "PYTHONHASHSEED": seed},
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        for seed in ("1", "2")
    }
    assert len(outputs) == 1


def test_structs_have_platform_sizes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_files(generate(API, LOCK), tmp_path / "widgets_generated")
    monkeypatch.setattr(sys, "path", [str(tmp_path), *sys.path])
    structs = importlib.import_module("widgets_generated.structs")

    windows = sys.platform == "win32"
    expected = {
        "Platform_t": 16 if windows else 12,  # u32 + u64 under pack 8 or pack 4
        "Packed_t": 5,
        "Natural_t": 16,
        "WithUnion_t": 24 if windows else 16,  # union {u64, u8[12]} + u32
        "Empty_t": 1,
    }
    assert {name: ctypes.sizeof(getattr(structs, name)) for name in expected} == expected


def test_check_fails_after_a_file_is_modified(tmp_path: Path) -> None:
    files = generate(API, LOCK)
    write_files(files, tmp_path)
    assert compare_files(files, tmp_path) == []

    with (tmp_path / "structs.py").open("a", encoding="utf-8") as f:
        f.write("# edited by hand\n")
    assert compare_files(files, tmp_path) == ["structs.py: differs"]
