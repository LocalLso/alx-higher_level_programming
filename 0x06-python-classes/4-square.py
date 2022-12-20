#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ This class represents a square. """
    def __init__(self, size=0):
        """ This init instance attributes. """
        self.size = size

    @property
    def size(self):
        """ Size getter. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size setter or mutator. """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates current area. """
        area = self.__size * self.__size
        return area
