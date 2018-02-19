#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: reverse_string.py

@desc: 反转字符床的多种方法

@hint:

"""


def recursice(s):
    l = len(s)
    if l < 2:
        return s
    return recursice(s[l // 2:]) + recursice(s[: l // 2])


def iterative(s):
    r = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return "".join(r)


def pythonic(s):
    r = list(reversed(s))
    return "".join(r)


def ultra_pythonic(s):
    return s[::-1]


if __name__ == '__main__':
    s = "hello world"
    r = ultra_pythonic(s)
    print(r)