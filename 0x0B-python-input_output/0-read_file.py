#!/usr/bin/python3
"""
read_file
"""


def read_file(filename=""):
    """
    function that writes a string to a text file
    Args:
    filename (str): Filename
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
