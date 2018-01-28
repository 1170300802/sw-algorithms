#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: shortest_palindrome.py

@desc:  最短回文串：给定一个字符串，在字符串的前面加入字符，将该字符串变成一个最短的回文字符串

@hint:
"""

def shortest_palindrome(string):
    if len(string) <= 1:
        return string
    str_reverse = string[::-1]
    l = s + "#" + str_reverse
    print(l)

    #下面找出公共的最长前后缀
    p = [0] * len(l)
    max_length = 0
    for i in range(1, len(l)):
        while max_length > 0 and l[max_length] != l[i]:
            max_length = p[max_length - 1]
        if l[i] == l[max_length]:
            max_length += 1
        p[i] = max_length

    print(p)
if __name__ == '__main__':
    s = "bcba"
    shortest_palindrome(s)