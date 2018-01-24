#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: validate_binary_search_tree.py

@desc:  验证二叉查找树：

@hint: 多种方法： 1. 中序遍历树，看是否递增
                 2. 递归, 分别找到左右子树的最大，最小值左比较
                 3. 预定上下届， 递归判断，看否满足要求
"""

# 方法2：
from binary_tree import BinaryTree
import math


def validate_binary_search_tree(root):
    return is_validate(root, -math.inf, math.inf)


def is_validate(node, low, up):
    if node is None:
        return True
    if low >= node.data or up <= node.data:
        return False
    return is_validate(node.left_child, low, node.data) and is_validate(node.right_child, node.data, up)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    result = validate_binary_search_tree(tree.root)
    print(result)