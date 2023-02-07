#!/usr/bin/python3
"""
Geometry module
"""

class BaseGeometry:
    """ a class named BaseGeometry """
    def area(self):
        """raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validate value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
