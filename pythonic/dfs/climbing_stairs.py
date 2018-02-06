#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: climbing_stairs.py

@desc: 爬梯子问题：n阶的梯子，每次可以爬1或2阶， 其所有可能的情况

@hint:
"""

def climbing_stairs(n):
    if n <= 1:
        return n
    temp = [0] * (n + 1)
    temp[1] = 1
    temp[2] = 2
    for i in range(3, len(temp)):
        temp[i] = temp[i - 1] + temp[i - 2]
    return temp[n]

def climbing_stairs_two(n):
    arr = [1, 1]
    for i in range(2, n + 1):
        arr.append(arr[-1] + arr[-2])
    return arr[-1]

def climbing_stairs_three(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n = 5
    r = climbing_stairs_two(n)
    print(r)