#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: valid_parenthesis.py

@desc: 验证括号

@hint:
"""


def valid_parenthesis(string):
    stack = []
    dic = {")": "(",
           "]": "[",
           "}": "{"}
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if not stack:
                return False
            temp_s = stack.pop()
            if dic[char] != temp_s:
                return False
    return stack == []




if __name__ == '__main__':
    s = "([]{})"
    r = valid_parenthesis(s)
    print(r)
