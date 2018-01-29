#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: reverse_bits.py

@desc:  反转位：翻转32位无符号整型数

@hint: 如果此方法被大量调用，如何优化
"""

# 原数不断右移取出最低位，赋给新数的最低位后新数再不断左移。
def reverse_bits(n):
    result = 0
    for i in range(0, 32):  #[0:32]
        if i == 0:
            temp = n & 1  #get bit
            result = result | temp
        else:
            temp = (n >> 1) & 1
            n = n >> 1
            result = (result << 1) | temp
    print(result)
    return result


# 方法被大量调用：按字节(8位bit保存中间结果)
def reverse_bits_two(n, cache):
    bytes = [0] * 4
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


