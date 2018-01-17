#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: remove_nth_node_from_end_of_list.py

@time: 2018/1/17 21:22

@desc: 删除链表的倒数第k个元素

@hint:  解法：龟兔算法。先让一个节点前进k，在用一个节点同时前进，当前节点为None时，后节点即为要删除的节点。
        注意特殊情况， k为0， 删除倒数第一个和倒数最后一个的情况。
"""

from singly_linked_list_implementation import LinkedList

def create_list():

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # ll.append(7)
    # ll.append(8)
    return ll

def remove_nth_node_from_end_of_list_one(node, k):
    # 参数合法性， 还有特殊清情况，删除第一个和最后一个
    if node is None or k == 0:
        return -1

    temp_node_fast = node
    while k > 0:
        if temp_node_fast is None:
            return -1
        temp_node_fast = temp_node_fast.next
        k -= 1

    if temp_node_fast is None:
        #删除的刚好是头节点
        data = node.data
        node.data = node.next.data
        node.next = node.next.next
        return data

    # 找到要删除节点的前一个节点
    temp_node_slow = node
    while temp_node_fast.next is not None:
        temp_node_slow = temp_node_slow.next
        temp_node_fast = temp_node_fast.next
    data = (temp_node_slow.next.data)
    temp_node_slow.next = temp_node_slow.next.next
    return data



#递归解法
def remove_nth_node_from_end_of_list_two(node, k):
    # 递归找到需要删除的节点
    if node is None or k == 0:
        return None
    global temp_k
    temp_k = k
    find_node(node)
    if temp_k == 0:
        newhead = node.next
        node.next = None
        node = newhead
    return node
    # if temp_k == 1:
    #     #第一个节点
    #     return node.next
    # else:
    #     delete_node.next = delete_node.next.next
    #     return node


#注意temp_k的位置
def find_node(node):
    if node is None:
        return
    find_node(node.next)
    global temp_k
    if temp_k == 0:
        node.next = node.next.next
    temp_k -= 1

if __name__ == '__main__':
    ll = create_list()
    temp_k = 0
    head = remove_nth_node_from_end_of_list_two(ll.head, 7)
    if head is not None:
        ll.head = head
    ll.print_list_two()