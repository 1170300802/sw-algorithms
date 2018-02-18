#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: decode_string.py

@desc: 字符串解码

@hint:

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""

def decode_string(s):
    """
    :param s: str
    :return: str
    """
    stack = []
    cur_num = 0
    cur_string = ''

    for c in s:
        print(cur_string)
        if c == '[':
            stack.append((cur_string, cur_num))
            cur_string = ''
            cur_num = 0
        elif c == ']':
            prev_string, num = stack.pop()
            cur_string = prev_string + num * cur_string
        elif c.isdigit():
            cur_num = cur_num * 10 + int(c)
        else:
            cur_string += c
    return cur_string


if __name__ == '__main__':
    a = "3[ab2[c]]"
    r = decode_string(a)
    print(r)