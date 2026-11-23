import copy
from typing import Any

import pytest

from tools.generator.constants import evaluate
from tools.generator.ctype import TypeResolver, UnknownTypesError, parse_type
from tools.generator.load import build_api
from tools.generator.model import (
    Accessor,
    AccessorKind,
    Annotation,
    AnnotationKind,
    Api,
    Array,
    Constant,
    Enum,
    EnumValue,
    Field,
    Function,
    FunctionPointer,
    Interface,
    Named,
    NamedKind,
    Param,
    Pointer,
    Primitive,
    Struct,
    Typedef,
)
from tools.generator.overrides import OverrideError
from tools.generator.parser import SchemaError, parse_api

FIXTURE: dict[str, Any] = {
    "callback_structs": [
        {
            "callback_id": 4201,
            "fields": [{"fieldname": "m_nWidgets", "fieldtype": "uint32"}],
            "struct": "WidgetsCounted_t",
        }
    ],
    "consts": [
        {"constname": "k_nLow", "consttype": "uint32", "constval": "7"},
        {"constname": "k_nTag", "consttype": "uint32", "constval": "( uint32 ) 'w' << 8 | k_nLow"},
    ],
    "enums": [
        {
            "enumname": "EWidgetColor",
            "values": [
                {"name": "k_EWidgetColorRed", "value": "1"},
                {"name": "k_EWidgetColorBlue", "value": "2"},
            ],
        }
    ],
    "interfaces": [
        {
            "accessors": [
                {"kind": "user", "name": "SteamWidgets", "name_flat": "SteamAPI_SteamWidgets_v001"}
            ],
            "classname": "ISteamWidgets",
            "fields": [],
            "methods": [
                {
                    "callresult": "WidgetsCounted_t",
                    "methodname": "CountWidgets",
                    "methodname_flat": "SteamAPI_ISteamWidgets_CountWidgets",
                    "params": [
                        {
                            "paramname": "pchName",
                            "paramtype": "char *",
                            "out_string_count": "cchName",
                        },
                        {"paramname": "cchName", "paramtype": "int"},
                        {"paramname": "eColor", "paramtype": "EWidgetColor"},
                    ],
                    "returntype": "SteamAPICall_t",
                }
            ],
            "version_string": "SteamWidgets001",
        }
    ],
    "structs": [],
    "typedefs": [
        {"typedef": "uint32", "type": "unsigned int"},
        {"typedef": "SteamAPICall_t", "type": "unsigned long long"},
    ],
}


def test_fixture_parses_into_ir() -> None:
    uint32 = Named("uint32", NamedKind.TYPEDEF)
    count_widgets = Function(
        name="CountWidgets",
        flat_name="SteamAPI_ISteamWidgets_CountWidgets",
        params=(
            Param(
                "pchName",
                Pointer(Primitive("char")),
                (Annotation(AnnotationKind.OUT_STRING_COUNT, "cchName"),),
            ),
            Param("cchName", Primitive("int")),
            Param("eColor", Named("EWidgetColor", NamedKind.ENUM)),
        ),
        returns=Named("SteamAPICall_t", NamedKind.TYPEDEF),
        call_result="WidgetsCounted_t",
    )
    assert build_api(FIXTURE, {"not_init_interfaces": ["ISteamWidgets"]}) == Api(
        interfaces=(
            Interface(
                name="ISteamWidgets",
                version="SteamWidgets001",
                accessors=(
                    Accessor(AccessorKind.USER, "SteamWidgets", "SteamAPI_SteamWidgets_v001"),
                ),
                methods=(count_widgets,),
            ),
        ),
        structs=(
            Struct("WidgetsCounted_t", None, (Field("m_nWidgets", uint32),), callback_id=4201),
        ),
        enums=(
            Enum(
                "EWidgetColor",
                None,
                (EnumValue("k_EWidgetColorRed", 1), EnumValue("k_EWidgetColorBlue", 2)),
            ),
        ),
        constants=(
            Constant("k_nLow", None, uint32, "7", 7),
            Constant("k_nTag", None, uint32, "( uint32 ) 'w' << 8 | k_nLow", ord("w") << 8 | 7),
        ),
        typedefs=(
            Typedef("uint32", Primitive("unsigned int")),
            Typedef("SteamAPICall_t", Primitive("unsigned long long")),
        ),
    )


def test_unknown_json_key_fails() -> None:
    data = copy.deepcopy(FIXTURE)
    data["interfaces"][0]["methods"][0]["newkey"] = True
    with pytest.raises(SchemaError, match=r"methods\[CountWidgets\]: unknown key 'newkey'"):
        parse_api(data)


def test_type_mapper() -> None:
    kinds = {
        "uint32": NamedKind.TYPEDEF,
        "CSteamID": NamedKind.STRUCT,
        "EWidgetColor": NamedKind.ENUM,
        "Widget_t": NamedKind.STRUCT,
    }
    widget = Named("Widget_t", NamedKind.STRUCT)
    expected = {
        "const char *": Pointer(Primitive("char"), const=True),
        "uint32 *": Pointer(Named("uint32", NamedKind.TYPEDEF)),
        "char [128]": Array(Primitive("char"), 128),
        "char [k_cchName]": Array(Primitive("char"), "k_cchName"),
        "void (*)(Widget_t *, int)": FunctionPointer(
            Primitive("void"), (Pointer(widget), Primitive("int"))
        ),
        "CSteamID": Named("CSteamID", NamedKind.STRUCT),
        "EWidgetColor": Named("EWidgetColor", NamedKind.ENUM),
        "const Widget_t *": Pointer(widget, const=True),
    }
    resolver = TypeResolver(kinds, {"k_cchName"})
    for text, ctype in expected.items():
        assert resolver.resolve(parse_type(text), text) == ctype
    resolver.check()

    resolver.resolve(parse_type("Gadget_t *"), "a field")
    resolver.resolve(parse_type("EGizmo"), "a parameter")
    with pytest.raises(
        UnknownTypesError, match=r"(?s)type EGizmo, used in a parameter.*type Gadget_t"
    ):
        resolver.check()


def test_constant_evaluator() -> None:
    names = {"k_nLow": 7}.get
    int_types = {"uint32": (32, False), "uint8": (8, False)}.get
    assert evaluate("( ( uint32 ) 'd' << 16U ) | k_nLow", names, int_types) == (100 << 16) | 7
    assert evaluate("( uint8 ) ~ 0", names, int_types) == 0xFF


def test_override_for_missing_name_fails() -> None:
    with pytest.raises(OverrideError, match=r"no enum EGizmoFlags in steam_api\.json"):
        build_api(FIXTURE, {"flag_enums": ["EGizmoFlags"]})
