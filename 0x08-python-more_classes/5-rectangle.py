#!/usr/bin/python3
""" This module defines a rectangle."""


class Rectangle:
    """ This class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """This instance method initializes class instances."""
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
        """ Gets the property height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
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

    def __str__(self):
        """ Returns a printable represantation of a rectangle.

        With a rectangle represented by # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_repr = []
        for i in range(self.__height):
            [rect_repr.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect_repr.append("\n")
        return ("".join(rect_repr))

    def __repr__(self):
        """ Returns a string representation of a rectangle."""
        rect_repr = "Rectangle(" + str(self.__width)
        rect_repr += ", " + str(self.__height) + ")"
        return (rect_repr)

    def __del__(self):
        """ Called when the instance is destroyed."""
        print("Bye rectangle...")
