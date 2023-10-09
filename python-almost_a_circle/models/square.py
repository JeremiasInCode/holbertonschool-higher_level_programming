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
