#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: pattern_match.py

@desc: 模式匹配： 给定一个模式和一个字符串，判断是否匹配


Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.

@hint:  skip
"""

def pattern_match(pattern, string):
    return back_track(pattern, string, {})


def back_track(pattern,  string, dic):
    print(dic)
    if len(pattern) == 0 and len(string) > 0:
        return False
    if len(pattern) == len(string) == 0:
        return True
    for end in range(1, len(string) - len(pattern) + 2):
        if pattern[0] not in dic and string[:end] not in dic.values():
            dic[pattern[0]] = string[:end]
            if back_track(pattern[1:], string[end:], dic):
                return True
            del dic[pattern[0]]
        elif pattern[0] in dic and dic[pattern[0]] == string[:end]:
            if back_track(pattern[1:], string[end:], dic):
                return True
    return False


if __name__ == '__main__':
    pattern = "aabb"
    string = "xyzxyzabcabc"
    r = pattern_match(pattern, string)
    print(r)