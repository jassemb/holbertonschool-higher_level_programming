#!/usr/bin/python3
"""
print_sorted function
"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """
        prints the list
        """
        print(sorted(self))
