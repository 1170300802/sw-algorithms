#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: counting_sort.py

@desc: 计数排序， 空间换时间

@hint:
"""

def counting_sort(array):
    min_data = 0
    max_data = 0
    for i in range(len(array)):
        min_data = min(array[i], min_data)
        max_data = max(array[i], max_data)
    temp_array = [0] * (max_data - min_data + 1)
    for i in range(len(array)):
        temp_array[i - min_data] += 1

    index = 0
    for i in range(len(array)):
        array[i] = index + min_data
        temp_array[index] -= 1
        if temp_array[index] == 0:
            index += 1

if __name__ == '__main__':
    array = [3, 1, 10, 8, 9,  5, 4, 2, 6, 7, 0]
    print(array)
    counting_sort(array)
    print(array)