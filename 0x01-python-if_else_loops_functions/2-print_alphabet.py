#!/usr/bin/python3

#  Printing ASCII alphabet in lowercase with no new line
#  .....................RULES...........................
#  One print function with .format()
#  one loop....used a for loop
#  characters can't be stored in a variable
#  no import

# a = ord('a')
for x in range(97, 122):
    c = "{}".format(chr(x))
    print(c)
