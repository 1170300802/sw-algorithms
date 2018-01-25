#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_tree_sIde_view.py

@desc:  二叉树的左右视图

@hint: 其实就是求二叉树每一个的第一个(最后一个)节点。
       1. 分层次遍历，取出所需要的节点
       2. dfs(类前序遍历)
"""
from binary_tree import BinaryTree


def binary_tree_side_view(root):
    if root is None:
        return None
    result_list = []  #记录当前树的高度
    left_view(root, result_list, 0)
    return result_list

def left_view(node, l, number):
    if node is None:
        return None
    if len(l) == number:
        l.append(node.data)
    left_view(node.left_child, l, number + 1)
    left_view(node.right_child, l, number + 1)

if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    result = binary_tree_side_view(tree.root)
    print(result)
