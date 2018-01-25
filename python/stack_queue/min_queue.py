#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: min_stack.py

@desc: 最小队列

@hint: 借助一个队列来实现
"""

class MinQueue:
    def __init__(self):
        self.min = []
        self.queue = []

    def push(self, data):
        self.queue.append(data)
        if len(self.min) == 0 or self.min[-1] <= data:
            self.min.append(data)
        else:
            while len(self.min) != 0 and self.min[-1] > data:
                self.min.pop()
            self.min.append(data)

    def pop(self):
        data = self.queue.pop()
        if data == self.min[0]:
            self.min.pop(0)
        return data

    def get_min(self):
        return self.min[0]

if __name__ == '__main__':
    q = MinQueue()
    q.push(4)
    q.push(1)
    q.push(2)
    print(q.get_min())
    q.pop()
    q.pop()
    print(q.get_min())
    q.push(0)
    print(q.get_min())