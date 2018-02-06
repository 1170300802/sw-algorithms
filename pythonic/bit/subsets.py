#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: subsets.py

@desc: 子集问题：给定数组(无重复元素），求出所有子集

@hint:  怎么用位运算来做：[1,2,3] -> {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}  一共2^3=8个结果，每个元素选或不选两种可能。

0) 0 0 0  -> Dont take 3 , Dont take 2 , Dont take 1 = { }
1) 0 0 1  -> Dont take 3 , Dont take 2 ,   take 1    = { 1 }
2) 0 1 0  -> Dont take 3 ,    take 2   , Dont take 1 = { 2 }
3) 0 1 1  -> Dont take 3 ,    take 2   ,   take 1    = { 1 , 2 }
4) 1 0 0  ->    take 3   , Dont take 2 , Dont take 1 = { 3 }
5) 1 0 1  ->    take 3   , Dont take 2 ,   take 1    = { 1 , 3 }
6) 1 1 0  ->    take 3   ,    take 2   , Dont take 1 = { 2 , 3 }
7) 1 1 1  ->    take 3   ,    take 2   ,   take 1    = { 1 , 2 , 3 }

"""

def subsets(array):
    array.sort()
    total = pow(2, len(array))
    res = [] * total
    res2 = [] * total     #返回所有的组合情况: [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    for i in range(total):
        res.append([])
        res2.append([])

    for i in range(len(array)):
        for j in range(total):
            res2[j].append((j >> i) & 1)
            if ((j >> i) & 1) > 0:
                res[j].append(array[i])
    return res, res2

if __name__ == '__main__':
    a = [2, 3, 1]
    r, r2 = subsets(a)
    print(r)
    print(r2)