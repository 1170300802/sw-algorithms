#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: sort_colors.py

@desc: 颜色排序

@hint:
"""

def sort_colors(colors):
    i = j = 0
    for k in range(len(colors)):
        v = colors[k]
        colors[k] = 2
        if v < 2:
            colors[j] = 1
            j += 1
        if v == 0:
            colors[i] = 0
            i += 1
        print(colors)


if __name__ == '__main__':
    nums = [2, 0, 1, 2, 1, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 2]
    sort_colors(nums)
    print(nums)