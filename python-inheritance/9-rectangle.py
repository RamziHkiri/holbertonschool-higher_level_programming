#!/usr/bin/python3
"""Create an empty class named BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define the fields and methods here"""

    def __init__(self, width, height):
        """ Rectangle Constructor.

            args:
                size:size of the square
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        rec_str = "[Rectangle] " + "{}/{}".format(self.__width, self.__height)
        return rec_str
