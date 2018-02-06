#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: single_number.py

@desc: 寻找出现一次的数

@hint:
"""

#数组里面每个数出现2次，其中一个只出现一次，求出这个数
def single_number(list):
    res = 0
    for num in list:
        res = res ^ num
    return res

#还是同一个数组，每个数出现3次。其中一个数出现一次，求出这个数。
def single_number_two(list):
    res = 0
    for i in range(32):
        count = 0
        for num in list:
            count += ((num >> i) & 1)
        res = res | ((count % 3) << i)
    if res >= 2 ** 31:
        res -= 2 ** 32
    return res

if __name__ == '__main__':
    a = [2, 2, 3, 5, 3, 4, 5, 7, 7]
    r = single_number(a)
    print(r)
    b = [2, 2, 2, 3, 3, 3, 5]
    r = single_number_two(b)
    print(r)
