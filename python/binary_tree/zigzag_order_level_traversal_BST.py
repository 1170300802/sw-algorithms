#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: zigzag_rrder_level_traversal_BST.py

@desc:  二叉树的锯齿形层次遍历

@hint:  多用一个变量记录是否需要reverse, 或者保存成链表再倒转
"""
from binary_tree import BinaryTree


def zigzag_order_level_traversal_BST(root):
    if root is None:
        return None
    result = [] #最终结果
    node_list = []  #借助的队列
    level_node_list = [] # 每一层的node值
    node_list.append(root)
    level_count = 1
    while len(node_list) != 0:
        temp_node = node_list.pop(0)
        level_count -= 1
        if temp_node.left_child is not None:
            node_list.append(temp_node.left_child)
        if temp_node.right_child is not None:
            node_list.append(temp_node.right_child)
        level_node_list.append(temp_node.data)
        if level_count == 0:   # 一层遍历完
            level_count = len(node_list)
            result.append(level_node_list)
            level_node_list = []
    for index, _ in enumerate(result):
        if index % 2 == 1:
            result[index].reverse()
    return result

if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    result = zigzag_order_level_traversal_BST(tree.root)
    print(result)
