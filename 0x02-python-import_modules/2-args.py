#!/usr/bin/python3
from sys import argv  # sys.argv == argv and argc in C

if __name__ == "__main__":
    for a in argv:
        ln = int(len(argv[1:]))

if ln == 0:
    print("0 arguments.")
if ln == 1:
    print("1 argument:")
    print(ln, ": ", a, sep='')  # sep='' removes space
if ln >= 2:
    print(ln, "arguments:")
# The next line, 'in enumerate' allows us to auto number
# the ',1' after 'argv[1:]' allows us to start indexing
# from one

    for index, arg in enumerate(argv[1:], 1):
        print(index, ": ", arg, sep='')
