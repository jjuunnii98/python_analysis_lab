from __future__ import annotations

from typing import Iterable, Iterator, TypeVar

T = TypeVar("T")


def enumerate_pairs(values: Iterable[T]) -> list[tuple[int, T]]:
    """enumerate 결과를 리스트로 반환."""
    return list(enumerate(values))


def zip_pairs(a: Iterable[T], b: Iterable[T]) -> list[tuple[T, T]]:
    """zip 결과를 리스트로 반환(짧은 쪽 기준)."""
    return list(zip(a, b))


def sorted_copy(values: Iterable[T]) -> list[T]:
    """원본을 건드리지 않고 정렬된 리스트 반환."""
    return sorted(values)