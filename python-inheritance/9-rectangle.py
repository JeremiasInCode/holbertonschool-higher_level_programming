#!/usr/bin/python3
""" Task 9 """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class represented a rectangle. """
    def __init__(self, width, height):
        """ Initialize attributes and validations. """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return implementation of area """
        return self.__width * self.__height

    def str(self) -> str:
        return (f"[Rectangle] {self.__width}/{self.__height}")