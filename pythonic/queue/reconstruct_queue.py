#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: reconstruct_queue.py

@desc: 重建队列：给出每个人的身高和前面高于或者等于自己身高的人的个数，重排列这个队伍。

@hint:
"""

def reconstruct_queue(array):
    queue = []
    array.sort(key=lambda x:(-x[0], x[1]))
    for h, k in array:
        queue.insert(k, (h, k))
        print(queue)
    return queue

if __name__ == '__main__':
    a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    r = reconstruct_queue(a)
    print(r)