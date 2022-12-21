#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ This class represents a square. """
    def __init__(self, size=0, position=(0, 0)):
        """ Init instances of attributes. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Size setter. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size setter. """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ Position getter. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Position setter. """
        self.__position = value
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculates the current square area. """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Prints in stdout the square with #. """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

