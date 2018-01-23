#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: maximum_depth_of_binary_tree.py

@desc:  二叉树的最大深度

@hint:
"""
from binary_tree import BinaryTree



def maximum_depth_of_binary_tree(root):
    if root is None:
        return 0
    return max(maximum_depth_of_binary_tree(root.left_child), maximum_depth_of_binary_tree(root.right_child)) + 1

if __name__ == '__main__':
    tree = BinaryTree()
    result = maximum_depth_of_binary_tree(tree.root)
    print(result)
    tree.create_symmetric_tree()
    result = maximum_depth_of_binary_tree(tree.root)
    print(result)
