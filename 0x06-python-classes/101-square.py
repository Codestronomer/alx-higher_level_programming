#!/usr/bin/python3
# -square.py
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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
    def position(self, position):
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
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    def __str__(self):
        """return string representation of the square with the character #"""
        rtn_str = ""
        if not self.__size:
            return rtn_str
        for i in range(self.__position[1]):
            rtn_str += "\n"
        for i in range(0, self.__size):
            for k in range(self.__position[0]):
                rtn_str += " "
            for j in range(self.__size):
                rtn_str += "#"
            if i is not (self.__size - 1):
                rtn_str += "\n"

        return rtn_str
