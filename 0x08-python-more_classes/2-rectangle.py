#!/usr/bin/python3
""" This module defines a rectangle. """


class Rectangle:
    """ This class represents a class rectangle. """
    def __init__(self, width=0, height= 0):
        """ This intance method initializes class instances. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the property width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the property width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the property height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the property height."""
        if not isinstance(value, int):
            raise TypeError("height must  be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area."""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
