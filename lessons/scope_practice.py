"""September 25th virtual class; some scope examples."""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # initializing new string
    index: int = 0  # local variables
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # global variable

    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
    # print(remove_chars(msg="football", char="o"))
