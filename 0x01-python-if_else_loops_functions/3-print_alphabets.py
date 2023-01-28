#!/usr/bin/python3

#  Printing ASCII alphabet in lowercase excluding q and e with no new line
#  ..............................RULES.................................
#  One print function with .format()
#  one loop
#  characters can't be stored in a variable
#  no import
#  end="" --- allows me to print without a new line in py

for x in range(97, 123):
    if x == 101:
	    break
    c = "{}".format(chr(x))
    print(c, end="")
