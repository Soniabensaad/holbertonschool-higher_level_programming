#!/usr/bin/python3
"""
Introduce class Base
"""
import json


class Base:
    """a new class called Base
    Class Base:
     -private class attribute __nb_objects = 0
     -class constructor: def __init__(self, id=None)::
          +if id is not None, assign the public instance attribute id
           with this argument value+
          + increment __nb_objects and assign
          the new value to the public instance attribute id+
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
         of list_dictionaries"""
        if list_dictionaries is None:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:

             list_objs is a list of instances who inherits of Base -
             example: list of Rectangle or list of Square instances
             If list_objs is None, save an empty list
             The filename must be: <Class name>.json - example: Rectangle.json
             You must use the static method to_json_string (created before)
             You must overwrite the file if it already exists"""
        list = []
        filename = f"{cls.__name__}.json"
        if list_objs:
            list = [a.to_dictionary() for a in (list_objs)]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        To use the update method to assign all attributes,
         you must create a “dummy” instance before"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            dummy = cls(1, 0, 0)
        else:
            return None
        dummy.update(**dictionary)
        return dummy
