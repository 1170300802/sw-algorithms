#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: shortest_distance_from_all_buildings.py

@desc: 建筑物间的最短距离

@hint:  skip
"""


def shortest_distance(grid):
    if not grid and not grid[0]:
        return -1
    #
    matrix = [[[0, 0] for i in range(len(grid[0]))] for j in range(len(grid))]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                bfs(grid, matrix, i, j, count)
                count += 1
    res = float('inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j][1] == count:
                res = min(res, matrix[i][j][0])
    return res if res != float('inf') else -1


def bfs(grid, matrix, i, j, count):
    q = [(i, j, 0)]
    while q:
        i, j, step = q.pop(0)
        for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and \
                    matrix[k][l][1] == count and grid[k][l] == 0:
                matrix[k][l][0] += step + 1
                matrix[k][l][1] += count + 1
                q.append((k, l, step + 1))


if __name__ == '__main__':
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    for i in grid:
        print(i)
    r = shortest_distance(grid)
    print(r)
