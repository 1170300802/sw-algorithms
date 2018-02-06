#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: reverse_bits.py

@desc:  反转位

@hint:
"""


# 方法被大量调用：按字节(8位bit保存中间结果)
def reverse_bits_two(n, cache):
    bytes = [0] * 4  #32位，4个字节
    for i in range(4):
        bytes[i] = (n >> (8 * i)) & 0xFF
    print(bytes)
    result = 0
    for i in range(4):
        result += reverse_byte(bytes[i], cache)
        if i != 3:
            result = result << 8
    print(result)


def reverse_byte(byte, cache):
    v = cache.get(byte)
    if v is not None:
        return v
    v = 0
    for i in range(8):
        v += (byte >> i) & 1
        if i != 7:
            v = v << 1
    cache.setdefault(byte, v)
    return v

if __name__ == '__main__':
    # 00000010 10010100 00011110 10011100
    cache = {}
    n = 43261596
    # reverse_bits(n)
    reverse_bits_two(n, cache)