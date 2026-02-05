from __future__ import annotations

from typing import Any, Mapping, TypeVar

K = TypeVar("K")
V = TypeVar("V")


def safe_get(mapping: Mapping[K, V], key: K, default: V) -> V:
    """dict.get 패턴을 명시적으로 캡슐화."""
    return mapping.get(key, default)


def invert_unique(d: Mapping[K, V]) -> dict[V, K]:
    """
    값이 유일하다는 가정 하에 key<->value 반전.
    값이 중복이면 마지막 key로 덮어씀(문서화된 동작).
    """
    return {v: k for k, v in d.items()}


def merge_dicts(a: Mapping[Any, Any], b: Mapping[Any, Any]) -> dict[Any, Any]:
    """두 dict를 병합(b가 우선)."""
    out = dict(a)
    out.update(b)
    return out