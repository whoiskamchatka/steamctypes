"""Emit the raw ctypes layer in src/steamctypes/_generated from the IR."""

import keyword
import re
import shutil
import subprocess
import sys
from collections import Counter
from collections.abc import Callable, Iterable, Iterator, Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from tools.generator.ctype import named_types
from tools.generator.model import (
    Api,
    Array,
    CType,
    Function,
    FunctionPointer,
    Named,
    NamedKind,
    Pack,
    Pointer,
    Primitive,
    Union,
)
from tools.sdk import REDIST_DIR, REPO_ROOT, Lock

OUTPUT_DIR = REPO_ROOT / "src" / "steamctypes" / "_generated"

_CTYPES = {
    "bool": "ctypes.c_bool",
    "char": "ctypes.c_char",
    "signed char": "ctypes.c_byte",
    "unsigned char": "ctypes.c_ubyte",
    "short": "ctypes.c_short",
    "unsigned short": "ctypes.c_ushort",
    "int": "ctypes.c_int",
    "unsigned int": "ctypes.c_uint",
    "long long": "ctypes.c_longlong",
    "unsigned long long": "ctypes.c_ulonglong",
    "float": "ctypes.c_float",
    "double": "ctypes.c_double",
    "int8_t": "ctypes.c_int8",
    "uint8_t": "ctypes.c_uint8",
    "int16_t": "ctypes.c_int16",
    "uint16_t": "ctypes.c_uint16",
    "int32_t": "ctypes.c_int32",
    "uint32_t": "ctypes.c_uint32",
    "int64_t": "ctypes.c_int64",
    "uint64_t": "ctypes.c_uint64",
    "intptr_t": "ctypes.c_ssize_t",
    "uintptr_t": "ctypes.c_size_t",
    "size_t": "ctypes.c_size_t",
}
_NOT_IDENTIFIER = re.compile(r"\W")


class EmitError(ValueError):
    pass


def identifier(name: str) -> str:
    """The Python name for an SDK name: scopes joined with "_", keywords get a trailing "_"."""
    result = _NOT_IDENTIFIER.sub("_", name.replace("::", "_"))
    if result[:1].isdigit():
        result = f"_{result}"
    return f"{result}_" if keyword.iskeyword(result) else result


def _check_unique(names: Iterable[str], what: str) -> None:
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    if duplicates:
        raise EmitError(f"{what} would be defined more than once: {', '.join(duplicates)}")


def _dependency_order(names: list[str], depends: Mapping[str, Iterable[str]]) -> list[str]:
    """Names ordered so that each comes after its dependencies, otherwise keeping their order."""
    ordered: list[str] = []
    done: set[str] = set()
    visiting: set[str] = set()

    def visit(name: str) -> None:
        if name in done:
            return
        if name in visiting:
            raise EmitError(f"{name} contains itself")
        visiting.add(name)
        for dependency in depends.get(name, ()):
            visit(dependency)
        visiting.discard(name)
        done.add(name)
        ordered.append(name)

    for name in names:
        visit(name)
    return ordered


@dataclass(frozen=True)
class _Refs:
    """How one generated module refers to typedefs, structs and array-length constants."""

    typedefs: str
    structs: str | None  # None where structs are unavailable
    constants: Mapping[str, int]

    def expression(self, ctype: CType) -> str:
        match ctype:
            case Primitive(name="void"):
                raise EmitError("void is only valid as a return type or pointer target")
            case Primitive(name=name):
                return _CTYPES[name]
            case Named(name=name, kind=NamedKind.TYPEDEF):
                return self.typedefs + identifier(name)
            case Named(kind=NamedKind.ENUM):
                return "ctypes.c_int"
            case Named(name=name, kind=NamedKind.STRUCT) if self.structs is not None:
                return self.structs + identifier(name)
            case Named(name=name, kind=kind):
                raise EmitError(f"{name} ({kind}) cannot be used by value here")
            case Pointer(target=Primitive(name="char")):
                return "ctypes.c_char_p"
            case Pointer(target=Primitive(name="void")):
                return "ctypes.c_void_p"
            case Pointer(target=Named(kind=NamedKind.INTERFACE | NamedKind.OPAQUE)):
                return "ctypes.c_void_p"
            case Pointer(target=target):
                return f"ctypes.POINTER({self.expression(target)})"
            case Array(element=element, length=length):
                return f"{self.expression(element)} * {self.length(length)}"
            case FunctionPointer():
                return "ctypes.c_void_p"
            case Union():
                raise EmitError("unions are only valid as struct fields")

    def returns(self, ctype: CType) -> str:
        return "None" if ctype == Primitive("void") else self.expression(ctype)

    def field(self, ctype: CType) -> str:
        # Pointers in structs point into memory Steam owns. As c_void_p they are read explicitly
        # and losslessly; c_char_p would dereference on every access and stop at a zero byte.
        if isinstance(ctype, Pointer):
            return "ctypes.c_void_p"
        if isinstance(ctype, Array):
            return f"{self.field(ctype.element)} * {self.length(ctype.length)}"
        return self.expression(ctype)

    def length(self, length: int | str) -> int:
        return length if isinstance(length, int) else self.constants[length]


