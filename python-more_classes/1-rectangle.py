#!/usr/bin/python3
"""Create an empty class named Rectangle"""


class Rectangle:
    """define the fields and methods here"""

    def __init__(self, width=0, height=0):
        """ Rectangle Constructor.

            args:
                width:width of rectangle
                height:height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """heigth getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
