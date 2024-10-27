"""Practice with dictionary functions!"""

__author__ = "730760471"


def invert(i_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the initial dictionary."""
    f_dict: dict[str, str] = {}
    for key in i_dict:  # iterating through each initial key
        for new_key in f_dict:  # iterating through keys in f_dict so far
            if i_dict[key] == new_key:
                raise KeyError()
        f_dict[i_dict[key]] = key  # if no error is raised, can add to f_dict

    return f_dict


def favorite_color(favs: dict[str, str]) -> str:
    """Iterates through dictionary containing names of ppl and their fav color,
    & returns the most popular color."""

    # create a dictionary to keep track of # of each color
    colors_num: dict[str, int] = {}
    for name in favs:
        # if color already exists in colors_num, add 1 to its value
        if favs[name] in colors_num:
            colors_num[favs[name]] += 1
        # otherwise, add new key to colors_num with value 1
        else:
            colors_num[favs[name]] = 1

    max_num: int = 0  # initialize variable to find max value
    max_color: str = ""  # initialize variable to find key corresponding to max value
    for color in colors_num:
        if colors_num[color] > max_num:
            max_num = colors_num[color]
            max_color = color

    return max_color


def count(i_list: list[str]) -> dict[str, int]:
    """Counts frequencies of values in input list."""
    count_dict: dict[str, int] = {}

    # Loop through each item in the input list
    for value in i_list:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1

    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Returns dictionary where keys are unique lowercase letters in the alphabet
    and values are lists of words that start with the letter in their key."""

    final_dict: dict[str, list[str]] = {}
    for word in word_list:
        if word[0].lower() in final_dict:
            final_dict[word[0].lower()].append(word)
        else:
            final_dict[word[0].lower()] = [word]

    return final_dict


def update_attendance(
    attendance: dict[str, list[str]], weekday: str, student: str
) -> None:
    """Updates existing attendance dictionary with new attendance info."""

    if weekday in attendance:
        attendance[weekday].append(student)
    else:
        attendance[weekday] = [student]
