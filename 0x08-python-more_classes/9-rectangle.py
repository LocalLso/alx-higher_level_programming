#!/usr/bin/python3
""" This module defines a rectangle."""


class Rectangle:
    """ This class represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This instance method initializes class instances."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Returns a new rectangle."""
        return (cls(size, size))

    def __str__(self):
        """ Returns a printable represantation of a rectangle.

        With a rectangle represented by # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rep = []
        for i in range(self.__height):
            [rep.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rep.append("\n")
        return ("".join(rep))

    def __repr__(self):
        """ Returns a string representation of a rectangle."""
        rep = "Rectangle(" + str(self.__width)
        rep += ", " + str(self.__height) + ")"
        return (rep)

    def __del__(self):
        """ Called when the instance is destroyed."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
