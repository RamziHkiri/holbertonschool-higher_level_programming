#!/usr/bin/python3
"""define a class Base"""


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
