#!/usr/bin/python3
""" Task 1 """


class Rectangle:
    """ A class representing a rectangle. """
    def __init__(self, width=0, height=0):
        """Initializate the Rectangle."""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Return the height of Rectangle as a property."""
        return self.__height

    @property
    def width(self):
        """Return the width of Rectangle as a property."""
        return self.__width

    @height.setter
    def height(self, value):
        """Set the height to the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Set the width to the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value
