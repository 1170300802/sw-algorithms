#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: max_sum_subarray.py

@desc: 最大子数组的和

@hint:
"""

def max_sum_subarray(array):
    max_so_far = max_now = 0
    for i in range(len(array)):
        max_now = max(array[i], max_now + array[i])
        max_so_far = max(max_so_far, max_now)
    return max_so_far

def max_sum_subarray_two(array):
    result = [0] * len(array)
    result[0] = array[0]
    for i in range(1, len(array)):
        if result[i - 1] + array[i] >= 0:
            result[i] = result[i - 1] + array[i]
        else:
            result[i] = array[i]
    return max(result)

if __name__ == '__main__':
    a = [2, 2, -6, 4, 5, -7, 23]
    print(a)
    r = max_sum_subarray_two(a)
    print(r)
