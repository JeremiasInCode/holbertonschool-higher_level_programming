#!/usr/bin/python3
""" Task 3 """


def is_kind_of_class(obj, a_class):
    if obj is None or not isinstance(obj, a_class):
        return False
    return True
