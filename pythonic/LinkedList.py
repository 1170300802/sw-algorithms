#!/usr/bin/env python

# encoding: utf-8

"""
@author: swensun

@github:https://github.com/yunshuipiao

@software: python

@file: linked_list.py

@desc:

@hint:
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None  # first
        self.tail = None  # last

    def is_empty(self):
        return self.length == 0

    def get_length(self):
        return self.length

    def append(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.length += 1

    def insert(self, index, value):
        if index > self.length:
            return None
        if index == self.length:
            self.append(value)
            return
        elif index == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
        else:
            temp_index = 0
            temp_node = self.head
            while temp_index < index - 1:
                temp_index += 1
                temp_node = temp_node.next
            node = Node(value)
            node.next = temp_node.next
            temp_node.next = node
        self.length += 1

    def delete(self, index):
        if index > self.length - 1:
            return None
        if index == 0:
            self.head = self.head.next
        else:
            # 找到删除节点的前一个节点
            temp_index = 0
            temp_node = self.head
            while temp_index < index - 1:
                temp_index += 1
                temp_node = temp_node.next
            if index == self.length - 1:  # 最后一个节点
                temp_node.next = None
                self.tail = temp_node
            else:
                temp_node.next = temp_node.next.next
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

    def print_list_one(self):
        # print(self.length)
        if self.length != 0:
            temp_node = self.head
            for i in range(self.length - 1):
                print(temp_node.data, end=" -> ")
                temp_node = temp_node.next
            print(temp_node.data)

    def print_list_two(self):
        if self.head is not None:
            self._print_list_recursive(self.head)

    # 正序递归输出
    def _print_list_recursive(self, node):
        if node.next is None:
            print(node.data)
            return
        print(node.data, end=" -> ")
        self._print_list_recursive(node.next)

    # 外部变量可以传入递归，做其他或者中断操作。
    def print_list_recursive_reverse(self, node, data):
        if node.next is None:
            print(node.data, end=" -> ")
            return
        self.print_list_recursive_reverse(node.next, data)
        if node.data == data:
            print(data)
        else:
            print(node.data, end=" -> ")


def create_sorted_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(7)
    ll.append(10)
    ll.append(12)
    ll.append(24)
    ll.append(35)
    ll.append(40)
    return ll

if __name__ == '__main__':
    ll = LinkedList()
    # print_list(ll)
    ll.append(11)
    ll.append(12)
    ll.append(20)
    ll.insert(0, 10)
    ll.insert(0, 13)
    print(ll.get_value(2))
    ll.print_list_one()
    ll.print_list_two()
