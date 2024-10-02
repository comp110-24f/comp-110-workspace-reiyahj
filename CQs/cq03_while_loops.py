"""Third challenge question in COMP110 (practicing while loops)"""

__author__ = "730760471"


def num_instances(phrase: str, search_char: str) -> int:
    """Counting number of occurences of a character in a phrase."""
    count: int = 0  # initializing count variable
    i: int = 0  # initializing index variable
    while i < len(phrase):  # iterating over all indices, from 0 to len(phrase)-1
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count
