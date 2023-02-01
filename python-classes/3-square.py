#!/usr/bin/python3
"""
class that defines a square
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """initialize data"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return square area"""
        area = self.__size ** 2
        return area
