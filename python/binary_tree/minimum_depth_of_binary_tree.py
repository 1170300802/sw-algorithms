#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: minimum_depth_of_binary_tree.py

@desc: 二叉树的最小深度

@hint:
"""
from binary_tree import BinaryTree


def minimum_depth_of_binary_tree(root):
    if root is None:
        return 0
    left_d = minimum_depth_of_binary_tree(root.left_child)
    right_d = minimum_depth_of_binary_tree(root.right_child)
    if left_d == 0 or right_d == 0:
        return max(left_d, right_d) + 1
    else:
        return min(left_d, right_d) + 1


if __name__ == '__main__':
    tree = BinaryTree()
    result = minimum_depth_of_binary_tree(tree.root)
    print(result)
    tree.create_symmetric_tree()
    result = minimum_depth_of_binary_tree(tree.root)
    print(result)


