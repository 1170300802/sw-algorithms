#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: kth_smallest_element_in_a_BST.py

@desc: 二叉搜索树中的第k小元素

@hint: 1. 中序遍历找k。2.  left+1 = K，则根节点即为第K个元素。 否则根据比较大小判断在左子树还是右子树
"""
from binary_tree import BinaryTree
from binary_tree_level_order_traversal import binary_tree_level_order_traversal_one


def kth_smallest_element_in_a_BST(root, k):
    if root is None or k < 0:
        return None
    left_count = get_node_count(root.left_child)
    if k == left_count + 1:
        return root.data
    if k < left_count + 1:
        return kth_smallest_element_in_a_BST(root.left_child, k)
    else:
        return kth_smallest_element_in_a_BST(root.right_child, k - 1 - left_count) # 1 is current node





def get_node_count(node):
    if node is None:
        return 0
    return get_node_count(node.left_child) + get_node_count(node.right_child) + 1



if __name__ == '__main__':
    tree = BinaryTree()
    tree.create_bst()
    for i in range(12):
        r = kth_smallest_element_in_a_BST(tree.root, i)
        print(r)
    # binary_tree_level_order_traversal_one(tree.root)