#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: longest_non_repeat.py

@desc: 最长不重复子串  （字串连续， 子序列不连续)

@hint:
"""


def longest_non_repeat(string):
    if string is None:
        return 0
    temp = []
    max_len = 0
    for i in string:
        if i in temp:
            temp = []
        temp.append(i)
        max_len = max(max_len, len(temp))
    return max_len

def longest_non_repeat_two(string):
    if string is None:
        return 0
    start, max_len = 0, 0
    user_char = {}
    for index, char in enumerate(string):
        if char in user_char and start <= user_char[char]:
            start = user_char[char] + 1
        else:
            max_len = max(max_len, index - start + 1)
        user_char[char] = index
    return  max_len

if __name__ == '__main__':
    a = "abcabcdefbb"
    print(a)
    print(longest_non_repeat(a))
    print(longest_non_repeat_two(a))
