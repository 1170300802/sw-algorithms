#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: factor_combinations.py

@desc:  因数分解：给定一个正整数，求出所有的因数乘组合。

@hint:  递归和迭代

1 -> []  37 -> []   12 -> [[2,2,3], [2, 6], [3, 4]]
"""


#  迭代
def get_factors_two(num):
    todo, res = [(num, 2, [])], []
    while todo:
        n, i, r = todo.pop()
        while i * i <= n:
            if n % i == 0:
                res.append(r + [i,  n // i]),
                todo.append([n // i , i, r + [i]])
                # print(todo)
            i += 1
    return res


# 递归
def get_factors(num):
    def factors(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis.append(combi + [i, n // i])
                factors(n // i, i, combi + [i], combis)
            i += 1
        return combis
    return factors(num, 2, [], [])



if __name__ == '__main__':
    # a = [1]        #list的元素个数为0， bool(a) = True
    # print(bool(a))
    num = 12
    r = get_factors_two(num)
    print(r)

