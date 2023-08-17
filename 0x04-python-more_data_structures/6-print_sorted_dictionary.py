#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    key_dictionary = sorted(a_dictionary.keys())
    for key in key_dictionary:
            value = a_dictionary[key]
            print(key, value)
