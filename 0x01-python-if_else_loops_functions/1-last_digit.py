#!/usr/bin/python3
import math
import ctypes
import random
number = random.randint(-10000, 10000)

num = id(number)  # This stores the memory address of number.

a = ctypes.cast(num, ctypes.py_object).value
# This retrieve the value from the num

b = int (math.fmod(a, 10)) # This prints the last digit of the value

if (b < 6):
    print("Last digit of", number, "is", b,"and is less than 6 and not 0")
if (b == 0):
    print("Last digit of", number, "is", b, "and is 0")
if (b > 5):
    print("Last digit of", number, "is", b, "and is greater than 5")
