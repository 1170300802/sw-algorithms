#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: longest_increasing_subsequence.py

@desc: 最长递增子序列

@hint:
"""

def longest_increasing_subsequence(array):
    a = [1] * len(array)
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i]:
                a[i] = max(a[i], a[j] + 1)
        print(a)
    return max(a)


if __name__ == '__main__':
    array = [1, 101, 10, 2, 3, 100, 4, 6, 2]
    r = longest_increasing_subsequence(array)
    print(r)