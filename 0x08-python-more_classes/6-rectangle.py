#!/usr/bin/python3
# 6-rectangle.py
""" Defines a rectangle class:"""


class Rectangle:
    """ A class representing a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initiatization an instance when an object is created

        Args:
            param1 (int): width of the rectangle
            param2 (int): height of the rectangle
            param3 (int): number of instances of the rectangle class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle class"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle class"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Method calculates the area of the rectangle

        Returns:
            area of the rectangle

        """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Method calculates the perimeter of the rectangle

        Returns:
            Perimeter of the rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """string representation of the rectangle

        Returns:
            returns the string representation of the object
        """
        rtn_str = ''
        if self.__width == 0 or self.__height == 0:
            return rtn_str
        for i in range(self.__height):
            for j in range(self.__width):
                rtn_str += '#'
            if i != (self.__height - 1):
                rtn_str += '\n'
        return (rtn_str)

    def __repr__(self):
        """A string representation of the rectangle to be able to
        recreate a new instance by using eval()

        Returns:
            returns the string representation that can use eval()

        """
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        """Called when all references to the object is deleted

        Returns:
            Nothing"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
