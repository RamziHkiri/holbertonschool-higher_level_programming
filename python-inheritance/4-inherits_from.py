#!/usr/bin/python3
"""defie a methode is_same_class"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of the given class.

    args:
        obj: the object to be checked
        a_class:the class that willbe compared with obj type
    Returns:
        if type of obj equal to a_class or inherits from it True
        otherwise false
    """
    if type(obj) == a_class:
        return False
    else:
        if isinstance(obj, a_class):
            return True
        else:
            return False
