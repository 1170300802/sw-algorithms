#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: implement_stack_using_queues.py

@desc: 用队列实现栈

@hint: 栈是后进先出，因此保证队列出的元素是刚进的。
"""


class StackInQueue:

    def __init__(self):
        self.queue = []
        self.temp_queue = []

    def push(self,data):
        if len(self.queue) == 0:
            self.queue.append(data)
        else:
            while len(self.queue) != 0:
                self.temp_queue.append(self.queue.pop(0))
            self.queue.append(data)
            while len(self.temp_queue) != 0:
                self.queue.append(self.temp_queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    stack = StackInQueue()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.top())