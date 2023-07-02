#!/usr/bin/python3
"""define function returns the JSON representation of an object"""
import json


def from_json_string(my_str):
    """return the JSON representation of an object"""

    x = json.loads(my_str)
    return x
