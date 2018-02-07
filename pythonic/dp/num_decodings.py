#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: num_decodings.py

@desc:  数字编码：给定一个数字字符串，编码如下。

'A' -> 1
'B' -> 2
...
'Z' -> 26

例子：
"12" -> "AB", "L"  return 2。 "12" 编码为 2.

@hint: 类似爬楼梯问题
"""

def num_decodings(s):   #"hint: 只允许： 10-26"
    if not s or s[0] == "0":
        return 0
    wo_last, wo_last_two = 1, 1
    for i in range(1, len(s)):
        x = wo_last if s[i] != "0" else 0
        y = wo_last_two if int(s[i-1: i+1]) < 27 and s[i-1] != "0" else 0
        wo_last_two = wo_last
        wo_last = x + y
        print(wo_last_two, wo_last)
    return wo_last

if __name__ == '__main__':
    s = "172"
    r = num_decodings(s)
    print(r)

