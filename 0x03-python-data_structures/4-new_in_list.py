#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    length_list = len(my_list)

    if idx < 0 or idx >= length_list:
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
