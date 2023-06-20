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

    def area(self):
        """calculate the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rec_string = ""
            for i in range(0, self.__height - 1):
                rec_string += "#" * self.__width + "\n"
            rec_string += "#" * self.__width
            return rec_string
