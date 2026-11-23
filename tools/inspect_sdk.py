"""Write a Markdown inventory of the local SDK's steam_api.json to build/sdk-inventory.md."""

import json
import re
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable, Sequence
from typing import Any, cast

from tools.sdk import JSON_PATH, REPO_ROOT, SdkError, file_sha256, locate_sdk, sdk_version

REPORT_PATH = REPO_ROOT / "build" / "sdk-inventory.md"

# Keys present in fewer than this share of the objects at their level are marked rare.
RARE_SHARE = 0.1

C_TYPES = frozenset(
    {
        "void",
        "bool",
        "char",
        "signed char",
        "unsigned char",
        "short",
        "unsigned short",
        "int",
        "unsigned int",
        "long long",
        "unsigned long long",
        "float",
        "double",
    }
)
STANDARD_C_TYPES = frozenset(
    {
        "size_t",
        "intptr_t",
        "uintptr_t",
        "int8_t",
        "uint8_t",
        "int16_t",
        "uint16_t",
        "int32_t",
        "uint32_t",
        "int64_t",
        "uint64_t",
    }
)
LAYOUT_WORDS = ("union", "pack", "align", "size", "offset", "bit")
PARAM_CORE_KEYS = frozenset({"paramname", "paramtype", "paramtype_flat"})
# Keys holding documentation text, which must never be copied into the report.
FREE_TEXT_KEYS = frozenset({"desc"})
TYPE_COLUMNS = ("Type", "Uses", "Where")

_QUALIFIERS = re.compile(r"\[\s*\d+\s*\]|\bconst\b|[*&]")
_ARRAY = re.compile(r"\[\s*\d+\s*\]")
_FUNCTION_POINTER = re.compile(r"(?P<ret>.+?)\s*\(\s*\*\s*\)\s*\((?P<args>.*)\)")
_IDENTIFIER = re.compile(r"[A-Za-z_]\w*")
_IDENTIFIER_LIST = re.compile(r"[A-Za-z_]\w*(?:,[A-Za-z_]\w*)+")
_INT_LITERAL = re.compile(r"-?(?:0[xX][0-9a-fA-F]+|\d+)")
_FLOAT_LITERAL = re.compile(r"-?\d+\.\d*")
_SUFFIXED_LITERAL = re.compile(r"-?(?:0[xX][0-9a-fA-F]+|\d+\.?\d*)[uUlLfF]+")
_FLAGS_NAME = re.compile(r"flags?$", re.IGNORECASE)

Obj = dict[str, Any]


class Api:
    def __init__(self, data: Obj) -> None:
        self.interfaces: list[Obj] = data["interfaces"]
        self.structs: list[Obj] = data["structs"]
        self.callbacks: list[Obj] = data["callback_structs"]
        self.typedefs: list[Obj] = data["typedefs"]
        self.methods: list[tuple[str, Obj]] = [
            (i["classname"], m) for i in self.interfaces for m in i["methods"]
        ] + [(s["struct"], m) for s in self.structs for m in s.get("methods", [])]
        self.params: list[tuple[Obj, Obj]] = [(m, p) for _, m in self.methods for p in m["params"]]
        self.fields: list[tuple[str, Obj]] = [
            (s["struct"], f) for s in self.structs + self.callbacks for f in s["fields"]
        ]
        scopes = [(i["classname"], i) for i in self.interfaces] + [
            (s["struct"], s) for s in self.structs + self.callbacks
        ]
        # Top-level enums and constants have the empty scope.
        self.enums: list[tuple[str, Obj]] = [("", e) for e in data["enums"]] + [
            (name, e) for name, o in scopes for e in o.get("enums", [])
        ]
        self.consts: list[tuple[str, Obj]] = [("", c) for c in data["consts"]] + [
            (name, c) for name, o in scopes for c in o.get("consts", [])
        ]
        self.callback_names = {c["struct"] for c in self.callbacks}
        self.struct_names = {s["struct"] for s in self.structs} | self.callback_names
        self.enum_names = {e["enumname"] for _, e in self.enums} | {
            e["fqname"] for _, e in self.enums if "fqname" in e
        }
        self.const_names = {c["constname"] for _, c in self.consts}
        self.defined_types = (
            C_TYPES
            | {t["typedef"] for t in self.typedefs}
            | self.struct_names
            | {i["classname"] for i in self.interfaces}
            | self.enum_names
        )


