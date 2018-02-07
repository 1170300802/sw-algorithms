#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: combination_sum.py

@desc: 和组合问题：给定包含正整数并且无重复的数组，找出所有和为给定数的情况

@hint:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

"""


def combination_sum(array, target):
    comb = [0] * (target + 1)
    comb[0] = 1
    for i in range(len(comb)):
        for j in range(len(array)):
            if i - array[j] >= 0:
                comb[i] += comb[i - array[j]]
    print(comb)
    return comb[target]


if __name__ == '__main__':
    array = [1, 3]
    target = 4
    r = combination_sum(array, target)
    print(r)
