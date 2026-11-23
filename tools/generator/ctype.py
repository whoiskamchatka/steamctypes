"""Parse the C type strings in steam_api.json and resolve the names they refer to."""

import re
from collections import defaultdict
from collections.abc import Collection, Iterator, Mapping
from dataclasses import replace

from tools.generator.model import (
    Array,
    CType,
    FunctionPointer,
    Named,
    NamedKind,
    Pointer,
    Primitive,
    Union,
)

# Bits and signedness. steamctypes only supports 64-bit platforms.
INTEGER_TYPES: dict[str, tuple[int, bool]] = {
    "char": (8, True),
    "signed char": (8, True),
    "unsigned char": (8, False),
    "short": (16, True),
    "unsigned short": (16, False),
    "int": (32, True),
    "unsigned int": (32, False),
    "long long": (64, True),
    "unsigned long long": (64, False),
    "int8_t": (8, True),
    "uint8_t": (8, False),
    "int16_t": (16, True),
    "uint16_t": (16, False),
    "int32_t": (32, True),
    "uint32_t": (32, False),
    "int64_t": (64, True),
    "uint64_t": (64, False),
    "intptr_t": (64, True),
    "uintptr_t": (64, False),
    "size_t": (64, False),
}
PRIMITIVES = frozenset({"void", "bool", "float", "double", *INTEGER_TYPES})

_NAME = re.compile(r"[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*")
_FUNCTION_POINTER = re.compile(r"(?P<returns>.+?)\(\s*\*\s*\)\s*\((?P<params>.*)\)")
_ARRAY = re.compile(r"(?P<element>.+?)\[\s*(?P<length>\w+(?:::\w+)*)\s*\]")


class TypeSyntaxError(ValueError):
    pass


class UnknownTypesError(ValueError):
    pass


def _strip_const(text: str) -> tuple[str, bool]:
    words = text.split()
    rest = [w for w in words if w != "const"]
    return " ".join(rest), len(rest) != len(words)


def parse_type(text: str) -> CType:
    text = " ".join(text.split())
    if match := _FUNCTION_POINTER.fullmatch(text):
        params = match["params"].strip()
        args = () if params in ("", "void") else tuple(map(parse_type, params.split(",")))
        return FunctionPointer(parse_type(match["returns"]), args)
    if match := _ARRAY.fullmatch(text):
        length = match["length"]
        return Array(parse_type(match["element"]), int(length) if length.isdigit() else length)
    if text.endswith(("*", "&")):
        target = text[:-1].strip()
        const = False
        if not target.endswith("*"):
            target, const = _strip_const(target)
        return Pointer(parse_type(target), const=const, reference=text.endswith("&"))
    # A const value type behaves like the plain type when passed or stored.
    base, _ = _strip_const(text)
    if base in PRIMITIVES:
        return Primitive(base)
    if _NAME.fullmatch(base):
        return Named(base)
    raise TypeSyntaxError(f"cannot parse C type {text!r}")


def named_types(ctype: CType) -> Iterator[Named]:
    match ctype:
        case Primitive():
            pass
        case Named():
            yield ctype
        case Pointer(target=target):
            yield from named_types(target)
        case Array(element=element):
            yield from named_types(element)
        case FunctionPointer(returns=returns, params=params):
            yield from named_types(returns)
            for param in params:
                yield from named_types(param)
        case Union(members=members):
            for member in members:
                yield from named_types(member.type)


def array_lengths(ctype: CType) -> Iterator[str]:
    """Names of the constants that size arrays inside ctype."""
    match ctype:
        case Primitive() | Named():
            pass
        case Pointer(target=target):
            yield from array_lengths(target)
        case Array(element=element, length=length):
            if isinstance(length, str):
                yield length
            yield from array_lengths(element)
        case FunctionPointer(returns=returns, params=params):
            for part in (returns, *params):
                yield from array_lengths(part)
        case Union(members=members):
            for member in members:
                yield from array_lengths(member.type)


class TypeResolver:
    """Resolves names to their kind and collects every unknown one for a single error."""

    def __init__(self, kinds: Mapping[str, NamedKind], constants: Collection[str]) -> None:
        self.kinds = kinds
        self.constants = constants
        self.unknown: defaultdict[str, list[str]] = defaultdict(list)

    def resolve(self, ctype: CType, where: str) -> CType:
        match ctype:
            case Primitive():
                return ctype
            case Named(name=name):
                kind = self.kinds.get(name)
                if kind is None:
                    self.unknown[f"type {name}"].append(where)
                    return ctype
                return Named(name, kind)
            case Pointer(target=target):
                return replace(ctype, target=self.resolve(target, where))
            case Array(element=element, length=length):
                if isinstance(length, str) and length not in self.constants:
                    self.unknown[f"constant {length}"].append(where)
                return replace(ctype, element=self.resolve(element, where))
            case FunctionPointer(returns=returns, params=params):
                return FunctionPointer(
                    self.resolve(returns, where), tuple(self.resolve(p, where) for p in params)
                )
            case Union(members=members):
                return Union(tuple(replace(m, type=self.resolve(m.type, where)) for m in members))

    def check(self) -> None:
        if not self.unknown:
            return
        lines = [
            f"  {name}, used in {', '.join(places[:3])}{', ...' if len(places) > 3 else ''}"
            for name, places in sorted(self.unknown.items())
        ]
        raise UnknownTypesError(f"{len(lines)} unknown names:\n" + "\n".join(lines))
