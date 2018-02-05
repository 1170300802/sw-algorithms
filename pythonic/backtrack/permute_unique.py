#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: permute_unique.py

@desc:给定一个数组， 包含重复数字，输出其元素的全排列

@hint: [1, 1, 2] -> [1, 1, 2], [1,2,1], [2, 1, 1]
"""

def permute_unique(array):
    perms = [[]]
    for n in array:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                if i < len(perm) and perm[i] == n:  #连续重复的两个元素就跳过
                    break
        perms = new_perms
    return perms


if __name__ == '__main__':
    array = [1, 2, 1]
    r = permute_unique(array)
    print(r)