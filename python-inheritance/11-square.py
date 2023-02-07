#!/usr/bin/python3
"""
Square #2
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from Rectangle """
    def __init__(self, size):
        """private instance/positive validated by
        integer_validator from class basegeometry by super() """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """print format area of rectangle"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
