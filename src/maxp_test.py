from maxp import max_product


def test_max_product():
    assert max_product([]) == None
    assert max_product([1]) == None
    assert max_product([1, 2, 3]) == 6
    assert max_product([1, 2, 3, 20]) == 60
    assert max_product([1, 200]) == 200

