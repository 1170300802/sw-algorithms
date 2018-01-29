#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: minimum_square_sum.py

@desc:  平方和的最小个数： Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

@hint: dp
"""

def minimum_square_sum(p):
    dp = [0] * (p + 1)
    # init base case
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, len(dp)):
        # init max value
        dp[i] = i

        for x in range(1, i + 1):  #[1, i]
            temp = x * x
            if temp > i:
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i - temp])
    print(dp)
    return dp[p]
if __name__ == '__main__':
    minimum_square_sum(13)

