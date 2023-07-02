#!/usr/bin/python3
""" define """
import json


def load_from_json_file(filename):
    """load data from json file"""

    with open(filename, 'r') as f:
        return json.load(f)
