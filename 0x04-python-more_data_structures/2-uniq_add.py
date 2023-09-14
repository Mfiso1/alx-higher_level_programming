#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set(my_list)
    results = 0
    for number in unique_values:
        results += number
    return results
