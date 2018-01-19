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
from singly_linked_list_implementation import LinkedList, Node


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

def merge_k_sorted_lists_two(nodelist):
    #首先堆化数组， 可以包含头节点。
    last_root_node_index = (len(nodelist) >> 1) - 1
    for node_index in range(last_root_node_index, -1, -1):
        small_heap_array(nodelist, node_index, len(nodelist))
    new_head = Node(-1)
    temp_node = new_head
    while len(nodelist) != 0:
        temp_node.next = nodelist[0]
        nodelist[0] = nodelist[0].next
        temp_node = temp_node.next
        if nodelist[0] is None:
            nodelist = nodelist[1:]
        small_heap_array(nodelist, 0, len(nodelist))
    return new_head.next

def small_heap_array(node_list, root_index, array_length):
    # 参数合法性检测
    if array_length == 0:
        return
    temp_node = node_list[root_index]
    # 左叶子节点
    node_index = (root_index << 1) + 1
    while node_index < array_length:
        if node_index + 1 < array_length and node_list[node_index].data > node_list[node_index + 1].data:
            node_index += 1
        if node_list[node_index].data >= temp_node.data:
            break
        node_list[root_index] = node_list[node_index]
        root_index = node_index
        node_index = (root_index << 1) + 1
    node_list[root_index] = temp_node





if __name__ == '__main__':

    # result = merge_sorted_list(l1.head, l2.head)
    ll_list = []
    node_list = []
    for i in range(10):
        ll_list.append(LinkedList())

    for i in range(50):
        if i in [13,  36, 18, 19, 15, 25, 35, 45]:
            continue
        ll_list[i % 10].append(i)
    for i in range(10):
        node_list.append(ll_list[i].head)
    for i in range(10):
        ll_list[i].print_list_two()
    node_list.reverse()
    result = merge_k_sorted_lists_two(node_list)
    lll = LinkedList()
    lll.head = result
    lll.print_list_two()
