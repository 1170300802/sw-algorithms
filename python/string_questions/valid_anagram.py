#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: valid_anagram.py

@desc: anagram字符串验证：由颠倒字母顺序而构成的字符串(假设都是小写字母)

@hint: 由于出现的都是26个字母， 因此可以类计数排序的思想
"""


def valid_anagram(a, b):
    if len(a) != len(b):
        return False
    temp_array = [0] * 26
    for i in range(0, len(a)):
        temp_array[ord(a[i]) - ord('a')] += 1
        temp_array[ord(b[i]) - ord('a')] -= 1
    for i in temp_array:
        if i != 0:
            return False
    return True


if __name__ == '__main__':
    a = "qwertyuiop"
    b = "ertuiyopwq"
    result = valid_anagram(a, b)
    print(result)