def _by_value_structs(ctype: CType) -> Iterator[str]:
    match ctype:
        case Named(name=name, kind=NamedKind.STRUCT):
            yield identifier(name)
        case Array(element=element):
            yield from _by_value_structs(element)
        case _:
            pass


def _tuple(items: list[str]) -> str:
    return f"({items[0]},)" if len(items) == 1 else f"({', '.join(items)})"


def _module(imports: list[str], siblings: list[str], body: list[str]) -> str:
    """A module that imports the sibling modules its body refers to."""
    text = "\n".join(body)
    used = [name for name in siblings if f"{name}." in text]
    local = ["", f"from . import {', '.join(used)}"] if used else []
    # isort puts two blank lines after the imports before a class, one otherwise.
    gap = ["", ""] if text.startswith("class ") else [""]
    return "\n".join([*imports, *local, *gap, text, ""])


def _constants_module(api: Api) -> str:
    # Top-level constants first, then the ones nested in structs.
    constants = sorted(api.constants, key=lambda c: c.scope is not None)
    values: list[tuple[str, int | float | None]] = [
        (identifier(c.qualified_name), c.value) for c in constants
    ]
    values += [(identifier(m.name), m.value) for m in api.macros]
    _check_unique((name for name, _ in values), "constants")
    lines: list[str] = []
    for name, value in values:
        if value is None:
            raise EmitError(f"constant {name} has not been evaluated")
        lines.append(f"{name}: Final[{type(value).__name__}] = {value!r}")
    return _module(["from typing import Final"], [], lines)


def _enums_module(api: Api) -> str:
    _check_unique((identifier(e.qualified_name) for e in api.enums), "enums")
    lines: list[str] = []
    for enum in api.enums:
        members = [identifier(v.name) for v in enum.values]
        _check_unique(members, f"members of {enum.qualified_name}")
        base = "IntFlag" if enum.flags else "IntEnum"
        lines.append(f"class {identifier(enum.qualified_name)}({base}):")
        lines += [
            f"    {member} = {v.value}" for member, v in zip(members, enum.values, strict=True)
        ]
        lines += [] if members else ["    pass"]
        lines += ["", ""]
    bases = sorted({"IntFlag" if e.flags else "IntEnum" for e in api.enums})
    return _module([f"from enum import {', '.join(bases)}"] if bases else [], [], lines)


def _typedefs_module(api: Api, constants: Mapping[str, int]) -> str:
    refs = _Refs("", None, constants)
    by_name = {t.name: t for t in api.typedefs}
    depends = {
        t.name: [n.name for n in named_types(t.type) if n.kind is NamedKind.TYPEDEF]
        for t in api.typedefs
    }
    order = _dependency_order(list(by_name), depends)
    _check_unique((identifier(name) for name in order), "typedefs")
    lines = [f"{identifier(name)} = {refs.expression(by_name[name].type)}" for name in order]
    return _module(["import ctypes"], [], lines)


@dataclass(frozen=True)
class _Class:
    name: str
    base: str  # "Structure" or "Union"
    pack: Pack
    fields: tuple[tuple[str, str], ...]
    depends: tuple[str, ...]  # classes this one contains by value
    anonymous: tuple[str, ...] = ()
    callback_id: int | None = None


