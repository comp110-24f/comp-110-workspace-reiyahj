"""October 14th, 2024 in-class practice"""


def get_first(list: list[str]) -> str:
    """Returns first element of inputted list."""
    if len(list) == 0:
        return ""
    return list[0]


def remove_first(list: list[str]) -> None:
    """Removes first element of inputted list w/o returning anything."""
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    """Returns and removes first element of inputted list."""
    # first_element: str = list.pop(0) somehow works too????????????
    first_elem: str = list[0]
    list.pop(0)  # remove first_elem
    return first_elem


# introducing unit tests (function specifically designed to test your other functions)
