#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: add_binary.py

@desc: 二进制字符串相加

@hint:

a = "11"
b = "1"
sum = "100"
"""

def add_binary(a, b):
    s = ""
    c, i, j = 0, len(a) - 1, len(b) - 1
    zero = ord('0')
    while i >= 0 or j >= 0 or c == 1:
        if i >= 0:
            c += ord(a[i]) - zero
            i -= 1
        if j >= 0:
            c += ord(b[j]) - zero
            j -= 1
        s = chr(c % 2 + zero) + s
        c //= 2
    return s

if __name__ == '__main__':
    a = "1111"
    b = "101"
    r = add_binary(a, b)
    print(r)