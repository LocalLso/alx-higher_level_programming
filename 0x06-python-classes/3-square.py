#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ This class represents the square. """
    def __init__(self, size=0):
        """ Init instance attributes. """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        area = self.__size * self.__size
        return area
