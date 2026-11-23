"""Apply the hand-maintained fixes in overrides.toml to the IR."""

import contextlib
import tomllib
from collections.abc import Collection, Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any, cast

from tools.generator import constants
from tools.generator.ctype import TypeSyntaxError, array_lengths, named_types, parse_type
from tools.generator.model import (
    AnnotationKind,
    Api,
    CType,
    Field,
    Function,
    Macro,
    Opaque,
    Pack,
    Primitive,
    Struct,
    Typedef,
    Union,
    type_uses,
)

OVERRIDES_PATH = Path(__file__).with_name("overrides.toml")
SECTIONS = frozenset(
    {
        "flag_enums",
        "game_server_callbacks",
        "init_interfaces",
        "macros",
        "pack",
        "types",
        "unions",
        "annotations",
        "unsupported",
    }
)


class OverrideError(ValueError):
    pass


def load_overrides(path: Path = OVERRIDES_PATH) -> dict[str, Any]:
    with path.open("rb") as f:
        return tomllib.load(f)


def _key(value: object, key: str) -> object:
    return cast(dict[str, object], value).get(key) if isinstance(value, dict) else None


class _Applier:
    def __init__(self, api: Api) -> None:
        self.api = api
        self.problems: list[str] = []
        self.structs = {s.qualified_name: s for s in api.structs}
        self.enums = {e.qualified_name: e for e in api.enums}
        self.interfaces = {i.name: i for i in api.interfaces}
        self.defined = {
            *self.structs,
            *self.enums,
            *self.interfaces,
            *(t.name for t in api.typedefs),
        }
        self.new_structs: list[Struct] = []
        self.new_typedefs: list[Typedef] = []
        self.opaques: list[Opaque] = []
        self.macros: list[Macro] = []
        self.init_interfaces: list[str] = []
        self.game_server_callbacks: list[str] = []

    def table(
        self,
        value: object,
        where: str,
        required: Collection[str] = (),
        optional: Collection[str] = (),
    ) -> dict[str, Any] | None:
        if not isinstance(value, dict):
            self.problems.append(f"{where}: expected a table")
            return None
        table = cast(dict[str, Any], value)
        missing = set(required) - table.keys()
        unknown = table.keys() - set(required) - set(optional)
        if missing or unknown:
            self.problems += [f"{where}: missing key {key!r}" for key in sorted(missing)]
            self.problems += [f"{where}: unknown key {key!r}" for key in sorted(unknown)]
            return None
        return table

    def ctype(self, text: object, where: str) -> CType:
        try:
            if not isinstance(text, str):
                raise TypeSyntaxError(f"expected a type string, found {text!r}")
            return parse_type(text)
        except TypeSyntaxError as error:
            self.problems.append(f"{where}: {error}")
            return Primitive("void")

    def fields(self, value: object, where: str) -> tuple[Field, ...]:
        if not isinstance(value, list):
            self.problems.append(f"{where}: expected a list of fields")
            return ()
        fields: list[Field] = []
        for i, item in enumerate(cast(list[object], value)):
            entry = self.table(item, f"{where}[{i}]", {"name", "type"})
            if entry is None:
                continue
            if not isinstance(entry["name"], str):
                self.problems.append(f"{where}[{i}]: name must be a string")
            fields.append(Field(entry["name"], self.ctype(entry["type"], f"{where}[{i}]")))
        return tuple(fields)

    def pack(self, value: object, where: str) -> Pack | None:
        packs: dict[object, Pack] = {
            1: Pack.ONE,
            "natural": Pack.NATURAL,
            "platform": Pack.PLATFORM,
        }
        if isinstance(value, bool) or not isinstance(value, int | str) or value not in packs:
            self.problems.append(f"{where}: pack must be 1, 'natural' or 'platform', not {value!r}")
            return None
        return packs[value]

    def types(self, section: Mapping[str, Any]) -> None:
        for name, value in section.items():
            where = f"types.{name}"
            if name in self.defined:
                self.problems.append(f"{where}: already defined in steam_api.json")
                continue
            kind = _key(value, "kind")
            if kind == "struct":
                spec = self.table(value, where, {"kind", "pack", "fields"})
                if spec is None or (pack := self.pack(spec["pack"], where)) is None:
                    continue
                scope, _, short = name.rpartition("::")
                if scope and scope not in self.structs:
                    self.problems.append(f"{where}: no struct {scope} in steam_api.json")
                fields = self.fields(spec["fields"], f"{where}.fields")
                self.new_structs.append(Struct(short, scope or None, fields, pack=pack))
            elif kind == "alias":
                if (spec := self.table(value, where, {"kind", "type"})) is not None:
                    self.new_typedefs.append(Typedef(name, self.ctype(spec["type"], where)))
            elif kind == "opaque":
                if self.table(value, where, {"kind"}) is not None:
                    self.opaques.append(Opaque(name))
            else:
                self.problems.append(f"{where}: kind must be 'struct', 'alias' or 'opaque'")

    def packs(self, section: Mapping[str, Any]) -> None:
        for name, value in section.items():
            struct = self.structs.get(name)
            if struct is None:
                self.problems.append(f"pack.{name}: no such struct in steam_api.json")
            elif (pack := self.pack(value, f"pack.{name}")) is Pack.PLATFORM:
                self.problems.append(f"pack.{name}: 'platform' is already the default")
            elif pack is not None:
                self.structs[name] = replace(struct, pack=pack)

    def unions(self, section: Mapping[str, Any]) -> None:
        for name, value in section.items():
            where = f"unions.{name}"
            struct = self.structs.get(name)
            spec = self.table(value, where, {"replaces", "members"}, {"field"})
            if struct is None:
                self.problems.append(f"{where}: no such struct in steam_api.json")
                continue
            if spec is None:
                continue
            names = [f.name for f in struct.fields]
            if spec["replaces"] not in names:
                self.problems.append(f"{where}: {name} has no field {spec['replaces']!r}")
                continue
            index = names.index(spec["replaces"])
            union = Field(
                spec.get("field"), Union(self.fields(spec["members"], f"{where}.members"))
            )
            fields = (*struct.fields[:index], union, *struct.fields[index + 1 :])
            self.structs[name] = replace(struct, fields=fields)

    def flag_enums(self, names: object) -> None:
        if not isinstance(names, list):
            self.problems.append("flag_enums: expected a list of enum names")
            return
        for name in cast(list[Any], names):
            enum = self.enums.get(name)
            if enum is None:
                self.problems.append(f"flag_enums: no enum {name} in steam_api.json")
            elif enum.flags:
                self.problems.append(f"flag_enums: {name} is listed twice")
            else:
                self.enums[name] = replace(enum, flags=True)

    def macro_values(self, section: Mapping[str, Any]) -> None:
        json_constants = {c.qualified_name for c in self.api.constants}
        for name, value in section.items():
            if name in json_constants:
                self.problems.append(f"macros.{name}: already a constant in steam_api.json")
            elif not isinstance(value, int):
                self.problems.append(f"macros.{name}: value must be an integer")
            else:
                self.macros.append(Macro(name, value))

    def annotations(self, section: Mapping[str, Any]) -> None:
        applied: set[str] = set()

        def fix(function: Function) -> Function:
            fixes = section.get(function.flat_name)
            if fixes is None:
                return function
            applied.add(function.flat_name)
            if not isinstance(fixes, dict):
                self.problems.append(f"annotations.{function.flat_name}: expected a table")
                return function
            fixes = cast(dict[str, Any], fixes)
            params = list(function.params)
            for param_name, value in fixes.items():
                where = f"annotations.{function.flat_name}.{param_name}"
                index = next((i for i, p in enumerate(params) if p.name == param_name), None)
                values = self.table(value, where, optional=[k.value for k in AnnotationKind])
                if index is None:
                    self.problems.append(f"{where}: no such parameter")
                    continue
                for key, size in (values or {}).items():
                    param = params[index]
                    current = next((a for a in param.annotations if a.kind.value == key), None)
                    if current is None:
                        self.problems.append(f"{where}: the parameter has no {key!r} annotation")
                    elif not isinstance(size, str):
                        self.problems.append(f"{where}.{key}: must name a parameter or constant")
                    elif current.size == size:
                        self.problems.append(f"{where}.{key}: steam_api.json already says {size!r}")
                    else:
                        annotations = tuple(
                            replace(a, size=size) if a is current else a for a in param.annotations
                        )
                        params[index] = replace(param, annotations=annotations)
            return replace(function, params=tuple(params))

        for name, interface in self.interfaces.items():
            self.interfaces[name] = replace(interface, methods=tuple(map(fix, interface.methods)))
        for name, struct in self.structs.items():
            self.structs[name] = replace(struct, methods=tuple(map(fix, struct.methods)))
        self.problems += [
            f"annotations.{name}: no such method in steam_api.json"
            for name in section.keys() - applied
        ]

    def unsupported(self, section: Mapping[str, Any]) -> None:
        for name, reason in section.items():
            interface = self.interfaces.get(name)
            if interface is None:
                self.problems.append(f"unsupported.{name}: no such interface in steam_api.json")
            else:
                self.interfaces[name] = replace(interface, unsupported=str(reason))

    def init_interface_names(self, names: object) -> None:
        if not isinstance(names, list):
            self.problems.append("init_interfaces: expected a list of interface names")
            return
        for name in cast(list[Any], names):
            interface = self.interfaces.get(name)
            if interface is None:
                self.problems.append(f"init_interfaces: no interface {name} in steam_api.json")
            elif interface.version is None:
                self.problems.append(f"init_interfaces: {name} has no version string")
            elif name in self.init_interfaces:
                self.problems.append(f"init_interfaces: {name} is listed twice")
            else:
                self.init_interfaces.append(name)

    def game_server_callback_names(self, names: object) -> None:
        if not isinstance(names, list):
            self.problems.append("game_server_callbacks: expected a list of struct names")
            return
        by_id: dict[int, list[str]] = {}
        for struct in self.structs.values():
            if struct.callback_id is not None:
                by_id.setdefault(struct.callback_id, []).append(struct.name)
        for name in cast(list[Any], names):
            struct = self.structs.get(name)
            if struct is None or struct.callback_id is None:
                self.problems.append(f"game_server_callbacks: no callback struct {name}")
            elif len(by_id[struct.callback_id]) < 2:
                self.problems.append(f"game_server_callbacks: {name} shares no callback id")
            elif name in self.game_server_callbacks:
                self.problems.append(f"game_server_callbacks: {name} is listed twice")
            else:
                self.game_server_callbacks.append(name)
        for callback_id, sharing in sorted(by_id.items()):
            user = [n for n in sharing if n not in self.game_server_callbacks]
            if len(sharing) > 1 and len(user) != 1:
                self.problems.append(
                    f"game_server_callbacks: callback id {callback_id} is shared by "
                    f"{', '.join(sharing)}; list every one but the user struct"
                )

    def result(self) -> Api:
        return replace(
            self.api,
            interfaces=tuple(self.interfaces.values()),
            structs=(*self.structs.values(), *self.new_structs),
            enums=tuple(self.enums.values()),
            typedefs=(*self.api.typedefs, *self.new_typedefs),
            opaques=tuple(self.opaques),
            macros=tuple(self.macros),
            init_interfaces=tuple(self.init_interfaces),
            game_server_callbacks=tuple(self.game_server_callbacks),
        )

    def check_used(self, api: Api) -> None:
        uses = type_uses(api)
        referenced = {n.name for ctype, _ in uses for n in named_types(ctype)}
        added = [s.qualified_name for s in self.new_structs] + [t.name for t in self.new_typedefs]
        added += [o.name for o in self.opaques]
        self.problems += [
            f"types.{name}: nothing refers to it" for name in added if name not in referenced
        ]

        mentioned = {length for ctype, _ in uses for length in array_lengths(ctype)}
        for _, function in api.functions():
            mentioned |= {a.size for p in function.params for a in p.annotations if a.size}
        for constant in api.constants:
            # A malformed expression is reported when the constant is evaluated.
            with contextlib.suppress(constants.ConstantError):
                mentioned |= constants.names_in(constant.expression)
        self.problems += [
            f"macros.{m.name}: nothing refers to it" for m in self.macros if m.name not in mentioned
        ]


def apply_overrides(api: Api, overrides: Mapping[str, Any]) -> Api:
    applier = _Applier(api)
    applier.problems += [
        f"unknown section {name!r}" for name in sorted(overrides.keys() - SECTIONS)
    ]
    applier.types(overrides.get("types", {}))
    applier.packs(overrides.get("pack", {}))
    applier.unions(overrides.get("unions", {}))
    applier.flag_enums(overrides.get("flag_enums", []))
    applier.macro_values(overrides.get("macros", {}))
    applier.annotations(overrides.get("annotations", {}))
    applier.unsupported(overrides.get("unsupported", {}))
    applier.init_interface_names(overrides.get("init_interfaces", []))
    applier.game_server_callback_names(overrides.get("game_server_callbacks", []))
    result = applier.result()
    applier.check_used(result)
    if applier.problems:
        raise OverrideError(
            f"{len(applier.problems)} problems in overrides:\n  " + "\n  ".join(applier.problems)
        )
    return result
