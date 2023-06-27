#!/usr/bin/python3
"""Task Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initialize the instance """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print [Square] (<id>) <x>/<y> - <size> """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Private instance attributes,
        Return width of the Rectangle as a property.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """ Sets the width of the Square"""
        self.width = value
        self.height = value