def _struct_classes(api: Api, refs: _Refs) -> list[_Class]:
    classes: list[_Class] = []
    for struct in api.structs:
        name = identifier(struct.qualified_name)
        fields: list[tuple[str, str]] = []
        depends: list[str] = []
        anonymous: list[str] = []
        for field in struct.fields:
            if isinstance(field.type, Union):
                field_name = "_union" if field.name is None else identifier(field.name)
                union_name = f"{name}_{field_name.lstrip('_')}"
                if any(m.name is None for m in field.type.members):
                    raise EmitError(f"{struct.qualified_name} has an unnamed union member")
                members = tuple(
                    (identifier(m.name or ""), refs.field(m.type)) for m in field.type.members
                )
                member_depends = tuple(
                    d for m in field.type.members for d in _by_value_structs(m.type)
                )
                classes.append(_Class(union_name, "Union", struct.pack, members, member_depends))
                if field.name is None:
                    anonymous.append(field_name)
                fields.append((field_name, union_name))
                depends.append(union_name)
            elif field.name is None:
                raise EmitError(f"{struct.qualified_name} has an unnamed field that is not a union")
            else:
                fields.append((identifier(field.name), refs.field(field.type)))
                depends += _by_value_structs(field.type)
        if struct.is_empty:
            fields = [("_padding", "ctypes.c_ubyte")]  # C++ gives an empty struct size 1
        _check_unique((f for f, _ in fields), f"fields of {struct.qualified_name}")
        classes.append(
            _Class(
                name,
                "Structure",
                struct.pack,
                tuple(fields),
                tuple(depends),
                tuple(anonymous),
                struct.callback_id,
            )
        )
    _check_unique((c.name for c in classes), "structs and unions")
    return classes


def _structs_module(api: Api, constants: Mapping[str, int]) -> str:
    classes = _struct_classes(api, _Refs("typedefs.", "", constants))
    platform = any(c.pack is Pack.PLATFORM for c in classes)
    lines = (
        [
            "# Steam packs most structs to 8 bytes on Windows and 4 elsewhere. _layout_ 'ms' makes",
            "# ctypes honour _pack_ the same way on every OS.",
            '_PLATFORM_PACK = 8 if sys.platform == "win32" else 4',
            "",
            "",
        ]
        if platform
        else []
    )
    for cls in classes:
        body: list[str] = []
        if cls.pack is not Pack.NATURAL:
            body += [
                f"_pack_ = {1 if cls.pack is Pack.ONE else '_PLATFORM_PACK'}",
                '_layout_ = "ms"',
            ]
        if cls.anonymous:
            body.append(f"_anonymous_ = {cls.anonymous!r}")
        if cls.callback_id is not None:
            body.append(f"k_iCallback = {cls.callback_id}")
        lines += [f"class {cls.name}(ctypes.{cls.base}):", *(f"    {b}" for b in body or ["pass"])]
        lines += ["", ""]
    by_name = {c.name: c for c in classes}
    for name in _dependency_order(list(by_name), {c.name: c.depends for c in classes}):
        fields = ", ".join(
            f"({field!r}, {expression})" for field, expression in by_name[name].fields
        )
        lines.append(f"{name}._fields_ = [{fields}]")
    return _module(["import ctypes", *(["import sys"] if platform else [])], ["typedefs"], lines)


def _callbacks_module(api: Api) -> str:
    by_id: dict[int, list[str]] = {}
    layouts: dict[int, set[tuple[object, ...]]] = {}
    # User structs first: a sorted() key of False puts them before the game server ones.
    callbacks = sorted(api.callbacks, key=lambda s: s.name in api.game_server_callbacks)
    for struct in callbacks:
        assert struct.callback_id is not None
        by_id.setdefault(struct.callback_id, []).append(identifier(struct.qualified_name))
        layouts.setdefault(struct.callback_id, set()).add(
            (struct.pack, *(f.type for f in struct.fields))
        )
    shared = [str(i) for i, variants in sorted(layouts.items()) if len(variants) > 1]
    if shared:
        raise EmitError(
            f"callback ids shared by structs with different layouts: {', '.join(shared)}"
        )
    entries = [
        f"{callback_id}: {_tuple([f'structs.{n}' for n in names])}"
        for callback_id, names in sorted(by_id.items())
    ]
    lines = [
        "# Every id maps to a tuple. An id shared by a user and a game server struct lists the",
        "# user struct first; both have the same layout.",
        "CALLBACKS: Final[Mapping[int, tuple[type[ctypes.Structure], ...]]] = {"
        + ", ".join(entries)
        + "}",
    ]
    return _module(
        ["import ctypes", "from collections.abc import Mapping", "from typing import Final"],
        ["structs"],
        lines,
    )


def _prototype(function: Function, this: str | None, refs: _Refs) -> tuple[str, str, list[str]]:
    args = [*([this] if this else []), *(refs.expression(p.type) for p in function.params)]
    return function.flat_name, refs.returns(function.returns), args


