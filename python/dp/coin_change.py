#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: coin_change.py

@desc: 硬币找零:如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元

@hint:
"""

import math

def coin_change(coins, value):
    coins.sort()
    a = [math.inf] * (value + 1)
    a[0] = 0
    print(a)
    for i in range(1, len(a)):
        for j in range(len(coins)):
            if coins[j] > i:
                break
            else:
                a[i] = min(a[i - coins[j]] + 1, a[i])
    print(a)
    return a[value]



def coin_change_two(coins, value):
    coins.sort()
    a = [0] * (value + 1)
    find_mid_recursive(coins, value, a)



def find_mid_recursive(coins, value, a):
    if value < 0:
        return math.inf
    if value == 0:
        return 0
    if a[value] != 0:
        return a[value]  # already find it
    min_value = math.inf  #
    for i in range(len(coins)):
        res = find_mid_recursive(coins, value-coins[i], a)
        min_value = min(min_value, res)
    if min_value != math.inf:
        a[value] = min_value + 1
    else:
        a[value] = math.inf
    print(a)
    return a[value]

if __name__ == '__main__':
    coins = [10, 9, 5, 3]
    value = 10
    coin_change(coins, value)
    # coin_change_two(coins, value)