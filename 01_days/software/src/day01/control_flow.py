from __future__ import annotations


def sum_skip_none(values: list[int | None]) -> int:
    total = 0
    for v in values:
        if v is None:
            continue
        total += v
    return total


def sum_until(values: list[int], stop_value: int) -> int:
    total = 0
    for v in values:
        if v == stop_value:
            break
        total += v
    return total


def sum_multiples_3_or_5(limit: int) -> int:
    """0 이상 limit 미만 정수 중 3 또는 5의 배수 합."""
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
