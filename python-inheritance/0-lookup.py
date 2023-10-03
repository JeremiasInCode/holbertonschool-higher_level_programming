#!/usr/bin/python3
""" Task 0 """


def lookup(obj):
    """ Return the list of available attributes and methods of an object """
    propertys = dir(obj)
    return propertys
