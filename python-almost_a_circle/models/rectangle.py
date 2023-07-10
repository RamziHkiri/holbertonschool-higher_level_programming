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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value

    @property
    def id(self):
        """id getter"""
        return self.__id

    @id.setter
    def id(self, value):
        """id setter"""
        self.__id = value
