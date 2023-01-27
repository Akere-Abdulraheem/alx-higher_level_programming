#!/usr/bin/python3

#  Printing ASCII alphabet in lowercase except q and e with no new line
#  .............................RULES..................................
#  One print function with .format()
#  one loop
#  characters can't be stored in a variable
#  no import

for x in range(97, 122):
    c = "{}".format(chr(x))
    print(c, end="")
