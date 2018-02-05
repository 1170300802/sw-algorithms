#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: subsets_unique.py

@desc: 给定一个数组， 包含重复数字，输出数组的子集

@hint: [1,2,2] -> [1,2,2], [1, 2], [2,2], [1] , [2], []
"""


def subsets(array):
    res = set()
    back_track(res, array, [], 0)
    return list(res)

def back_track(res, array, stack, pos):
    if pos == len(array):
        res.add(tuple(stack))
    else:
        stack.append(array[pos])
        back_track(res, array, stack, pos + 1)
        stack.pop()
        back_track(res, array, stack, pos + 1)

if __name__ == '__main__':
    a = [1, 2, 3]
    r = subsets(a)
    print(r)