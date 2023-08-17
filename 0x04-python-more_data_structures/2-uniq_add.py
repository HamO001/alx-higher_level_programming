#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    new_list = set()
    sum_of_unique = 0

    for num in my_list:
        if num not in new_list:
            new_list.add(num)
            sum_of_unique += num
    return sum_of_unique

