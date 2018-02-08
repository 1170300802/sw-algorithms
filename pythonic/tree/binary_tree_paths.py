#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_tree_paths.py

@desc: 二叉树到每个叶子的节点的所有路径

@hint:

"""
from binary_tree import BinaryTree


def binary_tree_paths(root):
    res = []
    if not root:
        return res
    dfs(res, root, str(root.data))
    return res


def dfs(res, root, cur):
    if not root.left_child and not root.right_child:
        res.append(cur)
    if root.left_child:
        dfs(res, root.left_child, cur + '->' + str(root.left_child.data))
    if root.right_child:
        dfs(res, root.right_child, cur + '->' + str(root.right_child.data))


if __name__ == '__main__':
    tree = BinaryTree()
    r = binary_tree_paths(tree.root)
    print(r)
