import pytest
from main import int_to_roman

# do not change this file

def test_int_to_roman_3():
    assert int_to_roman(3) == "III"

def test_int_to_roman_58():
    assert int_to_roman(58) == "LVIII"

def test_int_to_roman_400():
    assert int_to_roman(400) == "CD"

def test_int_to_roman_1994():
    assert int_to_roman(1994) == "MCMXCIV"

def test_int_to_roman_3999():
    assert int_to_roman(3999) == "MMMCMXCIX"

