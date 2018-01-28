#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: knapsack_01.py

@desc: 01背包问题： 给定n种物品和一背包，物品i的重量是wi，其价值是pi，背包的容量是M，问如何选择装入背包中的物品总价值最大

@hint: dp，子集合的变种问题:即a[i][j]表示前i件物品恰放入一个容量为j的背包可以获得的最大价值
"""

def knaspack_01(values, weights, k):
    a = [[0 for i in range(k + 1)] for j in range(len(values))]
    for i in range(len(a)):
        for j in range(1, len(a[i])):
            if i == 0:
                if weights[i] <= j:
                    a[i][j] = values[i]
            else:
                if j < weights[i]:
                    a[i][j] = a[i-1][j]
                else:
                    a[i][j] = max(a[i-1][j], values[i] + a[i-1][j - weights[i]])



    for i in a:
        print(i)


if __name__ == '__main__':
    values = [1, 4, 5, 10]
    weights = [1, 3, 4, 5]
    k = 7
    knaspack_01(values, weights, k)