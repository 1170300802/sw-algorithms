#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: power_of_two.py

@desc: 2的n次方判断

@hint:
"""

def is_power_of_two(n):
    # if n == 0:
    #     return True
    # r = n & (n - 1)
    # if r == 0:
    #     return True
    # return False
    return n > 0 and not n & (n - 1)


if __name__ == '__main__':
    n = 16
    r = is_power_of_two(n)
    print(r)