#!/usr/bin/python3
"""define function that add an attribute to an existant object """


def add_attribute(obj, att_name, att_val):
    """create function that add an attribute to an object.

    Args:
        obj (any): The object to add an attribute to.
        att_name (str): The name of the attribute to add to obj.
        att_value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, att_name, att_val)
