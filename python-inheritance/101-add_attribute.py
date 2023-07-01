#!/usr/bin/python3
"""define function that add an attribute to an existant object """


def add_attribute(obj, att_name, att_val):
    if hasattr(obj, "__dict__"):
        setattr(obj, att_name, att_val)
    else:
        raise TypeError("Can't add new attribute")
        
        