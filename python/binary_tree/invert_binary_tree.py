#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: Invert_binary_tree.py

@desc: 反转二叉树

@hint: 递归与非递归
"""

from binary_tree import BinaryTree
from binary_tree_level_order_traversal import binary_tree_level_order_traversal_two


def invert_binary_tree_one(root):
    if root is None:
        return None
    root.left_child, root.right_child = root.right_child, root.left_child
    invert_binary_tree_one(root.left_child)
    invert_binary_tree_one(root.right_child)
    return root


# 反转二叉树，即是将每一个节点的左右节点左右置换。即可参考层次遍历。
def invert_binary_tree_two(root):
    if root is None:
        return
    node_list = []
    node_list.append(root)
    while len(node_list) != 0:
        temp_node = node_list.pop(0)
        temp_node.left_child, temp_node.right_child = temp_node.right_child, temp_node.left_child
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
    return root


if __name__ == '__main__':
    tree = BinaryTree()
    root = invert_binary_tree_two(tree.root)
    binary_tree_level_order_traversal_two(tree.root)