class Level:
    def __init__(self) -> None:
        self.objects = 0
        self.keys = Counter[str]()
        self.value_types: defaultdict[str, set[str]] = defaultdict(set)
        self.empty_lists = Counter[str]()

    def describe_values(self, key: str) -> str:
        types = ", ".join(sorted(self.value_types[key]))
        empty = self.empty_lists[key]
        return f"{types} ({empty} empty)" if empty else types


class Markdown:
    def __init__(self) -> None:
        self.lines: list[str] = []

    def heading(self, level: int, text: str) -> None:
        self.lines += [f"{'#' * level} {text}", ""]

    def para(self, text: str) -> None:
        self.lines += [text, ""]

    def table(self, headers: Sequence[str], rows: Iterable[Sequence[object]]) -> None:
        body = ["| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |" for row in rows]
        if not body:
            self.para("None.")
            return
        self.lines += ["| " + " | ".join(headers) + " |", "|" + " --- |" * len(headers), *body, ""]

    def text(self) -> str:
        return "\n".join(self.lines)


def code(value: object) -> str:
    return f"`{value}`"


def codes(values: Iterable[object]) -> str:
    return ", ".join(map(code, values)) or "none"


def first(items: Iterable[str], limit: int = 3) -> str:
    listed = list(items)
    return ", ".join(listed[:limit]) + (", ..." if len(listed) > limit else "")


def by_count(counter: Counter[str]) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))


def counts_text(counter: Counter[str]) -> str:
    return ", ".join(f"{key} ({n})" for key, n in by_count(counter))


def qualified(scope: str, name: str) -> str:
    return f"{scope}::{name}" if scope else name


def parse_int(value: object) -> int | None:
    if not isinstance(value, str):
        return None
    try:
        return int(value, 0)
    except ValueError:
        return None


def base_types(type_: str) -> list[str]:
    """Names a type string refers to, without qualifiers, pointers, references or array sizes."""
    if match := _FUNCTION_POINTER.fullmatch(type_):
        parts = [match["ret"], *match["args"].split(",")]
        return [name for part in parts for name in base_types(part)]
    name = " ".join(_QUALIFIERS.sub(" ", type_).split())
    return [name] if name else []


def type_uses(api: Api) -> list[tuple[str, str]]:
    """Every type mentioned in the JSON, paired with where it is mentioned."""
    uses: list[tuple[str, str]] = []
    for _, method in api.methods:
        name = method["methodname_flat"]
        uses.append((method["returntype"], f"{name} return"))
        if "returntype_flat" in method:
            uses.append((method["returntype_flat"], f"{name} return (flat)"))
    for method, param in api.params:
        where = f"{method['methodname_flat']}({param['paramname']})"
        uses.append((param["paramtype"], where))
        if "paramtype_flat" in param:
            uses.append((param["paramtype_flat"], f"{where} (flat)"))
    uses += [(f["fieldtype"], f"{owner}.{f['fieldname']}") for owner, f in api.fields]
    uses += [(t["type"], f"typedef {t['typedef']}") for t in api.typedefs]
    uses += [(c["consttype"], f"constant {qualified(s, c['constname'])}") for s, c in api.consts]
    return uses


def grouped(uses: Iterable[tuple[str, str]]) -> list[tuple[str, int, str]]:
    by_type: defaultdict[str, list[str]] = defaultdict(list)
    for type_, where in uses:
        by_type[type_].append(where)
    ordered = sorted(by_type.items(), key=lambda item: (-len(item[1]), item[0]))
    return [(code(type_), len(places), first(places)) for type_, places in ordered]


def collect_levels(node: object, path: str, levels: dict[str, Level]) -> None:
    if isinstance(node, list):
        for item in cast(list[object], node):
            collect_levels(item, f"{path}[]", levels)
    elif isinstance(node, dict):
        level = levels.setdefault(path, Level())
        level.objects += 1
        for key, value in cast(dict[str, object], node).items():
            level.keys[key] += 1
            level.value_types[key].add(type(value).__name__)
            if value == []:
                level.empty_lists[key] += 1
            collect_levels(value, f"{path}.{key}" if path else key, levels)


def presence(count: int, total: int) -> str:
    if count == total:
        return "all"
    share = count / total
    return f"{share:.1%} (rare)" if share < RARE_SHARE else f"{share:.1%}"


def annotation_kind(value: object, params: set[str], consts: set[str]) -> str:
    if not isinstance(value, str):
        return type(value).__name__
    if not value:
        return "empty"
    if value in params:
        return "parameter of the method"
    if value in consts:
        return "constant"
    if _IDENTIFIER.fullmatch(value):
        return "other identifier"
    if _IDENTIFIER_LIST.fullmatch(value):
        return "comma-separated identifiers"
    return "other text"


