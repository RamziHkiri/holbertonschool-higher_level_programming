#!/usr/bin/python3
"""Define Square class"""


class Square:
    """define fields and methods of Square"""

    def __init__(self, size=0):
        """ Square Constructor.

            args:
                size:size of the square
        """
        self.size = size

    def size(self):
        return self.__size

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    def area(self):
        return self.size * self.size
