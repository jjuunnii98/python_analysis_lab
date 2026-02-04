"""
Day 01 — Analysis Walkthrough (script version)

노트북(ipynb)처럼 셀 단위로 실행하는 느낌을 .py로 재구성:
- "실험 → 관찰 → 결론" 흐름을 유지
- 의도적으로 발생하는 TypeError는 try/except로 캡처해 학습 포인트를 명확히 함
"""

from __future__ import annotations

from datetime import datetime


def section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def demo_mutable_vs_immutable() -> None:
    section("1) Mutable vs Immutable")

    # Mutable: list
    a_list = ["foo", 2, [4, 5]]
    print("Original list:", a_list)
    a_list[2] = (3, 4)
    print("After reassignment:", a_list)

    # Immutable: tuple
    a_tuple = (3, 5, (4, 5))
    print("\nTuple:", a_tuple)
    try:
        a_tuple[1] = "four"  # type: ignore[misc]
    except TypeError as e:
        print("Expected error (tuple is immutable):", e)


def demo_scalar_types() -> None:
    section("2) Scalar types (int, float, str)")

    ival = 17239871
    print("ival:", ival, "| ival**6:", ival**6)

    fval = 7.243
    fval2 = 6.78e-5
    print("fval:", fval, "| fval2:", fval2)

    print("3 / 2 =", 3 / 2)
    print("3 // 2 =", 3 // 2)

    a = "one way of writing a string"
    b = "another way"
    c = """
This is a longer string that
spans multiple lines
"""
    print("a:", a)
    print("b:", b)
    print("c newline count:", c.count("\n"))


def demo_strings() -> None:
    section("3) Strings: immutability, replace, slicing, raw string, formatting")

    a = "this is a string"
    try:
        a[10] = "f"  # type: ignore[misc]
    except TypeError as e:
        print("Expected error (str is immutable):", e)

    b = a.replace("string", "longer string")
    print("replace result:", b)
    print("original unchanged:", a)

    s = str(5.6)
    print("str(5.6) ->", s)

    s2 = "python"
    print("list('python') ->", list(s2))
    print("s2[:3] ->", s2[:3])

    raw = r"this\has\no\special\characters"
    print("raw string ->", raw)

    left = "this is the first half"
    right = "and this is the second half"
    print("concat ->", left + right)

    template = "{0:.2f} {1:s} are worth US${2:d}"
    print("format ->", template.format(88.46, "Argentine Pesos", 1))

    amount, rate, currency = 10, 88.46, "Pesos"
    print("f-string ->", f"{amount} {currency} is worth US${amount / rate:.2f}")


def demo_bytes_unicode() -> None:
    section("4) Bytes and Unicode")

    val = "español"
    val_utf8 = val.encode("utf-8")
    print("val:", val)
    print("val.encode('utf-8'):", val_utf8)
    print("type:", type(val_utf8))


def demo_casting_and_none() -> None:
    section("5) Casting + None")

    s = "3.14159"
    fval = float(s)
    print("float('3.14159'):", fval, "| type:", type(fval))
    print("int(fval):", int(fval))
    print("bool(fval):", bool(fval))
    print("bool(0):", bool(0))

    a = None
    print("a is None:", a is None)
    b = 5
    print("b is not None:", b is not None)

    def add_and_maybe_multiply(x: float, y: float, c: float | None = None) -> float:
        result = x + y
        if c is not None:
            result *= c
        return result

    print("add_and_maybe_multiply(2,3) ->", add_and_maybe_multiply(2, 3))
    print("add_and_maybe_multiply(2,3,c=10) ->", add_and_maybe_multiply(2, 3, c=10))


def demo_datetime() -> None:
    section("6) datetime basics")

    dt = datetime(2011, 10, 29, 20, 30, 21)
    print("dt:", dt)
    print("day:", dt.day)
    print("minute:", dt.minute)
    print("date():", dt.date())
    print("time():", dt.time())
    print("strftime('%Y-%m-%d %H:%M'):", dt.strftime("%Y-%m-%d %H:%M"))

    parsed = datetime.strptime("20091031 12:00", "%Y%m%d %H:%M")
    print("strptime:", parsed)

    dt_hour = dt.replace(minute=0, second=0)
    print("replace(minute=0, second=0):", dt_hour)


def demo_control_flow() -> None:
    section("7) Control flow (if/elif/else, for, while, range)")

    x = -5
    if x < 0:
        print("It's negative")

    x = 5
    if x < 0:
        print("It's negative")
    elif x == 0:
        print("Equal to zero")
    elif 0 < x < 5:
        print("Positive but smaller than 5")
    else:
        print("Positive and larger than or equal to 5")

    sequence = [1, 2, None, 4, None, 5]
    total = 0
    for value in sequence:
        if value is None:
            continue
        total += value
    print("sum(skip None) ->", total)

    sequence2 = [1, 2, 0, 4, 6, 5, 2, 1]
    total_until_5 = 0
    for value in sequence2:
        if value == 5:
            break
        total_until_5 += value
    print("sum(until 5) ->", total_until_5)

    x = 256
    total = 0
    while x > 0:
        if total > 500:
            break
        total += x
        x //= 2
    print("while sum with break ->", total)

    print("list(range(10)) ->", list(range(10)))
    print("list(range(0, 20, 2)) ->", list(range(0, 20, 2)))
    print("list(range(5, 0, -1)) ->", list(range(5, 0, -1)))

    seq = [1, 2, 3, 4]
    for i in range(len(seq)):
        print(f"element {i}: {seq[i]}")

    # example: sum of multiples of 3 or 5 below 100,000
    total = 0
    for i in range(100_000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print("sum(multiples of 3 or 5 below 100000) ->", total)


def main() -> None:
    demo_mutable_vs_immutable()
    demo_scalar_types()
    demo_strings()
    demo_bytes_unicode()
    demo_casting_and_none()
    demo_datetime()
    demo_control_flow()


if __name__ == "__main__":
    main()
