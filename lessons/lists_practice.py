"""Basic syntax of lists."""

# you can initialize an empty list in 2 different ways
list_name1: list[str] = list()
list_name2: list[str] = []

# create an empty list of floats with the name my_numbers
my_numbers: list[float] = list()
# print(my_numbers)

# adding item to a list
my_numbers.append(2.0)
"""Append is a "method", a type of function that is used in a specific class
(in this case, the list class)"""
list_name1.append("bananas")
my_numbers.append(1.5)
# print(my_numbers)


# initializing already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# subscription notation/indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# modifying by index
game_points[1] = 72
print(game_points)

# notice you can't do the same thing with strings!
# strings are immutable, lists are mutable
# test_string: str = ""
# test_string = "110"
# test_string[0] = "2"

print("The length of game_points is " + str(len(game_points)))

# removing item from a list
game_points.pop(1)  # notice we use the index of the item here
print(game_points)


# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points!


def display(list: list[int]) -> None:
    i: int = 0
    while i < len(list):
        print(list[i])
        i += 1


display(game_points)
