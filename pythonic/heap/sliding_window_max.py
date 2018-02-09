#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: sliding_window_max.py

@desc: 滑动窗口最大值

@hint: 堆的应用
"""

import collections

def sliding_window_max(array, k):
    if not array:
        return array
    queue = collections.deque()
    res = []
    for num in array:
        if len(queue) < k:
            queue.append(num)
        else:
            res.append(max(queue))
            queue.popleft()
            queue.append(num)
    res.append(max(queue))
    return res

def slide_window_max_two(array, k):
    pass


if __name__ == '__main__':
    windows = [1,3,-1,-3,5,3,6,7]
    k = 3
    r = sliding_window_max(windows, k)
    print(r)