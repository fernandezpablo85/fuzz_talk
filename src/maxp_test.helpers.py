# from hypothesis import given
# from hypothesis.strategies import integers, lists

# import numpy as np


# @given(lists(integers(), min_size=2))
# def test_max_product_largest_than_any_two(ns):
#     p = max_product(ns)
#     one, two = np.random.choice(ns, 2)
#     assert p >= (int(one) * int(two))
