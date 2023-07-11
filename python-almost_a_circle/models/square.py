#!/usr/bin/python3
"""define a class Rectangle inherit from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """d"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor of square object

        Args:
            size (int): size of Square
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value