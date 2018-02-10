#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: nth_digit.py

@desc: 第n位数字:123456789101112131415...的第n位数字是什么

@hint:
"""

def nth_digit(n):
    len = 1
    count = 9
    start = 1
    while n > len * count:
        n -= len * count
        len += 1
        count *= 10
        start *= 10
    start += (n - 1) // len
    s = str(start)
    return int(s[(n - 1) % len])


if __name__ == '__main__':
    n = 15
    r = nth_digit(n)
    print(r)