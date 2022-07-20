#!/usr/bin/python3
import math


class MagicClass:
    """A Class reprenting a circle"""
    def __init__(self, radius=0):
        """Initialize method of the MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """return the area of MagicClass instance"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """return the circumference of MagicClass instance"""
        return ((2 * math.pi) * self.__radius)
