#!/usr/bin/python3
"""
Module to print a square
"""


def print_square(size):
    """
    a function that prints a square with the character #.
    Args:
        size(int): size of the square
    Raises:
        TypeError: if size is not integer
        ValueError: if size less than 0
    Returns:
        a printed square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print("")
