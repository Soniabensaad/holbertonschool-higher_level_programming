#!/usr/bin/python3
"""
Introduce class Rectangle inherits from base
we should import from models the class Base
"""

from models.base import Base


class Rectangle(Base):
    """a class inherits from Base
    class Rectangle that inherits from Base:
       +Class Rectangle inherits from Base
       +Private instance attributes,
       each with its own public getter and setter:
            -__width -> width
            -__height -> height
            -__x -> x
            -__y -> y
        +Class constructor: def __init__(self, width,
        height, x=0, y=0, id=None):
            *Call the super class with id
              - this super call with use the logic
              of the __init__ of the Base class
            *Assign each argument
                width, height, x and y to the right attribute-
    """
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """private instance attributes to Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get to introduce width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set a value to width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get to introduce height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set a value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get to introduce x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set a value to x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get to introduce y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set a value to y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle
        instance with the character #"""
        for space_y in range(self.__y):
            print()
        for b in range(self.__height):
            for space_x in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Update the class Rectangle by overriding
        the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        str = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return str

    def update(self, *args, **kwargs):
        """**kwargs can be thought of as a double pointer to a dictionary: key/value
          As Python doesn’t have pointers,
          **kwargs is not literally a double pointer –
          describing it as such is just a way of explaining
           its behavior in terms you’re already familiar with
          **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance"""
        for i in kwargs:
            if (i == 'id'):
                self.id = kwargs[i]
            if (i == 'width'):
                self.width = kwargs[i]
            if (i == 'height'):
                self.height = kwargs[i]
            if (i == 'x'):
                self.x = kwargs[i]
            if (i == 'y'):
                self.y = kwargs[i]
        """Assign an argument to each attribute:
              -1st argument should be the id attribute
              -2nd argument should be the width attribute
              -3rd argument should be the height attribute
              -4th argument should be the x attribute
              -5th argument should be the y attribute"""
        j = 0
        for i in args:
            if (j == 0):
                self.__id = i
            if (j == 1):
                self.__width = i
            if (j == 2):
                self.__height = i
            if (j == 3):
                self.__x = i
            if (j == 4):
                self.__y = i
            j += 1

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y
        , 'id': self.id, 'height': self.height, 'width': self.width}
