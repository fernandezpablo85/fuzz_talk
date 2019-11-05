from example import add
from hypothesis import given
from hypothesis.strategies import integers


def test_add():
    assert add(1, 1) == 2
    assert add(1, 0) == 1
    assert add(5, 4) == 9
    assert add(-1, 10) == 9
    assert add(10, 10) == 20


# @given(integers())
# def test_add_props_zero(a):
#     assert add(a, 0) == a
#     assert add(0, a) == a


# @given(integers())
# def test_add_props_zero(a):
#     assert add(a, 0) == a
#     assert add(0, a) == a


# @given(integers(), integers())
# def test_add_props_gt(a, b):
#     assert add(a, b) >= a
#     assert add(a, b) >= b

