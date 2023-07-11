#!/usr/bin/python3
"""define a class Base"""
import json


class Base:
    """creation of the classe base methods and fields"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base Constructor.

            args:
                id: id of an instance
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation

        Args:
            list_dictionaries (dictionary): _description
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
