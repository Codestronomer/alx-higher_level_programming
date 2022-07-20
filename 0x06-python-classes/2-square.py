#!/usr/bin/python3
# 2-square.py
# Rumide John <johnrumide6@gmail.com>
"""Defines a class Square: Size validation"""


class Square:
    """Class Square representing a square."""
    def __init__(self, size=0):
        """ Initialize method that stores the size of square

        Args:
            param1 (int): size of the square
        """
        if type(size) == int:
            if size > 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
