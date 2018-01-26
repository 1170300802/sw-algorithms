#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: reverse_string.py

@desc: 反转字符串

@hint:
"""

def reverse_string(string):
    #由于python的字符串不能执行  string[0] == 'a' 操作
    result = ''
    for i in range(len(string) - 1, -1, -1):
        result += string[i]
    return result



if __name__ == '__main__':
    s = "qwertyuio"
    print(s)
    ss = reverse_string(s)
    print(ss)
    sss = s[::-1]
    print(sss)
