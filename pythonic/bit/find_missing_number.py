#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: find_missing_number.py

@desc: 寻找缺失数：[0，n]之间求缺失的数，连续整数之前的差为1。若没有，则为n+1.

@hint:  find_missing_number([4, 1, 3, 0, 6, 5, 2])
"""

# 异或运算的性质： x^x=0, x^0=x

#对于这题：[0,n]之间，假设有序，下标和其值异或为0, 0^x = 缺失值。


def find_missing_number(list):
    missing = len(list)
    for index, num in enumerate(list):
        temp = index ^ num
        missing = missing ^ temp
    return missing


if __name__ == '__main__':
    a = [0, 1, 2, 4, 5, 6, 7]
    r = find_missing_number(a)
    print(r)