#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: work_break.py

@desc: 单词分割:判断字符串是否能由给定字典中的若干单词拼接而成

@hint:
"""

def word_break(string, str_list):
    dp = [False] * (len(string) + 1)
    dp[0] = True
    for i in range(1, len(dp)):
        for j in range(i):
            if dp[j] and s[j:i] in str_list:
                dp[i] = True
                break
    print(dp)
    return dp[-1]


if __name__ == '__main__':
    s = "codell"
    l = ["l", "code", "ll"]
    result = word_break(s, l)
    print(result)