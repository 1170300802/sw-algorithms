#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: binary_search_tree_iterator.py

@desc: 二叉搜索树迭代器， 调用next()返回二叉查找树中的最小的元素。next()和hasNext()运行的平均时间复杂度为O(1)，空间复杂度为O(h)，其中h是树的高度。

@hint: 类中序遍历，利用栈维护。
"""
from binary_tree import Node, BinaryTree


class BSTIterator:

    def __init__(self, root):
        self.node_list = []
        self.binary_search_tree_iterator(root)

    def binary_search_tree_iterator(self, root):
        # self.node_list.append(Node(-1)) #辅助节点。防止根节点出站后不能访问后续变量
        temp_node = root
        while temp_node is not None:
            self.node_list.append(temp_node)
            temp_node = temp_node.left_child

    def has_next(self):
        return len(self.node_list) > 0

    def next(self):
        if len(self.node_list) == 0:
            return None
        next_node = self.node_list.pop()
        temp_node = next_node.right_child
        while temp_node is not None:
            self.node_list.append(temp_node)
            temp_node = temp_node.left_child
        return next_node.data

if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    iter = BSTIterator(tree.root)
    while iter.has_next():
        print(iter.next())