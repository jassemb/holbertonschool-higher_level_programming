#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 argument.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        print("{}: {}".format(i, argv[i]))
