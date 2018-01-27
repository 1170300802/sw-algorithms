#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: fibonacci_number.py

@desc:  斐波那契数列

@hint:
"""

def fib(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    f1 = 1
    f2 = 2
    while f1 < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f1

def fib_two(a, n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if a[n] != 0:
        return a[n]
    a[n] = fib_two(a, n - 1) + fib_two(a, n - 2)
    return a[n]


