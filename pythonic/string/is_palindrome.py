#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: is_palindrome.py

@desc: 判断回文字符串

@hint:

Have you consider that the string might be empty?
This is a good question to ask during an interview.
For the purpose of this problem,
we define empty string as valid palindrome.

"""

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():  #isalnum: 字母数字
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    r = is_palindrome(s)
    print(r)