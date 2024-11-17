"""In-Class, November 13, 2024"""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    # introducing magic methods (__init__ is also a magic method!)
    # when print() is called, it automatically calls __str__
    def __str__(self) -> str:
        """Represent a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
            # could also use "rest = self.next.__str__()"
            # but this is not often done in practice
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
# one_two: Node = Node(1, Node(2, None))
courses: Node = Node(110, Node(210, Node(301, None)))

# default representation
print(one)
print(courses)

# Challenge: try to get "3" to output too!
# three: Node = Node(3, None)
# two: Node = Node(2, three)
# one: Node = Node(1, two)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a Linked List."""
    # 1. If head is followed by None?
    #   Return head's value
    # 2. Else, return the last of the rest of the list (next Node)
    if head.next is None:
        return head.value  # Base case!
    else:
        last_value: int = last(head.next)  # Recursive case!
        return last_value


# print(last(one))  # Expect 2
print(last(courses))  # Expect 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (not inclusive)."""
    # TODO: Raise an exception with string "Invalid use of recursive_range"
    # when called improperly
    # Edge case:
    if start > end:
        # raise Exception("Invalid use of recursive_range")
        raise ValueError("Invalid use of recursive_range")

    if start == end:
        return None
    else:
        # Recursive case:
        # Intuition: handle the first case based on the specific call
        first: int = start
        # Build the rest of the list using the builder function recursively.
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


# Try declaring a variable and assigning it the result of recursive_range
# Then try printing that variable as a string
a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
c: Node | None = recursive_range(115, 112)
print(a)
print(b)
print(c)
print(str(a))
print(str(b))


# scale(head: Node, factor: float) -> scale(None, 4) -> None
# scale(1 -> None, 4) -> 4 -> None
