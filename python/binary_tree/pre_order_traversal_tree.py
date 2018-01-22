#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: pre_ordef_traversal_tree.py

@desc: 前序遍历

@hint: 递归和非递归
"""
from binary_tree import BinaryTree


def pre_order_traversal_tree(root):
    if root is None:
        return
    print(root.data, end="   ")
    pre_order_traversal_tree(root.left_child)
    pre_order_traversal_tree(root.right_child)


# 非递归遍历: 借助栈
def pre_order_traversal_tree_two(root):
    if root is None:
        return
    node_list = []
    node_list.append(root)
    while len(node_list) != 0:
        temp_node = node_list.pop()
        print(temp_node.data, end="   ")
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
    print()


if __name__ == '__main__':
    tree = BinaryTree()
    pre_order_traversal_tree(tree.root)
    print()
    pre_order_traversal_tree_two(tree.root)
