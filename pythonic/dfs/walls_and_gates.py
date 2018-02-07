#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: walls_and_gates.py

@desc: 墙和门：一个二维矩阵，0代表门，-1代表障碍物。求每个点到0的最短距离

@hint:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

  ->

3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4

"""

import math

def walls_and_gates(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                dfs(grid, i, j, 0)
    return grid


def dfs(grid, i, j, depth):
    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
        return
    if grid[i][j] < depth:
        return
    grid[i][j] = depth
    dfs(grid, i, j + 1, depth + 1)
    dfs(grid, i, j - 1, depth + 1)
    dfs(grid, i + 1, j, depth + 1)
    dfs(grid, i - 1, j, depth + 1)

if __name__ == '__main__':
    grid = [[float('inf'), -1, 0, float('inf')], [float('inf'),float('inf'),float('inf'),-1], [float('inf'),-1,float('inf'),-1], [-1, 0, float('inf'),float('inf')]]
    r = walls_and_gates(grid)
    for i in r:
        print(i)