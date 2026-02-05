from __future__ import annotations


def unique(values: list[int]) -> set[int]:
    """중복 제거."""
    return set(values)


def union(a: set[int], b: set[int]) -> set[int]:
    return a | b


def intersection(a: set[int], b: set[int]) -> set[int]:
    return a & b


def difference(a: set[int], b: set[int]) -> set[int]:
    return a - b