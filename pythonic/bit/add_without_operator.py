#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: add_without_operator.py

@desc: 无+操作符的加法：给定两个非负数， 用位运算计算和

@hint:  根据真值表

位二进制加法真值表:(对应于硬件中的半加器)
x	y	sum	carry
0	0	0	0
0	1	1	0
1	0	1	0
1	1	0	1

"""


def add(a, b):
    while b != 0:
        temp = a & b    #没有进位就停止
        a = a ^ b
        b = temp << 1
        print(a, b)
    return a

if __name__ == '__main__':
    a = 4
    b = 16
    r = add(a, b)
    print(r)
