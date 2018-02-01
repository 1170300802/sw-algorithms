#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: missing_ranges.py

@desc: 寻找给定范围内数组中缺失的内容。

@hint: ex) [3, 5] lo=1 hi=10 => answer: [1->2, 4, 6->10]
"""

def missing_ranges(nums, lo, hi):
    if lo > hi:
        return None
    if nums is None:
        return [].append(get_range(lo, hi))
    nums.sort()
    res = []
    start = lo
    for i in nums:
        if start > i:
            continue
        if start == i:
            start += 1
            continue
        if start < i:
            res.append(get_range(start, i - 1))
            start = i + 1
    if start <= hi:
        res.append(get_range(start, hi))
    return res

def get_range(lo, hi):
    if lo == hi:
        return str(lo)
    else:
        return str(lo) + "->" + str(hi)

if __name__ == '__main__':
    nums = [3,4,  5, 10, 11, 12, 15, 19]
    print("original:", nums)
    print("missing range: ", missing_ranges(nums, 0, 20))
