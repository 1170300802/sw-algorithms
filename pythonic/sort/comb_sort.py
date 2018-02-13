#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: comb_sort.py

@desc:  梳排序

@hint: 冒泡排序的改良版
"""

from math import floor

def comb_sort(array):
    n = len(array)

    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(floor(gap / shrink))
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False
            i += 1


if __name__ == '__main__':
    array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
             4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print(array)
    comb_sort(array)
    print(array)