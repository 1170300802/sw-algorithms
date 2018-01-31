#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: garage.py

@desc: 停车场问题：有一个空位的停车场，给定初始状态， 求最短移动次数。

@hint:
"""


def garage(initial, final):
    steps = 0
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        steps += 1

    return steps


def equal(initial, final):
    if len(initial) != len(final):
        return False
    for i in range(len(initial)):
        if initial[i] != final[i]:
            return False
    return True


if __name__ == '__main__':
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    # final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))
    print(initial == final)


