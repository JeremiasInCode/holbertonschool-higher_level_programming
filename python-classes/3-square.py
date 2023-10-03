#!/usr/bin/python3
""" Task 3 """


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        if (type(size) == int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        area = self.__size ** 2
        return area
    pass
