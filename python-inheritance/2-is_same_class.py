#!/usr/bin/python3
"""defie a methode is_same_class"""


def is_same_class(obj, a_class):
    """returns true if object is an instance of the given class """
    if type(obj) == a_class:
        return True
    else:
        return False
