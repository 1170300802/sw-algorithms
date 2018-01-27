#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: AVL.py

@desc: 平衡二叉查找树（BBST）

@hint:
"""

class Node:
    def __init__(self, data=0):
        self.data = data
        self.size = 1
        self.height = 0
        self.left_child = None
        self.right_child = None



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

class AVLT:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.put(self.root, data)

    def put(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left_child = self.put(node.left_child, data)
        elif data > node.data:
            node.right_child = self.put(node.right_child, data)

        balance = self._height(node.left_child) - self._height(node.right_child)
        if balance > 1:
            if self._height(node.left_child.left_child) >= self._height(node.right_child):
                node = self._rotate_right(node)
            else:
                node.left_child = self._rotate_left(node.left_child)
                node = self._rotate_right(node)
        elif balance < -1:
            if self._height(node.right_child.right_child) >= self._height(node.right_child.left_child):
                node = self._rotate_left(node)
            else:
                node.right_child = self._rotate_left(node.right_child)
                node = self._rotate_left(node)
        else:
            node.height = max(self._height(node.left_child), self._height(node.right_child)) + 1
            node.size = self.size(node.left_child) + self.size(node.right_child) + 1
        return node



    def _height(self, node):
        return -1 if node is None else node.height

    def _rotate_left(self, node):
        new_root = node.right_child
        node.right_child = new_root.left_child
        new_root.left_child = node
        node.height = max(self._height(node.left_child), self._height(node.right_child)) + 1
        new_root.height = max(self._height(new_root.left_child),  self._height(new_root.right_child)) + 1
        return new_root

    def _rotate_right(self, node):
        new_root = node.left_child
        node.left_child = new_root.right_child
        new_root.right_child = node
        node.height = max(self._height(node.left_child), self._height(node.right_child)) + 1
        new_root.height = max(self._height(new_root.left_child),  self._height(new_root.right_child)) + 1
        return new_root

    def size(self, node):
        return 0 if node is None else node.size


if __name__ == '__main__':
    bst = AVLT()
    bst.insert(10)
    bst.insert(9)
    bst.insert(8)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(5)
    binary_tree_level_order_traversal_one(bst.root)


