#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: post_order_traversal_tree.py

@desc:  二叉树的后序遍历

@hint:  递归和非递归
"""
from binary_tree import BinaryTree


def post_order_traversal_tree(root):
    if root is None:
        return
    post_order_traversal_tree(root.right_child)
    post_order_traversal_tree(root.left_child)
    print(root.data, end="  ")


#非递归遍历
def post_order_traversal_tree_two(root):
    if root is None:
        return
    node_list = []
    node_list.append(root)
    temp_node = root
    while temp_node.left_child is not None or temp_node.right_child is not None:
        pass



if __name__ == '__main__':
    # tree = BinaryTree()
    # post_order_traversal_tree(tree.root)
    # print()
    pass
