#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: sieve_of_eratosthenes.py

@desc: 埃拉托斯特尼筛法: 用来找出一定范围内所有的素数

@hint: 分别去掉各素数的倍数
"""

def sieve_of_eratosthenes(n):
    find_primes(n)

def find_primes(n):
    primes = [True] * n
    for i in range(2, n):
        if primes[i]:
            j = i * i
            while j < n:
                primes[j] = False
                j += i
    for i in range(2, n):
        if primes[i]:
            print(i, end="   ")
    print()

if __name__ == '__main__':
    sieve_of_eratosthenes(100)