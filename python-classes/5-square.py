#!/usr/bin/python3
""" Task 5 """


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


    @property
    def size(self):
        """Return the size of the Square as a property."""
        return self.__size


    @size.setter
    def size(self, value):
        """ Sets the size of the Square. """

        if (type(value) == int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")


    def area(self):
        """ Return the area of the Square. """
        area = self.__size ** 2
        return area


    def my_print(self):
        """ prints in stdout the square with the character # """
        cant = self.__size
        if (cant == 0):
            print("")
            return
        for first_element in range(0, cant):
            for second_element in range(0, cant):
                print("#", end="")
            print("")
    pass
