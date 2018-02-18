#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: encode_decode.py

@desc: 字符串编解码

@hint:
"""


def encode(strs):
    """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
    """
    res = ''
    for string in strs.split():
        res += str(len(string)) + ":" + string
    return res

def decode(string):
    strs = []
    i = 0
    while i < len(string):
        index = string.find(":", i)
        # print(index)
        size = int(string[i:index])
        strs.append(string[index + 1: index + 1 + size])
        i = index + 1 + size
    return strs


if __name__ == '__main__':
    strs = "keno is awesome"
    r = encode(strs)
    print(r)
    r = decode(r)
    print(r)
