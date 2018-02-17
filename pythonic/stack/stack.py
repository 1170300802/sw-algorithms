#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: stack.py

@desc: 栈的实现

@hint:
"""


class AbstractStack:
    def __init__(self):
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def __len__(self):
        return self.top

    def __str__(self):
        result = "------\n"
        for element in self:
            result += str(element) + '\n'
        return result[:-1] + '\n------'


class ArrayStack(AbstractStack):
    def __init__(self, size=10):
        AbstractStack.__init__(self)
        self.array = [None] * size

    def push(self, data):
        if self.top == len(self.array):
            self.expand()
        self.array[self.top] = data
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        data = self.array[self.top - 1]
        self.array[self.top - 1] = None
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.array[self.top - 1]

    def expand(self):
        newArray = [None] * len(self.array) * 2
        for index, ele in enumerate(self.array):
            newArray[index] = ele
        self.array = newArray

    def __iter__(self):
        probe = self.top - 1
        while True:
            if probe < 0:
                raise StopIteration
            yield self.array[probe]
            probe -= 1


class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack(AbstractStack):
    def __init__(self):
        AbstractStack.__init__(self)
        self.head = None

    def push(self, data):
        node = StackNode(data)
        node.next = self.head
        self.head = node
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        data = self.head.data
        self.head = self.head.next
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.head.data

    def __iter__(self):
        probe = self.head
        while True:
            if probe is None:
                raise StopIteration
            yield probe.data
            probe = probe.next


if __name__ == '__main__':
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.peek())
    print(s.pop())
    for i in s:
        print(i)
