#!/usr/bin/python3
"""define funtion that write inside file"""


def write_file(filename="", text=""):
    """add text into filename"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
