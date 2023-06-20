#!/usr/bin/python3
""" Task 8 """


class BaseGeometry:
    """ Creation of classes for future tasks. """
    def area(self):
        """ Return Exception area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Class represented a rectangle. """
    def __init__(self, width, height):
        """ Initialize attributes and validations. """
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__height = height
