#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: flatten_binary_tree_to_llinked_list.py

@desc: 将二叉树按照先序遍历的顺序展开成链表，也可考虑中序，后续。

@hint:  递归和非递归, 主要还是7种遍历方法。
"""
from binary_tree import BinaryTree

def flatten_binary_tree_to_linked_list(root):
    if root is None:
        return None
    if root.left_child is not None:
        flatten_binary_tree_to_linked_list(root.left_child)
    if root.right_child is not None:
        flatten_binary_tree_to_linked_list(root.right_child)
    temp_node = root.right_child
    root.right_child = root.left_child
    root.left_child = None

    temp_root = root
    while temp_root.right_child is not None: #将展开的右子树， 接在左子树的最后一个节点。
        temp_root = temp_root.right_child
    temp_root.right_child = temp_node
    return root


def flatten_binary_tree_to_linked_list_two(root):
    if root is None:
        return None
    temp_root = root
    while temp_root.right_child is not None:
        if temp_root.left_child is not None:
            temp_node = temp_root.right_child
            temp_root.right_child = temp_root.left_child

            temp_right = temp_root.right_child
            while temp_right is not None:
                temp_right = temp_right.right_child
            temp_right.right = temp_node

        temp_root = temp_root.right_child
    return root

if __name__ == '__main__':
    tree = BinaryTree()
    temp_root = flatten_binary_tree_to_linked_list(tree.root)
    while temp_root is not None:
        print(temp_root.data, end="  ")
        temp_root = temp_root.right_child
    print()
    temp_root = flatten_binary_tree_to_linked_list_two(tree.root)
    while temp_root is not None:
        print(temp_root.data, end="  ")
        temp_root = temp_root.right_child
    print()