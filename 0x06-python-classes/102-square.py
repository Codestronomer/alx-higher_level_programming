#!/usr/bin/python3
# 4-square.py
# Rumide John <johnrumide6@gmail.com>
"""Defines a class Square: Access and update private attrs"""


class Square:
    """Class Square representing a square."""
    def __init__(self, size=0):
        """ Initialize method that stores the size of square

        Args:
            param1 (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """ Returns the square object current area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ Getter method for size attribute"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """ Setter method for size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __eq__(self, other):
        """checks for equality with another instance"""
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        """checks if instance is less than another instance"""
        return self.__size < other.__size

    def __le__(self, other):
        """checks if less than or equal to another instance"""
        return self.__size <= other.__size

    def __ne__(self, other):
        """checks if not equal to another instance"""
        return self.__dict__ != other.__dict__

    def __gt__(self, other):
        """checks if greater than another instance"""
        return self.__size > other.__size

    def __ge__(self, other):
        """checks if greater than or equal to another instance"""
        return self.__size >= other.__size
