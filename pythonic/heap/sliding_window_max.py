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

from heapq import heappop, heapify, heappush, heapreplace


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


#  O(n)
def sliding_window_max_two(array, k):
    res = []
    temp_max = []
    for i in range(k):
        if not temp_max:
            temp_max.append(i)
        else:
            if array[temp_max[-1]] < array[i]:
                temp_max.pop()
                temp_max.append(i)
    res.append(array[temp_max[0]])

    for i in range(k, len(array)):
        print(temp_max)
        if i - temp_max[0] >= k:
            temp_max.pop(0)  # 移除窗口外的元素
        if not temp_max:
            temp_max.append(i)
        else:
            if array[temp_max[-1]] < array[i]:
                temp_max.pop()
                temp_max.append(i)
        res.append(array[temp_max[0]])
    print(res)


if __name__ == '__main__':
    windows = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    r = sliding_window_max_two(windows, k)
    print(r)
