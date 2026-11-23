"""Intermediate representation of the Steamworks flat API."""

import enum
from collections.abc import Callable, Iterator
from dataclasses import dataclass, replace


def qualify(scope: str | None, name: str) -> str:
    return f"{scope}::{name}" if scope else name


class NamedKind(enum.Enum):
    ENUM = "enum"
    STRUCT = "struct"
    TYPEDEF = "typedef"
    INTERFACE = "interface"
    OPAQUE = "opaque"


@dataclass(frozen=True)
class Primitive:
    name: str


@dataclass(frozen=True)
class Named:
    name: str
    kind: NamedKind | None = None  # None until types are resolved


@dataclass(frozen=True)
class Pointer:
    target: "CType"
    const: bool = False  # the pointee is const
    reference: bool = False  # a C++ reference, passed as a pointer by the flat API


@dataclass(frozen=True)
class Array:
    element: "CType"
    length: int | str  # a number or the name of a constant


@dataclass(frozen=True)
class FunctionPointer:
    returns: "CType"
    params: tuple["CType", ...]


@dataclass(frozen=True)
class Union:
    members: tuple["Field", ...]


CType = Primitive | Named | Pointer | Array | FunctionPointer | Union


@dataclass(frozen=True)
class Field:
    name: str | None  # None for an anonymous union
    type: CType
    private: bool = False


class AnnotationKind(enum.Enum):
    ARRAY_COUNT = "array_count"
    OUT_ARRAY_COUNT = "out_array_count"
    OUT_ARRAY_CALL = "out_array_call"
    OUT_STRING_COUNT = "out_string_count"
    OUT_STRING = "out_string"
    BUFFER_COUNT = "buffer_count"
    OUT_BUFFER_COUNT = "out_buffer_count"
    OUT_STRUCT = "out_struct"


@dataclass(frozen=True)
class SizeCall:
    """For out_array_call: the array size is the result of calling `method` with `args`."""

    method: str
    args: tuple[str, ...]


@dataclass(frozen=True)
class Annotation:
    kind: AnnotationKind
    size: str | None = None  # a parameter, constant or macro name
    call: SizeCall | None = None


@dataclass(frozen=True)
class Param:
    name: str
    type: CType  # as passed to the flat function
    annotations: tuple[Annotation, ...] = ()


@dataclass(frozen=True)
class Function:
    name: str  # C++ method name; overloads share it
    flat_name: str
    params: tuple[Param, ...]
    returns: CType
    call_result: str | None = None  # struct delivered through SteamAPICallCompleted_t
    callback: str | None = None  # callback struct the call posts


class AccessorKind(enum.Enum):
    USER = "user"
    GAME_SERVER = "gameserver"
    GLOBAL = "global"


@dataclass(frozen=True)
class Accessor:
    kind: AccessorKind
    name: str
    flat_name: str


@dataclass(frozen=True)
class Interface:
    name: str
    version: str | None
    accessors: tuple[Accessor, ...]
    methods: tuple[Function, ...]
    unsupported: str | None = None  # why no bindings can be generated


class Pack(enum.Enum):
    PLATFORM = "platform"  # 8 on Windows, 4 on Linux and macOS
    ONE = "1"
    NATURAL = "natural"  # declared outside any #pragma pack


@dataclass(frozen=True)
class Struct:
    name: str
    scope: str | None
    fields: tuple[Field, ...]
    methods: tuple[Function, ...] = ()
    pack: Pack = Pack.PLATFORM
    callback_id: int | None = None

    @property
    def qualified_name(self) -> str:
        return qualify(self.scope, self.name)

    @property
    def is_empty(self) -> bool:
        """C++ gives an empty struct size 1, ctypes gives it size 0."""
        return not self.fields


@dataclass(frozen=True)
class EnumValue:
    name: str
    value: int


@dataclass(frozen=True)
class Enum:
    name: str
    scope: str | None
    values: tuple[EnumValue, ...]
    flags: bool = False

    @property
    def qualified_name(self) -> str:
        return qualify(self.scope, self.name)


@dataclass(frozen=True)
class Constant:
    name: str
    scope: str | None
    type: CType
    expression: str
    value: int | float | None = None  # None until the expression is evaluated

    @property
    def qualified_name(self) -> str:
        return qualify(self.scope, self.name)


@dataclass(frozen=True)
class Macro:
    """A name the JSON refers to without defining it, with its value from the headers."""

    name: str
    value: int


@dataclass(frozen=True)
class Typedef:
    name: str
    type: CType


@dataclass(frozen=True)
class Opaque:
    """A type only ever handled through pointers."""

    name: str


@dataclass(frozen=True)
class Api:
    interfaces: tuple[Interface, ...]
    structs: tuple[Struct, ...]  # including callback structs and nested types
    enums: tuple[Enum, ...]
    constants: tuple[Constant, ...]
    typedefs: tuple[Typedef, ...]
    opaques: tuple[Opaque, ...] = ()
    macros: tuple[Macro, ...] = ()
    # Interfaces whose versions init asks the Steam client to support, in the SDK's order.
    init_interfaces: tuple[str, ...] = ()
    # Game server structs that share their callback id with a user struct.
    game_server_callbacks: tuple[str, ...] = ()

    @property
    def callbacks(self) -> tuple[Struct, ...]:
        return tuple(s for s in self.structs if s.callback_id is not None)

    def functions(self) -> Iterator[tuple[str, Function]]:
        """Every flat function with the interface or struct it belongs to."""
        for interface in self.interfaces:
            for method in interface.methods:
                yield interface.name, method
        for struct in self.structs:
            for method in struct.methods:
                yield struct.qualified_name, method


def map_types(api: Api, convert: Callable[[CType, str], CType]) -> Api:
    """Rebuild the API with every type replaced by convert(type, where it is used)."""

    def function(f: Function) -> Function:
        params = tuple(
            replace(p, type=convert(p.type, f"{f.flat_name}({p.name})")) for p in f.params
        )
        return replace(f, params=params, returns=convert(f.returns, f"{f.flat_name} return"))

    def struct(s: Struct) -> Struct:
        fields = tuple(
            replace(f, type=convert(f.type, f"{s.qualified_name}.{f.name or '<union>'}"))
            for f in s.fields
        )
        return replace(s, fields=fields, methods=tuple(map(function, s.methods)))

    return replace(
        api,
        interfaces=tuple(
            replace(i, methods=tuple(map(function, i.methods))) for i in api.interfaces
        ),
        structs=tuple(map(struct, api.structs)),
        typedefs=tuple(replace(t, type=convert(t.type, f"typedef {t.name}")) for t in api.typedefs),
        constants=tuple(
            replace(c, type=convert(c.type, f"constant {c.qualified_name}")) for c in api.constants
        ),
    )


def type_uses(api: Api) -> list[tuple[CType, str]]:
    uses: list[tuple[CType, str]] = []

    def record(ctype: CType, where: str) -> CType:
        uses.append((ctype, where))
        return ctype

    map_types(api, record)
    return uses
