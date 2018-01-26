#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: longest_common_prefix.py

@desc:  字符串数组的最长公共前缀

@hint:  两个循环
"""


def longest_common_prefix(str_list):
    if len(str_list) == 0:
        return ''
    str_0_len = len(str_list[0])
    for i in range(0, str_0_len):
        for j in range(0, len(str_list)):
            if len(str_list[j]) == 0:
                return ""
            if i == len(str_list[j]) or str_list[0][i] != str_list[j][i]:
                return str_list[0][0: i]

    return str_list[0]


if __name__ == '__main__':
    str_list = []
    str_list.append("qwas")
    str_list.append("qwwer")
    str_list.append("qw")
    str_list.append("qwae")
    result = longest_common_prefix(str_list)
    print(result)