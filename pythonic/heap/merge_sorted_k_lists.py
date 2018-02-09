#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: merge_sorted_k_lists.py

@desc: 合并k个有序链表

@hint:
"""

from heapq import heappop, heapify, heappush, heapreplace

from sys import path

path.append("/Users/swensun/code/algorithms/sw-algorithms/")

from pythonic.linked_list import LinkedList, Node


def merge_sorted_k_lists(node_list):
    dummy = node = Node(-1)
    h = [(n.data, n) for n in node_list if n]
    heapify(h)
    while h:
        v, n = h[0]
        if n.next is None:
            heappop(h)  #change heap size
        else:
            heapreplace(h, (n.next.data, n.next))
        node.next = n
        node = node.next

    return dummy.next


if __name__ == '__main__':
    ll_list = []
    node_list = []
    for i in range(10):
        ll_list.append(LinkedList())
    for i in range(50):
        if i in [13, 36, 18, 19, 15, 25, 35, 45]:
            continue
        ll_list[i % 10].append(i)
    for i in range(10):
        node_list.append(ll_list[i].head)
    for i in range(10):
        ll_list[i].print_list_two()

    node_list.reverse()
    result = merge_sorted_k_lists(node_list)
    lll = LinkedList()
    lll.head = result
    lll.print_list_two()
