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
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculates the current square area. """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Prints in stdout the square with #. """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                if self.__position[1] > 0:
                    print(""*self.__position[0]+"#"*self.__size)
                else:
                    print(" "*self.__position[0]+"#"*self.__size)
