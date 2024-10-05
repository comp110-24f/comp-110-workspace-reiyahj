"""Write a docstring."""

__author__ = "730760471"


def all(list: list[int], num: int) -> bool:
    """Returns whether all elements of list are equal to num."""
    i: int = 0
    while i < len(list):
        if list[i] != num:
            return False  # short-circuits loop and returns immediately
        i += 1
    return True
    # if function has not returned False by end of list, then
    # all elements must be equal to num and we return True


def max(list: list[int]) -> int:  # not sure what a "skeleton function" means?
    """Returns maximum value in list as long as list is not empty."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max: int = list[0]  # initialize maximum variable
        i: int = 1
        while i < len(list):
            # iterates through each of the values in list and
            # replaces max with greatest value so far
            if list[i] > max:
                max = list[i]
            i += 1
        return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if every element at every index is equal in both lists."""
    if len(list1) == len(list2):
        i: int = 0
        while i < len(list1):  # same concept as in function all
            if list1[i] != list2[i]:
                return False
            i += 1
        return True
    else:  # if the lengths of the two lists are not equal, then they cannot be equal!
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutates list1 by appending list2 to it."""
    i: int = 0
    while i < len(list2):
        list1.append(list2[i])
        # initially tried to add on indices without using the append function,
        # which did not work out well!
        i += 1


# testing using main function:
# def main(list1: list[int], list2: list[int], num: int) -> None:
#   all(list1, num)
#   max(list1)
#   is_equal(list1, list2)
#   extend(list1, list2)


# if __name__ == "__main__":
#    main([1, 1], [1, 2], 1)
