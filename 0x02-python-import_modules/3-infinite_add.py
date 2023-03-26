#!/usr/bin/python3
from sys import argv  # sys.argv == argv and argc in C

n = len(argv)  # total arg
sum = 0  # initalize addition to zero

if __name__ == "__main__":
   for a in range(1, n):
       sum += int(argv[a])
print(sum)  # prints sum of all args
