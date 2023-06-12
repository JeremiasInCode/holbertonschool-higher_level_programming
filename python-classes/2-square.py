#!/usr/bin/python3
""" Task 2 """


class Square:
    """A class representing a square."""
    def __init__(self, size) -> 0:
        if (type(size) == int):
            if (size < 0):
                TypeError("size must be >= 0")
            else:
                self.__size = size
        else:
            TypeError("size must be an integer")
