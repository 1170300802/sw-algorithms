#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: selection_sort.py

@desc:  选择排序

@hint:
"""

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

if __name__ == '__main__':
    array = [3, 1, 10, 8, 9,  5, 4, 2, 6, 7, 0]
    print(array)
    selection_sort(array)
    print(array)