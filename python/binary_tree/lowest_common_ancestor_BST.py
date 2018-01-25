#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: lowest_common_ancestor_BST.py

@desc: 二叉查找树的最近公共祖先

@hint: 利用二叉查找树的性质， 递归求解
"""
from binary_tree import BinaryTree


def lowest_common_ancestor_BST(root, node_one, node_two):
    if root is None:
        return None
    if root.data > node_one.data and root.data > node_two.data:
        return lowest_common_ancestor_BST(root.left_child, node_one, node_two)
    if root.data < node_one.data and root.data < node_two.data:
        return lowest_common_ancestor_BST(root.right_child, node_one, node_two)
    return root.data


if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    node_one = tree.root.left_child.left_child
    node_two = node_one.left_child
    result = lowest_common_ancestor_BST(tree.root, node_one, node_two)
    print(result)
