from example import add


def test_add():
    assert add(1, 1) == 2
    assert add(1, 0) == 1
    assert add(5, 4) == 9
    assert add(-1, 10) == 9
    assert add(10, 10) == 20
