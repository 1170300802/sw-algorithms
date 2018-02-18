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

if __name__ == '__main__':
    strs = "keno is awesome"
    r = encode(strs)
    print(r)
