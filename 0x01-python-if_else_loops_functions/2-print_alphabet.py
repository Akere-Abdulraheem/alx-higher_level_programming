#!/usr/bin/python3

#  Printing ASCII alphabet in lowercase with no new line
#  .....................RULES...........................
#  One print function with .format()
#  one loop....used while loop
#  characters can't be stored in a variable
#  no import

# a = ord('a')
for x in range(97,122):
    b = chr(x)
    c = "{}".format(b)
    print(c)
#    a += 1
