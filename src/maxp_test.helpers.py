# from hypothesis import given
# from hypothesis.strategies import integers, lists


# @given(lists(integers(), min_size=2))
# def test_max_product_largest_than_first_two(ns):
#     first, second = ns[:2]
#     assert max_product(ns) >= first * second


# @given(lists(integers(), min_size=2))
# def test_max_product_slow_oracle(ns):
#     assert max_product(ns) == slow_max_product(ns)


# @given(lists(integers(), min_size=2))
# def test_max_product_slow_oracle(ns):
#     times_two = [n * 2 for n in ns]
#     p = max_product(ns)
#     px2 = max_product(times_two)
#     assert p * 4 == px2
