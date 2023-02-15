#!/usr/bin/python3
"""
Introduce class Square inherits from Rectangle
we should import from models the class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Write the class Square that inherits from Rectangle:

       In the file models/square.py
       Class Square inherits from Rectangle
       Class constructor: def __init__(self, size, x=0, y=0, id=None)::
       Call the super class with id, x, y, width and height -
        this super call will use the logic of
         the __init__ of the Rectangle class.
         The width and height must be assigned to the value of size
        You must not create new attributes for this class,
        use all attributes of Rectangle -
       As reminder: a Square is a Rectangle with the same width and height
       All width, height, x and y validation must inherit from Rectangle -
       same behavior in case of wrong data
       The overloading __str__ method should return
       [Square] (<id>) <x>/<y> - <size> - in our case, width or height
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Update the class Square by overriding
        the __str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>"""
        str = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)
        return str

    @property
    def size(self):
        """get a size"""
        return self.width

    @size.setter
    def size(self, value):
        """set a size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes:
            *args is the list of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs can be thought of as a double pointer to a dictionary:
                 key/value (keyworded arguments)"""
        for i in kwargs:
            if (i == 'id'):
                self.id = kwargs[i]
            if (i == 'size'):
                self.size = kwargs[i]
            if (i == 'x'):
                self.x = kwargs[i]
            if (i == 'y'):
                self.y = kwargs[i]
        j = 0
        for i in args:
            if (j == 0):
                self.id = i
            if (j == 1):
                self.size = i
            if (j == 2):
                self.x = i
            if (j == 3):
                self.y = i
            j += 1

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
