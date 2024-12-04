"""Some happy, little trees!"""

from .turtle import Turtle
from math import pi


# from random import random

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0  # Constant


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas!"""
    t: Turtle = Turtle()
    t.setSpeed(100)
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)

    # Code for a flower:
    # Write a while loop where i starts from 150
    # WHILE i > 0.0
    # and moves the turtle forward by i units
    # turns the turtle left by pi / 2.0
    # and decreases i by 2.0
    # i: int = 200
    # while i > 0.0:
    #     t.forward(i)
    #     t.left(pi / 2.0 - pi / 8.0)
    #     i -= 2

    # Code for L-path:
    # t.forward(150)
    # t.left(pi / 2.0)
    # t.forward(140)
    # t.left(pi / 2.0)

    branch(t, y * 0.15, 90 * DEGREE)

    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)

    if length > 10.0:
        branch(t, 0.75 * length, angle + (35 * DEGREE))
        branch(t, 0.75 * length, angle - (35 * DEGREE))

    t.turnTo(angle + pi)
    t.forward(length)
