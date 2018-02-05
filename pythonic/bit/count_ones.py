#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: count_ones.py

@desc: 1出现的次数：给一个无符号整数，返回 '1' bit出现的次数

@hint:  11 -> 3
"""

def count_ones(num):
    if num < 0:
        return
    res = 0
    while num > 0:
        res += num & 1
        num >>= 1
    return res



if __name__ == '__main__':
    num = 7
    r = count_ones(num)
    print(r)

