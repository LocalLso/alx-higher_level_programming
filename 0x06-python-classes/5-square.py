#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ This class represents a square. """
    def __init__(self, size=0):
        """ Init instance attributes. """
        self.size = size

    @property
    def size(self):
        """ Size getter. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size setter. """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the current area. """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Prints in stdout the square with # """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                print("#"*self.__size)
