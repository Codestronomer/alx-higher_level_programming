#!/usr/bin/python3
"""
    filename: 10-student.py

    defines a student class
"""


class Student:
    """represent a student"""
    def __init__(self, first_name, last_name, age):
        """
            Initializes the student instance

            Args:
                arg1: (string)first_name
                arg2: (string)last_name
                arg3: (int)age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            dct = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    dct[k] = v
            return dct
        else:
            return self.__dict__
