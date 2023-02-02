#!/usr/bin/python3
"""9-rectangle, built for Holberton Python.
"""


class Rectangle:
    """
    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.height * rect_1.width
        area2 = rect_2.height * rect_2.width
        if area1 >= area2:
            return rect_1
        return rect_2

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

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)


    def __str__(self):
        """Create a new string object from the given object"""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Return the canonical string representation of the object"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """called when an instance of the class is about to be destroyed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
