#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: two_sum.py

@desc: 两数和：给定数组和目标值，求数组中的两个值的和等于给定值，假设有且只有一组解。

@hint: Given nums = [2, 7, 11, 15], target = 9 -->  return [0, 1]
"""

def two_sum(array, k):
    if array is None:
        return None
    temp = {}
    for index, num in enumerate(array):
        if num in temp:
            return [temp[num], index]
        temp.setdefault(k - num, index)

if __name__ == '__main__':
    a = [2,3,4]
    print(a)
    print(two_sum(a, 6))