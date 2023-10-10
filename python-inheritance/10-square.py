#!/usr/bin/python3
""" Task 10 """
BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class represented a rectangle. """
    def __init__(self, size):
        """Intialize a rectangule"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Return implementation of area """
        return self.__size ** 2
