#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: flatten.py

@desc: 数组中可能有内嵌数组，将所有的内嵌数组展开

@hint:
"""

def flatten(l, a=None):
    for i in l:
        if isinstance(i, (list, tuple)):  #多重嵌套, 递归解决
            a = flatten(i, a)
        else:
            a.append(i)
    return a



if __name__ == '__main__':
    l = [2, 1, [3, [4, [5]], 6], 7, [8]]
    a = []
    flatten(l, a)
    print(a)
