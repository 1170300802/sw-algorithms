#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: linked_list_cycle.py

@time: 2018/1/17 21:11

@desc: 判断带环链表并找出入环点

@hint: 见寻找两链表的交差点
"""

from singly_linked_list_implementation import LinkedList
from reverse_linked_list import reverse_linked_list_two


def create_list():
    ll = LinkedList()
    ll.append(1)
    cycle_node = ll.tail
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.tail.next = cycle_node
    return ll

def linked_list_cycle(node):
    temp_node_fast = node
    temp_node_slow = node
    while temp_node_fast is not None or temp_node_fast.next is not None:
        temp_node_fast = temp_node_fast.next.next
        temp_node_slow = temp_node_slow.next
        if temp_node_fast is None:
            return -1
        if temp_node_fast == temp_node_slow:
            meeting_node = temp_node_slow
            break
    temp_node_slow = node
    temp_node_fast = meeting_node
    while temp_node_slow != temp_node_fast:
        temp_node_slow = temp_node_slow.next
        temp_node_fast = temp_node_fast.next
    return temp_node_slow.data

if __name__ == '__main__':
    ll = create_list()
    result = linked_list_cycle(ll.head)
    print(result)