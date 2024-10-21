"""Test file for find_max.py"""

__author__ = "730760471"
from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_ret_value() -> None:
    """Tests that function returns the expected value."""
    list1: list[int] = [5, 9, 9, 2, 1, 8, 9, -2]
    assert find_and_remove_max(list1) == 9


def test_find_and_remove_max_behavior() -> None:
    """Tests that function mutates the input correctly."""
    list1: list[int] = [5, 9, 9, 2, 1, 8, 9, -2]
    find_and_remove_max(list1)
    assert list1 == [5, 2, 1, 8, -2]


def test_find_and_remove_max_edge_case() -> None:
    """Tests that function returns correct value for unconventional input."""
    input1: list[int] = [0, 0, 0]
    input2 = []
    assert find_and_remove_max(input1) == 0
    assert find_and_remove_max(input2) == -1
