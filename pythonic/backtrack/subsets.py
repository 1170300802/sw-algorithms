#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: subsets.py

@desc: 子集：给定数组，求该数组的所有子集

@hint: [1, ,2 ,3] -> [ [1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], []]  O(2**n)
"""


def subsets(array):
    res = []
    back_track_two(res, array, [], 0)
    return res

def back_track(res, array, stack, pos):
    if pos == len(array):
        res.append(list(stack))
    else:
        stack.append(array[pos])
        back_track(res, array, stack, pos + 1)
        stack.pop()
        back_track(res, array, stack, pos + 1)


def back_track_two(res, array, cur, pos):
    # print(cur)
    if pos >= len(array):
        res.append(cur)
    else:
        back_track_two(res, array, cur + [array[pos]], pos + 1)
        back_track_two(res, array, cur, pos + 1)

#迭代

def subsets_two(array):
    res = [[]]
    for a in array:
        res += [item + [a] for item in res]
    return res




if __name__ == '__main__':
    a = [1, 2, 3]
    r = subsets_two(a)
    print(r)