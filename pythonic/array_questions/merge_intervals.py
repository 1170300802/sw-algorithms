#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: merge_intervals.py

@desc: 合并间隔

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


def merge_intervals(l):
    #sort
    if l is None:
        return None
    l.sort(key=lambda i: i[0])
    out = [l.pop(0)]
    for i in l:
        if out[-1][-1] >= i[0]:
            out[-1][-1] = max(out[-1][-1], i[-1])
        else:
            out.append(i)
    return out


if __name__ == '__main__':
    l = [[15,18],[2,5], [1,6], [8,10]]
    print(l)
    print(merge_intervals(l))