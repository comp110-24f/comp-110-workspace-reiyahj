"""Finding and removing max value from list."""

__author__ = "730760471"


def find_and_remove_max(list: list[int]) -> int:
    """Finds and returns largest value, then removes all instances of that value."""
    if len(list) == 0:
        return -1
    else:
        max: int = list[0]
        i: int = 0
        while i < len(list):
            if list[i] > max:
                max = list[i]
            i += 1

        i: int = 0
        while i < len(list):
            if list[i] == max:
                list.pop(i)
            else:
                i += 1  # only increase the index when you don't remove an element!
                # (when you remove an element, the next value automatically shifts down
                # to the orig. index)
        return max
