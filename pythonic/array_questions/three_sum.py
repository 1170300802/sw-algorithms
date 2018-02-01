#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: three_sum.py

@desc: 三数和为零：在给定数组中找 a+b+c=0的所有组合

@hint: 多种方法，接近穷举
"""


def three_sum(array: list) -> list:
    if array is None:
        return []
    res = []
    array.sort()
    for i in range(len(array) - 2):  #空出后面两个
        if array[i] * array[-1] > 0:  # 符号相同，不存在
            break
        if i > 0 and array[i] == array[i - 1]:
            continue
        l, r = i + 1, len(array) - 1
        while l < r:
            s = array[i] + array[l] + array[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([array[i],  array[l], array[r]])
                # 去除重复
                while l < r and array[l] == array[l + 1]:
                    l += 1
                while l < r and array[r] == array[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


if __name__ == '__main__':
    a = [-1, 0, 1, 2, -1, -4, -1, -1]
    print(a)
    print(three_sum(a))