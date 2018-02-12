#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: queue.py

@desc: 队列的实现

@hint:
"""

class AbstractQueue:
    def __init__(self):
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def __len__(self):
        return self.top

    def __str__(self):
        result = '------\n'
        for element in self:
            result += str(element) + "\n"
        return result[:-1] + '\n------'

class ArrayQueue(AbstractQueue):
    def __init__(self, size = 10):
        AbstractQueue.__init__(self)
        self.array = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, value):
        if self.rear == len(self.array):
            self.expand()
        self.array[self.rear] = value
        self.rear += 1
        self.top += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        value = self.array[self.front]
        self.array[self.front] = None
        self.front += 1
        self.top -= 1
        return value

    def expand(self):
        new_array = [None] * len(self.array) * 2
        for i, ele in enumerate(self.array):
            new_array[i] = ele
        self.array = new_array

    def __iter__(self):
        probe = self.rear
        while True:
            if probe < 0:
                raise StopIteration
            yield self.array[probe]
            probe -= 1

class QueueNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue(AbstractQueue):
    def __init__(self):
        AbstractQueue.__init__(self)
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = QueueNode(value)
        if not self.front:
            self.front = node
            self.rear = node

        else:
            self.rear,next = node
            self.rear = node
        self.top += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        value = self.front.value
        if self.front is self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.top -= 1
        return value

    def __iter__(self):
        probe = self.rear
        while True:
            if probe is None:
                raise StopIteration
            yield probe.value
            probe = probe.next

class HeapPriorityQueue(AbstractQueue):
    def __init__(self):
        AbstractQueue.__init__(self)
        pass


if __name__ == '__main__':
    pass

