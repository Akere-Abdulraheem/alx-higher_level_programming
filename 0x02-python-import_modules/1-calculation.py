#!/usr/bin/python3

'''
To write a program thats imports the function 'add' from file 'add_0.py'
........................RULES.....................
print with .format()
assign values to variable(a and b)
programs displays 'value a + value b = addition of a and b'
CAN ONE USE ADD_0 once
no __import__ or *
code shouldn't run when imported using __import__
'''

# CODE...
# def add is the function which as arg: a and b and return the addition
# a and b are the var which store values
# var d store the f-format


#def add(a, b):
#    """My addition function
#
#    Args:
#        a: first integer
#	b: second integer
#
#    Returns:
#        The return value. a + b
#    """
#    return (a + b)

import calculator_1
a = 10
b = 5
d = "{0} + {1} = {2}".format(a, b, calculator_1(a, b))
print(d)
