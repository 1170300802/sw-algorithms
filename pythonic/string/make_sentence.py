#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: make_sentence.py

@desc: 造句: 给定字典和一个字符串，求字典中能组成字符串的所有情况

@hint:

"applet", {app, let, apple, t, applet} => 3
"thing", {"thing"} -> 1

"""


def make_sentence(string, dic_str):
    global count
    if len(string) == 0:
        return True
    for i in range(0, len(string)):
        prefix, suffix = string[0:i], string[i:]
        if (prefix in dic_str and suffix in dic_str) or \
            (prefix in dic_str and make_sentence(suffix, dic_str)):
            count += 1
    return True



if __name__ == '__main__':
    count = 0
    dic_str = ["", "app", "let", "t", "apple", "applet"]
    word = "applet"
    make_sentence(word, dic_str)
    print(count)
