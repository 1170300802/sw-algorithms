#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: generate_abbreviations.py

@desc: 单词缩写

@hint: word => [1ord, w1rd, wo1d, w2d, 3d, w3 ... etc]
"""

def generate_abbreviations(word):
    result = []
    back_track(result, word, 0, 0, "")
    return result


def back_track(result, word, pos, count, cur):
    # print(cur)
    if pos == len(word):
        if count > 0:
            cur += str(count)
        result.append(cur)
        return
    if count > 0:
        back_track(result, word, pos + 1, 0, cur + str(count) + word[pos])
    else:
        back_track(result, word, pos + 1, 0, cur + word[pos])
    back_track(result, word, pos + 1, count + 1, cur)

if __name__ == '__main__':
    a = "ab"
    r = generate_abbreviations(a)
    print(r)