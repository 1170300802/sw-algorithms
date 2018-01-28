#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: subset_sum.py

@desc:  子集合问题

@hint: 给定集合和一个数，判断该数能否等于某个子集的和

      动态规划和回溯法
"""


# dp: 建立一个二维数组：a[i- 1][j]=True 表示list的前i个(不包括i)元素的子集合为j。
def subset_sum(list, sum):
    a = [[False for i in range(sum + 1)] for j in range(len(list))]
    list.sort()
    a[0][list[0]] = True
    for i in range(1, len(a)):
        a[i - 1][0] = True
        for j in range(1, len(a[i])):
            if j < list[i]:
                a[i][j] = a[i - 1][j]
            else:
                a[i][j] = a[i - 1][j] or a[i - 1][j - list[i]]
    for i in a:
        print(i)
    return a[len(list) - 1][sum]


# 回溯法求解
def subset_sum_two(list, sum):
    a = [False] * len(list)

    back_track(0, list, a, sum)


def back_track(index, list, a, sum):
    global cur_sum
    global flag
    if index == len(list):
        if cur_sum == sum:
            flag = True
            for index, _ in enumerate(a):
                if a[index]:
                    print(list[index], end="   ")
            print()
            return
    else:
        cur_sum += list[index]
        a[index] = True
        back_track(index + 1, list, a, sum)
        a[index] = False
        cur_sum -= list[index]
        back_track(index + 1, list, a, sum)


if __name__ == '__main__':
    l = [2, 5, 10]
    sum = 16
    # subset_sum(l, sum)
    cur_sum = 0
    flag = False
    subset_sum_two(l, sum)
