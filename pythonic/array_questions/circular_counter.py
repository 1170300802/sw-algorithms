#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: circular_counter.py

@desc: 约瑟夫环

@hint:  一般解法和动态规划
"""

#  简单方法：每次移除删除的元素并打印出来:O()
def circular_counter(n, m):
    temp = [i for i in range(1, n + 1)]
    i = 0
    while len(temp) > 1:
        i = (i + m - 1) % len(temp)
        temp.pop(i)
    print(temp[0])

# 动态规划：找状态转移方程
def circular_counter_two(n, m):
    if n < 1 or m < 1:
        return -1
    win_index = [0] * (n + 1)
    for i in range(2, n + 1): # [2: n]
        win_index[i] = (win_index[i - 1] + m) % i
    print(win_index[n] + 1)

if __name__ == '__main__':
    circular_counter(9, 3)
    circular_counter_two(9, 3)