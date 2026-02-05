from __future__ import annotations

from typing import Iterable, TypeVar

T = TypeVar("T")


def unpack_first_two(values: Iterable[T]) -> tuple[T, T, list[T]]:
    """
    iterable에서 앞 2개 + 나머지를 분리한다.
    예: (1,2,3,4,5) -> (1,2,[3,4,5])
    """
    lst = list(values)
    if len(lst) < 2:
        raise ValueError("values must contain at least two elements")
    a, b, *rest = lst
    return a, b, rest


def flatten(list_of_lists: list[list[T]]) -> list[T]:
    """2중 리스트를 1중 리스트로 평탄화."""
    out: list[T] = []
    for chunk in list_of_lists:
        out.extend(chunk)
    return out