def const_kind(value: str) -> str:
    if _INT_LITERAL.fullmatch(value):
        return "integer literal"
    if _FLOAT_LITERAL.fullmatch(value):
        return "float literal"
    if _SUFFIXED_LITERAL.fullmatch(value):
        return "literal with C suffix"
    return "expression"


def write_counts(api: Api, md: Markdown) -> None:
    md.heading(2, "Counts")
    md.table(
        ["Item", "Count"],
        [
            ("interfaces", len(api.interfaces)),
            ("interface methods", sum(len(i["methods"]) for i in api.interfaces)),
            ("accessors", sum(len(i.get("accessors", [])) for i in api.interfaces)),
            ("structs", len(api.structs)),
            ("struct methods", sum(len(s.get("methods", [])) for s in api.structs)),
            ("struct fields", sum(len(s["fields"]) for s in api.structs)),
            ("callback structs", len(api.callbacks)),
            ("callback struct fields", sum(len(c["fields"]) for c in api.callbacks)),
            ("enums, top level", sum(not scope for scope, _ in api.enums)),
            ("enums, nested", sum(bool(scope) for scope, _ in api.enums)),
            ("enum values, all enums", sum(len(e["values"]) for _, e in api.enums)),
            ("constants, top level", sum(not scope for scope, _ in api.consts)),
            ("constants, nested", sum(bool(scope) for scope, _ in api.consts)),
            ("typedefs", len(api.typedefs)),
            ("method parameters", len(api.params)),
        ],
    )


def write_keys(levels: dict[str, Level], md: Markdown) -> None:
    md.heading(2, "Keys by level")
    md.para(
        f"`[]` marks array elements. Keys present in fewer than {RARE_SHARE:.0%} of the objects "
        "at their level are marked rare. Value types are Python types after JSON decoding."
    )
    for path, level in levels.items():
        noun = "object" if level.objects == 1 else "objects"
        md.heading(3, f"{code(path or '(top level)')}: {level.objects} {noun}")
        md.table(
            ["Key", "Count", "Present in", "Value types"],
            [
                (code(key), n, presence(n, level.objects), level.describe_values(key))
                for key, n in by_count(level.keys)
            ],
        )


def write_types(api: Api, md: Markdown) -> None:
    md.heading(2, "Types")
    md.heading(3, "Parameter types")
    param_types = Counter[str](p["paramtype"] for _, p in api.params)
    md.table(["Type", "Count"], [(code(t), n) for t, n in by_count(param_types)])

    md.heading(3, "Field types")
    in_structs = Counter[str](f["fieldtype"] for s in api.structs for f in s["fields"])
    in_callbacks = Counter[str](f["fieldtype"] for c in api.callbacks for f in c["fields"])
    md.table(
        ["Type", "Count", "In structs", "In callback structs"],
        [
            (code(t), n, in_structs[t], in_callbacks[t])
            for t, n in by_count(in_structs + in_callbacks)
        ],
    )

    md.heading(3, "Return types")
    return_types = Counter[str](m["returntype"] for _, m in api.methods)
    md.table(["Type", "Count"], [(code(t), n) for t, n in by_count(return_types)])

    md.heading(3, "Flat type overrides")
    overrides = Counter[tuple[str, str, str]](
        (p["paramtype"], p["paramtype_flat"], "parameter")
        for _, p in api.params
        if "paramtype_flat" in p
    )
    overrides.update(
        (m["returntype"], m["returntype_flat"], "return")
        for _, m in api.methods
        if "returntype_flat" in m
    )
    md.table(
        ["Type", "Flat type", "Used as", "Count"],
        [(code(t), code(flat), used, n) for (t, flat, used), n in sorted(overrides.items())],
    )


