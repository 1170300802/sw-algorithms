#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: delete_node_single_linked_list.py

@time: 2018/1/16 15:11

@desc: 删除单向链表的节点(非表头或表尾)，参数只有节点这个元素， O(1)

@hint:  在插入和删除节点，都是需要找到需要插入和删除元素的前一个节点进行操作。因此可以把要删除的节点变为前一个节点。
"""

from linked_list.singly_linked_list_implementation import Node, LinkedList

def delete_node(node):
    if node is None:
        return
    node.data = node.next.data
    node.next = node.next.next

if __name__ == '__main__':
    pass