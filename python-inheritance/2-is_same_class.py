#!/usr/bin/python3
""" Task 2 """

def is_same_class(obj, a_class):
    """ True if the object is exactly an instance of the specified class, otherwise False. """
    if not isinstance(obj, a_class):
        return False
    return True
