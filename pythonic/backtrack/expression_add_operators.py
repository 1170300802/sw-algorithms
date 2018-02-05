#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: expression_add_operators.py

@desc: 给表达式添加运算符号

@hint: skip

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

def add_operator(num_str, target):  #回溯法就是找到所有的可能性
    res = []
    if not num_str:
        return res
    helper(res, "", num_str, target, 0, 0, 0)
    return res


def helper(res, path, num_str, target, pos, prev, multed):
    if pos == len(num_str):
        if target == prev:
            res.append(path)
        return
    for i in range(pos, len(num_str)):
        if i != pos and num_str[pos] == '0':
            break
        cur = int(num_str[pos:i+1])
        if pos == 0:
            helper(res, path + str(cur), num_str, target, i + 1, cur, cur)
        else:
            helper(res, path + "+" + str(cur), num_str, target, i + 1, prev + cur, cur)
            helper(res, path + "-" + str(cur), num_str, target, i + 1, prev - cur, -cur)
            helper(res, path + "*" + str(cur), num_str, target, i + 1, prev - multed + multed * cur, multed * cur)

if __name__ == '__main__':
    #  空字符串表示False：bool
    s = "105"
    target = 6
    print(add_operator(s, target))
