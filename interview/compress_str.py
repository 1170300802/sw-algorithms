#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: compress_str.py

@desc:

@hint:
"""


def compress_str(string):
    # 边界检测
    if len(string) == 0:
        return string

    result = ""
    cur_char = "" #当前字符
    cur_num = 0  # 当前出现次数
    for i in string:
        if i != cur_char:
            if cur_num > 1:
                result += str(cur_num)
            cur_char = i
            result += i
            cur_num = 1
        else:
            cur_num += 1
    # 最后情况
    if cur_num > 1:
        result += str(cur_num)
    return result



if __name__ == '__main__':
    str_list = ["aabccccaaa", "", "affffffv"]
    for i in str_list:
        result = compress_str(i)
        if len(i) != 0:
            print(i + " --> " + result)
