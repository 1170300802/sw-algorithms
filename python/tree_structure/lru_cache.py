#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: lru_cache.py

@desc:  最近最少使用缓存

@hint:
"""

class ListNode:
    def __init__(self, data=0, key=0):
        self.data = data
        self.key = key

    def equals(self, node):
        return self.key == node.key


class LRUCache:
    def __init__(self, capacity=0):
        self.n = capacity
        self.map = {}
        self.list = []

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return -1
        self.list.remove(node)
        self.list.append(node)
        return node.data

    def put(self, key, data):
        node = ListNode(data, key)
        if key in self.map.keys():
            self.list.remove(node)
        self.list.append(node)

        if len(self.list) > self.n:
            old = self.list.pop(0)  # remove first
            self.map.pop(old.key)

        self.map.setdefault(key, node)





if __name__ == '__main__':
    l = LRUCache(3)
    l.put(1, 'a')
    l.put(2, 'b')
    l.put(3, 'c')
    l.put(4, 'd')
    print(l.get(1))
    print(l.get(2))