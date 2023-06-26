#!/usr/bin/python3
"""Task 1"""


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize an instance abd verify if id is None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
        self.id = Base.__nb_objects
