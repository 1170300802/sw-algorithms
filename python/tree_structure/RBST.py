#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: RBST.py

@desc: 二叉查找树(递归)

@hint: 涉及插入，删除，查找
"""

class Node:
    def __init__(self, data=0, parent=None):
        self.data = data
        self.size = 1
        self.left_child = None
        self.right_child = None
        self.parent = parent


class RBST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._put(self.root, data, None)

    def search(self, data):
        return self._find_node(data, self.root) is not None

    def delete(self, data):
        d_node = self._find_node(data, self.root)
        self._delete_node(d_node)

    def _put(self, node, data, parent):
        if node is None:
            return Node(data, parent)
        if node.data > data:
            node.left_child = self._put(node.left_child, data, node)
        else:
            node.right_child = self._put(node.right_child, data, node)
        node.size = self.size(node.left_child) + self.size(node.right_child) + 1
        return node

    def _find_node(self, data, node):
        if node is None:
            return None
        if data == node.data:
            return node
        elif data > node.data:
            return self._find_node(data, node.right_child)
        else:
            return self._find_node(data, node.left_child)

    def _delete_node(self, node):
        if node is None:
            return None
        node_p = node.parent   #有父节点，删除后才知道怎么连接
        if node.left_child is None and node.right_child is None:  # case: no child
            node_p.parent = None  # break parent
            if node_p.left_child == node:
                node_p.left_child = None
            else:
                node_p.right_child = None
        elif node_p.left_child is None or node_p.right_child is None: # case: one child
            node.parent = None
            if node.left_child is None:  #node has right child
                if node_p.left_child == node:  # node is left_child
                    node_p.left_child = node.right_child
                else:
                    node_p.right_child = node.right_child  # node is right_child
                node.right_child.parent = node_p
            else:
                if node_p.left_child == node:  # node is left_child
                    node_p.left_child = node.left_child
                else:
                    node_p.right_child = node.left_child  # node is right_child
                node.left_child.parent = node_p
        else:                                             # has two child
            successor = self._find_min(node.right_child)  # smallest node on right subtree
            temp_data = node.data
            node.data = successor.data
            successor.data = temp_data
            self._delete_node(successor)


    def _find_min(self, node):
        if node is None:
            return None
        if node.left_child is None:
            return node
        else:
            return self._find_min(node.left_child)

    def _find_max(self, node):
        if node is None:
            return None
        if node.right_child is None:
            return node
        else:
            return self._find_max(node.right_child)

    def size(self, node):
        if node is None:
            return 0
        return node.size



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



if __name__ == '__main__':
    bst = RBST()
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