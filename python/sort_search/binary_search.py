#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_search.py

@desc: 二分查找

@hint:
"""

def binary_search(array, key):
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) >> 1
        if array[mid] == key:
            return mid
        if array[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

if __name__ == '__main__':
    array = [0, 1, 2, 3, 4,  5, 6, 7, 8, 9, 10, 15]
    result = binary_search(array, 15)
    print(result)