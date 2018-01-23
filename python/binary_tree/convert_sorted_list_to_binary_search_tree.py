#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: convert_sorted_list_to_binary_search_tree.py

@desc: 有序链表转为 平衡二叉查找树

@hint: 类似归并排序，两两切开又合并。注意递归返回和对前一节点的处理
"""

import sys



sys.path.append("/Users/swensun/code/algorithms/sw-algorithms/python/")
from linked_list.singly_linked_list_implementation import create_sorted_list
from binary_tree import Node
from binary_tree_level_order_traversal import binary_tree_level_order_traversal_one


def convert_sorted_list_to_binary_search_tree(head):
    if head is None:
        return None
    #龟兔算法找节点
    fast = head
    slow = head
    pre = None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        pre = slow
        slow = slow.next
    if pre is not None:  # break link
        pre.next = None
    else:
        head = None  #递归返回：当链表只有一个节点时
    root = Node(slow.data)
    root.left_child = convert_sorted_list_to_binary_search_tree(head)
    root.right_child = convert_sorted_list_to_binary_search_tree(slow.next)
    return root



if __name__ == '__main__':
    l = create_sorted_list()
    l.print_list_two()
    root = convert_sorted_list_to_binary_search_tree(l.head)
    binary_tree_level_order_traversal_one(root)
