#!/usr/bin/python3
"""This module defines the print_square function
"""


def print_square(size):
    """ Function that prints a square.
    Args:
        size (int): size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be integer")
    for i in range(size):
        for y in range(size):
            print("#", end="")
        print()
