#!/usr/bin/python3
# 4-only_diff_elements.py

def only_diff_elements(set_1, set_2):
    sort_list = set()
    for element in set_1:
        if element not in set_2:
            sort_list.add(element)
    for element in set_2:
        if element not in set_1:
            sort_list.add(element)
    return sort_list
