#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: IBST.py

@desc: 二叉查找树(迭代)

@hint:
"""


class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.size = 1
        self.left_child = None
        self.right_child = None
        self.parent = parent


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


class IBST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        x = self.root
        p = self.root
        while x is not None:  # find parent
            p = x
            if x.data == data:
                return
            if data < x.data:
                x = x.left_child
            else:
                x = x.right_child
        new_node = Node(data, p)
        if data < p.data:
            p.left_child = new_node
        else:
            p.right_child = new_node

    def search(self, data):
        x = self._find_node(self.root, data)
        return x is not None

    def _find_node(self, node, data):
        while node is not None:
            if data == node.data:
                return node
            if data < node.data:
                node = node.left_child
            else:
                node = node.right_child
        return Node

    def delete(self, data):
        x = self._find_node(self.root, data)
        self._delete_node(x)

    def _delete_node(self, node):
        if node is None:
            return
        p = node.parent
        if node.left_child is None and node.right_child is None:
            node.parent = None
            if p.left_child == node:
                p.left_child = None
            else:
                p.right_child = None
        elif node.left_child is None or node.right_child is None:
            node.parent = None
            if node.left_child is None:  # node has right child
                if p.left_child == node:
                    p.left_child = node.right_child
                else:
                    p.right_child = node.right_child
                node.right_child.parent = p
            else:
                if p.left_child == node:
                    p.left_child = node.left_child
                else:
                    p.right_child = node.left_child
                node.left_child.parent = p
        else:
            successor = self._find_min(node.right_child)  # smallest on right subtree
            temp_data = node.data
            node.data = successor.data
            successor.data = temp_data
            self._delete_node(successor)

    def _find_min(self, node):
        if node is None:
            return None
        while node.left_child is not None:
            node = node.left_child
        return node


if __name__ == '__main__':
    bst = IBST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    bst.insert(8)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    bst.insert(0)
    bst.insert(2)
    bst.delete(1)
    binary_tree_level_order_traversal_one(bst.root)
