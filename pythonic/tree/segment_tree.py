#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: segment_tree.py

@desc: 线段树: 数列的更新与区间的查询

@hint:  skip
"""

class segment_tree:
    def __init__(self, arr, function):
        self.segment = [0 for _ in range(4 * len(arr))] #保守空间
        self.arr = arr
        self.fn = function
        self.maketree(0, 0, len(arr) - 1)

    def maketree(self, i, l, r):
        if l == r:
            self.segment[i] = self.arr[l]
        elif l < r:
            mid = (l + r) >> 1
            self.maketree(2 * i + 1, l, mid)
            self.maketree(2 * i + 2, mid + 1, r)
            self.segment[i] = self.fn(self.segment[2 * i + 1],  self.segment[2 * i + 2])

    def query(self, l, r):
        return self._query(0, 0, len(self.arr) - 1, l, r)

    def _query(self, i, L, R, l, r):
        if l > R or r < L or L > R or l > r:
            return None
        if L >= l and R <= r:
            return self.segment[i]
        mid = (L + R) >> 1
        val1 = self._query(2 * i + 1, L, mid, l, r)
        val2 = self._query(2 * i + 2, mid + 1, R, l, r)
        # print(L, R, " returned ", val1, val2)
        if val1 is not None:
            if val2 is not None:
                return val1 + val2
            return val1
        return val2


if __name__ == '__main__':
    t = segment_tree([1, 2, 3], lambda x, y: x + y)
    print(t.segment)
    r = t.query(0, 1)
    print(r)


