#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: quick_sort.py

@desc:  快速排序

@hint:
"""

def quick_sort(array, lo, hi):
    if lo >= hi:
        return
    mid = portion_two(array, lo, hi)
    quick_sort(array, lo, mid - 1)
    quick_sort(array, mid + 1, hi)

def portion_two(array, lo, hi):
    i = lo
    j = hi
    while i < j:
        while i < j and array[i] <= array[hi]:
            i += 1
        while i < j and array[j] >= array[hi]:
            j -= 1
        array[i], array[j] = array[j], array[i]
    array[i], array[hi] = array[hi],array[i]
    return i

if __name__ == '__main__':
    array = [3, 1, 10, 8, 9,  5, 4, 2, 6, 7, 0]
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print(array)