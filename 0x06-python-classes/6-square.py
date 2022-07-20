#!/usr/bin/python3
# 6-square.py
# Rumide John <johnrumide6@gmail.com>
"""Defines a class Square: Coordinates of a square"""


class Square:
    """Class Square representing a square."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize method that stores the size of square

        Args:
            param1 (int): size of the square
            param2 (tuple): coordinates of a square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ retrieves the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """ sets the position of the square"""
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """prints in stdout the square with the character #"""
        if not self.__size:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
