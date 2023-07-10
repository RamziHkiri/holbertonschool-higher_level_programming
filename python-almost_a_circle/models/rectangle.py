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
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area's rectangle method"""
        return self.__width * self.__height

    def display(self):
        """display rectangle using #"""
        rec_string = ""
        rec_string += "\n" * self.__y
        for i in range(0, self.__height - 1):
            rec_string += " " * self.__x + str(
                self.print_symbol) * self.__width + "\n"
        rec_string += " " * self.__x + str(self.print_symbol) * self.__width
        print(rec_string)

    def __str__(self):
        """"""
        string = "[" + self.__class__.__name__ + "] " + (
            "({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height))
        return string

    def update(self, *args):
        """assigns an argument to each attribute"""

        attr = ["id", "width", "height", "x", "y"]
        for i in range(0, len(args)):
            self.__setattr__(attr[i], args[i])
