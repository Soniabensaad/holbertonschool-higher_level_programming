#!/usr/bin/python3
"""
Full rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """width and height must be positive integers,
         validated by integer_validator"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """print format area of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
