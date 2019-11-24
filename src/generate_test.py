from hypothesis import note, given
from hypothesis.strategies import composite, text, integers

import pytest

from dataclasses import dataclass


@dataclass
class ComplexObject:
    number_one: int
    number_two: int
    and_a_string: str

    def sum(self):
        return self.number_one + self.number_two


@composite
def complex_objects(draw, ints=integers(), strs=text()):
    a = draw(ints)
    b = draw(ints)
    c = draw(strs)
    return ComplexObject(number_one=a, number_two=b, and_a_string=c)


@pytest.mark.skip(reason="complex object generation example")
@given(complex_objects())
def test_complex_object(obj: ComplexObject):
    assert obj.number_one + obj.number_two == obj.sum()
