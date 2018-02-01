#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: plus_one.py

@desc: 数组的每一位表示一个0-9的数， 进行加一操作

@hint: [1, 9, 2] -> [1, 9, 3]
"""

def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1): #[n-1:0]
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    if digits[0] == 0:
        digits.insert(0, 1)
    return digits

if __name__ == '__main__':
    a = [1, 9, 9, 9]
    print(plus_one(a))