def write_annotations(api: Api, md: Markdown) -> None:
    md.heading(2, "Parameter annotations")
    md.para(
        f"All parameter keys except {codes(sorted(PARAM_CORE_KEYS))}. Values of "
        f"{codes(sorted(FREE_TEXT_KEYS))} are free text and are not reproduced."
    )
    uses: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    unresolved: list[tuple[str, str, str]] = []
    for method, param in api.params:
        name = method["methodname_flat"]
        param_names = {p["paramname"] for p in method["params"]}
        for key in sorted(param.keys() - PARAM_CORE_KEYS):
            kind = (
                "free text"
                if key in FREE_TEXT_KEYS
                else annotation_kind(param[key], param_names, api.const_names)
            )
            uses[key].append((name, kind))
            if kind == "other identifier":
                unresolved.append((name, key, param[key]))
    md.table(
        ["Annotation", "Count", "Value kinds", "Example methods"],
        [
            (
                code(key),
                len(entries),
                counts_text(Counter(kind for _, kind in entries)),
                first(map(code, dict.fromkeys(name for name, _ in entries))),
            )
            for key, entries in sorted(uses.items(), key=lambda item: (-len(item[1]), item[0]))
        ],
    )
    md.heading(3, "Annotation values naming neither a parameter of the method nor a constant")
    md.table(
        ["Method", "Annotation", "Value"], [(code(n), code(k), code(v)) for n, k, v in unresolved]
    )


def write_call_results(api: Api, md: Markdown) -> None:
    md.heading(2, "Async call results")
    marked = [m for _, m in api.methods if "callresult" in m]
    unmarked = [
        m["methodname_flat"]
        for _, m in api.methods
        if m["returntype"] == "SteamAPICall_t" and "callresult" not in m
    ]
    unknown = sorted({m["callresult"] for m in marked} - api.callback_names)
    md.para(
        f"{len(marked)} methods have a `callresult` key naming the result struct. "
        f"Their return types: {counts_text(Counter(m['returntype'] for m in marked))}. "
        f"`callresult` values that are not callback structs: {codes(unknown)}. "
        f"Methods returning `SteamAPICall_t` without `callresult`: {codes(unmarked)}."
    )
    md.heading(3, "Methods with a `callback` key")
    md.table(
        ["Method", "Return type", "callback"],
        [
            (code(m["methodname_flat"]), code(m["returntype"]), code(m["callback"]))
            for _, m in api.methods
            if "callback" in m
        ],
    )
    md.heading(3, "All methods with a call result")
    md.table(
        ["Method", "Result struct"],
        [(code(m["methodname_flat"]), code(m["callresult"])) for m in marked],
    )


