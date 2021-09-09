#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    x = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            x += int(argv[i])
        print(x)
