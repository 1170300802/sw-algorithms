#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: rabin_karp.py

@desc: rabin_karp 字符串匹配算法

@hint: skip
"""

class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            self.hash += (ord(self.text[i]) - ord("a") + 1) * (26 ** (sizeWord - i - 1))

        self.window_start = 0
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1) * 26 ** (self.sizeWord - 1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end]) - ord("a") + 1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]


def rabin_karp(word, text):
    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return None
    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for i in range(len(text) - len(word) + 1):
        if rolling_hash == word_hash:
            if rolling_hash.window_text() == word:
                return i
        rolling_hash.move_window()
    return None