#!/usr/bin/python3
"""
class that defines a square
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.__size = size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return square area"""
        area = self.__size ** 2
        return area
