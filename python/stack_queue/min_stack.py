#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: min_stack.py

@desc: 最小栈

@hint: 借助一个栈来实现
"""

class MinStack:
    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.min) == 0 or data <= self.min[-1]:
            self.min.append(data)

    def pop(self):
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min[-1]

if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(10)
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(4)
    print(min_stack.pop())
    print(min_stack.get_min())