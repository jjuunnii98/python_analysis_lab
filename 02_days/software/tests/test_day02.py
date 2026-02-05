from day02.iter_utils import enumerate_pairs, sorted_copy, zip_pairs
from day02.mappings import invert_unique, merge_dicts, safe_get
from day02.sequences import flatten, unpack_first_two
from day02.sets_ops import difference, intersection, union, unique


def test_unpack_first_two():
    a, b, rest = unpack_first_two([1, 2, 3, 4, 5])
    assert (a, b) == (1, 2)
    assert rest == [3, 4, 5]


def test_flatten():
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]


def test_safe_get_and_merge():
    d = {"a": 1}
    assert safe_get(d, "a", 0) == 1
    assert safe_get(d, "missing", 0) == 0
    assert merge_dicts({"a": 1}, {"a": 2, "b": 3}) == {"a": 2, "b": 3}


def test_invert_unique():
    d = {"x": 1, "y": 2}
    assert invert_unique(d) == {1: "x", 2: "y"}


def test_sets_ops():
    data = [1, 2, 2, 3]
    assert unique(data) == {1, 2, 3}
    assert union({1, 2}, {2, 3}) == {1, 2, 3}
    assert intersection({1, 2}, {2, 3}) == {2}
    assert difference({1, 2}, {2, 3}) == {1}


def test_iter_utils():
    assert enumerate_pairs(["a", "b"]) == [(0, "a"), (1, "b")]
    assert sorted_copy([3, 1, 2]) == [1, 2, 3]
    assert zip_pairs(["foo", "bar"], ["one", "two"]) == [("foo", "one"), ("bar", "two")]