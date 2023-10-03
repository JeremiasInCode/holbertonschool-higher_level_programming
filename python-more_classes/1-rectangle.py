#!/usr/bin/python3
""" Task 1 """


class Rectangle:
    """ Empty class for Rectangle """

    def __init__(self, width=0, height=0):
        """Initializate the rectangle."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of Rectangle as a property."""
        return self.__width

    @property
    def height(self):
        """Return the height of Rectangle as a property."""
        return self.__height

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
