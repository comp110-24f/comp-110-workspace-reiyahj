"""Working with recursive functions!"""

from __future__ import annotations

__author__ = "730760471"


class Node:
    """Defining Node object."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Constructing new Node object."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Returns last value of a Linked List."""
    # 1. If head is followed by None?
    #   Return head's value
    # 2. Else, return the last of the rest of the list (next Node)
    if head.next is None:
        return head.value  # Base case!
    else:
        last_value: int = last(head.next)  # Recursive case!
        return last_value


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)."""
    if start > end:
        # raise Exception("Invalid use of recursive_range")
        raise ValueError("Invalid use of recursive_range")
    elif start == end:
        return None
    else:
        # Recursive case:
        # Intuition: handle the first case based on the specific call
        first: int = start
        # Build the rest of the list using the builder function recursively.
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


# Try declaring a variable and assigning it the result of recursive_range
a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)


def value_at(head: Node | None, index: int) -> int:
    """Returns data of Node stored at the given index/raises IndexError if index DNE."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)  # index will eventually reach 0


def max(head: Node | None) -> int:
    """Returns max data value in linked list. If linked list empty, raise ValueError."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    elif head.next is None:
        # Base Case: only one value, so this current value must be max.
        return head.value
    else:
        max_value: int = max(head.next)  # Recursive call!
        if head.value > max_value:
            # if current value > subsequent max, current value is new max.
            return head.value
        else:
            return max_value  # if current value <= subs. max, max remains subs. max.


def linkify(items: list[int]) -> Node | None:
    """Returns Linked List of Nodes with same values, in same order, as input list."""
    if items == []:
        # Base Case: if items contains no values then we return None
        return None
    else:
        # Recursive Case: at least 1 value in items
        # calls linkify on all elements excluding first
        linked_list = Node(items[0], linkify(items[1:]))

        # print(linked_list)
        return linked_list


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns new linked list where each value in orig. is scaled by factor."""
    if head is None:
        return None
    else:
        new_linked_list = Node(head.value * factor, scale(head.next, factor))

        # print(new_linked_list)
        return new_linked_list
