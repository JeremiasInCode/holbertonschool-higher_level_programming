#!/usr/bin/python3
""" Task 3 """


class Rectangle:
    """Representation for Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializate the rectangle."""

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
    def width(self):
        """Return the width of Rectangle as a property."""
        return self.__width

    @property
    def height(self):
        """Return the height of Rectangle as a property."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        area = self.__width * self.height
        return area

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """ Print rectangle. """
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height - 1):
            print("#" * self.__width)
        print('#' * self.__width, end="")
        return ''

    def __repr__(self):
        """Return a formal representation of the Rectangle"""
        string = f"Rectangle({self.__width}, {self.__height})"
        return string