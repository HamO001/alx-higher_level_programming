#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            diff = ord('A') - ord('a')
            result += chr(ord(c) + diff)
        else:
            result += c
    print(result)
