#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: permute.py

@desc:排列：给定一个数组，输出其元素的全排列

[1,2,3] -》  [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2],  [3,2,1] ]

@hint:
"""

def permutes(array):
    perms = [[]]
    for n in array:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms


# dfs
def permutes_two(array):
    res = []
    dfs(res, array, [])
    return res


def dfs(res, array, path):
    # print(path)
    if not array:
        return res.append(path)
    for i in range(len(array)):
        dfs(res, array[:i] + array[i+1:], path+[array[i]])

if __name__ == '__main__':
    array = [1, 2, 3]  # list 为None 或者[] ,bool(array) = False
    r = permutes_two(array)
    print(r)

