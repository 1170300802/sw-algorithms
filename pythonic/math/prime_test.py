#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: prime_test.py

@desc: 素数判断

@hint: 速度较快
"""

def prime_test(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        print(j)
        print(j + 2)
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


if __name__ == '__main__':
    a = 139
    print(prime_test(a))