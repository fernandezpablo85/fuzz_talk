# from hypothesis import given, settings
# from hypothesis.strategies import integers

# @settings(max_examples=1000)


# @given(integers())
# def test_add_props_zero(a):
#     assert add(a, 0) == a
#     assert add(0, a) == a


# @given(integers(), integers())
# def test_add_props_commutative(a, b):
#     assert add(a, b) == add(b, a)


# def is_even(n):
#     return n % 2 == 0

# def evens():
#     return integers().filter(is_even)

# @given(evens(), evens())
# def test_add_props_gt(a, b):
#     assert is_even(add(a, b))
#     assert is_even(add(a, b))
