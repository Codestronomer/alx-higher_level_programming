#!/usr/bin/python3
""" This modules defines a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class represent a square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of the Square class"""
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """ String representation of the square class """
        s = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return s

    @property
    def size(self):
        """ getter method for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method for Square class attributes"""
        if args is not None and len(args) != 0:
            attr_arr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr_arr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr_arr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """method returns the dictionary representation of a Square"""
        attr_arr = ['id', 'size', 'x', 'y']
        rtn_dict = {}

        for i in attr_arr:
            if i == 'size':
                rtn_dict[i] = getattr(self, 'width')
            else:
                rtn_dict[i] = getattr(self, i)

        return rtn_dict
