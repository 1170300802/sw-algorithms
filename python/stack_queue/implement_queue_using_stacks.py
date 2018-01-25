#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: implement_queue_using_stacks.py

@desc: 用栈实现队列

@hint:
"""

class QueueInStack:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def push(self, data):
        self.stack_one.append(data)

    def pop(self):
        if len(self.stack_two) == 0:
            while len(self.stack_one) != 0:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()

    def peek(self):
        if len(self.stack_two) == 0:
            while len(self.stack_one) != 0:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two[-1]

    def empty(self):
        return len(self.stack_two) == 0 and len(self.stack_one) == 0

if __name__ == '__main__':
    q = QueueInStack()
    q.push(4)
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    q.push(3)
    print(q.peek())