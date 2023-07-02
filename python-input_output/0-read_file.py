#!/usr/bin/python3
"""define function that read data from file"""


def read_file(filename=""):
    """reading and printing data from file"""

    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
