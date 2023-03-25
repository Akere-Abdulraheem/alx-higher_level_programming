#!/usr/bin/python3

#  To write a program thats imports the function 'add' from file 'add_0.py'

#  ........................RULES.....................
#  print with .format()
#  assign values to variable(a and b)
#  programs displays 'value a + value b = addition of a and b'
#  CAN ONE USE *ADD_0* once
#  no __import__ or *
#  code shouldn't run when imported using __import__

# CODE...
# def add is the function which as arg: a and b and return the addition
# a and b are the var which store values
# var c stores the function

import add_0 as addition
if __name__ == "__main__":
    a = 1
    b = 5
    c = addition.add(a, b)
    print("{0} + {1} = {2}".format(a, b, c))
