#!/usr/bin/python3
""" Task 9 """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class represented a rectangle. """
    def __init__(self, width, height):
        """Intialize a rectangule"""
        self.integer_validator(width)
        self.__width = width
        self.integer_validator(height)
        self.__height = height

    def area(self):
        """ Return implementation of area """
        return self.__width * self.__height

    def __str__(self) -> str:
        return (f"[Rectangle] {self.__width}/{self.__height}")
