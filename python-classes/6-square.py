#!/usr/bin/python3
"""
class that defines a square
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """get value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if ((len(value)) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """return square area"""
        area = self.__size ** 2
        return area

    def my_print(self):
        """prints line"""
        if self.__size == 0:
            print()
        else:
            for p in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