def _functions_module(api: Api, constants: Mapping[str, int]) -> str:
    refs = _Refs("typedefs.", "structs.", constants)
    prototypes = [_prototype(f, None, refs) for f in api.global_functions]
    for interface in api.interfaces:
        prototypes += [(a.flat_name, "ctypes.c_void_p", []) for a in interface.accessors]
        prototypes += [_prototype(m, "ctypes.c_void_p", refs) for m in interface.methods]
    for struct in api.structs:
        this = f"ctypes.POINTER(structs.{identifier(struct.qualified_name)})"
        prototypes += [_prototype(m, this, refs) for m in struct.methods]
    _check_unique((name for name, _, _ in prototypes), "prototypes")

    entries = [f"{name!r}: ({restype}, {_tuple(args)})" for name, restype, args in prototypes]
    accessors = [
        f'"{i.name}": {_mapping((a.kind.value, a.flat_name) for a in i.accessors)}'
        for i in sorted(api.interfaces, key=lambda i: i.name)
        if i.accessors
    ]
    lines = [
        "# restype and argtypes of every global function, flat function and interface accessor.",
        "# Interface and struct methods take the object pointer as their first argument.",
        "Prototype = tuple[type[Any] | None, tuple[type[Any], ...]]",
        "",
        "PROTOTYPES: Final[Mapping[str, Prototype]] = {" + ", ".join(entries) + "}",
        "# The accessor of each interface by kind: user, gameserver or global.",
        "ACCESSORS: Final[Mapping[str, Mapping[str, str]]] = {" + ", ".join(accessors) + "}",
    ]
    return _module(
        ["import ctypes", "from collections.abc import Mapping", "from typing import Any, Final"],
        ["structs", "typedefs"],
        lines,
    )


def _format(source: str, path: Path) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", "--stdin-filename", str(path), "-"],
        input=source.encode(),
        capture_output=True,
        cwd=REPO_ROOT,
        check=False,
    )
    if result.returncode != 0:
        raise EmitError(f"ruff format failed on {path.name}:\n{result.stderr.decode()}")
    return result.stdout.decode()


def _mapping(items: Iterable[tuple[str, str]]) -> str:
    return "{" + ", ".join(f'"{key}": "{value}"' for key, value in sorted(items)) + "}"


def _init_module(api: Api, lock: Lock) -> str:
    libraries = [
        (PurePosixPath(path).parent.name, digest)
        for path, digest in lock.sha256.items()
        if path.startswith(f"{REDIST_DIR}/")
    ]
    versions = {i.name: i.version for i in api.interfaces}
    init_versions = [f'"{versions[name]}"' for name in api.init_interfaces]
    lines = [
        f'SDK_VERSION: Final = "{lock.version}"',
        "# sha256 of the SDK's steam_api library, by its redistributable_bin folder.",
        f"LIBRARY_SHA256: Final[Mapping[str, str]] = {_mapping(libraries)}",
        "# The interface versions init asks the Steam client to support, in the SDK's order.",
        f"INIT_INTERFACE_VERSIONS: Final[tuple[str, ...]] = {_tuple(init_versions)}",
    ]
    return _module(["from collections.abc import Mapping", "from typing import Final"], [], lines)


def generate(api: Api, lock: Lock) -> dict[str, str]:
    """Every generated file name with its formatted source."""
    constants = {c.qualified_name: c.value for c in api.constants if isinstance(c.value, int)}
    constants |= {m.name: m.value for m in api.macros}
    emitters: dict[str, Callable[[], str]] = {
        "__init__.py": lambda: _init_module(api, lock),
        "callbacks.py": lambda: _callbacks_module(api),
        "constants.py": lambda: _constants_module(api),
        "enums.py": lambda: _enums_module(api),
        "functions.py": lambda: _functions_module(api, constants),
        "structs.py": lambda: _structs_module(api, constants),
        "typedefs.py": lambda: _typedefs_module(api, constants),
    }
    header = f"# Generated from Steamworks SDK {lock.version} by tools/generator. Do not edit.\n"
    return {name: _format(header + emit(), OUTPUT_DIR / name) for name, emit in emitters.items()}


def write_files(files: Mapping[str, str], directory: Path) -> None:
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True)
    for name, source in files.items():
        (directory / name).write_text(source, encoding="utf-8", newline="\n")


def compare_files(files: Mapping[str, str], directory: Path) -> list[str]:
    """Describe every difference between the generated files and the directory; empty if none."""
    on_disk: set[str] = set()
    if directory.is_dir():
        on_disk = {p.name for p in directory.iterdir() if p.is_file()}
    problems = [f"{name}: missing" for name in sorted(files.keys() - on_disk)]
    problems += [f"{name}: not generated" for name in sorted(on_disk - files.keys())]
    problems += [
        f"{name}: differs"
        for name in sorted(files.keys() & on_disk)
        if (directory / name).read_bytes() != files[name].encode()
    ]
    return problems
