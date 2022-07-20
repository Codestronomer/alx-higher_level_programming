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

    def my_print(self):
        """prints in stdout the square with the character #"""
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
