#!/usr/bin/python3
from operator import truediv


def islower(c):
    code_ascii = ord(c)
    if code_ascii >= 97 and code_ascii <= 122:
        return True
    else:
        return False
