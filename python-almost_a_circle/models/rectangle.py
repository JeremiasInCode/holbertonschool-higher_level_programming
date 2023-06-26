#!/usr/bin/python3
"""Task 2"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize an instance """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        pass

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
        pass

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
        pass

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
        pass
