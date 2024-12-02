from ones_threes_and_nines import Ones_threes_nines
import pytest

def test_class():
    test_case = Ones_threes_nines(5)
    assert test_case.ones == 5
    assert test_case.threes == 1
    assert test_case.nines == 0

def test_class_lower():
    test_case = Ones_threes_nines(1)
    assert test_case.ones == 1
    assert test_case.threes == 0
    assert test_case.nines == 0

def test_case_nine():
    test_case = Ones_threes_nines(9)
    assert test_case.ones == 9
    assert test_case.threes == 3
    assert test_case.nines == 1

def test_zero():
    test_case = Ones_threes_nines(0)
    assert test_case.ones == 0
    assert test_case.threes == 0
    assert test_case.nines == 0