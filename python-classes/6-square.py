#!/usr/bin/python3
""" Task 6 """


class Square:
    error = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2 and isinstance(value, tuple):
            x = value
            y = value
            if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
                self.__position = value
            else:
                raise ValueError(Square.error)
        else:
            raise TypeError(Square.error)

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        cant = self.__size
        if cant == 0:
            print("")
            return
        for element in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            print("#", end="")
        print("")
