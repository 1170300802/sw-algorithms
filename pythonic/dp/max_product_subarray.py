#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: max_product_subarray.py

@desc: 最大子数组积

@hint:
"""

def max_product_subarray(array):
    t_min = t_max = r_max = 1
    for i in range(len(array)):
        t1 = array[i] * t_max
        t2 = array[i] * t_min
        t_max = max(max(t1, t2), array[i])
        t_min = min(min(t1, t2), array[i])
        r_max = max(t_max, r_max)
        print(t_min, t_max, r_max)
    return r_max


if __name__ == '__main__':
    array = [2,3,-3,4]
    r = max_product_subarray(array)
    print(r)