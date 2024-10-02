"""EX03 - Actually remaking Wordle."""

__author__ = "730760471"


def input_guess(secret_word_len: int) -> str:
    """Asks user to input guess word of specific length."""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # using f-string for conciseness!
    while len(guess) != secret_word_len:
        guess: str = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # program won't move past this until user inputs a word of correct len
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Looking for occurrences of specific character within the secret word."""
    assert (
        len(char_guess) == 1
    )  # we assume the given arguments are correct, & we raise an error if they aren't
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True  # function ends as soon as a matching character is located
        i += 1
    return False
    # program only reaches this last line if none of the characters
    # in secret_word match char_guess


def emojified(guess: str, secret_word: str) -> str:
    """Compares user's guess and the secret word, then
    returns emojis indicating accuracy of guess."""
    assert len(guess) == len(secret_word)

    # named constants which refer to white, green, and yellow box emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i: int = 0
    emoji_str: str = ""  # initializing string of emojis
    while i < len(guess):
        # if characters match exactly:
        if guess[i] == secret_word[i]:
            emoji_str += GREEN_BOX
        # if character doesn't share an index but is contained in both words:
        elif contains_char(secret_word, guess[i]):
            emoji_str += YELLOW_BOX
        # if character in guess is NOT in the secret word:
        else:
            emoji_str += WHITE_BOX
        i += 1
    return emoji_str


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    num_turns: int = 1
    max_turns: int = 6

    while num_turns <= max_turns:
        print(f"=== Turn {num_turns}/{max_turns}===")
        guess: str = input_guess(len(secret))
        emoji_str: str = emojified(guess, secret)
        print(emoji_str)

        if guess == secret:
            print(f"You won in {num_turns}/{max_turns} turns!")
            num_turns = max_turns + 2  # this ensures that we exit the while loop!
        num_turns += 1  # if user hasn't won, we continue the loop

    if num_turns == max_turns + 1:
        # only possible when we have iterated through every turn
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
