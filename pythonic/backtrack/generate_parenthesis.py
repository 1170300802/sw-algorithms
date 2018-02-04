#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: generate_parenthesis.py

@desc: 括号生成：给定n组括号，求出所有满足的括号组合

@hint:
"""

def generate_parenthesis(n):
    res = []
    add_pair(res, "", n, 0)
    return res


def add_pair(res, temp_s, left, right):
    print(temp_s)
    if left == 0 and right == 0:
        res.append(temp_s)
        return
    if left > 0:
        add_pair(res, temp_s + "(", left - 1, right + 1)
    if right > 0:
        add_pair(res, temp_s + ")", left, right - 1)


if __name__ == '__main__':
    a = 3
    r = generate_parenthesis(a)
    print(r)