#!/usr/bin/python3
""" Defines a rectange class that inherits from BASE"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectange class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of the rectangle class

        Args:
            arg1 = (int)width
            arg2 = (int)height
            arg3 = (int)x
            arg3 = (int)y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value
        else:
            raise TypeError("width should be an integer")

    @property
    def height(self):
        """ getter method for height

        Return: height of object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height"""
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
        else:
            raise TypeError("height should be an integer")

    @property
    def x(self):
        """ getter method for x

        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """getter method for y

        return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ Calculates and returns the area of a the Rectangle instance """
        return (self.__width * self.__height)

    def display(self):
        """prints out the Rectangle instance with the character '#' """
        import sys

        for i in range(self.__y):
            sys.stdout.write('\n')
        for j in range(self.__height):
            for k in range(self.__x):
                sys.stdout.write(" ")
            for l in range(self.__width):
                sys.stdout.write("#")
            if j != (self.__height):
                sys.stdout.write('\n')

    def __str__(self):
        """string representation of the rectangle class"""
        s = f"[Rectangle] ({self.id}) "
        s += f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return s

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            attr_arr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_arr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method returns the dictionary representation of a Rectangle"""
        attr_arr = ['id', 'width', 'height', 'x', 'y']
        rtn_dict = {}

        for i in attr_arr:
            rtn_dict[i] = getattr(self, i)
        return rtn_dict
