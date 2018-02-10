#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: gcd.py

@desc: 最大公约数最小公倍数

@hint:
"""


def gcd(a, b):
    while True:
        if b == 0:
            return a
        a, b = b, a % b

def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    a = 4
    b = 8
    print(gcd(a, b))
    print(lcm(a, b))
