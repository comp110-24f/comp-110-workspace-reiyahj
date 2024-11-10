"""File to define River class."""

__author__ = "730760471"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Constructs a river object containing Fish and Bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals from River as they age."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def bears_eating(self):
        """If there are at least 5 fish in the river, each bear eats 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(num_fish=3)
                self.remove_fish(amount=3)
        return None

    def check_hunger(self):
        """Removes bear from river if its hunger score is below 0."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Adds (n//2) * 4 new fish, where n is number of current fish."""
        num_offspring: int = (len(self.fish) // 2) * 4
        i: int = 0
        while i < num_offspring:
            new_fish: Fish = Fish()
            self.fish.append(new_fish)
            i += 1
        return None

    def repopulate_bears(self):
        """Adds n//2 new bears to bears, where n is number of current bears."""
        num_offspring: int = len(self.bears) // 2
        i: int = 0
        while i < num_offspring:
            new_bear: Bear = Bear()
            self.bears.append(new_bear)
            i += 1
        return None

    def view_river(self):
        """Prints current state of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        i = 0
        while i < 7:
            self.one_river_day()
            i += 1

    def remove_fish(self, amount: int):
        """Removes a specified number of frontmost fish from River."""
        new_list: list[Fish] = []
        for i in range(amount, len(self.fish)):
            new_list.append(self.fish[i])

        self.fish = new_list
