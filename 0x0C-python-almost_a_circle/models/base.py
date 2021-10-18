#!/usr/bin/python3
"""This module creates the Base class"""


import json
from os import path


class Base:

    """A class named Base
    Attributes:
    attr1(__nb_objects): number of objects
    attr2(id): object id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiliazes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        list_dictionaries = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
                file.write(Base.to_json_string(list_dictionaries))
            return
        for model in list_objs:
            list_dictionaries.append(model.to_dictionary())
        with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
            file.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        L = []
        if json_string is None or json_string == "":
            return L
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create a dummy
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
