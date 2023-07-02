#!/usr/bin/python3
"""define function returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object"""

    x = json.dumps(my_obj)
    return x
