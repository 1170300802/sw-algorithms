#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_tree_level_order_traversal.py

@desc: 二叉树的层次遍历, 每层分别输出

@hint:  多种方法考虑
"""
from binary_tree import BinaryTree


# 最简单的方法，一次全部输出
def binary_tree_level_order_traversal_one(root):
    if root is None:
        return
    node_list = []
    node_list.append(root)
    while len(node_list) != 0:
        temp_node = node_list.pop(0)
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
        print(temp_node.data, end="  ")

    print()


# 分层次输出, 多用一个临时变量，来记录当前层数目
def binary_tree_level_order_traversal_two(root):
    if root is None:
        return
    node_list = []
    result = []
    temp = []
    node_list.append(root)
    level = 1
    while len(node_list) != 0:
        temp_node = node_list.pop(0)
        level -= 1
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
        print(temp_node.data, end="  ")
        temp.append(temp_node.data)
        if level == 0 and len(node_list) != 0:
            level = len(node_list)
            print()
            result.append(temp)
            temp = []
    print()
    result.append(temp)
    print(result)



if __name__ == '__main__':
    tree = BinaryTree()
    binary_tree_level_order_traversal_two(tree.root)
