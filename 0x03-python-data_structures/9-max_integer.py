#!/usr/bin/python3

def max_integer(my_list=[]):
    max_value = None
    for integer_value in my_list:
        if max_value is None or integer_value > max_value:
            max_value = integer_value
    return max_value
