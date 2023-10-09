"""Task 1"""
import json


class Base:
    """ Define a private attribute """
    __nb_objects = 0
    """ Class constructor"""
    def __init__(self, id=None):
        """
            Initialize an instance abd verify if id is None
        """
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
