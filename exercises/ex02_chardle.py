"""EX02 - A Remake of Wordle?!"""

__author__ = "730760471"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Obtains 5-letter word from user input."""
    user_word = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # stopping program if input does not satisfy requirements
    # print("'" + user_word + "'")  # prints user_word with single quotes surrounding it
    return user_word


def input_letter() -> str:
    """Obtains single letter from user input."""
    user_letter = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # stopping program if input does not satisfy requirements
    # print("'" + user_letter + "'")  # prints user_letter with single quotes around it
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Locates the user-inputted letter in the user-inputted word by manually checking
    each of the 5 indices of the word."""
    print("Searching for " + letter + " in " + word)

    i: int = 0  # initializing counting variable
    if letter == word[0]:  # checking index 0 of word
        print(letter + " found at index 0")
        i = i + 1  # adding 1 to counting variable for each index that matches letter
    if letter == word[1]:  # checking index 1 of word
        print(letter + " found at index 1")
        i = i + 1
    if letter == word[2]:  # checking index 2 of word
        print(letter + " found at index 2")
        i = i + 1
    if letter == word[3]:  # checking index 3 of word
        print(letter + " found at index 3")
        i = i + 1
    if letter == word[4]:  # checking index 4 of word
        print(letter + " found at index 4")
        i = i + 1

    if i == 0:
        print(
            "No instances of " + letter + " found in " + word
        )  # if no indices match letter
    elif i == 1:
        print(
            str(i) + " instance of " + letter + " found in " + word
        )  # if 1 index matches letter
    else:
        print(
            str(i) + " instances of " + letter + " found in " + word
        )  # if multiple indices match letter


if __name__ == "__main__":
    main()
