#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Initialize an instance """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Private instance attributes,
        Return width of the Rectangle as a property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the Rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Private instance attributes,
        Return height of the Rectangle as a property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the Rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Private instance attributes,
        Return x of the Rectangle as a property.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x of the Rectangle. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Private instance attributes,
        Return x of the Rectangle as a property.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Private instance attributes,
        Return y of the Rectangle as a property.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height
