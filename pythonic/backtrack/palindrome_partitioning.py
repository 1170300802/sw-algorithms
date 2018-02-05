#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: palindrome_partitioning.py

@desc:  字符串的回文子序列： 子序列不连续

@hint:
"""

def palindromic_substrings(string):
    if not string:
        return [[]]
    results = []
    for i in range(len(string), 0, -1):
        sub = string[:i]
        if sub == sub[::-1]:  #字符串的逆序
            for rest in palindromic_substrings(string[i:]):
                results.append([sub] + rest)
    return results
# 用yield
def palindromic_substrings_two(string):
    if not string:
        yield []
        return
    for i in range(len(string), 0, -1):
        sub = string[:i]
        if sub == sub[::-1]:
            for rest in palindromic_substrings_two(string[i:]):
                yield [sub] + rest

if __name__ == '__main__':
    # s = ""
    # print(bool(s))   # 字符串为None或者len(s) == 0: bool(s) -> False
    s = "ababa"
    r = palindromic_substrings(s)
    print(r)