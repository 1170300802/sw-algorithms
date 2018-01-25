#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: bubble_sort.py

@desc: 冒泡排序

@hint:
"""

# 从小到大排序，每一趟保证最后一个有序
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]


#有一处优化：当前次遍历没有数据交换，则有序。后面不用再继续遍历
def bubble_sort_two(array):
    for i in range(len(array)):
        sorted = True
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
                sorted = False
        if sorted:
            break

if __name__ == '__main__':
    array = [3, 1, 10, 8, 9,  5, 4, 2, 6, 7, 0]
    print(array)
    bubble_sort_two(array)
    print(array)