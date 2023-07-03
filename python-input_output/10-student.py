#!/usr/bin/python3
"""define class student"""


class Student:
    """define student"""

    def __init__(self, first_name, last_name, age):
        """class construtor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a dictionary representation of a Student instance """
        if type(attrs) == list and attrs is not None:
            return {attr: getattr(
                self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
