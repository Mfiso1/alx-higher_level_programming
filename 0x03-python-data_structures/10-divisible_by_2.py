#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for integer_value in my_list:
            if integer_value % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
    else:
        return None
