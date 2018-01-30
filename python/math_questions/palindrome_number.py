#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: palindrome_number.py

@desc:  判断是不是回文数

@hint:  得到数的每一位的值
"""


def palindrome_number(n):
    if n < 0:
        return False
    if n == 0:
        return True
    temp = n
    result = 0
    while temp > 0:
        result = result * 10 + temp % 10
        temp = temp // 10
    print(result)
    return result == n


if __name__ == '__main__':
    n = 123321
    palindrome_number(n)