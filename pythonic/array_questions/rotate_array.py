#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: rotate_array.py

@desc: 反转数组

@hint:
"""


def rotate_array(array, k):
    if array is None:
        return None
    length = len(array)
    return array[length - k:] + array[:length - k]


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(rotate_array(a, 4))