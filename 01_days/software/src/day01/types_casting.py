from __future__ import annotations


def to_float(text: str) -> float:
    return float(text)


def to_int(x: float) -> int:
    return int(x)


def to_bool(x: object) -> bool:
    return bool(x)


def add_and_maybe_multiply(a: float, b: float, c: float | None = None) -> float:
    result = a + b
    if c is not None:
        result *= c
    return result
