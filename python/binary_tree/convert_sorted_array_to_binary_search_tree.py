#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: convert_sorted_array_to_binary_search_tree.py

@desc:  有序数组转为 平衡二叉查找树

@hint:  类似归并排序，两两切开又合并。注意递归返回和对前一节点的处理
"""
from binary_tree_level_order_traversal import binary_tree_level_order_traversal_one

from binary_tree import Node


def convert_sorted_array_to_binary_search_tree(l):
    if len(l) == 0:
        return None
    root = helper(l, 0, len(l) - 1)
    return root

def helper(l, lo, hi):
    if lo > hi:
        return
    mid = (lo + hi) >> 1
    node = Node(l[mid])
    node.left_child = helper(l, lo, mid - 1)
    node.right_child = helper(l, mid + 1, hi)
    return node


if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    root = convert_sorted_array_to_binary_search_tree(l)
    binary_tree_level_order_traversal_one(root)