def write_callbacks(api: Api, md: Markdown) -> None:
    md.heading(2, "Callback structs")
    id_types = Counter(type(c["callback_id"]).__name__ for c in api.callbacks)
    by_id: defaultdict[int, list[str]] = defaultdict(list)
    for c in api.callbacks:
        by_id[c["callback_id"]].append(c["struct"])
    results = {m["callresult"] for _, m in api.methods if "callresult" in m}
    md.para(
        f"Every callback struct gives its id in the `callback_id` key (value types: "
        f"{counts_text(id_types)}). Ids range from {min(by_id)} to {max(by_id)}: {len(by_id)} "
        f"distinct ids for {len(api.callbacks)} structs. "
        f"{len(api.callback_names & results)} callback structs are named by a `callresult` key, "
        f"{len(api.callback_names - results)} are not. "
        f"{sum(not c['fields'] for c in api.callbacks)} have no fields."
    )
    md.heading(3, "Ids shared by several structs")
    md.table(
        ["Id", "Structs"],
        [(i, ", ".join(map(code, s))) for i, s in sorted(by_id.items()) if len(s) > 1],
    )
    md.heading(3, "Ids by block of 100")
    blocks: defaultdict[int, list[str]] = defaultdict(list)
    for i, structs in sorted(by_id.items()):
        blocks[i // 100 * 100].extend(structs)
    md.table(
        ["Block", "Structs", "Examples"],
        [(f"{b} to {b + 99}", len(s), first(map(code, s))) for b, s in blocks.items()],
    )


def write_generator_notes(api: Api, levels: dict[str, Level], md: Markdown) -> None:
    uses = type_uses(api)
    md.heading(2, "Things a generator must handle")

    md.heading(3, "Function pointers")
    md.table(TYPE_COLUMNS, grouped((t, w) for t, w in uses if _FUNCTION_POINTER.fullmatch(t)))

    md.heading(3, "Fixed-size arrays")
    md.table(TYPE_COLUMNS, grouped((t, w) for t, w in uses if _ARRAY.search(t)))

    md.heading(3, "C++ references")
    md.table(TYPE_COLUMNS, grouped((t, w) for t, w in uses if "&" in t))

    md.heading(3, "Pointers to pointers")
    md.table(TYPE_COLUMNS, grouped((t, w) for t, w in uses if re.search(r"\*\s*\*", t)))

    md.heading(3, "Structs embedded, passed or returned by value")
    md.table(
        TYPE_COLUMNS,
        grouped(
            (t, w)
            for t, w in uses
            if not re.search(r"[*&(]", t) and api.struct_names.intersection(base_types(t))
        ),
    )

    md.heading(3, "Scoped type names")
    md.table(TYPE_COLUMNS, grouped((t, w) for t, w in uses if "::" in t))
    scoped = sorted({name for t, _ in uses for name in base_types(t) if "::" in name})
    undefined_scoped = [n for n in scoped if n not in api.defined_types]
    md.para(f"Not defined anywhere in the JSON: {codes(undefined_scoped)}.")

    md.heading(3, "Layout information")
    layout_keys = sorted(
        {
            k
            for level in levels.values()
            for k in level.keys
            if any(w in k.lower() for w in LAYOUT_WORDS)
        }
    )
    field_keys = sorted(
        {k for path, level in levels.items() if path.endswith("fields[]") for k in level.keys}
    )
    md.para(
        f"Keys at any level containing {codes(LAYOUT_WORDS)}: {codes(layout_keys)}. "
        f"Field objects have only the keys {codes(field_keys)}."
    )

    md.heading(3, "Structs with methods")
    md.table(
        ["Struct", "Methods", "Flat names"],
        [
            (
                code(s["struct"]),
                len(s["methods"]),
                first(code(m["methodname_flat"]) for m in s["methods"]),
            )
            for s in api.structs
            if s.get("methods")
        ],
    )

    md.heading(3, "Private fields")
    md.table(
        ["Field", "Type"],
        [
            (code(f"{o}.{f['fieldname']}"), code(f["fieldtype"]))
            for o, f in api.fields
            if "private" in f
        ],
    )

    md.heading(3, "Pointer fields")
    md.table(
        ["Field", "Type"],
        [
            (code(f"{o}.{f['fieldname']}"), code(f["fieldtype"]))
            for o, f in api.fields
            if "*" in f["fieldtype"]
        ],
    )

    md.heading(3, "Enums that look like flags")
    md.para(
        'Heuristic: the name contains "flag", or at least three positive values are powers of two '
        "and they make up at least 80% of the positive values."
    )
    flag_rows: list[tuple[str, int, str, str]] = []
    for scope, enum in api.enums:
        values = [parse_int(v["value"]) for v in enum["values"]]
        positive = [v for v in values if v is not None and v > 0]
        powers = [v for v in positive if v & (v - 1) == 0]
        named = "flag" in enum["enumname"].lower()
        if named or (len(powers) >= 3 and len(powers) >= 0.8 * len(positive)):
            flag_rows.append(
                (
                    code(qualified(scope, enum["enumname"])),
                    len(values),
                    f"{len(powers)} of {len(positive)}",
                    "yes" if named else "no",
                )
            )
    md.table(["Enum", "Values", "Positive powers of two", "Name mentions flag"], flag_rows)

    md.heading(3, "Non-enum parameters and fields named as flags")
    named_flags = [
        (f"{m['methodname_flat']}({p['paramname']})", p["paramtype"])
        for m, p in api.params
        if _FLAGS_NAME.search(p["paramname"])
    ] + [
        (f"{o}.{f['fieldname']}", f["fieldtype"])
        for o, f in api.fields
        if _FLAGS_NAME.search(f["fieldname"])
    ]
    md.table(
        ["Where", "Type"],
        [
            (code(w), code(t))
            for w, t in named_flags
            if not api.enum_names.intersection(base_types(t))
        ],
    )

    md.heading(3, "Enum values")
    parsed = [
        (qualified(scope, e["enumname"]), parse_int(v["value"]))
        for scope, e in api.enums
        for v in e["values"]
    ]
    numbers = [n for _, n in parsed if n is not None]
    value_types = Counter(type(v["value"]).__name__ for _, e in api.enums for v in e["values"])
    negative = sorted({name for name, n in parsed if n is not None and n < 0})
    md.para(
        f"Value types: {counts_text(value_types)}. {len(numbers)} of {len(parsed)} values parse as "
        f"integer literals, ranging from {min(numbers)} to {max(numbers)}. "
        f"Enums with negative values: {codes(negative)}."
    )
    aliases: list[tuple[str, str]] = []
    for scope, e in api.enums:
        shared = sorted(v for v, n in Counter(v["value"] for v in e["values"]).items() if n > 1)
        if shared:
            aliases.append((code(qualified(scope, e["enumname"])), ", ".join(shared)))
    md.table(["Enum", "Values used by more than one name"], aliases)

    md.heading(3, "Enums and constants nested in other objects")
    md.table(
        ["Scope", "Kind", "Name", "fqname or type"],
        [
            (code(s), "enum", code(e["enumname"]), code(e.get("fqname", "")))
            for s, e in api.enums
            if s
        ]
        + [
            (code(s), "constant", code(c["constname"]), code(c["consttype"]))
            for s, c in api.consts
            if s
        ],
    )

    md.heading(3, "Constant values")
    kinds = [(scope, c, const_kind(c["constval"])) for scope, c in api.consts]
    md.para(
        f"Value kinds: {counts_text(Counter(k for _, _, k in kinds))}. All but integer literals:"
    )
    md.table(
        ["Constant", "Type", "Kind", "Value"],
        [
            (code(qualified(s, c["constname"])), code(c["consttype"]), k, code(c["constval"]))
            for s, c, k in kinds
            if k != "integer literal"
        ],
    )

    md.heading(3, "Types used but never defined")
    undefined = [
        (name, w) for t, w in uses for name in base_types(t) if name not in api.defined_types
    ]
    md.table(TYPE_COLUMNS, grouped(undefined))
    standard = sorted({n for n, _ in undefined if n in STANDARD_C_TYPES})
    md.para(
        f"Standard C types among them: {codes(standard)}. "
        f"Built-in C types are not listed: {codes(sorted(C_TYPES))}."
    )

    md.heading(3, "Interfaces without an accessor")
    iface_rows: list[tuple[str, int, str, str]] = []
    for iface in api.interfaces:
        if iface.get("accessors"):
            continue
        name = iface["classname"]
        returned = [
            m["methodname_flat"] for _, m in api.methods if name in base_types(m["returntype"])
        ]
        passed = [
            f"{m['methodname_flat']}({p['paramname']})"
            for m, p in api.params
            if name in base_types(p["paramtype"])
        ]
        iface_rows.append(
            (code(name), len(iface["methods"]), first(returned) or "-", first(passed) or "-")
        )
    md.table(["Interface", "Methods", "Returned by", "Passed to"], iface_rows)

    md.heading(3, "Accessors")
    accessors = [(i["classname"], a) for i in api.interfaces for a in i.get("accessors", [])]
    md.para(
        f"Kinds: {counts_text(Counter(a['kind'] for _, a in accessors))}. Interfaces with several:"
    )
    per_interface: defaultdict[str, list[str]] = defaultdict(list)
    for name, a in accessors:
        per_interface[name].append(f"{a['kind']}: {code(a['name_flat'])}")
    md.table(
        ["Interface", "Accessors"],
        [(code(n), ", ".join(a)) for n, a in per_interface.items() if len(a) > 1],
    )

    md.heading(3, "Overloaded method names")
    overloads: defaultdict[str, list[str]] = defaultdict(list)
    for owner, m in api.methods:
        overloads[f"{owner}::{m['methodname']}"].append(m["methodname_flat"])
    md.table(
        ["Method", "Flat names"],
        [(code(n), ", ".join(map(code, flat))) for n, flat in overloads.items() if len(flat) > 1],
    )
    flat_names = Counter(m["methodname_flat"] for _, m in api.methods)
    shared_flat = [n for n, c in flat_names.items() if c > 1]
    md.para(f"Flat names used by more than one method: {codes(shared_flat)}.")


def render(data: Obj, version: str, json_sha256: str) -> str:
    api = Api(data)
    levels: dict[str, Level] = {}
    collect_levels(data, "", levels)
    md = Markdown()
    md.heading(1, "Steamworks SDK inventory")
    md.para(f"SDK {version}. {code(JSON_PATH)} sha256 {code(json_sha256)}.")
    write_counts(api, md)
    write_keys(levels, md)
    write_types(api, md)
    write_annotations(api, md)
    write_call_results(api, md)
    write_callbacks(api, md)
    write_generator_notes(api, levels, md)
    return md.text()


def main() -> int:
    try:
        root = locate_sdk()
        version = sdk_version(root)
    except SdkError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    json_path = root / JSON_PATH
    with json_path.open(encoding="utf-8") as f:
        data: Obj = json.load(f)
    REPORT_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.write_text(
        render(data, version, file_sha256(json_path)), encoding="utf-8", newline="\n"
    )
    print(f"wrote {REPORT_PATH.relative_to(REPO_ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
