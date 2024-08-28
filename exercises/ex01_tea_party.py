"""How to plan a tea party!"""

__author__ = "730760471"


def main_planner(guests: int) -> None:
    """Entrypoint of program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # originally I wrote "2" instead of str(guests), but I realized that it
    # would be irritating to change it every time I changed my guest number!
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
            # I wonder if there is a more succinct way to write this?
        )
    )


def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Calculates number of treats needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost of tea bags and treats combined."""
    return (0.50 * tea_count) + (0.75 * treat_count)
    # note that 0.50(tea_count) makes program think that you
    # are calling a function named 0.5.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# note that we cannot place this above our function definitions because
# then our call to main_planner would result in an error (since it wouldn't
# have been defined yet!)
