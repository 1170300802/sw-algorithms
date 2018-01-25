#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: insertion_sort.py

@desc: 插入排序

@hint: 和冒泡排序一样，存在一样的优化点
"""

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break




if __name__ == '__main__':
    array = [3, 1, 10, 8, 9,  5, 4, 2, 6, 7, 0]
    print(array)
    insertion_sort(array)
    print(array)