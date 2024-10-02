"""September 25 virtual lesson; practicing importing."""

from lessons.scope_practice import remove_chars

print(remove_chars("zebra", "e"))


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)
