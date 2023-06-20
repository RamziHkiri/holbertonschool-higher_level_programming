#!/usr/bin/python3
"""Create function tha add two integers"""


def add_integer(a, b=98):
    """ Return sum of two integers a and b
        args:
            a:integer
            b:integer
            return: a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
