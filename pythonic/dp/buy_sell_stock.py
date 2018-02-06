#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: buy_sell_stock.py

@desc:  股票买卖:一个数组代表i天股票的交易价格，求最大获益值。

@hint: [7, 1, 5, 3, 6, 4] -> 5, 不能是6， 买进才能卖出
        [7, 5, 4, 3] -> 0,连续跌，不发生交易
"""

#1. 只允许一次交易，即一次买进，一次卖出

# 暴力搜索
def max_profit(array):
    max_profit = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            max_profit = max(max_profit, array[j] - array[i])
    return max_profit

def max_profit_dp(array):
    cur_min = array[0]
    max_so_far = 0
    for i in range(len(array)):
        cur_min = min(cur_min, array[i])
        max_so_far = max(max_so_far, array[i] - cur_min)
        # print(cur_min, max_so_far)
    return max_so_far



if __name__ == '__main__':
    a = [7, 2, 5, 3, 6, 1]
    # a = [7, 6, 5, 4, 3, 1]
    r = max_profit_dp(a)
    print(r)