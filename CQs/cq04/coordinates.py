"""Challenge Question 04 - Coordinates."""

__author__ = "730760471"


def get_coords(xs: str, ys: str) -> None:
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
