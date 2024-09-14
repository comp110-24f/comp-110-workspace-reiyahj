"""Practicing my conditionals."""


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to COMP110!"
    else:
        return "Keep sleeping. You deserve it. :)"


print(wake_up(alarm=True))


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=7)


def check_first_letter(word: str, letter: str) -> str:
    """Write a function check_first_letter that takes an input two strs: word and letter
    It should return “match!” if the first character of word is letter
    Otherwise, return “no match!”"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hello", letter="b"))
