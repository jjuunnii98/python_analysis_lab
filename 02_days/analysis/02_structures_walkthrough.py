# 02_days/analysis/02_structures_walkthrough.py
"""
Day 02 — Analysis Track (Pages 83–107)
주요 주제: 튜플/리스트/딕셔너리/집합 + 내장 함수(enumerate, sorted, zip)

목적:
- 교재 예제를 '실험 → 관찰 → 결론' 흐름으로 재구성
- 실행 불가능한 placeholder 셀 제거
"""

from __future__ import annotations


def section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def tuples_demo() -> None:
    section("1) Tuple: 생성, 인덱싱, 언패킹, *rest")

    tup = (4, 5, 6)
    print("tup:", tup)

    tup2 = 4, 5, (6, 7)
    a, b, (c, d) = tup2
    print("unpack:", a, b, c, d)

    values = (1, 2, 3, 4, 5)
    x, y, *rest = values
    print("x,y,rest:", x, y, rest)

    # 튜플은 불변(immutable)
    t = (1, 2, 3)
    try:
        t[0] = 999  # type: ignore[misc]
    except TypeError as e:
        print("expected TypeError:", e)


def lists_demo() -> None:
    section("2) List: 생성, 변경, 슬라이싱, append/extend")

    a_list = [2, 3, 7, None]
    print("a_list:", a_list)

    tup = ("foo", "bar", "baz")
    b_list = list(tup)
    b_list[1] = "peekaboo"
    print("b_list modified:", b_list)

    # append vs extend
    x = [1, 2, 3]
    x.append([4, 5])
    print("append:", x)

    y = [1, 2, 3]
    y.extend([4, 5])
    print("extend:", y)

    # slicing
    s = [0, 1, 2, 3, 4, 5]
    print("s[2:5]:", s[2:5])
    print("s[:3]:", s[:3])
    print("s[::2]:", s[::2])


def dicts_demo() -> None:
    section("3) Dict: 생성/조회/삽입, in, get, keys/values/items")

    d1 = {"a": "some value", "b": [1, 2, 3, 4]}
    d1[7] = "an integer"
    print("d1:", d1)
    print("'b' in d1:", "b" in d1)

    # get: 키가 없을 때 예외 대신 기본값 반환
    print("get existing:", d1.get("a"))
    print("get missing:", d1.get("missing", "DEFAULT"))

    for k, v in d1.items():
        print(f"item: {k} -> {v}")

    # dict comprehension 예시
    mapping = {x: x**2 for x in range(5)}
    print("dict comprehension:", mapping)


def sets_demo() -> None:
    section("4) Set: 중복 제거, 합/교/차집합")

    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    print("a | b (union):", a | b)
    print("a & b (intersection):", a & b)
    print("a - b (difference):", a - b)

    # 중복 제거 활용
    data = [1, 2, 2, 3, 3, 3, 4]
    print("unique:", set(data))


def builtin_iter_demo() -> None:
    section("5) Built-ins: enumerate, sorted, zip")

    collection = ["apple", "banana", "cherry"]

    # enumerate: 인덱스+값을 안전하게 같이 얻기
    for idx, value in enumerate(collection):
        print(idx, value)

    # sorted: iterable을 정렬된 리스트로 반환 (원본은 유지)
    nums = [7, 1, 2, 6, 0, 3, 2]
    print("sorted(nums):", sorted(nums))
    print("original nums:", nums)

    # zip: 여러 iterable 동시 순회
    seq1 = ["foo", "bar", "baz"]
    seq2 = ["one", "two", "three"]
    for a, b in zip(seq1, seq2):
        print("zipped:", a, b)


def main() -> None:
    tuples_demo()
    lists_demo()
    dicts_demo()
    sets_demo()
    builtin_iter_demo()


if __name__ == "__main__":
    main()