#!/usr/bin/python3
"""Create an empty class named BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """define the fields and methods here"""

    def __init__(self, size):
        """ Rectangle Constructor.

            args:
                size:size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
