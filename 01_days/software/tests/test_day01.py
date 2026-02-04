from datetime import datetime

from day01.control_flow import sum_multiples_3_or_5, sum_skip_none, sum_until
from day01.datetime_utils import floor_to_hour, format_dt, parse_dt
from day01.mutability import list_reassignment_demo, tuple_is_immutable
from day01.strings_bytes import is_string_immutable, safe_replace, to_utf8_bytes
from day01.types_casting import add_and_maybe_multiply, to_bool, to_float, to_int


def test_mutability():
    res = list_reassignment_demo()
    assert res.before != res.after
    assert tuple_is_immutable() is True


def test_strings_bytes():
    assert is_string_immutable() is True
    assert safe_replace("this is a string", "string", "longer string") == "this is a longer string"
    assert isinstance(to_utf8_bytes("español"), (bytes,))


def test_casting_and_none():
    f = to_float("3.14159")
    assert isinstance(f, float)
    assert to_int(f) == 3
    assert to_bool(0) is False
    assert add_and_maybe_multiply(2, 3) == 5
    assert add_and_maybe_multiply(2, 3, c=10) == 50


def test_datetime_utils():
    dt = datetime(2011, 10, 29, 20, 30, 21)
    assert format_dt(dt) == "2011-10-29 20:30"
    parsed = parse_dt("20091031 12:00")
    assert parsed.year == 2009 and parsed.month == 10 and parsed.day == 31
    floored = floor_to_hour(dt)
    assert floored.minute == 0 and floored.second == 0


def test_control_flow():
    assert sum_skip_none([1, 2, None, 4, None, 5]) == 12
    assert sum_until([1, 2, 0, 4, 6, 5, 2, 1], stop_value=5) == 13
    assert sum_multiples_3_or_5(10) == 23  # 0,3,5,6,9
