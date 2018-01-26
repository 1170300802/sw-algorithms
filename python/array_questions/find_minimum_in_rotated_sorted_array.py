#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: find_minimum_in_rotated_sorted_array.py

@time: 2018/1/15 09:42

@desc: 寻找旋转排序数组中的最小值。

@hint: 二分查找，注意条件比较。
"""


#假设数组不重复
def find_minimum_in_rotated_sorted_array_one(array):
    #参数合法性
    if array is None or len(array) == 0:
        return -1
    i = 0
    j = len(array) - 1
    while i < j:
        mid = (i + j) >> 1
        if array[mid] >= array[i] and array[mid] > array[j]: # 注意等号
            i = mid + 1
        else:
            j = mid

    return i

# 假设数组有重复, 上面算法一样适用。


#递归实现
def find_minimum_in_rotated_sorted_array_two(array):
    if array is None or len(array) == 0:
        return -1
    result = binary_find(array, 0, len(array) - 1)
    return result


def binary_find(array, lo, hi):
    if lo == hi:
        return array[lo]
    mid = (lo + hi) >> 1
    if array[mid] >= array[lo] and array[mid] > array[hi]:
        return binary_find(array, mid + 1, hi)
    else:
        return binary_find(array, lo, mid)


if __name__ == '__main__':
    a = [5, 6, 8]
    print(find_minimum_in_rotated_sorted_array_two(a))