#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: merge_sort.py

@desc: 归并排序：应用很多

@hint: 借助而外的数组实现
"""

def merge_sort(array):
    temp_array = [0] * len(array)
    sort(array, 0, len(array) - 1, temp_array)


def sort(array, lo, hi, temp_array):
    if lo >= hi :
        return
    mid = (lo + hi) >> 1
    sort(array, lo, mid, temp_array)
    sort(array, mid + 1, hi, temp_array)
    merge(array, lo, mid, hi, temp_array)

def merge(array, lo, mid, hi, temp_array):
    for i in range(lo, hi + 1):
        temp_array[i] = array[i]
    print(temp_array)
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            array[k] = temp_array[j]
            j += 1
        elif j > hi:
            array[k] = temp_array[i]
            i += 1
        elif temp_array[i] <= temp_array[j]:
            array[k] = temp_array[i]
            i += 1
        else:
            array[k] = temp_array[j]
            j += 1



if __name__ == '__main__':
    array = [3, 1, 2]
    print(array)
    merge_sort(array)
    print(array)