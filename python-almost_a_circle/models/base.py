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

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (list): _description_
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_objs_to_dict = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(list_objs_to_dict))

    @staticmethod
    def from_json_string(json_string):
        """define static method return the list of the json string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
