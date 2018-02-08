#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: regex_matching.py

@desc: 最简单的正则匹配：支持 . 或者 *

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

@hint: 字符串匹配 : skip
"""

def is_match(s, p):
    m, n = len(s) + 1, len(p) + 1
    matches = [[False] * n for _ in range(m)]

    # Match empty string with empty pattern
    matches[0][0] = True

    # Match empty string with .*
    for i, element in enumerate(p[1:], 2):
        matches[0][i] = matches[0][i - 2] and element == '*'

    for i, ss in enumerate(s, 1):
        for j, pp in enumerate(p, 1):
            if pp != '*':
                # The previous character has matched and the current one
                # has to be matched. Two possible matches: the same or .
                matches[i][j] = matches[i - 1][j - 1] and \
                                (ss == pp or pp == '.')
            else:
                # Horizontal look up [j - 2].
                # Not use the character before *.
                matches[i][j] |= matches[i][j - 2]

                # Vertical look up [i - 1].
                # Use at least one character before *.
                #   p a b *
                # s 1 0 0 0
                # a 0 1 0 1
                # b 0 0 1 1
                # b 0 0 0 ?
                if ss == p[j - 2] or p[j - 2] == '.':
                    matches[i][j] |= matches[i - 1][j]

    return matches[-1][-1]


if __name__ == '__main__':
    s1 = "aa"
    s2 = "a*"
    r = is_match(s1, s2)
    print(r)
