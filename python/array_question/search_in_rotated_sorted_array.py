#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: search_in_rotated_sorted_array.py

@time: 2018/1/15 10:31

@desc: 在旋转排序数组中查找某个值，数组可重复，可不重复。

@hint: 找到分界点后二分查找
"""


#无论数组重复与否。可以找到分界点，两边进行二分查找。
def search_in_rotated_sorted_array_one(array, k):
    i = 0
    j = len(array) - 1
    while i < j:
        mid = (i + j) >> 1
        if array[mid] >= array[i] and array[mid] > array[j]: # 后面这个条件是判断数组是不是没有旋转过。
            i = mid + 1
        else:
            j = mid
    print(i)
    #如果没有重复元素，可以简单判断是否有旋转array[i] > array[j]
    #如果有重复元素，就如解法判断。
    if i == 0:
        #没有旋转
        return binary_find_one(array, 0, len(array) - 1, k)

    one = binary_find_one(array, 0, i - 1, k)
    two = binary_find_one(array, i, len(array) - 1, k)
    if one == two:
        return -1
    else:
        return max(one, two)


def binary_find_one(array, lo, hi, k):
    if lo == hi and array[lo] != k:
        return -1
    mid = (lo + hi) >> 1
    if array[mid] == k:
        return mid
    if array[mid] > k:
        return binary_find_one(array, lo, mid - 1, k)
    else:
        return binary_find_one(array, mid + 1, hi, k)

#这是另一种方法，无论元素重复与否都能找到。
def search_in_rotated_sorted_array_three(array, k):
    if array is None or len(array) is 0:
        return -1
    result = binary_find_three(array, 0, len(array) - 1, k)
    return result


def binary_find_three(array, lo, hi, k):
    if lo == hi:
        if array[lo] == k:
            return lo
        else:
            return -1
    mid = (hi + lo) >> 1
    if array[mid] == k:
        return mid
    if array[mid] > k:
        if k >= array[lo]:
            return binary_find_three(array, lo, mid, k)
        else:
            return binary_find_three(array, mid + 1, hi, k)
    if array[mid] < k:
        if k <= array[hi]:
            return binary_find_three(array, mid + 1, hi, k)
        else:
            return binary_find_three(array, lo, mid, k)



if __name__ == '__main__':
    a = [1, 2, 1, 1, 1, 1, 1, 1, 1]
    r = search_in_rotated_sorted_array_one(a, 2)
    print(r)

