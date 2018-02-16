#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: top_sort.py

@desc: top排序，类似python安装的依赖，安装某个包必须先安装某个包。

@hint:
"""

def top_sort(visited, start):
    queue = []
    out = []
    queue.append(start)

    while queue:
        new_node = queue.pop(0)
        if new_node not in visited:
            visited.add(new_node)
        for child in depGraph[new_node]:
            queue.append(child)
            out.append(child)
    out.append(start)
    return out

def retDepGraph():
    visited = set()
    out = []
    for pac in given:
        if pac in visited:
            continue
        visited.add(pac)
        if pac in depGraph:
            for child in depGraph[pac]:
                if child in visited:
                    continue
                out.extend(top_sort(visited, child))
        out.append(pac)
        print(visited)
    print(out)

if __name__ == '__main__':
    depGraph = {

        "a": ["b"],
        "b": ["c"],
        "c": ['e'],
        'e': [],
        "d": [],
        "f": ["e", "d"]
    }
    given = ["b", "c", "a", "d", "e", "f"]
    retDepGraph()


