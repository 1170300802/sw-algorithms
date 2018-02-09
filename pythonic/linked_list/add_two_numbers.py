#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: add_two_numbers.py

@desc:  链表数相加:假设链表不包含0元素，长度相等

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

@hint:
"""

import sys
sys.path.append("/Users/swensun/code/algorithms/sw-algorithms/")
from pythonic.LinkedList import Node, LinkedList

def add_two_numbers(left, right):
    head = Node(-1)
    current = head
    sum = 0
    while left or right:
        sum = sum // 10
        if left:
            sum += left.data
            left = left.next
        if right:
            sum += right.data
            right = right.next
        current.next = Node(sum % 10)
        current = current.next
    if sum == 10:
        current.next = Node(1)
    return head.next


if __name__ == '__main__':
    left = Node(2)
    left.next = Node(4)
    left.next.next = Node(3)

    right = Node(5)
    right.next = Node(6)
    right.next.next = Node(4)
    node = Node(-1)
    res = add_two_numbers(left, right)
    l = LinkedList()
    l.head = res
    l.print_list_two()