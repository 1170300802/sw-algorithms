#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: merge_sorted_list.py

@desc: 合并两个有序链表。

@hint: 引出链表排序：即利用龟兔算法找到中间节点，将链表分为两半进行排序，后面在利用本题合并（类数组的递归排序）

"""

from singly_linked_list_implementation import LinkedList
from reverse_linked_list import reverse_linked_list_two


def create_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(1)
    # ll.append(3)
    # ll.append(4)
    # ll.append(10)
    # ll.append(4)
    # ll.append(3)
    # ll.append(2)
    # ll.append(1)
    return ll

# 非递归合并
def merge_sorted_list_one(node_one, node_two):
    if node_one is None:
        return node_two
    if node_two is None:
        return node_one
    new_head = None  #新头节点
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



def sort_linked_list(node):
    if node is None or node.next is None:
        return node
    temp_node_fast = node.next  #找到中间节点的前一个节点
    temp_node_slow = node
    while temp_node_fast is not None and temp_node_fast.next is not None:
        temp_node_fast = temp_node_fast.next.next
        temp_node_slow = temp_node_slow.next
    temp_node_one = node
    temp_node_two = temp_node_slow.next
    temp_node_slow.next = None
    temp_node_one = sort_linked_list(temp_node_one) #不要去深入递归，就在当前层考虑。还有递归退出。
    temp_node_two = sort_linked_list(temp_node_two)
    return merge_sorted_list_two(temp_node_one, temp_node_two)

def merge_sorted_list_two(node_one, node_two):
    if node_one is None:
        return node_two
    if node_two is None:
        return node_one
    temp_node = node_one #记录较小的节点
    if node_one.data < node_two.data:
        temp_node.next = merge_sorted_list_two(node_one.next, node_two)
    else:
        temp_node = node_two
        temp_node.next = merge_sorted_list_two(node_one, node_two.next)
    return temp_node

if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(2)
    l1.append(5)
    l1.append(8)
    l1.append(1)
    l1.append(12)
    l1.append(5)
    l1.append(10)

    l2 = LinkedList()


    # result = merge_sorted_list(l1.head, l2.head)
    result = sort_linked_list(l1.head)
    l2.head = result
    l2.print_list_two()
