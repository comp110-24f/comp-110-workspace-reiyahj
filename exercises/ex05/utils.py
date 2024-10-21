"""Exercise 05, using unit tests."""

__author__ = "730760471"


def only_evens(input: list[int]) -> list[int]:
    """Returns list of even integers in input list."""
    i: int = 0
    even_list = []
    while i < len(input):
        if input[i] % 2 == 0:
            even_list.append(input[i])
        i += 1
    return even_list


def sub(input: list[int], start_i: int, end_i: int) -> list[int]:
    """Returns subsection of input list between indices start_i and end_i."""
    sub_list = []

    if start_i < 0:  # index cannot be negative
        i: int = 0
    else:
        i: int = start_i

    while i < end_i and i < len(input):
        # since empty list has length 0, while loop will not be run in this case
        sub_list.append(input[i])
        i += 1
    return sub_list


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """Modifies input list to place element at given index."""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    else:
        input.append(0)  # increases len(input) by 1
        shift_idx = len(input) - 1
        while idx < shift_idx:
            input[shift_idx] = input[shift_idx - 1]
            shift_idx -= 1
        input[shift_idx] = elem  # occurs when shift_idx == idx
