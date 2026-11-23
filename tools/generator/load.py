"""Build the finished IR from steam_api.json and overrides.toml."""

import json
from collections.abc import Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any

from tools.generator import constants
from tools.generator.ctype import INTEGER_TYPES, TypeResolver
from tools.generator.model import (
    Api,
    Constant,
    CType,
    Named,
    NamedKind,
    Primitive,
    map_types,
    qualify,
)
from tools.generator.overrides import apply_overrides, load_overrides
from tools.generator.parser import parse_api
from tools.sdk import JSON_PATH


class ApiError(ValueError):
    pass


def load_api(sdk_path: Path) -> Api:
    with (sdk_path / JSON_PATH).open(encoding="utf-8") as f:
        data = json.load(f)
    return build_api(data, load_overrides())


def build_api(data: Mapping[str, Any], overrides: Mapping[str, Any]) -> Api:
    api = _resolve_types(apply_overrides(parse_api(data), overrides))
    _check_references(api)
    return _evaluate_constants(api)


def _resolve_types(api: Api) -> Api:
    definitions = [(s.qualified_name, NamedKind.STRUCT) for s in api.structs]
    definitions += [(e.qualified_name, NamedKind.ENUM) for e in api.enums]
    definitions += [(t.name, NamedKind.TYPEDEF) for t in api.typedefs]
    definitions += [(i.name, NamedKind.INTERFACE) for i in api.interfaces]
    definitions += [(o.name, NamedKind.OPAQUE) for o in api.opaques]
    kinds = dict(definitions)
    if len(kinds) != len(definitions):
        names = [name for name, _ in definitions]
        duplicates = sorted({name for name in names if names.count(name) > 1})
        raise ApiError(f"defined more than once: {', '.join(duplicates)}")
    resolver = TypeResolver(
        kinds, {c.qualified_name for c in api.constants} | {m.name for m in api.macros}
    )
    api = map_types(api, resolver.resolve)
    resolver.check()
    return api


def _check_references(api: Api) -> None:
    problems: list[str] = []
    callbacks = {s.name for s in api.callbacks}
    sizes = {c.qualified_name for c in api.constants} | {m.name for m in api.macros}
    owners = [(i.name, i.methods) for i in api.interfaces] + [
        (s.qualified_name, s.methods) for s in api.structs
    ]
    for owner, methods in owners:
        method_names = {m.name for m in methods}
        for function in methods:
            for kind, name in (
                ("callresult", function.call_result),
                ("callback", function.callback),
            ):
                if name is not None and name not in callbacks:
                    problems.append(f"{function.flat_name}: {kind} {name} is not a callback struct")
            params = {p.name for p in function.params}
            for param in function.params:
                where = f"{function.flat_name}({param.name})"
                for annotation in param.annotations:
                    size = annotation.size
                    if size is not None and (size == param.name or size not in params | sizes):
                        problems.append(
                            f"{where}: {annotation.kind.value} names {size!r}, "
                            "which is neither another parameter nor a constant"
                        )
                    call = annotation.call
                    if call is not None and call.method not in method_names:
                        problems.append(f"{where}: {owner} has no method {call.method}")
                    if call is not None and not set(call.args) <= params:
                        problems.append(f"{where}: {call.method} arguments are not all parameters")
    if problems:
        raise ApiError(f"{len(problems)} broken references:\n  " + "\n  ".join(problems))


class _ConstantEvaluator:
    def __init__(self, api: Api) -> None:
        self.constants = {c.qualified_name: c for c in api.constants}
        self.macros = {m.name: m.value for m in api.macros}
        self.typedefs = {t.name: t.type for t in api.typedefs}
        self.values: dict[str, constants.Value] = {}
        self.pending: set[str] = set()

    def integer_type(self, ctype: CType) -> tuple[int, bool] | None:
        match ctype:
            case Primitive(name=name):
                return INTEGER_TYPES.get(name)
            case Named(name=name, kind=NamedKind.TYPEDEF):
                return self.integer_type(self.typedefs[name])
            case Named(kind=NamedKind.ENUM):
                return INTEGER_TYPES["int"]
            case _:
                return None

    def integer_type_named(self, name: str) -> tuple[int, bool] | None:
        if name in INTEGER_TYPES:
            return INTEGER_TYPES[name]
        if name in self.typedefs:
            return self.integer_type(self.typedefs[name])
        return None

    def value(self, constant: Constant) -> constants.Value:
        name = constant.qualified_name
        if name in self.values:
            return self.values[name]
        if name in self.pending:
            raise constants.ConstantError(f"{name} depends on itself")
        self.pending.add(name)

        def lookup(reference: str) -> constants.Value | None:
            for candidate in (qualify(constant.scope, reference), reference):
                if candidate in self.constants:
                    return self.value(self.constants[candidate])
            return self.macros.get(reference)

        try:
            raw = constants.evaluate(constant.expression, lookup, self.integer_type_named)
        finally:
            self.pending.discard(name)
        int_type = self.integer_type(constant.type)
        if int_type is not None:
            result = constants.to_int_type(raw, *int_type)
        elif constant.type in (Primitive("float"), Primitive("double")):
            result = float(raw)
        else:
            raise constants.ConstantError(f"{name} has unsupported type {constant.type}")
        self.values[name] = result
        return result


def _evaluate_constants(api: Api) -> Api:
    evaluator = _ConstantEvaluator(api)
    problems: list[str] = []
    evaluated: list[Constant] = []
    for constant in api.constants:
        try:
            evaluated.append(replace(constant, value=evaluator.value(constant)))
        except constants.ConstantError as error:
            problems.append(f"{constant.qualified_name}: {error}")
    if problems:
        raise ApiError(
            f"{len(problems)} constants could not be evaluated:\n  " + "\n  ".join(problems)
        )
    return replace(api, constants=tuple(evaluated))
