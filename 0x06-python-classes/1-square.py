#!/usr/bin/python3

'''
a class 'square' that define a square by

* private instance attribute: size
* instantiation with size no type or value

'''


class Square:
    '''
A class with size as private instance attribute

	The two underscores made it a privste instance!
    '''
    def __init__(self, size):
        self.__size = size
