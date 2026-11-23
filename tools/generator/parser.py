"""Turn steam_api.json into the IR, rejecting every key it does not know."""

from collections.abc import Collection, Mapping
from typing import Any, cast

from tools.generator import constants
from tools.generator.ctype import TypeSyntaxError, parse_type
from tools.generator.model import (
    Accessor,
    AccessorKind,
    Annotation,
    AnnotationKind,
    Api,
    Constant,
    CType,
    Enum,
    EnumValue,
    Field,
    Function,
    Interface,
    Param,
    Primitive,
    SizeCall,
    Struct,
    Typedef,
    qualify,
)

# Free-text documentation in the SDK. Deliberately never read.
IGNORED_PARAM_KEYS = frozenset({"desc"})
ANNOTATION_KEYS = frozenset(kind.value for kind in AnnotationKind)
_SIZELESS = frozenset({AnnotationKind.OUT_STRING, AnnotationKind.OUT_STRUCT})


class SchemaError(ValueError):
    pass


def _no_names(_: str) -> None:
    return None


class _Parser:
    def __init__(self) -> None:
        self.problems: list[str] = []
        self.enums: list[Enum] = []
        self.constants: list[Constant] = []

    def read_object(
        self,
        value: object,
        path: str,
        required: Collection[str],
        optional: Collection[str] = (),
        ignored: Collection[str] = (),
    ) -> dict[str, Any]:
        if not isinstance(value, dict):
            raise SchemaError(f"{path}: expected an object")
        obj = cast(dict[str, Any], value)
        missing = sorted(set(required) - obj.keys())
        if missing:
            raise SchemaError(f"{path}: missing {', '.join(map(repr, missing))}")
        known = {*required, *optional, *ignored}
        self.problems += [f"{path}: unknown key {key!r}" for key in sorted(obj.keys() - known)]
        return obj

    def items(self, value: object, path: str) -> list[object]:
        if not isinstance(value, list):
            raise SchemaError(f"{path}: expected a list")
        return cast(list[object], value)

    def text(self, obj: Mapping[str, Any], key: str, path: str) -> str:
        value = obj[key]
        if not isinstance(value, str):
            raise SchemaError(f"{path}.{key}: expected a string")
        return value

    def ctype(self, text: str, path: str) -> CType:
        try:
            return parse_type(text)
        except TypeSyntaxError as error:
            self.problems.append(f"{path}: {error}")
            return Primitive("void")

    def api(self, data: object) -> Api:
        top = self.read_object(
            data,
            "steam_api.json",
            {"callback_structs", "consts", "enums", "interfaces", "structs", "typedefs"},
        )
        typedefs = [
            self.typedef(t, f"typedefs[{i}]")
            for i, t in enumerate(self.items(top["typedefs"], "typedefs"))
        ]
        structs = [
            self.struct(s, "structs", callback=False) for s in self.items(top["structs"], "structs")
        ]
        structs += [
            self.struct(s, "callback_structs", callback=True)
            for s in self.items(top["callback_structs"], "callback_structs")
        ]
        interfaces = [self.interface(i) for i in self.items(top["interfaces"], "interfaces")]
        for value in self.items(top["enums"], "enums"):
            self.enum(value, "enums", None)
        for value in self.items(top["consts"], "consts"):
            self.constant(value, "consts", None)
        return Api(
            interfaces=tuple(interfaces),
            structs=tuple(structs),
            enums=tuple(self.enums),
            constants=tuple(self.constants),
            typedefs=tuple(typedefs),
        )

    def typedef(self, value: object, path: str) -> Typedef:
        obj = self.read_object(value, path, {"typedef", "type"})
        return Typedef(
            self.text(obj, "typedef", path), self.ctype(self.text(obj, "type", path), path)
        )

    def interface(self, value: object) -> Interface:
        name = _label(value, "classname")
        path = f"interfaces[{name}]"
        obj = self.read_object(
            value,
            path,
            {"classname", "fields", "methods"},
            {"accessors", "version_string", "enums"},
        )
        if self.items(obj["fields"], f"{path}.fields"):
            self.problems.append(f"{path}: interface fields are not supported")
        for enum in self.items(obj.get("enums", []), f"{path}.enums"):
            self.enum(enum, f"{path}.enums", name)
        accessors = [
            self.accessor(a, f"{path}.accessors")
            for a in self.items(obj.get("accessors", []), f"{path}.accessors")
        ]
        version = self.text(obj, "version_string", path) if "version_string" in obj else None
        methods = [
            self.function(m, f"{path}.methods")
            for m in self.items(obj["methods"], f"{path}.methods")
        ]
        return Interface(name, version, tuple(accessors), tuple(methods))

    def accessor(self, value: object, path: str) -> Accessor:
        obj = self.read_object(value, path, {"kind", "name", "name_flat"})
        kind = self.text(obj, "kind", path)
        try:
            accessor_kind = AccessorKind(kind)
        except ValueError:
            self.problems.append(f"{path}: unknown accessor kind {kind!r}")
            accessor_kind = AccessorKind.USER
        return Accessor(
            accessor_kind, self.text(obj, "name", path), self.text(obj, "name_flat", path)
        )

    def function(self, value: object, parent: str) -> Function:
        path = f"{parent}[{_label(value, 'methodname')}]"
        obj = self.read_object(
            value,
            path,
            {"methodname", "methodname_flat", "params", "returntype"},
            {"returntype_flat", "callresult", "callback"},
        )
        returns = self.text(
            obj, "returntype_flat" if "returntype_flat" in obj else "returntype", path
        )
        params = [
            self.param(p, f"{path}.params[{i}]")
            for i, p in enumerate(self.items(obj["params"], f"{path}.params"))
        ]
        return Function(
            name=self.text(obj, "methodname", path),
            flat_name=self.text(obj, "methodname_flat", path),
            params=tuple(params),
            returns=self.ctype(returns, path),
            call_result=self.text(obj, "callresult", path) if "callresult" in obj else None,
            callback=self.text(obj, "callback", path) if "callback" in obj else None,
        )

    def param(self, value: object, path: str) -> Param:
        obj = self.read_object(
            value,
            path,
            {"paramname", "paramtype"},
            {"paramtype_flat", *ANNOTATION_KEYS},
            IGNORED_PARAM_KEYS,
        )
        type_key = "paramtype_flat" if "paramtype_flat" in obj else "paramtype"
        annotations = [
            self.annotation(AnnotationKind(key), self.text(obj, key, path), path)
            for key in sorted(obj.keys() & ANNOTATION_KEYS)
        ]
        return Param(
            self.text(obj, "paramname", path),
            self.ctype(self.text(obj, type_key, path), path),
            tuple(annotations),
        )

    def annotation(self, kind: AnnotationKind, value: str, path: str) -> Annotation:
        if kind in _SIZELESS:
            if value:
                self.problems.append(f"{path}.{kind.value}: expected an empty value")
            return Annotation(kind)
        if kind is AnnotationKind.OUT_ARRAY_CALL:
            size, *call = value.split(",")
            if not call:
                self.problems.append(f"{path}.{kind.value}: expected 'size,method,args...'")
                return Annotation(kind, size)
            return Annotation(kind, size, SizeCall(call[0], tuple(call[1:])))
        return Annotation(kind, value)

    def struct(self, value: object, parent: str, callback: bool) -> Struct:
        name = _label(value, "struct")
        path = f"{parent}[{name}]"
        if callback:
            obj = self.read_object(
                value, path, {"struct", "fields", "callback_id"}, {"consts", "enums"}
            )
        else:
            obj = self.read_object(value, path, {"struct", "fields"}, {"methods", "consts"})
        for enum in self.items(obj.get("enums", []), f"{path}.enums"):
            self.enum(enum, f"{path}.enums", name)
        for constant in self.items(obj.get("consts", []), f"{path}.consts"):
            self.constant(constant, f"{path}.consts", name)
        fields = [
            self.field(f, f"{path}.fields") for f in self.items(obj["fields"], f"{path}.fields")
        ]
        methods = [
            self.function(m, f"{path}.methods")
            for m in self.items(obj.get("methods", []), f"{path}.methods")
        ]
        callback_id = obj.get("callback_id")
        if callback and not isinstance(callback_id, int):
            raise SchemaError(f"{path}.callback_id: expected an integer")
        return Struct(name, None, tuple(fields), tuple(methods), callback_id=callback_id)

    def field(self, value: object, parent: str) -> Field:
        path = f"{parent}[{_label(value, 'fieldname')}]"
        obj = self.read_object(value, path, {"fieldname", "fieldtype"}, {"private"})
        private = obj.get("private", False)
        if not isinstance(private, bool):
            raise SchemaError(f"{path}.private: expected a boolean")
        return Field(
            self.text(obj, "fieldname", path),
            self.ctype(self.text(obj, "fieldtype", path), path),
            private,
        )

    def enum(self, value: object, parent: str, scope: str | None) -> None:
        name = _label(value, "enumname")
        path = f"{parent}[{name}]"
        if scope is None:
            obj = self.read_object(value, path, {"enumname", "values"})
        else:
            obj = self.read_object(value, path, {"enumname", "fqname", "values"})
            if self.text(obj, "fqname", path) != qualify(scope, name):
                self.problems.append(f"{path}: fqname does not match its scope {scope}")
        values: list[EnumValue] = []
        for item in self.items(obj["values"], f"{path}.values"):
            entry = self.read_object(
                item, f"{path}.values[{_label(item, 'name')}]", {"name", "value"}
            )
            text = self.text(entry, "value", path)
            try:
                number = constants.evaluate(text, _no_names, _no_names)
            except constants.ConstantError as error:
                self.problems.append(f"{path}: {error}")
                continue
            if not isinstance(number, int):
                self.problems.append(f"{path}: enum value {text!r} is not an integer")
                continue
            values.append(EnumValue(self.text(entry, "name", path), number))
        self.enums.append(Enum(name, scope, tuple(values)))

    def constant(self, value: object, parent: str, scope: str | None) -> None:
        path = f"{parent}[{_label(value, 'constname')}]"
        obj = self.read_object(value, path, {"constname", "consttype", "constval"})
        self.constants.append(
            Constant(
                name=self.text(obj, "constname", path),
                scope=scope,
                type=self.ctype(self.text(obj, "consttype", path), path),
                expression=self.text(obj, "constval", path),
            )
        )


def _label(value: object, key: str) -> str:
    """The object's name for error paths, before its keys are validated."""
    if isinstance(value, dict):
        name = cast(dict[str, Any], value).get(key)
        if isinstance(name, str):
            return name
    return "?"


def parse_api(data: Mapping[str, Any]) -> Api:
    parser = _Parser()
    api = parser.api(data)
    if parser.problems:
        raise SchemaError(
            f"{len(parser.problems)} problems in steam_api.json:\n  " + "\n  ".join(parser.problems)
        )
    return api
