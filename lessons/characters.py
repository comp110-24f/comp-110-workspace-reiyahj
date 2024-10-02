def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1


# if infinite loop, press ctrl+c to quit
characters(msg="Howdy")
