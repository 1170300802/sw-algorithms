#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: palindrome_linked_list.py

@time: 2018/1/16 15:36

@desc: 判断是不是回文链表。

@hint: 简单思路：反转链表与原链表比较，n / 2之前的每个节点都相等，则是回文链表。

龟兔算法： 一步两步，找链表的中间节点。反转该节点后的链表，逐次比较。

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


def palindrome_linked_list(node):
    if node is None or node.next is None:
        return True
    #龟兔算法找中点
    fast_node = node
    slow_node = node
    while fast_node.next is not None and fast_node.next.next is not None:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    #反转后半部分节点并返回, 后续可选择恢复反转现场
    new_head = reverse_linked_list_two(slow_node.next)
    while new_head is not None:
        if new_head.data != node.data:
            return False
        new_head = new_head.next
        node = node.next
    return True



if __name__ == '__main__':
    ll = create_list()
    print(palindrome_linked_list(ll.head))
