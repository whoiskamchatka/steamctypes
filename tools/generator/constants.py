"""Evaluate the C constant expressions in steam_api.json without eval."""

import re
from collections.abc import Callable
from dataclasses import dataclass

Value = int | float
NameLookup = Callable[[str], Value | None]
IntTypeLookup = Callable[[str], tuple[int, bool] | None]  # bits and signedness

_TOKEN = re.compile(
    r"""\s*(?:
        (?P<float>\d+\.\d*(?:[eE][-+]?\d+)?[fF]?)
      | (?P<int>0[xX][0-9a-fA-F]+|\d+)[uUlL]*
      | '(?P<char>\\.|[^\\'])'
      | (?P<name>[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*)
      | (?P<op><<|>>|[|^&~+\-*()])
    )""",
    re.VERBOSE,
)
_ESCAPES = {"0": 0, "n": 10, "t": 9, "\\": 92, "'": 39, '"': 34}
# Binding strength of the binary operators, as in C.
_BINARY = {"|": 1, "^": 2, "&": 3, "<<": 4, ">>": 4, "+": 5, "-": 5, "*": 6}


class ConstantError(ValueError):
    pass


@dataclass(frozen=True)
class _Token:
    kind: str  # "number", "name" or "op"
    text: str
    value: Value = 0


def _tokenize(expression: str) -> list[_Token]:
    tokens: list[_Token] = []
    position = 0
    expression = expression.rstrip()
    while position < len(expression):
        match = _TOKEN.match(expression, position)
        if match is None:
            raise ConstantError(f"unexpected {expression[position:]!r} in {expression!r}")
        position = match.end()
        if (text := match["float"]) is not None:
            tokens.append(_Token("number", text, float(text.rstrip("fF"))))
        elif (text := match["int"]) is not None:
            tokens.append(_Token("number", text, _parse_int(text)))
        elif (text := match["char"]) is not None:
            tokens.append(_Token("number", text, _char_value(text, expression)))
        elif (text := match["name"]) is not None:
            tokens.append(_Token("name", text))
        else:
            tokens.append(_Token("op", match["op"]))
    return tokens


def _parse_int(text: str) -> int:
    if text[:2] in ("0x", "0X"):
        return int(text, 16)
    if len(text) > 1 and text.startswith("0"):
        return int(text, 8)
    return int(text)


def _char_value(text: str, expression: str) -> int:
    if not text.startswith("\\"):
        return ord(text)
    if text[1] not in _ESCAPES:
        raise ConstantError(f"unsupported escape {text!r} in {expression!r}")
    return _ESCAPES[text[1]]


def _wrap(value: int, bits: int, signed: bool) -> int:
    value &= (1 << bits) - 1
    return value - (1 << bits) if signed and value >> (bits - 1) else value


def names_in(expression: str) -> set[str]:
    return {t.text for t in _tokenize(expression) if t.kind == "name"}


class _Parser:
    # Arithmetic uses unbounded integers. That is exact for every value that fits its type;
    # casts and the caller's conversion to the declared type apply C wrap-around.

    def __init__(self, expression: str, names: NameLookup, int_types: IntTypeLookup) -> None:
        self.expression = expression
        self.tokens = _tokenize(expression)
        self.position = 0
        self.names = names
        self.int_types = int_types

    def error(self, message: str) -> ConstantError:
        return ConstantError(f"{message} in {self.expression!r}")

    def peek(self) -> _Token | None:
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def take(self) -> _Token:
        token = self.peek()
        if token is None:
            raise self.error("unexpected end")
        self.position += 1
        return token

    def expect(self, op: str) -> None:
        token = self.take()
        if token.kind != "op" or token.text != op:
            raise self.error(f"expected {op!r}, found {token.text!r}")

    def parse(self) -> Value:
        value = self.binary(1)
        if (token := self.peek()) is not None:
            raise self.error(f"unexpected {token.text!r}")
        return value

    def binary(self, min_strength: int) -> Value:
        left = self.unary()
        while (token := self.peek()) is not None and token.kind == "op":
            strength = _BINARY.get(token.text, 0)
            if strength < min_strength:
                break
            self.position += 1
            left = self.apply(token.text, left, self.binary(strength + 1))
        return left

    def apply(self, op: str, left: Value, right: Value) -> Value:
        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if not isinstance(left, int) or not isinstance(right, int):
            raise self.error(f"{op!r} needs integers")
        if op == "|":
            return left | right
        if op == "^":
            return left ^ right
        if op == "&":
            return left & right
        if op == "<<":
            return left << right
        return left >> right

    def cast_type(self) -> tuple[int, bool] | None:
        """After "(": the integer type if the parentheses hold only a type name."""
        end = self.position
        while end < len(self.tokens) and self.tokens[end].kind == "name":
            end += 1
        closes = end < len(self.tokens) and self.tokens[end].text == ")"
        if end == self.position or not closes:
            return None
        int_type = self.int_types(" ".join(t.text for t in self.tokens[self.position : end]))
        if int_type is not None:
            self.position = end + 1
        return int_type

    def unary(self) -> Value:
        token = self.take()
        if token.kind == "number":
            return token.value
        if token.kind == "name":
            value = self.names(token.text)
            if value is None:
                raise self.error(f"unknown name {token.text!r}")
            return value
        if token.text == "-":
            return -self.unary()
        if token.text == "+":
            return self.unary()
        if token.text == "~":
            value = self.unary()
            if not isinstance(value, int):
                raise self.error("'~' needs an integer")
            return ~value
        if token.text == "(":
            if (int_type := self.cast_type()) is not None:
                value = self.unary()
                if not isinstance(value, int):
                    raise self.error("integer cast of a non-integer")
                return _wrap(value, *int_type)
            value = self.binary(1)
            self.expect(")")
            return value
        raise self.error(f"unexpected {token.text!r}")


def evaluate(expression: str, names: NameLookup, int_types: IntTypeLookup) -> Value:
    return _Parser(expression, names, int_types).parse()


def to_int_type(value: Value, bits: int, signed: bool) -> int:
    if not isinstance(value, int):
        raise ConstantError(f"{value!r} is not an integer")
    return _wrap(value, bits, signed)
