#!/usr/bin/python3

'''
a class 'square' that define a square by

* private instance attribute: size
* instantiation with size optional
  :def __init__(self, size=0)
  size must == int else
  Type error message : size must be an integer
  if size < 0:
  ValueError with message: size must be >= 0

'''


class Square:
    '''
A class with size as private instance attribute

The two underscores made it a privste instance!

To make a class constructor argument optional initialize it to 0

To compare str and int, change str to int by: int(str)

raise is akeyword used to raise an exception

raise TypeError........

raise ValueError.......

    '''

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (int(size) < 0):
            raise ValueError("size must be >= 0")
