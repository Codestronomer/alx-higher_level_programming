#!/usr/bin/python3
""" defines a Base class """
import json
import csv
import turtle
from random import Random


class Base:
    """ represents a Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes an instance of the class

        Args:
            id = (int)id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation of
        list_dictiionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = f"{cls.__name__}.json"
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls is Base:
            raise Exception("Must be called via a subclass")
        dum = cls(1, 1, 0, 0)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as f:
                str = f.read()
        except FileNotFoundError:
            str = ""
        json_list = cls.from_json_string(str)
        inst_list = []
        for i in json_list:
            inst_list.append(cls.create(**i))
        return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes objects into a csv file"""
        filename = f"{cls.__name__}.csv"

        if (type(list_objs) != list) and list_objs is not None:
            raise TypeError("list_objs must be a list of instances")

        with open(filename, 'w') as csvfile:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializees CSV format from a csv file"""
        filename = f"{cls.__name__}.csv"
        list_objs = []

        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)

                for i in reader:
                    for k, v in i.items():
                        i[k] = int(v)
                    list_objs.append(cls.create(**i))
        except FileNotFoundError:
            pass

        return list_objs

    @staticmethod
    def draw(rectangles_arr, squares_arr):
        """
        Draws rectangles and squares with turtle graphics
        """

        width, height = 200, 150
        ts = turtle.getscreen()
        turtle.screensize(width, height)
        turtle.setworldcoordinates(0, 0, width, height)
        turtle.pensize(5)
        shapes = rectangles_arr + squares_arr
        for shape in shapes:
            fill_color = (random(), random(), random())
            pen_color = (random(), random(), random())
            turtle.color(fill_color, pen_color)
            turtle.setpos((shape.x, shape.y))
            turtle.down()
            turtle.begin_fill()
            for i in range(2):
                turtle.forward(shape.height)
                turtle.left(90)
                turtle.forward(shape.width)
                turtle.left(90)
            turtle.end_fill()
            turtle.up()
        ts.exitonclick()
