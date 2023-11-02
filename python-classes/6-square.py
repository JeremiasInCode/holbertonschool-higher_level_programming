#!/usr/bin/python3
""" Task 6 """


class Square:
    """ A class representing a square. """

    # error by betty.
    error = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize an instance of Square. """

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

        if isinstance(position, tuple):
            try:
                if (isinstance(position[0], int) and
                        isinstance(position[1], int)):
                    if position[0] >= 0 and position[1] >= 0:
                        self.__position = position
                    else:
                        raise ValueError(Square.error)
                else:
                    raise TypeError(Square.error)
            except IndexError:
                print(Square.error)
        else:
            raise TypeError(Square.error)

    @property
    def size(self):
        """ Return the size of the Square as a property """
        return self.__size

    @property
    def position(self):
        """ Return the specific position of the Square as a property """
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """Set the position of the Square."""
        if isinstance(value, tuple):
            try:
                if (isinstance(value[0], int) and isinstance(value[1], int)):
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                    else:
                        raise ValueError(Square.error)
                else:
                    raise TypeError(Square.error)
            except IndexError:
                print(Square.error)
        else:
            raise TypeError(Square.error)

    def area(self):
        "This function to calulate the area of a square"
        area = self.__size ** 2
        return area

    def my_print(self):
        """ prints in stdout the square with the character # """
        cant = self.__size
        if cant == 0:
            print("")
            return
        for element in range(self.__position[1]):
            print("")
        for element1 in range(self.__size):
            for element1 in range(self.position[0]):
                print(" ", end="")
            for element3 in range(self.size):
                print("#", end="")
            print("")
