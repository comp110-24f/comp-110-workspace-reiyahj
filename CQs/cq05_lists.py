"""Mutating functions."""

__author__ = "730760471"


def manual_append(list: list[int], num: int) -> None:
    """Appends integer to list of integers."""
    list.append(num)


def double(list: list[int]) -> None:
    """Doubles every element of a list of integers."""
    i: int = 0
    while i < len(list):
        list[i] = list[i] * 2  # to mutate, must change specfic indices
        i += 1  # remember to prevent infinite loops!!!


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
# this doubles the values of both list_1 and list_2,
# since they are referring to the same construct in the heap

print(list_1)
print(list_2)
# as expected, list_1 and list_2 remain the same!
