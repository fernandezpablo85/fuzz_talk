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


@dataclass
class TooComplexObject:
    delegate: ComplexObject
    string_index: int


@composite
def complex_objects(draw, ints=integers(), strs=text()):
    """Strategy for generating a ComplexObject made of ints and strings"""
    a = draw(ints)
    b = draw(ints)
    c = draw(strs)
    return ComplexObject(number_one=a, number_two=b, and_a_string=c)


@composite
def too_complex_object(draw, objs=complex_objects()):
    obj: ComplexObject = draw(objs)
    index = draw(integers(min_value=len(obj.and_a_string)))
    too_complex = TooComplexObject(delegate=obj, string_index=index)
    return too_complex


@pytest.mark.skip(reason="complex object generation example")
@given(complex_objects())
def test_complex_object(obj: ComplexObject):
    assert obj.number_one + obj.number_two == obj.sum()

@pytest.mark.skip(reason="complex object generation example")
@given(too_complex_object())
def test_complex_object(obj: TooComplexObject):
    assert len(obj.delegate.and_a_string) <= obj.string_index
