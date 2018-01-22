#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: mid_order_traversal_tree.py

@desc: 二叉树的中序遍历

@hint: 递归和非递归
"""
from binary_tree import BinaryTree


def mid_order_traversal_tree(root):
    if root is None:
        return
    mid_order_traversal_tree(root.left_child)
    print(root.data, end="   ")
    mid_order_traversal_tree(root.right_child)


#非递归遍历
def mid_order_traversal_tree_two(root):
    if root is None:
        return
    node_list = []
    temp_node = root
    while temp_node is not None or len(node_list) != 0:
        while temp_node is not None:
            node_list.append(temp_node)
            temp_node = temp_node.left_child
        temp_node = node_list.pop()  #访问过，要出栈。
        print(temp_node.data, end="   ")
        temp_node = temp_node.right_child
    print()



if __name__ == '__main__':
    tree = BinaryTree()
    mid_order_traversal_tree(tree.root)
    print()
    mid_order_traversal_tree_two(tree.root)