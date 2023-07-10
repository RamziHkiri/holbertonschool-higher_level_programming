#!/usr/bin/python3
"""define a class Rectangle inherit from Base"""
from models.base import Base


class Rectangle(Base):
    """Creation of the Rectangle class define methods and fields
    args:
        width:rectangle width
        height: rectangle height
        x: x value
        y: y value
        id:the id of the rectangle instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
