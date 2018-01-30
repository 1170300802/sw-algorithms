#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: water_and_jug_problem.py

@desc: 水罐问题： 给定两个容量分别为x和y升的罐子。提供无限容量的水。你需要判断用这两个罐子是否可以恰好量出z升的体积

@hint:
"""

def water_and_jug_problem(x, y, z):
    if x == z or y == z:
        return True
    if x == 0 or y == 0 or x + y < z:
        return False
    a = getGCD(x, y)
    if z % a == 0:
        return True

def getGCD(x, y):
    if y == 0:
        return x
    return getGCD(y, x % y)


if __name__ == '__main__':
    x = 1
    y = 2
    z = 3
    print( getGCD(8, 12))