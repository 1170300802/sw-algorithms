#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: same_tree.py

@desc: 相同树判断

@hint: 有了对称树判断的经验，相同树就变的很简单。
"""

# !/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: symmetric_tree.py

@desc: 判断对称树

@hint: 比较对称位置，递归和非递归。也可以根据前面二叉树反转，来判断两棵树是不是一样。
"""
from binary_tree import BinaryTree


# 递归
def same_tree(root_one, root_two):
    if root_one is None and root_two is None:
        return True
    if root_one is None or root_two is None:
        return False
    return root_one.data == root_two.data and same_tree(root_one.left_child, root_two.left_child) \
           and same_tree(root_one.right_child, root_two.right_child)


if __name__ == '__main__':
    tree = BinaryTree()
    root_one = tree.root
    tree.create_symmetric_tree()
    root_two = tree.root
    result = same_tree(root_one, root_two)
    print(result)
