#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: all_factors.py

@desc: 因数分解

@hint:  8 = 2 x 2 x 2;
          = 2 x 4.
"""


# 递归
def all_factors(num):
    def factors(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n // i])
                factors(n // i, i, combi + [i], combis)
            i += 1
        return combis
    return factors(num, 2, [], [])


if __name__ == '__main__':
    a = 8
    r = all_factors(a)
    print(r)