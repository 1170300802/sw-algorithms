#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: knaspack.py

@desc: 背包问题：动态规划

@hint:
"""

def knaspack(values, weight, capacity):
    a = [[0 for i in range(capacity + 1)] for j in range(len(values))]
    for i in range(len(a)):
        for j in range(1, len(a[i])):
            if i == 0:
                if weight[i] <= j:
                    a[i][j] = values[i]
            else:
                if j < weight[i]:
                    a[i][j] = a[i-1][j]
                else:
                    a[i][j] = max(a[i-1][j], values[i] + a[i-1][j - weight[i]])
    for i in a:
        print(i)
    return a[-1][-1]


if __name__ == '__main__':
    values = [60, 50, 70, 20]
    weight = [5, 3, 4, 2]
    capacity = 9
    r = knaspack(values, weight, capacity)
    print(r)