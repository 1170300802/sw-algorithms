#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: merge_k_sorted_lists.py

@time: 2018/1/18 10:42

@desc: 合并k个有序链表,返回头节点

@hint: 与之前两个排序链表类似，可以顺序采用两两合并来完成，不过效率太低。

       两种解法：1. 分治。排序链表也是相当于合并k个有序链表.
                2. 将存在数组中的k个节点堆化成一个最小堆，分别取最小值作为新加入到新链表中，直到数组为空，即可得到新链表。
                下面分别实现：
"""
from singly_linked_list_implementation import LinkedList
from reverse_linked_list import reverse_linked_list_two

def merge_k_sorted_lists_one(nodelist, lo, hi):
    # 参数合法性检测
    if lo == hi:
        return node_list[lo]
    mid = (lo + hi) >> 1
    temp_node_one = merge_k_sorted_lists_one(nodelist, lo, mid)
    temp_node_two = merge_k_sorted_lists_one(nodelist, mid + 1, hi)
    return merge_two_sorted_list(temp_node_one, temp_node_two)

def merge_two_sorted_list(node_one, node_two):
    if node_one is None:
        return node_two
    if node_two is None:
        return node_one
    new_head = None
    if node_one.data < node_two.data:
        new_head = node_one
        node_one = node_one.next
    else:
        new_head = node_two
        node_two = node_two.next
    temp_node = new_head
    while node_one is not None or node_two is not None:
        if node_one is None:
            temp_node.next = node_two
            break
        if node_two is None:
            temp_node.next = node_one
            break
        if node_one.data < node_two.data:
            temp_node.next = node_one
            node_one = node_one.next
        else:
            temp_node.next = node_two
            node_two = node_two.next
        temp_node = temp_node.next
    return new_head




if __name__ == '__main__':



    # result = merge_sorted_list(l1.head, l2.head)
    ll_list = []
    node_list = []
    for i in range(10):
        ll_list.append(LinkedList())

    for i in range(50):
        if i in [13, 25, 36, 8, 19]:
            continue
        ll_list[i % 10].append(i)
    for i in range(10):
        node_list.append(ll_list[i].head)
    for i in range(10):
        ll_list[i].print_list_two()

    result = merge_k_sorted_lists_one(node_list, 0, len(node_list) - 1)
    lll = LinkedList()
    lll.head = result
    lll.print_list_two()
