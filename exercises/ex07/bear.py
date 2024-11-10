"""File to define Bear class."""


class Bear:
    """Constructing a bear object."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear's age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Each day, the bear's age increases by 1 and hunger score decreases by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Updates Bear's hunger score to increase by num_fish."""
        self.hunger_score += num_fish
