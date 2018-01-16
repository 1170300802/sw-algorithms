#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: doubly_linked_list_implementation.py

@time: 2018/1/16 11:10

@desc:  双向链表实现，还是简单的操作

@hint:
"""

class Node:
    def __init__(self, value=0):
        self.data = value
        self.pre = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def get_length(self):
        return self.length

    def append(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        self.length += 1

    def insert(self, index, value):
        if index > self.length:
            return
        if index == self.length:
            self.append(value) # 末尾插入
            return
        if index == 0: #头部插入
            node = Node(value)
            self.head.pre = node
            node.next = self.head
            self.head = node
        else:
            temp_index = 0
            temp_node = self.head
            while temp_index < index - 1:
                temp_index += 1
                temp_node = temp_node.next
            node = Node(value)

            #画图表示
            node.next = temp_node.next
            node.pre = temp_node
            temp_node.next.pre = node
            temp_node.next = node

        self.length += 1

    def delete(self, index):
        if index > self.length - 1:
            return
        if index == self.length - 1:
            self.tail = self.tail.pre
            self.tail.next = None
        elif index == 0:
            self.head = self.head.next
            self.head.pre = None
        else:
            temp_index = 0
            temp_node = self.head
            while temp_index < index - 1:
                temp_index += 1
                temp_node = temp_node.next

            temp_node.next = temp_node.next.next
            temp_node.next.pre = temp_node

        self.length -= 1

    def get_value(self, index):
        if index > self.length - 1:
            return None
        if index == self.length - 1:
            return self.tail.data
        i = 0
        temp_node = self.head
        while i < index:
            i += 1
            temp_node = temp_node.next
        return temp_node.data

    def print_list(self):
        print(self.length)
        if self.length != 0:
            temp_node = self.head
            for i in range(self.length - 1):
                print(temp_node.data, end=" -> ")
                temp_node = temp_node.next
            print(temp_node.data)
            temp_node = self.tail
            for i in range(self.length - 1, 0, -1):
                print(temp_node.data, end=" -> ")
                temp_node = temp_node.pre
            print(temp_node.data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.insert(2, 10)
    ll.delete(3)
    ll.print_list()
    print(ll.get_value(2))

