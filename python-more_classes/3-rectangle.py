#!/usr/bin/python3
"""3-rectangle, built for Holberton Python.
"""


class Rectangle:
    """
    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.
        Returns:
            __width (int): horizontal dimension of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle
        Attributes:
            __width (int): horizontal dimension of rectangle
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.
        Returns:
            __height (int): vertical dimension of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle
        Attributes:
            __height (int): vertical dimension of rectangle
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns:
            area (int): area of rectangle
        """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """
        Returns:
           perimeter (int): perimeter of rectangle
        """
        perimeter = (self.__height + self.__width) * 2
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return perimeter

    def __str__(self):
        """Create a new string object from the given object"""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += "#"
                rectangle += "\n"
        return rectangle[:-1]
        
