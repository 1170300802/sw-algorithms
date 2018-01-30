#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: math_pow.py

@desc: 求幂运算

@hint:
"""

def math_pow(x, n):
    temp = x
    if n == 0:
        return 1
    temp = math_pow(x, n // 2)
    if n % 2 == 0:
        return temp * temp
    else:
        if n > 0:
            return temp * temp * x
        else:
            return temp * temp // x



if __name__ == '__main__':
    x = 2
    n =10
    r = math_pow(x, n)
    print(r)