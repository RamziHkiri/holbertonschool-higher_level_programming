#!/usr/bin/python3
def islower(c):
    code_ascii = ord(c)
    if code_ascii >= 97 and code_ascii <= 122:
        return True
    else:
        return False
