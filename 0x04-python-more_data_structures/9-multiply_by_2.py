#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for integers in a_dictionary:
        new_dict[integers] = a_dictionary[integers] * 2
    return new_dict
