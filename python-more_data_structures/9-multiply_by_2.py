#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult_dic = {}
    for key in a_dictionary:
        mult_dic[key] = a_dictionary[key] * 2
    return mult_dic
