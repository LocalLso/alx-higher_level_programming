#!/usr/bin/python3
""" This module defines a rectangle. """


class Rectangle:
    """ This class represnets a rectangle. """

    def __init__(self, width=0, height=0):
        """ This initialize the instances of the class. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
