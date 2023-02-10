#!/usr/bin/python3

"""
Student to disk and reload
"""


class Student:
    """class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs ==None or not isinstance(attrs, list):
           return self.__dict__ 
        else:
            a = {}
            for i in attrs:
                if not isinstance(i, str):
                    return self.__dict__ 
                if i in self.__dict__.keys():
                    a[i] = self.__dict__[i]
            return a
    
    def reload_from_json(self, json):
        for j in json.keys():
            self.__dict__[j] = json[j]

