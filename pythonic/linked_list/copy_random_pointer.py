#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: copy_random_pointer.py

@desc: 复制带有随机指针的链表

@hint: 用字典保存来保存随机指针所指的节点
"""

class RandomListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copyRandomList(self, head):
    dic = dict()
    m = n = head
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    while n:
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get(head)