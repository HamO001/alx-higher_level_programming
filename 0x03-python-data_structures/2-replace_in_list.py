#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    list_length = len(my_list)
    
    if idx < 0 or idx >= list_length:
        return my_list
    
    my_list[idx] = element
    return my_list
