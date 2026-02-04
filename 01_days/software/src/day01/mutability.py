from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MutationDemoResult:
    before: list[Any]
    after: list[Any]


def list_reassignment_demo() -> MutationDemoResult:
    """리스트는 가변(mutable)이므로 요소 재할당이 가능하다."""
    a_list: list[Any] = ["foo", 2, [4, 5]]
    before = list(a_list)
    a_list[2] = (3, 4)
    after = list(a_list)
    return MutationDemoResult(before=before, after=after)


def tuple_is_immutable() -> bool:
    """튜플은 불변(immutable)이라 항목 재할당이 불가능함을 True/False로 확인."""
    a_tuple = (3, 5, (4, 5))
    try:
        a_tuple[1] = "four"  # type: ignore[misc]
        return False
    except TypeError:
        return True
