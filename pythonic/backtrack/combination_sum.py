#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: combination_sum.py

@desc: 和的组合：给定一个集合和目标数字，求集合中任意个数的和为目标数字的所有组合。数字可以重复。

@hint:  set [2, 3, 6, 7] and target 7
"""

def combination_sum(set, target):
    res = []
    set.sort()
    dfs(set, target, 0, [], res)
    return res


def dfs(set, target, index, path, res):
    # print(path)                       #递归函数：在入口处打印变量比较好理解
    if target < 0:
        return                          #backtrack
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(set)):
        dfs(set, target - set[i], i, path + [set[i]], res)

# def dfs(set, target, index, path, res):
#     res.append(path)
#     for i in range(index, len(set)):
#         dfs(set, target, i + 1, path + [set[i]], res)

if __name__ == '__main__':
    s = {2, 3, 6, 7}
    s = list(s)
    target = 7
    r = combination_sum(s, target=7)
    print(r)