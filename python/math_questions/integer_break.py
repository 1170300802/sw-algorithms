#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: integer_break.py

@desc: 拆分整数成至少两个正整数之和，使其乘积最大 10 = 3+3+4，return 36

@hint:  使用动态规划
"""

def integer_break(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    print(res * n)

def integer_break_two(n):
    a = [0, 0, 1, 2, 4, 6, 9]
    if n <= 6:
        print(a[n])
        return
    for i in range(7, n + 1):
        a.append(3 * a[i - 3])
    print(a[n])



if __name__ == '__main__':
    n = 5
    integer_break_two(n)