#!/usr/bin/python3
"""Define Square class"""


class Square:
    """define fields and methods of Square"""

    def __init__(self, size=0):
        """ Square Constructor.

            args:
                size:size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
