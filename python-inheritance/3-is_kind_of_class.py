#!/usr/bin/python3
"""defie a methode is_same_class"""


def is_same_class(obj, a_class):
    """returns true if object is an instance of the given class.
    
    args:
        obj: the object to be checked
        a_class:the class that willbe compared with obj type
    Returns:
        if type of obj equal to a_class or inherits from it True 
        otherwise false 
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
