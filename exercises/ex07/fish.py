"""File to define Fish class."""


class Fish:
    """Constructing a fish object."""

    age: int

    def __init__(self):
        """Initializes fish's age."""
        self.age = 0
        return None

    def one_day(self):
        """Each day, the fish's age increases by 1."""
        self.age += 1
        return None
