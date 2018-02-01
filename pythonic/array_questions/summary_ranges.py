#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: summary_ranges.py

@desc: 数组的范围：given [0,1,2,4,5,7], return ["0->2","4->5","7"].

@hint:
"""


def summary_ranges(array):
    if array is None:
        return None
    res = []
    start = 0
    array.sort()
    for i in range(1, len(array)):
        if array[i] - array[i - 1] == 1:
            pass
        else:
            res.append(get_range(array[start], array[i - 1]))
            start = i
    res.append(get_range(array[start], array[-1]))  #最后一次的结果
    return res


def get_range(lo, hi):
    if lo == hi:
        return str(lo)
    else:
        return str(lo) + "->" + str(hi)


if __name__ == '__main__':
    a = [0, 1, 2, 4, 5, 7]
    print(a)
    print(summary_ranges(a))
