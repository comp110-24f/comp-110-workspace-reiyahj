"""Summing the elements of a list using different loops"""

__author__ = "730760471"


def w_sum(vals: list[float]) -> float:
    """Takes list of floats and returns its sum, using while loop."""
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


test: int = round(1.3)
test_list = [1.1, 1.2, test]


def f_sum(vals: list[float]) -> float:
    """Takes list of floats and returns its sum, using for..in.. loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Takes list of floats and returns its sum, using for.. in range(..) loop."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
