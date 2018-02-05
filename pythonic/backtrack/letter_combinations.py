#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: letter_combinations.py

@desc:  字母组合：给定字符表。求出给定数字字符串在字符表中的所有组合

kmaps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

@hint:  str: "23" -> res: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

kmaps = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

# 后一个结果可以有前一个结果来推出: 参考排列组合， 由小及大
def letter_combinations(string):
    if string == "":
        return []
    res = [""]
    for num in string:
        temp = []
        for an in res:
            for char in kmaps[num]:
                temp.append(an + char)
        res = temp
    return res

if __name__ == '__main__':
    string = "234"
    r = letter_combinations(string)
    print(r)