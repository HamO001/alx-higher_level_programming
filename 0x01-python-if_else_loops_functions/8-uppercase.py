#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            diff = ord('A') - ord('a')
            print(chr(ord(c) + diff), end="")
        else:
            print(c, end="")
    print("")
