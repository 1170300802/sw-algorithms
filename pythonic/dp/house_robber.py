#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: house_robber.py

@desc: 打家劫舍：一个数组代表一个街道，数组值表示每家的财富。如果相邻的房子被偷就会报警，求最大值。

@hint:  动态规划
"""

def house_robber(array):
    last, now = 0, 0
    for a in array:
        # print(last, now)
        temp = now
        now = max(last + a, temp)
        last = temp
    return now


if __name__ == '__main__':
    houses = [1, 2, 16, 3, 15, 3, 12, 1]
    r = house_robber(houses)
    print(r)