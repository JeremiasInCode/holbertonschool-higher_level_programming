#!/usr/bin/python3
""" Task 4 """

def inherits_from(obj, a_class):
    if obj is None or type(obj) == a_class:
        return False

    if issubclass(type(obj), a_class):
        return True
    return False
