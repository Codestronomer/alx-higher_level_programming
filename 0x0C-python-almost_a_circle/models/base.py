#!/usr/bin/python3
""" defines a Base class """
import json

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
    def create(cls,**dictionary):
        """returns an instance with all attributes already set"""
        if cls is Base:
            raise Exception("Must be called via a subclass")
        dum = cls(1, 2, 4, 5)
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
            
