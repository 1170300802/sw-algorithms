#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: bytes_int_conversion.py

@desc: 字节整数转换:每一个byte可以是一个ASCII字符或者十六进制数从\x00到\xff

@hint:
"""



def int_to_bytes_big_endian(num):
    bytestr = []
    while num > 0:
        bytestr.insert(0, num & 0xff)
        num = num >> 8
    print(bytestr)
    return bytes(bytestr)

def int_to_bytes_little_endian(num):
    bytestr = []
    while num > 0:
        bytestr.append(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def bytes_big_endian_to_int(bytestr):
    num = 0
    for b in bytestr:
        num <<= 8
        num += b
        print(num)
    return num

def bytes_little_endian_to_int(bytestr):
    num = 0
    e = 0
    for b in bytestr:
        num += b << e
        e += 8
    return num


if __name__ == '__main__':
    a = 868
    r = int_to_bytes_little_endian(a)
    print(r)
