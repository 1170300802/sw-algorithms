#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: word_break.py

@desc: 单词分割:判断字符串是否能由给定字典中的若干单词拼接而成。

@hint: 动态规划
"""

def word_break(string, str_list):
    str_set = set(str_list)
    a = [False] * (len(string) + 1)
    a[0] = True
    for i in range(1, len(a)):  #a[i]==true代表字符串的前i个字符是可以用给定字典分割的。
        for j in range(i):
            if a[j] and string[j:i] in str_set:
                a[i] = True
                break
    print(a)
    return a[len(string)]


if __name__ == '__main__':
    s = "codecod"
    l = []
    l.append("l")
    l.append("code")
    result = word_break(s, l)
    print(result)