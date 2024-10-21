"""Exercise 05, using unit tests (test file)."""

__author__ = "730760471"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge() -> None:
    """Tests edge case (non-typical input) for only_evens."""
    test_list = []
    assert only_evens(test_list) == []


def test_only_evens_return_val() -> None:
    """Tests return value of only_evens."""
    test_list = [1, 2, 5, 8, 3, 2, 10, 6]
    assert only_evens(test_list) == [2, 8, 2, 10, 6]


def test_only_evens_behavior() -> None:
    """Tests how only_evens mutates/doesn't mutate input."""
    test_list = [1, 2, 3, 4, 5, 6]
    only_evens(test_list)
    assert test_list == [1, 2, 3, 4, 5, 6]  # original list should not be changed


def test_sub_edge() -> None:
    """Tests edge case (non-typical input) for sub."""
    test_list = []
    start = -2
    end = 5
    assert sub(test_list, start, end) == []


def test_sub_return_val() -> None:
    """Tests return value of sub."""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8]
    start = 3
    end = 5
    assert sub(test_list, start, end) == [4, 5]


def test_sub_behavior() -> None:
    """Tests how sub mutates/doesn't mutate input."""
    test_list = [23, 5, 6, 32]
    start = 1
    end = 3
    sub(test_list, start, end)
    assert test_list == [23, 5, 6, 32]  # original list should not be changed


def test_add_at_index_edge() -> None:
    """Tests edge case (non-typical input) for add_at_index."""
    test_list = [2, 3, 5, 7, 8]
    elem = 4
    idx = 10  # since test_list[10] does not exist, this should be IndexError
    with pytest.raises(IndexError):
        add_at_index(
            test_list, elem, idx
        )  # asked TA about this! explanation also in instructions


def test_add_at_index_return_val() -> None:
    """Tests return value of add_at_index."""
    test_list = [2, 3, 5, 7, 8]
    elem = 4
    idx = 2
    assert add_at_index(test_list, elem, idx) is None


def test_add_at_index_behavior() -> None:
    """Tests how add_at_index mutates/doesn't mutate input."""
    test_list = [2, 3, 5, 7, 8]
    elem = 4
    idx = 2
    add_at_index(test_list, elem, idx)
    assert test_list == [2, 3, 4, 5, 7, 8]  # original list should be changed!
