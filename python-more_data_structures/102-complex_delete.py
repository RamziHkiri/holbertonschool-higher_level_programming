#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_a_dictionary = a_dictionary.copy()
    for key in new_a_dictionary:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
