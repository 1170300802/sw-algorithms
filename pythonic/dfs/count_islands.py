#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: count_islands.py

@desc:  岛计数：给定一个包含0， 1(代表岛)的二维数组。求岛的个数(岛被水包围， 假设四面都是水)

@hint:

Example 1:

11110
11010
11000
00000

Answer: 1
Example 2:

11000
11000
00100
00011

Answer: 3

"""

def count_islands(grid):
    count = 0
    for i, row in enumerate(gird):
        for j, col in enumerate(grid[i]):
            if col == 1:
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    if (i < 0 or i >= len(grid)) and (j < 0 or j >= len(grid[0])):
        return
    if gird[i][j] != 1:
        return
    grid[i][j] = 0
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)


if __name__ == '__main__':
    gird = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
    r = count_islands(gird)
    print(r)