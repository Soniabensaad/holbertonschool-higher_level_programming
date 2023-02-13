#!/usr/bin/python3
"""
Introduce class Base
"""


class Base:
    """a new class called Base
    Class Base:
     -private class attribute __nb_objects = 0
     -class constructor: def __init__(self, id=None)::
          +if id is not None, assign the public instance attribute id with this argument value+
          + increment __nb_objects and assign the new value to the public instance attribute id+
    """
    """
    private class attribute __nb_objects without function
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            """Access to private class attribute __nb_objects
            without guetter or setter method
            """
            self.id = Base.__nb_objects
