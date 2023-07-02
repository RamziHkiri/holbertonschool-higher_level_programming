#!/usr/bin/python3
"""define function that append data into file"""


def append_write(filename="", text=""):
    """add content to file in append mode"""

    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
